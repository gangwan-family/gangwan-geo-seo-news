---
title: "Rank Math SEO WordPress Plugin Hit By 16 Vulnerabilities In 2026 via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-11-18T13:55:11+00:00
fetched_at: 2026-11-19T02:41:06.811446+00:00
url: "https://www.searchenginejournal.com/rank-math-seo-wordpress-plugin-hit-by-16-vulnerabilities-in-2026/597932/"
guid: "https://www.searchenginejournal.com/rank-math-seo-wordpress-plugin-hit-by-16-vulnerabilities-in-2026/597932/"
author: "Roger Montti"
categories:
  - "News"
  - "WordPress"
---

# Rank Math SEO WordPress Plugin Hit By 16 Vulnerabilities In 2026 via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-11-18
- URL: https://www.searchenginejournal.com/rank-math-seo-wordpress-plugin-hit-by-16-vulnerabilities-in-2026/597932/
- Author: Roger Montti
- Categories: News, WordPress

## RSS 摘要

Sixteen Rank Math SEO vulnerabilities in one year raise questions about how so many security exploits made it into a plugin used by millions. The post Rank Math SEO WordPress Plugin Hit By 16 Vulnerabilities In 2026 appeared first on Search Engine Journal .

## 原文正文

Rank Math SEO WordPress Plugin Hit By 16 Vulnerabilities In 2026 Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

- SEJ

- ⋅

- WordPress

## Rank Math SEO WordPress Plugin Hit By 16 Vulnerabilities In 2026

Sixteen Rank Math SEO vulnerabilities in one year could have exposed millions of WordPress websites to security exploits.

Sixteen vulnerabilities have been discovered in the popular Rank Math SEO plugin in 2026, setting a new record for vulnerabilities discovered, more than any other SEO plugin.

Rank Math’s 2026 vulnerabilities included potential pathways to website takeover, exposure of protected information, and unauthorized changes to WordPress content and data. All of these things could also have a negative impact on SEO.

Although AI is making vulnerability disclosures more common, other SEO plugins like Yoast SEO did not have anywhere near that many vulnerability discoveries. The free version of Yoast SEO was reported by Wordfence to have a total of four vulnerabilities in 2026 and only two were discovered in the paid version.

The sixteen vulnerabilities share certain issues in common but arguably the worst of them are:

- Vulnerabilities That Could Lead To Website Takeover

- Vulnerabilities That Could Expose Protected Content Or Website Data

- Vulnerabilities That Could Allow Unauthorized Website Changes

### Vulnerabilities That Could Lead To Website Takeover

Remote Code Execution (CVSS rated 8.8)

Two vulnerabilities with a CVSS severity score of 8.8 were discovered that could enable attackers with Contributor or Author-level access to execute arbitrary code on the server, potentially leading to complete website compromise.

- CVE-2026-1928: PHP Object Injection to Remote Code Execution, requiring Contributor-level access or higher. Disclosed October 27, 2026.

- CVE-2026-81757: Remote Code Execution, requiring Author-level access or higher. Disclosed August 27, 2026.

Arbitrary File Upload (7.2)

One of the vulnerabilities could potentially lead to a website takeover through malicious file uploads, although this vulnerability required Administrator privileges.

CVE-2026-104752: Arbitrary File Upload, requiring Administrator-level access or higher. Disclosed October 8, 2026. CVSS 7.2 (High).

Stored Cross-Site Scripting (7.2)

An unauthenticated attacker could potentially execute malicious JavaScript in an Administrator’s browser. Depending on the circumstances, that could lead to privileged actions or account compromise. CVE-2026-66702: Stored Cross-Site Scripting, requiring no authentication. Disclosed July 31, 2026. CVSS 7.2 (High).

Stored Cross-Site Scripting (7.2)

An unauthenticated attacker could potentially execute malicious JavaScript in an Administrator’s browser. Depending on the circumstances, this could enable an attacker to make unauthorized changes to the website or take control of an Administrator’s account. CVE-2026-66702: Stored Cross-Site Scripting, requiring no authentication. Disclosed July 31, 2026. CVSS 7.2 (High).

