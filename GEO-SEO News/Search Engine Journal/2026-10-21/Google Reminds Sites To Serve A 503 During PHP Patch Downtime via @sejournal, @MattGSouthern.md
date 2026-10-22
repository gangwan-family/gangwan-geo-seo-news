---
title: "Google Reminds Sites To Serve A 503 During PHP Patch Downtime via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-21T20:19:40+00:00
fetched_at: 2026-10-22T00:03:56.030283+00:00
url: "https://www.searchenginejournal.com/google-reminds-sites-to-serve-503s-during-server-downtime/593873/"
guid: "https://www.searchenginejournal.com/google-reminds-sites-to-serve-503s-during-server-downtime/593873/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Security"
---

# Google Reminds Sites To Serve A 503 During PHP Patch Downtime via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-21
- URL: https://www.searchenginejournal.com/google-reminds-sites-to-serve-503s-during-server-downtime/593873/
- Author: Matt G. Southern
- Categories: News, Security

## RSS 摘要

Taking a site offline to patch PHP? Serve a 503 from outside PHP and keep robots.txt reachable. Days of server errors may get URLs dropped. The post Google Reminds Sites To Serve A 503 During PHP Patch Downtime appeared first on Search Engine Journal .

## 原文正文

Google Reminds Sites To Serve A 503 During PHP Patch Downtime Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- Security

## Google Reminds Sites To Serve A 503 During PHP Patch Downtime

- Google reminded sites to serve a 503 when going offline for PHP patches.

- Google's docs warn URLs returning 503s for days may be dropped from the index.

- Mueller says the 503 can be served outside PHP, through DNS changes or a CDN.

Taking a site offline to patch PHP? Serve a 503 from outside PHP and keep robots.txt reachable. Days of server errors may get URLs dropped.

Google Search Central is reminding anyone who takes servers offline for PHP patches to return a 503 status code, which tells Google the outage is temporary.

The LinkedIn post went up Wednesday, the day PHP released emergency fixes for two critical flaws that can let attackers run code without logging in.

The post doesn’t say how long a 503 can stay up. Google’s crawl rate documentation recommends against serving one for more than one to two days, because URLs that return it for multiple days may be dropped from the index.

### What Google And Mueller Said

Google Search Central wrote:

“Serving a 503 (Service Unavailable) HTTP status code ensures already indexed URLs are preserved in Search while you work. Once you start serving 200 responses again, things naturally return to normal.”

The post also warned against generic 404s or 200 error pages during the downtime. It linked to Google’s page on how HTTP status codes affect its crawlers .

In a 2013 post , Google’s John Mueller wrote that returning an error page with a 200 OK status code causes Google to index that error content.

Mueller posted his own reminder on Bluesky earlier Wednesday and said where the 503 can come from:

“If you’re taking PHP sites down to schedule time to deal with “unplanned updates”, use HTTP 503 instead of letting responses time out / 404 / 500. You can do this outside of PHP / point DNS elsewhere / CDN.”

The 2011 Google post he linked shows how to send a 503 with PHP code, which won’t help when PHP is what’s coming down.

In a reply, a Bluesky user ranked the responses roughly, from best to worst, as 503, 500, 403, 404 and 200. Mueller called it “a good model.”

### How 503s Affect Crawling

Google’s crawl rate documentation lists 500, 503, and 429 responses as the way to urgently reduce crawler traffic for a short period. When Google’s crawlers hit a large number of URLs returning those status codes, they reduce the crawl rate across the entire hostname, including URLs that still return content. Once the number of errors drops, Google automatically increases the crawl rate again.

When returning a 503 or 429, you can add a Retry-After HTTP header that tells Google’s crawlers when to try again, either as a number of seconds or as a date and time in UTC.

Google’s crawl rate page also warns that slower crawling means Googlebot discovers fewer new pages and refreshes existing ones less often. Google Ads campaigns may be canceled or paused.

When I covered comments from Google’s Gary Illyes in 2024 , he said a 503 lasting 10-15 minutes every now and then “is not ‘extended’ by any means, so you should be fine.”

### How Long Google Recommends Serving A 503

Google’s crawl rate page warns:

“We don’t recommend that you do this for a long period of time (meaning, longer than 1-2 days) as it may have a negative effect on how your site appears in Google products. For example, in the case of Search, if Googlebot observes these status codes on the same URL for multiple days, the URL may be dropped from Google’s index.”

Google’s status codes page, the one the LinkedIn post linked to, says already indexed URLs that return server errors are “preserved in the index, but eventually dropped.”

Google’s guide to pausing a website calls disabling a whole site an extreme measure that should only last a very short time, a few days at most.

The guide also says not to return a 503 for the robots.txt file, because that blocks all crawling. It adds that Google’s systems can’t refresh titles, descriptions, metadata, or structured data on a page that returns a 503.

### Why This Matters

The 503 has to come from something that keeps running while PHP is offline, such as a CDN rule or a temporary server you’ve pointed DNS at. Your robots.txt file should keep responding normally so Google can still crawl the site. The 503 is a short-term measure, since Google’s documentation recommends against serving one for longer than one to two days.

### Looking Ahead

Sites on PHP 8.1 or older no longer get regular official updates. PHP has published limited source fixes for versions 7.4 through 8.1 for teams that build PHP themselves, and hosts or support vendors may supply their own, as Vahan Petrosyan reported for SEJ. For a closure that runs past a day or two, Google’s pause guide points to an indexable home page served with a 200 as a placeholder. Once the site returns 200s again, Google’s status codes page says crawling picks back up gradually.

Featured Image: Tetiana Yurchenko/Shutterstock

Category News Security

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-reminds-sites-to-serve-503s-during-server-downtime/593873/)
