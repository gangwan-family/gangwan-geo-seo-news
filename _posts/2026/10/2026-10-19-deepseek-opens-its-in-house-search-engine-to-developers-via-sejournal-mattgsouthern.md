---
layout: post
title: "DeepSeek Opens Its In-House Search Engine To Developers via @sejournal, @MattGSouthern"
date: 2026-10-19T15:02:15+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-19/DeepSeek Opens Its In-House Search Engine To Developers via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/deepseek-opens-its-in-house-search-engine-to-developers/593526/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# DeepSeek Opens Its In-House Search Engine To Developers via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-19
- URL: https://www.searchenginejournal.com/deepseek-opens-its-in-house-search-engine-to-developers/593526/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

A Chinese AI lab opened its search engine to developers. Each result carries a page-level authority tier, and DeepSeek says it filters GEO manipulation. The post DeepSeek Opens Its In-House Search Engine To Developers appeared first on Search Engine Journal .

## 原文正文

DeepSeek Opens Its In-House Search Engine To Developers Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- AI Search

## DeepSeek Opens Its In-House Search Engine To Developers

- DeepSeek opened its in-house search engine to developers and says it filters GEO manipulation.

- Each result includes an authority tier for the page and a relevance score.

- Site: queries return some of your indexed pages along with each page's authority tier.

A Chinese AI lab opened its search engine to developers. Each result carries a page-level authority tier, and DeepSeek says it filters GEO manipulation.

DeepSeek opened its in-house search engine to developers on Oct. 17, and the company’s changelog says the engine filters SEO spam, “GEO manipulation,” and low-quality AI-generated content.

Each result from the new Search API includes an authority tier for the page and a relevance score, and the API accepts site: queries that limit results to one domain.

### What DeepSeek Says About Its Engine

DeepSeek’s changelog says its in-house engine handles search on its website and in its API, indexes hundreds of billions of web pages, and takes in hundreds of millions of search requests a day from around the world.

GEO (generative engine optimization) is when you shape your content to be cited by AI answer engines. DeepSeek’s changelog states that they credit strict detection as the source of filtering; however, it has not defined what GEO manipulation is or described how their detection process operates. On May 15, Google said “our spam policies also apply to generative AI responses in Google Search.”

The privacy policy of DeepSeek was last revised Feb. 10, which states that the company integrates “third-party APIs to provide search services” and shares users’ input keywords with these companies. A Chinese-based search API company called Bocha states they are the official web search supplier of DeepSeek in the customer section of a GitHub README for one of their products. DeepSeek does not reference Bocha in their launch pages. The changelog and the privacy policy do not state if any web search queries are still sent to a third party service. Dan Petrovic from DEJAN referenced both the privacy policy and the GitHub README in his post about the DeepSeek launch.

### What The Search API Returns

Each Search API result contains an authority field; authority fields range from 0 to 4 with -1 being unknown. According to DeepSeek’s API reference , pages with tiers of 3+ are described as “highly authoritative” sources.

The rerank score (another field) is a scale of 0-3 and incorporates signals that include relevance, authority and freshness. A rerank score of 1.5+ is considered high quality. The guide and the reference do not explain how a page receives its tier or score.

Each result also comes with a snippet for display, typically 100 to 200 characters, and a summary meant for a model to read, typically 600 to 800 characters. Page content comes back too when a request asks for it and the content is available. Queries can be limited with site: and filtered by language and date published.

Search and Fetch each cost $0.75 per 1,000 successful requests. Searches that return no results aren’t billed, and requesting 50 results costs the same as requesting just one.

### What DeepSeek’s Pages Say About Crawling

DeepSeek’s Fetch API was released with Search. Fetch provides a single Markdown page and “is subject to the target site’s availability and access policies,” as per the guide.

According to the EU summary of the data used to train DeepSeek-V4, the crawler is “designed to respect robots.txt instructions and other standard web protocols, where applicable.” However, the summary does not identify which crawler this refers to.

Additionally, none of the launch pages (the guide, API references, changelog and announcement ) provide identification of a crawler for the search index nor do they provide information on what user agent Fetch uses.

In addition to providing information about several crawlers, the Known Agents bot directory lists a DeepSeekBot user agent and describes it as an AI training data crawler.

### Why This Matters

With a funded DeepSeek API account, individual site: searches are under $0.01. Each site: search can return up to 50 pages from your website; each page has both an authority tier and a relevance score for that query. If you see a missing result, it could be because the page was either outside the index or caught by filters described in DeepSeek’s changelog, or because it was excluded for some other reason; neither the user guide nor the API reference provides a method to figure this out.

Robots.txt rules intended to block DeepSeekBot are targeted against a crawler that the Known Agents bot directory describes as being associated with training data. It does not appear from DeepSeek’s initial launch pages if such a rule will affect what is included in DeepSeek’s search index.

### Looking Ahead

If you use Claude Code, Codex, or DeepSeek Harness with the DeepSeek API, your server-side searches and page fetches are already handled through the Search and Fetch APIs at no cost. Billing for these server-side calls will begin on Oct. 31 at 16:00 UTC (noon ET).

Watch DeepSeek’s docs for a definition of GEO manipulation, details on how tiers are set, and a named crawler for the index.

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/deepseek-opens-its-in-house-search-engine-to-developers/593526/)