### Vulnerabilities That Could Expose Protected Content Or Website Data

These vulnerabilities could allow attackers to access protected content or sensitive website information without the necessary permissions. Unlike vulnerabilities that enable unauthorized changes, these primarily concern exposing information that should remain restricted, although SQL injection could also allow attackers to manipulate website data.

Password-Protected Content Disclosure (5.3)

- Could allow unauthenticated attackers to read content protected by a password.

Information Exposure (5.3 and 4.3)

- Could disclose information to visitors or users who were not authorized to access it.

SQL Injection (4.9)

- Could potentially expose or manipulate database information, although exploitation required Administrator privileges.

### Vulnerabilities That Could Enable Unauthorized Website Changes

These vulnerabilities could enable attackers to make unauthorized changes to a WordPress website, including modifying content-related data, changing homepage settings, and deleting SEO information. Some could be exploited without logging in, while others required an account but allowed actions beyond that user level’s permissions.

Arbitrary Post/User Metadata Overwrite (4.3)

- Could allow Authors to modify WordPress post or user metadata beyond their permissions.

Unauthenticated Homepage Settings Modification (5.3)

- Could allow attackers to modify homepage settings.

Unauthenticated SEO Data Deletion (5.3)

- Could enable attackers to delete SEO data without having to gain a permission level.

Unauthorized SEO Object Updates (4.3)

- Could enmable users with the Author level credentials to modify SEO information without the necessary permissions.

### Frequency Of Vulnerability Discoveries

Most vulnerabilities were discovered within a relatively short period. Eleven of the 16 vulnerabilities were discovered between August 27 and October 14, 2026. Of those vulnerabilities, late August and early September saw a concentrated cluster of vulnerability discoveries. Eight were reported between August 27 and September 3, within just eight days.

#### Multiple vulnerabilities affected the same versions of Rank Math.

Version 1.0.276

- Two remote code execution vulnerabilities affected this version and earlier versions.

Version 1.0.277

- Seven vulnerabilities affected versions earlier than 1.0.277, including missing authorization, information exposure, and unauthorized metadata changes.

Version 1.0.279

- Three vulnerabilities affected this version and earlier versions, including SQL injection, arbitrary file upload, and stored cross-site scripting.

The disclosures continued into October. Five vulnerabilities were reported in October, including three disclosed on October 8 and the latest on October 27.

#### Takeaway:

As previously stated, Rank Math’s direct competitor, Yoast SEO, only experienced four vulnerabilities during a year which saw an increase in vulnerability discoveries. The unusually high number of vulnerabilities leads to questions about Rank Math’s coding practices, code review, and quality control.

### Recurring Security Weaknesses

The other issue in the sixteen vulnerabilities is that are repeated instances of the same kinds of exploits.

Missing authorization was the most frequently identified vulnerability category. Seven of the 16 entries explicitly mention inadequate permission checks, pointing to recurring problems with enforcing permissions before allowing actions.

Several vulnerabilities could be exploited without registering an account or logging in, while others required only Contributor or Author-level permissions. Five disclosures explicitly identified unauthenticated vulnerabilities, meaning an attacker would not need to log in.

Some security problems could lead to complete website compromise. Two vulnerabilities carried CVSS scores of 8.8 and involved remote code execution, allowing attackers who met the required conditions to potentially execute malicious code on the server.

### Takeaway

Overall, the vulnerabilities involved a broad range of security weaknesses. They included unauthorized modifications, information exposure, cross-site scripting, SQL injection, arbitrary file uploads, and remote code execution. The vulnerability discoveries do not point to just one type of coding lapse; they point to a wide range of coding issues.

The full list of Rank Math vulnerabilities can be found at Wordfence , with links to a description page for each vulnerability.

Featured Image by Shutterstock/file404

Category News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/rank-math-seo-wordpress-plugin-hit-by-16-vulnerabilities-in-2026/597932/)
