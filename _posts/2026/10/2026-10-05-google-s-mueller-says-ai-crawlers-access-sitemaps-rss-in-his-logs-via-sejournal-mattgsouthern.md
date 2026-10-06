---
layout: post
title: "Google’s Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs via @sejournal, @MattGSouthern"
date: 2026-10-05T22:47:18+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-05/Google’s Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/googles-mueller-says-ai-crawlers-access-sitemaps-rss-in-his-logs/592012/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# Google’s Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-05
- URL: https://www.searchenginejournal.com/googles-mueller-says-ai-crawlers-access-sitemaps-rss-in-his-logs/592012/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Google's John Mueller says AI training crawlers usually don't offer sitemap submission and suggests default sitemap names or RSS feeds to help them find sites. The post Google’s Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs appeared first on Search Engine Journal .

## 原文正文

Google's Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs Skip to content

SEJ Pro Sign In

Ebook: State Of Search 2027

Download The Report

- SEJ

- ⋅

- AI Search

## Google’s Mueller Says AI Crawlers Access Sitemaps & RSS In His Logs

- Mueller says AI training crawlers usually offer no submission option, so he suggests default names.

- He says he has seen AI crawlers access his sitemap and RSS files.

- He tied "Couldn't fetch" on valid sitemaps to host load and crawl demand.

Google's John Mueller says AI training crawlers usually don't offer sitemap submission and suggests default sitemap names or RSS feeds to help them find sites.

Google’s John Mueller says AI training crawlers usually don’t give site owners a way to submit a sitemap, and he suggests a default file name or an RSS feed for sites that want those crawlers to find their content.

He made the comments with Martin Splitt in the Oct. 1 episode of Google’s Search Off the Record podcast , titled “Do sitemaps still matter?” He also said he has seen AI crawlers access his sitemap and RSS files in his own server logs.

### Private Sitemaps And AI Crawlers

Mueller said site owners who want to keep a sitemap private can give it an unusual file name, leave it out of robots.txt, and submit it to Google directly. The downside is that other systems can’t find it, he said, and Bing would probably need its own submission.

AI training crawlers are different because “they usually don’t have any kind of a Console or any setup where you can submit a sitemap file.” For sites that want their content in AI systems, he suggested “either you stick to the generic naming, call it sitemap.xml, or you focus on RSS feeds.”

The sitemaps protocol says a robots.txt Sitemap line is independent of the user-agent line, so it isn’t tied to any one crawler’s rules. Feeds are easier to find, he noted, because they’re usually linked from a page’s HTML head.

“I’ve seen that happen in my server logs where some AI crawler accesses my sitemap file,” he said, and he’s seen the same with his RSS files. He didn’t name the crawlers and said he doesn’t know whether AI companies document this or what they do with the files.

### Llms.txt Isn’t A Sitemap Substitute

Asked whether llms.txt could replace an XML sitemap, Mueller compared the Markdown file to an HTML sitemap and said Google’s systems can’t use it as a sitemap because it lacks the strict format.

“I think the hope is bigger than the reality,” he said, allowing that search systems might read Markdown files someday. “Currently none of this happens.” He’s fine with sites trying it but wouldn’t rely on it.

In August, he said the only crawlers on his test sites that claimed to accept Markdown were SEO tools. In May, I covered Google’s AI optimization guide listing llms.txt among the tactics sites don’t need for generative AI features.

### Why A Valid Sitemap Can Show ‘Couldn’t Fetch’

Splitt closed by asking why Search Console reports “Couldn’t fetch” for a valid, public sitemap linked from robots.txt.

Mueller said one reason is host load. Google’s systems may be too busy to fetch the sitemap, and Search Console reports that as “Couldn’t fetch” too. The other is crawl demand, which can lead Google to skip the sitemap when its systems see no need to crawl much more from a site.

“And the crawl demand is very often based on the perceived quality of a website,” he said, adding that “it’s not purely a technical thing.” In February, he told a Reddit user that Google won’t use a sitemap if it isn’t convinced there’s new and important content to index.

Search Console’s Sitemaps report help page lists low crawl demand among the reasons a sitemap can’t be fetched and says better content brings more crawl demand. Other reasons it gives include robots.txt blocks, unresolved manual actions, and wrong URLs.

### Why This Matters

A sitemap with an unusual name and no robots.txt entry stays hidden from systems it isn’t submitted to, according to Mueller, and AI training crawlers usually don’t offer a way to submit one. He suggested a default sitemap name or an RSS feed for sites that want AI crawlers to find their content. A robots.txt listing also tells crawlers that support the Sitemap directive where the file is.

For a valid sitemap showing “Couldn’t fetch,” both causes Mueller described, host load and crawl demand, sit outside the file itself.

### Looking Ahead

Google’s Search Relations lead advised working from what’s documented now rather than planning around llms.txt. Server logs are where he saw AI crawlers reach his files, and they’re where you can check your own.

Featured Image: Tetiana Yurchenko/Shutterstock. Google wordmark: Source: Google.

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/googles-mueller-says-ai-crawlers-access-sitemaps-rss-in-his-logs/592012/)
