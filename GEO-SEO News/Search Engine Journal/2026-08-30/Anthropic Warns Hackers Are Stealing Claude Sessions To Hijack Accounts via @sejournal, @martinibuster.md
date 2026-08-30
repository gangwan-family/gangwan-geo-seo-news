---
title: "Anthropic Warns Hackers Are Stealing Claude Sessions To Hijack Accounts via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-30T22:45:39+00:00
fetched_at: 2026-08-30T23:38:25.082357+00:00
url: "https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/"
guid: "https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
---

# Anthropic Warns Hackers Are Stealing Claude Sessions To Hijack Accounts via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-30
- URL: https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/
- Author: Roger Montti
- Categories: AI Search, News

## RSS 摘要

Anthropic warns that infostealer malware is stealing Claude login sessions to drain account usage. The post Anthropic Warns Hackers Are Stealing Claude Sessions To Hijack Accounts appeared first on Search Engine Journal .

## 原文正文

Anthropic Warns Hackers Are Stealing Claude Sessions To Hijack Accounts Skip to content

- SEJ

- ⋅

- AI Search

## Anthropic Warns Hackers Are Stealing Claude Sessions To Hijack Accounts

Anthropic warns that hackers are using stolen Claude sessions to hijack accounts and drain account usage.

Anthropic Claude has been signing users out of their Claude sessions and removing payment methods for users whose computers have been compromised. A user published the email they received from Anthropic that they had become aware that the customer was compromised by an infostealer malware.

### Infostealer Malware

Infostealer malware is malicious software whose purpose is to secretly steal valuable information like passwords and credentials from a computer or device and transmit it back to the criminals that planted the malware.

This is different from ransomware which announces its presence by locking files and demanding a ransom for unlocking it. Infostealers are stealthy by design so as to have enough time to collect valuable information that can later be used or sold by criminals.

### Anthropic Noticed A Computer Was Compromised

A Redditor posted that they had received a notice from Anthropic about an attempt to steal tokens from their account via the API. The notice advised them that Anthropic had become aware that they are a victim of an infostealer malware. According to the Redditor, they run Anthropic’s models on their computer “ exclusively in permission-free mode .”

The Redditor posted some of the email message they had received:

“We recently signed you out of Claude and removed the payment method saved on your account, so you’ll need to log back in and re-add your card. We’re sorry for the disruption. Here’s what happened and what we’ve done about it.

What happened

We have recently become aware of a bad actor that is using common infostealer malware to steal Claude login sessions from people’s computers, then using those login sessions to access Claude accounts and consume their usage. Our systems detected this activity on your account, and we’ve therefore removed your card on file and signed out the sessions involved to help block further unauthorized access.

If your usage limits looked like they refilled and then drained while you weren’t using Claude, this was likely the cause.

How did this happen

Our investigation is ongoing. Our findings to date suggest that a computer you use with Claude is likely infected with infostealer malware, and may have been for some time. Phones and tablets do not appear to have been involved.

We have no reason to believe that this malware is related to Claude, installed through Claude, or related to anything you did with Claude. It’s general-purpose malware that typically arrives with an unofficial download or a malicious app, and it quietly copies saved passwords, login cookies in browsers, and credentials for other apps running locally. Your Claude session was likely one of the many things it collected. It appears that a bad actor has now started picking the Claude sessions out of what it collected and using them.

The malware identified in this campaign so far include Vidar, Lumma (LummaC2), StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of Macs.

What we’ve done

Signed out the sessions involved. Your Claude login session is saved on your computer, and the malware took a copy of it. Signing you out cancels that session everywhere, so the stolen copy stops working. This is why you had to log in again across all your own devices. Please note that we might sign you out again if we see similar signs of account misuse.

Removed your saved payment method, so it can’t be charged through Claude. Your current plan continues for the billing period you’ve already paid for. To renew after that, or to make any purchase, you’ll need to add a payment method again in Settings.”

### Origin Of The Infostealer Malware

In response to a question the Redditor admitted that they had downloaded a pirated game and that contained a hidden Infostealer malware. The malware apparently stole login information from the computer. The damage wasn’t limited to extracted passwords. The Redditor related that Chrome credentials, cookies, and session IDs were stolen, data that could be used to impersonate the person online.

### Two-Factor Authentication Failed

Quite likely the most startling part of this saga is the Redditors claim that two-factor authentication did not protect them. That’s probably because the session ID and cookies may have enabled the criminals to impersonate the Redditor’s logged-in Chrome session.

The criminals did not have to defeat two-factor authentication because they could just use the logged-in session state.

### Anthropic Opus’s Solution Terrified The User

Removing the infected software did not eliminate the malware itself. The Redditor’s explanation suggests that the malware itself had burrowed deep into their computer. The Redditor recounted that they deployed Claude directly into their computer, which proceeded to root out the malware.

They described the process :

“…I was already logged into Claude CLI. My assumption was that the virus was still present and active. So using Claude on my computer wouldn’t change anything until the virus was deactivated.

…According to the report, Opus detected the virus, deactivated it, identified it, and then reverse-engineered it to assess the extent of the threat. It almost terrified me. It was like watching a diabolical surgeon dissecting his prey.”

### PC Antivirus Useless

Claude Opus described how the infostealer worked and provided instructions on how to reset all of their login credentials.

They wrote:

“Apparently, the virus operated on a timer mechanism and sent a “batch” of login credentials to a remote server every few minutes.

In fact, if the hacker had acted quickly, he could have cut off my access to Claude (forcing me to reset my computer as a last resort and slowing down my efforts to counter him). Windows Defender was clueless”

### Was The Problem Truly Solved?

One user who identified themself as a security expert with twenty years of professional experience red-teaming malware recommended wiping their entire computer and starting anew with it because their experience is that these kinds of malware install backup files for restoring themselves.

Their advice :

“I strongly recommend you wipe your system and reset your passwords.

Or you can trust Claude who hallucinates.”

Featured Image by Shutterstock/Algi Febri Sugita

Category News AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/)
