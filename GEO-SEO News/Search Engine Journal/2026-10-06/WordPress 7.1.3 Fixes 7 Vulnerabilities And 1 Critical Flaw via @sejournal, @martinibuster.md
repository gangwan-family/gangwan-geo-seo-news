---
title: "WordPress 7.1.3 Fixes 7 Vulnerabilities And 1 Critical Flaw via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-10-06T20:05:17+00:00
fetched_at: 2026-10-07T00:51:35.717389+00:00
url: "https://www.searchenginejournal.com/wordpress-7-1-3-fixes-7-vulnerabilities-and-1-critical-flaw/592109/"
guid: "https://www.searchenginejournal.com/wordpress-7-1-3-fixes-7-vulnerabilities-and-1-critical-flaw/592109/"
author: "Roger Montti"
categories:
  - "News"
  - "WordPress"
---

# WordPress 7.1.3 Fixes 7 Vulnerabilities And 1 Critical Flaw via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-10-06
- URL: https://www.searchenginejournal.com/wordpress-7-1-3-fixes-7-vulnerabilities-and-1-critical-flaw/592109/
- Author: Roger Montti
- Categories: News, WordPress

## RSS 摘要

WordPress 7.1.3 fixes seven security vulnerabilities and a critical bug affecting image uploads that can result in a fatal error. The post WordPress 7.1.3 Fixes 7 Vulnerabilities And 1 Critical Flaw appeared first on Search Engine Journal .

## 原文正文

WordPress 7.1.3 Fixes 7 Vulnerabilities And 1 Critical Flaw Skip to content

SEJ Pro Sign In

Webinar: How to bring AI search into your SEO reporting

Register Now

- SEJ

- ⋅

- WordPress

## WordPress 7.1.3 Fixes 7 Vulnerabilities And 1 Critical Flaw

WordPress 7.1.3 addresses seven security vulnerabilities and fixes a critical flaw that can make image uploads fail with a fatal error.

WordPress announced a security release to address seven security vulnerabilities plus four bug fixes. This security release, Version 7.1.3, addresses a stored XSS, denial-of-service DoS and five other vulnerabilities of undisclosed severity level. WordPress recommends updating sites immediately.

### Seven Vulnerabilities

WordPress names seven vulnerabilities:

- Stored XSS

- DoS issue

- Second-Order SQL injection

- Weakness allowing Author role users to sticky posts

- Unauthenticated disclosure of comments

- Imgur embeds vulnerable to XSS

- Forgeable parameters that can lead to action name collision

The official announcement does not list severity ratings, CVSS scores,describe the vulnerabilities, or offer information of whether these vulnerabilities are being exploited in the the wild. However, WordPress recommends updating immediately.

The security fixes are also being backported to older WordPress branches eligible for security fixes, currently extending through WordPress 4.7, although those backports are still in progress. Backports will ship for older branches as they become ready.

### Bug Fixes

The four bug fixes include three relatively benign issues that cause a poor user experience plus one that is critical.

Two of the bug fixes address oEmbed endpoints that return a 404 message. One is related to a music promotion platform and the other an eCard humor site. One of the fixes addresses a bug that may cause a website icon image in the admin to toolbar expand to gigantic proportions. The fourth can lead to a fatal error that sounds bad but probably isn’t that bad.

### Critical Flaw Leads To Fatal Error

The fourth is a critical WordPress bug can make image uploads fail with a fatal error on hosts lacking an optional DOM library, leaving site owners unable to upload media. The WordPress ticket for this issue says that the image upload process stopped completely, so the image could not be uploaded. That sounds less bad than a complete page or site failure.

The missing component is PHP’s DOM extension (ext-dom), which provides the DOMDocument and DOMXPath classes WordPress was trying to use. The reason this problem may have arisen is that WordPress strongly recommends the extension but does not require it.

WordPress 7.0 introduced code that used DOMDocument without first checking whether the extension existed. On hosts without it, image uploads could trigger a fatal error and fail completely.

The WordPress ticket for this issue rates the bug as critical, but a core committer also indicated it was probably rare: the code had been released for 134 days before the first report, which implies that nearly all hosts already provide the DOM extension and that the critical flaw is not widespread.

Official announcement here .

Featured Image by Shutterstock/Yes058 Montree Nanta

Category News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/wordpress-7-1-3-fixes-7-vulnerabilities-and-1-critical-flaw/592109/)
