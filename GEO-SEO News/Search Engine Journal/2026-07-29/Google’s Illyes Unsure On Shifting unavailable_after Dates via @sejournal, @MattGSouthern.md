---
title: "Google’s Illyes Unsure On Shifting unavailable_after Dates via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-07-29T07:00:06+00:00
fetched_at: 2026-07-29T22:28:19.968691+00:00
url: "https://www.searchenginejournal.com/googles-illyes-unsure-on-shifting-unavailable_after-dates/584064/"
guid: "https://www.searchenginejournal.com/googles-illyes-unsure-on-shifting-unavailable_after-dates/584064/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Technical SEO"
---

# Google’s Illyes Unsure On Shifting unavailable_after Dates via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-07-29
- URL: https://www.searchenginejournal.com/googles-illyes-unsure-on-shifting-unavailable_after-dates/584064/
- Author: Matt G. Southern
- Categories: News, Technical SEO

## RSS 摘要

Google's Gary Illyes said he would need to check whether pushing an unavailable_after date forward on every renewal causes problems. He gave a first read. The post Google’s Illyes Unsure On Shifting unavailable_after Dates appeared first on Search Engine Journal .

## 原文正文

Google's Illyes Unsure On Shifting unavailable_after Dates Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- Technical SEO

## Google’s Illyes Unsure On Shifting unavailable_after Dates

- Illyes said he does not know whether rolling expiry dates cause problems.

- Google has to crawl the page again before it can see a changed date.

- Until Google says more, sites renewing listings are working without a documented answer.

Google's Gary Illyes said he would need to check whether pushing an unavailable_after date forward on every renewal causes problems. He gave a first read.

Google’s Gary Illyes said on LinkedIn that he’d have to check whether a site can safely extend an unavailable_after date. His first read, which he called a gut feeling, was that pushing the date forward is fine, but he left open whether the tag can be trusted for pages that expire and then get renewed.

### What Was Asked

SEO consultant Javier Lorente Murillo reached out to Google’s Search team with a question about a classifieds site that has a steady core of around 5,000 indexed URLs and adds approximately 10,000 new listings each month. Most of these listings stay live for 24 to 72 hours.

He planned to use unavailable_after on short-lived pages to avoid 404 errors and manage crawl budget. Because users can renew ads, his system would dynamically update the expiry date. He asked whether Googlebot would start to ignore a date that keeps changing with each renewal.

### What Illyes Said

Illyes opened by saying he didn’t know:

“that’s a great question… I have no idea, I have to check.”

He added:

“my gut feeling is that it’s fine to push forward the unavailable_after date BUT you need to keep in mind that we’ll need to crawl the page again to “see” the new date. it doesn’t have implications on anything but index selection, where it acts as a “you can drop this now” signal.”

In a later response to another comment on the same post, he said Google would fetch the page instead of checking it cheaply:

“we rarely see HEAD requests so we’d still download the content.”

### What Google’s Documentation Says

Google’s robots meta tag documentation explains ‘unavailable_after’ as a rule instructing Google not to display a page in search results after a specified date and time. The same page says Googlebot will crawl that URL considerably less often after that date.

The page also talks about the recrawl point Illyes mentioned, highlighting that Robots meta tags and X-Robots-Tag headers are detected when a URL is crawled. This means that a changed date will only appear on the next fetch.

That part of his answer echoes what Google already states. The claim that the rule touches nothing beyond index selection is his own, and it doesn’t appear in the docs.

### Why This Matters

Illyes didn’t say what happens if the last date Google saw passes before it gets back to the page. That is the case he said he would have to check.

With the renewal case unanswered, there’s nothing from Google to plan around. What decides the outcome is how often Google crawls the page, and a site owner can’t control that.

### Looking Ahead

As of publication, Google’s documentation doesn’t cover an expiry date that changes on every renewal.

The first call is what you’re asking the unavailable_after tag to do. Letting a page drop out of search results after a set date is what Google documents it for. Keeping a page alive while leaning on the tag to manage crawl is the case that’s still open.

Featured Image: ESB Essentials/Shutterstock

Category News Technical SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/googles-illyes-unsure-on-shifting-unavailable_after-dates/584064/)
