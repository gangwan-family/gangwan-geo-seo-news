---
title: "Google Recommends Using 304 Status Code To Conserve Crawl Budget via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-03T12:55:15+00:00
fetched_at: 2026-08-03T22:32:31.168973+00:00
url: "https://www.searchenginejournal.com/google-recommends-using-304-status-code-to-conserve-crawl-budget/584543/"
guid: "https://www.searchenginejournal.com/google-recommends-using-304-status-code-to-conserve-crawl-budget/584543/"
author: "Roger Montti"
categories:
  - "News"
  - "SEO"
---

# Google Recommends Using 304 Status Code To Conserve Crawl Budget via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-03
- URL: https://www.searchenginejournal.com/google-recommends-using-304-status-code-to-conserve-crawl-budget/584543/
- Author: Roger Montti
- Categories: News, SEO

## RSS 摘要

Google's updated crawl budget documentation recommends serving a 304 response code to Googlebot for pages that haven't changed. The post Google Recommends Using 304 Status Code To Conserve Crawl Budget appeared first on Search Engine Journal .

## 原文正文

Google Recommends Using 304 Status Code To Conserve Crawl Budget Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- SEO

## Google Recommends Using 304 Status Code To Conserve Crawl Budget

Google's updated crawl budget documentation recommends serving Googlebot a 304 server response code for pages that haven't changed.

Google updated its crawl budget documentation with new information about how Google’s different crawlers all share a website’s crawl capacity and added a recommendation to use a 304 server response to reduce the amount of server resources used by crawlers.

Both of these additions are to Google’s Optimize Your Crawl Budget Documentation that is for enterprise websites with over a million pages and medium sized websites of over 10,000 web pages that rapidly change. Although the documentation is not aimed at every website, the information on that page is useful for understanding how crawling works.

### Google’s Crawlers Share A Website’s Crawl Capacity

Google added the following passage:

“While each crawler has a different crawl demand, the crawl capacity limit is shared across all crawlers. This means that high demand from one crawler can reduce the capacity available for others.”

This means that if a site gets crawled by Googlebot-Image and Googlebot, both of the crawlers are sharing the crawl budget for the website. The impact is that a high rate of crawling by one bot can reduce the capacity available to other Google crawlers.

### Google Recommends 304 Server Response

The other interesting recommendation that Google added was the suggestion to use 304 Not Modified server response code. According to the Mozilla Developer Network web documentation:

“The HTTP 304 Not Modified redirection response status code indicates that there is no need to retransmit the requested resources.”

The thing about the 304 Not Modified response code is that there is no redirection happening, even though technically all 3xx server response codes are classed as redirection codes. Despite that technical detail, nothing is being redirected.

Google’s updated documentation says:

“Use HTTP caching: Support 304 (Not Modified) HTTP status codes. If a page hasn’t changed since Google last crawled it, returning a 304 code tells Google to reuse the cached version, saving your server bandwidth and resources.”

A 304 Not Modified response tells Google’s crawlers that a page has not changed since the last time it was crawled. The result is that the server doesn’t serve the page to Googlebot and Googlebot can go focus on indexing other pages.

Read Google’s updated documentation here . The two changes described here are the only new additions. There are other changes that here and there that make Google’s documentation more precise, which is documented here .

Category News SEO

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-recommends-using-304-status-code-to-conserve-crawl-budget/584543/)
