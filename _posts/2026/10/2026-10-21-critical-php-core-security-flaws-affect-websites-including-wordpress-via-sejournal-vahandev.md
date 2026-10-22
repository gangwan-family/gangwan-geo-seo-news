---
layout: post
title: "Critical PHP Core Security Flaws Affect Websites, Including WordPress via @sejournal, @vahandev"
date: 2026-10-21T13:46:10+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-21/Critical PHP Core Security Flaws Affect Websites, Including WordPress via @sejournal, @vahandev.md"
original_url: "https://www.searchenginejournal.com/critical-php-core-security-flaws-affect-websites-including-wordpress/593812/"
author: "Vahan Petrosyan"
categories:
  - "SEO"
  - "Security"
  - "_src_search-engine-journal"
---

# Critical PHP Core Security Flaws Affect Websites, Including WordPress via @sejournal, @vahandev

- Source: Search Engine Journal
- Published: 2026-10-21
- URL: https://www.searchenginejournal.com/critical-php-core-security-flaws-affect-websites-including-wordpress/593812/
- Author: Vahan Petrosyan
- Categories: SEO, Security

## RSS 摘要

PHP's emergency security fixes are available today, October 21, and website owners should ask their hosts to install them immediately. The post Critical PHP Core Security Flaws Affect Websites, Including WordPress appeared first on Search Engine Journal .

## 原文正文

Critical PHP Core Security Flaws Affect Websites, Including WordPress Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- Security

## Critical PHP Core Security Flaws Affect Websites, Including WordPress

- PHP has released fixes in versions 8.5.12, 8.4.27, 8.3.36, and 8.2.35 for two critical flaws that can let attackers run code without logging in.

- Apache servers using mod_php face the highest risk, though PHP says all installations serving website requests are at risk.

- PHP says updating is the only safe choice. A firewall or configuration change is not a complete substitute for patching.

- PHP 8.1 and older remain unsupported. Limited source fixes and vendor updates may be available while site owners arrange an upgrade.

PHP's emergency security update, scheduled for today, October 21, at 14:00 UTC, is now available. Ask your host to patch PHP and upgrade unsupported versions.

The PHP security team has released emergency fixes today, October 21, 2026, for two critical flaws that can let attackers run code on website servers without logging in.

The fixed versions are PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35 . PHP says updating is the only safe choice because no workaround fully addresses the vulnerabilities.

PHP says all installations serving website requests are at risk. Apache servers using mod_php , which runs PHP directly inside Apache, face the highest risk. A demonstrated attack can run before the website’s own code starts.

PHP runs WordPress on your web server. Updating WordPress or its plugins will not update PHP. Ask your host to install the fix. If your hosting account lets you switch PHP versions through cPanel, confirm that the version you select includes the patch.

### Older PHP Versions Need An Upgrade

PHP 8.1 and older remain on the end-of-life list and no longer receive regular official updates.

For this emergency, PHP has provided limited source-code fixes for PHP 7.4, 8.0, and 8.1 for teams that build PHP themselves. Hosting providers and long-term support vendors may also supply their own updates. These fixes do not restore ongoing support. Ask your host to confirm protection while arranging an upgrade to a supported version .

### Government Sites Taken Offline Ahead Of The PHP Patch

International Cyber Digest reported that Dutch parliament and cyber agency websites, Finnish government web services, and university sites went offline ahead of the release. It described the Finnish shutdowns as a precaution, not a breach.

Sansec also reported that the Dutch House of Representatives and National Cyber Security Centre took their websites offline as a precaution.

Ahead of the release, CERT-EU and the UK National Cyber Security Centre advised considering temporary isolation or shutdowns where immediate protection was not possible.

### What Website Owners Should Do Now

Follow the WordPress PHP guide to check your version: open Tools > Site Health , select Info , and expand Server .

- Ask your host to install one of the fixed versions listed above, or confirm that its PHP update includes both fixes.

- If you use PHP 8.1 or older, back up the site and arrange an upgrade. Ask your host whether it can apply a vendor-provided fix in the meantime.

If you cannot patch immediately, discuss taking the affected site offline until it can be updated. A web application firewall (WAF), such as Cloudflare , may block some attack attempts, but it is not a substitute for installing the fixes.

If you take your site offline to patch PHP, ask your host to show a maintenance page with an HTTP 503 (Service Unavailable) response, as Google recommends . This signals a temporary outage; your host can serve the page through the web server or a content delivery network (CDN), without relying on PHP.

If you use a firewall , make sure all visits pass through it. Attackers who can reach your website’s server directly can bypass those checks.

After patching, check for web shells (malicious scripts that give attackers access), unfamiliar admin accounts, and unexpected PHP file changes. A patch does not remove an existing compromise.

See also : Google Reminds Sites To Serve A 503 During PHP Patch Downtime

### Prepare For More Severe Vulnerabilities

As I predicted in August when writing about how AI is changing website security , attackers can move faster than software makers can deliver a fix. Reports of an attack tool circulating before this PHP patch show that timing problem is already happening.

The fix is now available, but it only protects your site once installed. A compromise can expose customer data and damage search visibility.

Ask your tech team to audit your code and monitor suspicious activity. Agree with your host who will apply emergency patches or take an affected site offline if it cannot be protected.

Attackers can use uncensored models with safety restrictions removed. These models can gain capabilities through distillation , which trains them on outputs from more powerful frontier models. As a result, more powerful AI can reach bad actors without the original models’ safeguards, giving them better tools to find and exploit weaknesses. That is why I expect severe vulnerabilities like these to be uncovered more frequently, with less time for website owners to respond. Preparing for that pace is becoming part of protecting your website and its search visibility.

Featured Image: Popartic/Shutterstock

Category SEO Security

Read Full Bio

SEJ STAFF Vahan Petrosyan Director of Technology at Search Engine Journal

As Director of Technology at Search Engine Journal, I lead the organization’s technology strategy and technical operations. I oversee technical ...

## 原文链接

[Read original](https://www.searchenginejournal.com/critical-php-core-security-flaws-affect-websites-including-wordpress/593812/)
