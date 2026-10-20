---
title: "ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-20T15:00:36+00:00
fetched_at: 2026-10-20T23:59:08.859444+00:00
url: "https://www.searchenginejournal.com/chatgpt-search-can-draw-on-more-pages-after-a-cloudflare-pilot/593720/"
guid: "https://www.searchenginejournal.com/chatgpt-search-can-draw-on-more-pages-after-a-cloudflare-pilot/593720/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-20
- URL: https://www.searchenginejournal.com/chatgpt-search-can-draw-on-more-pages-after-a-cloudflare-pilot/593720/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Cloudflare says its network signals helped OpenAI index hundreds of millions of new pages for ChatGPT search. The post ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot appeared first on Search Engine Journal .

## 原文正文

ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- AI Search

## ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot

- The companies say Cloudflare's network signals helped OpenAI find and index new pages.

- The signals also help the crawler skip dead URLs and spot changed pages.

- OpenAI ranks the pages on its own, and crawler access settings still apply.

Cloudflare says its network signals helped OpenAI index hundreds of millions of new pages for ChatGPT search.

Cloudflare and OpenAI say a research pilot has helped OpenAI discover and index hundreds of millions of new web pages. The pilot used a participating cohort of about 1% of Cloudflare’s total network.

The companies shared those early results on Oct. 15 in a post on Cloudflare’s blog coauthored by two OpenAI staff. Cloudflare announced the pilot on July 8.

The post says finding new pages can initially increase crawling, and it doesn’t report how often the new pages were cited in ChatGPT or how many visits they sent.

### How Cloudflare’s Signals Help OpenAI Find Pages

Cloudflare’s network signals are used by OpenAI to help its search crawler find web pages with value. The blog post gives several examples of these pages, such as the user guide of a particular washing machine, the most recent information regarding passport requirements and fees and a restaurant’s menu and hours. It states that these pages “can be valuable even if few other sites link to them.”

The July 8 announcement stated some of the new signals that will be utilized, including how recently a page has been updated, the quality of traffic to a website and what updates have actually been made to a page. Additionally, the announcement states that this information comes from participating websites. However, neither announcement explains who participated, nor whether the new pages are on their sites.

### What The Signals Do To Crawling

The Oct. 15 post states that Cloudflare’s signals will also assist in helping OpenAI’s crawlers avoid unnecessary requests. Bots make repeated attempts to obtain files that are not available on the server, some websites redirect nearly any address to their homepages, and other addresses lead to copies of the same content. Change signals indicate to the crawler whether a particular webpage should be visited again versus if there would be no value from doing so.

The companies are also testing signals that flag potentially harmful pages. Their example is a fake login form an attacker planted on one page of a legitimate site, where the goal is to flag that page rather than the whole domain. Early results suggest the signals can help identify pages to keep out of an index, the post says.

The post says the goal is to reduce unnecessary load for Cloudflare customers, though it doesn’t provide figures for crawl volume or server load. It also says, “Finding new pages can initially increase crawling as those pages are evaluated and indexed.”

### Crawler Settings Still Decide Access

The October 15th blog post includes the statement “A signal about a page doesn’t grant permission to access it.” The blog also states that the researchers are using metadata from the web to improve search and discovery capabilities of their search engines versus sharing page content for model training.

The document describing how OpenAI’s crawler works divides search and training into two separate robots.txt directives. So if a website blocks OAI-SearchBot (the robot searching for information) then the website will not be included in ChatGPT’s search engine results; however, the blocked websites may still appear as navigational links. If a website allows the crawling by both bots (GPTBot (the bot collecting content that may be used for training), and OAI-SearchBot) then OpenAI may utilize the data collected during one crawl for both purposes.

The Oct. 15 post directs the reader to Cloudflare’s AI Crawl Control which is currently available on every plan. This service shows which AI services are accessing your website and offers you an option to Allow or Block each crawler.

### Why This Matters

ChatGPT will have another source from which to pull information once a page is in OpenAI’s index. The companies state that OpenAI independently evaluates and ranks the pages it indexes, so there is no guarantee of getting cited when your pages are found through their pilot.

Allowing OAI-SearchBot while blocking GPTBot means that your site remains accessible via the search results for ChatGPT but indicates that your crawled content should not be used for training purposes. OpenAI has provided this same configuration as an example on their crawler page.

Tracking ChatGPT visits depends on a UTM tag or a referrer, and some ChatGPT links lacked both earlier this month, as I reported Oct. 15 . One analyst said a fix began rolling out that day.

### Looking Ahead

Cloudflare and OpenAI say that the next stage of development for this project includes improving how a web page is selected by an AI, testing more rapid and reliable indicators for changes to content, and measuring the results when the AI has found new content.

According to Cloudflare, they are currently working with OpenAI to determine how improved content discovery could translate into business outcomes.

Additionally, according to a July 1 blog post from Cloudflare announcing their research on network signals and AI search, Cloudflare intends to provide broad access to that capability at some point during the remainder of 2026 (as I mentioned in my September report ). According to the Oct. 15 announcement, there was no specific date announced.

In the meantime, OpenAI’s crawler activity on your own site shows up in your server logs and in AI Crawl Control.

Featured Image: Tetiana Yurchenko/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/chatgpt-search-can-draw-on-more-pages-after-a-cloudflare-pilot/593720/)
