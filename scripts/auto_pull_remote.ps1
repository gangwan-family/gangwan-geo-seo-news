param(
    [string]$RepoPath = "",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $RepoPath = Split-Path -Parent $PSScriptRoot
}

$LogDir = Join-Path $RepoPath "scripts\logs"
$LogPath = Join-Path $LogDir "auto-pull.log"
$AttentionPath = Join-Path $LogDir "NEEDS_ATTENTION.txt"

if (-not (Test-Path -LiteralPath $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}

function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $LogPath -Value "[$timestamp] $Message" -Encoding UTF8
}

function Notify-Attention {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Set-Content -LiteralPath $AttentionPath -Value "[$timestamp] $Message`r`nSee log: $LogPath" -Encoding UTF8

    try {
        & msg.exe $env:USERNAME /TIME:120 "Codex Git auto sync needs attention. See $AttentionPath" | Out-Null
    }
    catch {
        Write-Log "Windows message notification failed: $($_.Exception.Message)"
    }
}

function Invoke-Git {
    param(
        [string[]]$Arguments,
        [switch]$AllowFailure
    )

    Write-Log "git $($Arguments -join ' ')"
    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = & git @Arguments 2>&1
        $code = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    foreach ($line in $output) {
        Write-Log $line.ToString()
    }

    if (($code -ne 0) -and (-not $AllowFailure)) {
        throw "git $($Arguments -join ' ') failed with exit code $code."
    }

    return @{
        Code = $code
        Output = $output
    }
}

function Ensure-GitIdentity {
    $name = (& git config user.name 2>$null)
    $nameCode = $LASTEXITCODE
    $email = (& git config user.email 2>$null)
    $emailCode = $LASTEXITCODE

    if (($nameCode -ne 0) -or [string]::IsNullOrWhiteSpace($name)) {
        Invoke-Git -Arguments @("config", "user.name", "Codex Auto Sync") | Out-Null
    }

    if (($emailCode -ne 0) -or [string]::IsNullOrWhiteSpace($email)) {
        Invoke-Git -Arguments @("config", "user.email", "codex-auto-sync@local") | Out-Null
    }
}

function Commit-SafeLocalChanges {
    Invoke-Git -Arguments @(
        "add", "-A", "--", ".",
        ":!.obsidian/.obsidian-sync-helper-backup/config-history.json",
        ":!.obsidian/plugins/bijitongbu/data.json",
        ":!.obsidian/plugins/messager/data.json"
    ) | Out-Null

    & git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Log "No safe local changes to commit."
        return $false
    }

    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    Invoke-Git -Arguments @("commit", "-m", "Auto sync local changes $stamp") | Out-Null
    return $true
}

function Stash-ProtectedChanges {
    $protectedPaths = @(
        ".obsidian/.obsidian-sync-helper-backup/config-history.json",
        ".obsidian/plugins/bijitongbu/data.json",
        ".obsidian/plugins/messager/data.json"
    )

    $status = & git status --porcelain=v1 -uall -- $protectedPaths
    if (-not $status) {
        return $false
    }

    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    Write-Log "Stashing protected credential-bearing config changes: auto-sync-protected-$stamp."
    Invoke-Git -Arguments (@("stash", "push", "-u", "-m", "auto-sync-protected-$stamp", "--") + $protectedPaths) | Out-Null
    return $true
}

function Restore-ProtectedChanges {
    param([bool]$HasProtectedStash)

    if (-not $HasProtectedStash) {
        return
    }

    Write-Log "Restoring protected Obsidian changes from latest stash."
    $popResult = Invoke-Git -Arguments @("stash", "pop") -AllowFailure
    if ($popResult.Code -eq 0) {
        return
    }

    Write-Log "stash pop reported conflicts. Trying to preserve stashed .obsidian changes."
    Invoke-Git -Arguments @("checkout", "--theirs", "--", ".obsidian") -AllowFailure | Out-Null
    Invoke-Git -Arguments @("restore", "--staged", "--", ".obsidian") -AllowFailure | Out-Null

    $unmerged = & git diff --name-only --diff-filter=U
    if ($unmerged) {
        throw "Could not auto-resolve protected Obsidian conflicts: $($unmerged -join ', ')"
    }
}

function Push-WithRetry {
    $pushResult = Invoke-Git -Arguments @("push", "origin", $Branch) -AllowFailure
    if ($pushResult.Code -eq 0) {
        return
    }

    Write-Log "Push failed. Fetching/rebasing once, then retrying push."
    Invoke-Git -Arguments @("fetch", "origin", $Branch, "--verbose") | Out-Null
    Invoke-Git -Arguments @("rebase", "origin/$Branch") | Out-Null
    Invoke-Git -Arguments @("push", "origin", $Branch) | Out-Null
}

try {
    Write-Log "Starting hourly Git auto sync for $RepoPath"
    Set-Location -LiteralPath $RepoPath
    Remove-Item -LiteralPath $AttentionPath -Force -ErrorAction SilentlyContinue

    $currentBranch = (& git branch --show-current)
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to read current Git branch."
    }

    if ($currentBranch -ne $Branch) {
        throw "Current branch is '$currentBranch', expected '$Branch'."
    }

    Ensure-GitIdentity
    $madeCommit = Commit-SafeLocalChanges
    $stashedProtected = Stash-ProtectedChanges

    Invoke-Git -Arguments @("fetch", "origin", $Branch, "--verbose") | Out-Null
    Invoke-Git -Arguments @("rebase", "origin/$Branch") | Out-Null
    Restore-ProtectedChanges $stashedProtected

    if ($madeCommit) {
        Push-WithRetry
    }
    else {
        Write-Log "No local commit was created, so push is skipped."
    }

    $head = (& git rev-parse --short HEAD)
    Write-Log "Hourly Git auto sync completed. HEAD=$head"
    exit 0
}
catch {
    $message = $_.Exception.Message
    Write-Log "ERROR: $message"
    Notify-Attention $message
    exit 1
}
