---
layout: post
title: "Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse via @sejournal, @MattGSouthern"
date: 2026-11-07T13:00:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-07/Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/seo-pulse-rank-data-problems-pagespeed-scores-ai-training-opt-out/596104/"
author: "Matt G. Southern"
categories:
  - "SEO"
  - "SEO Pulse"
  - "_src_search-engine-journal"
---

# Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-07
- URL: https://www.searchenginejournal.com/seo-pulse-rank-data-problems-pagespeed-scores-ai-training-opt-out/596104/
- Author: Matt G. Southern
- Categories: SEO, SEO Pulse

## RSS 摘要

Rank data may carry one-word results and redirect URLs. Other updates cover PageSpeed lab scores, a shared AI training opt-out, technical SEO and AI search. The post Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse appeared first on Search Engine Journal .

## 原文正文

Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse Skip to content

Webinar: 9 AI Workflows For Better Content. Nov 18, 2 PM ET.

Save Your Spot

- SEJ

- ⋅

- SEO

## Rank Data Problems, PageSpeed Scores & AI Training Opt-Out – SEO Pulse

Rank data may carry one-word results and redirect URLs. Other updates cover PageSpeed lab scores, a shared AI training opt-out, technical SEO and AI search.

Welcome to the week’s Pulse: what you need to know about updates that are affecting how much you can rely on rank tracking data, why PageSpeed scores can go up or down on a page that has no changes and what a shared robots.txt control would mean in terms of preferences for AI training.

Here’s what matters for you and your work.

### Rank Data May Carry One-Word Results And Google Redirect URLs

Two issues in the Google results that rank tracking tools collect can throw off ranking reports. Unrelated listings can crowd a tracked page out of the collected results, and unresolved goto links can hide which page ranked.

Key facts:

In an SE Ranking review of 10,000 Google US desktop keywords published Nov. 3, 84 percent of the flagged cases were unrelated listings about a single word from the query. Of those unrelated blocks, 96.5% began at position 9 or below. A related pattern is tracked by Nozzle using a different methodology and it reports its weekly share of impacted SERPs had fallen to 1.5% in mid-October, then rose to 7.6% during the week of Oct. 26. DataForSEO states Google has implemented a mechanism to restrict the amount of goto links from a single results page that can be resolved over a given timeframe. As such, they state their High Priority and Live modes will now only resolve approximately half of goto URLs. The status page of Serper lists the limitation of goto URLs as being on Oct. 30, while SerpApi’s second incident of goto links replacing direct links, which opened on Nov. 3, still showed as Identified when last reviewed on Nov. 4.

#### Why This Matters

Check if you were dropped at a position of 9 or lower from late September on to see if your replacement URLs are about one word of your query. Also, starting with about Oct. 30 (if it was a Google redirect) compare the URL that your tracker stored versus where the redirect points. To verify which factor caused an issue use Search Console’s impression/clicks reports for the same query, as SE Ranking recommends.

Read our full coverage: Rank Trackers Find Google Results About One Word Of A Query and SERP Data Providers Say Google Is Throttling Goto Result Links

### PageSpeed Insights Scores Can Change After A Lighthouse Update

PageSpeed Insights now runs Lighthouse 13.6.0 , which updates the loading simulation used for its lab scores. As a result, your page’s score may change even if you haven’t changed anything on the page.

Key facts:

According to a post by Google’s Barry Pollard on Bluesky, the updated version of Lighthouse’s simulated FCP (First Contentful Paint) and LCP (Largest Contentful Paint) will be more accurate and will generally provide better results. He also stated that JavaScript-intensive websites would be more likely to experience the impact of this new version. The simulation used as the basis for these predictions, called Lantern, has been modified to use Chrome’s render-blocking label for every individual request made. It then defaults to using the fetch priority value if the render-blocking label cannot be found. In addition, the field data provided in the same report was based upon actual user data collected from the real world, not as part of a synthetic test like Lighthouse.

#### Why This Matters

The pre- and post-switch lab scores aren’t generated in the same simulation; therefore, some of the increase you see on pages you’ve optimized might be from the new version. Make sure each report lists the same Lighthouse version, and compare your field data, before claiming an improvement.

Read our full coverage: Google Lighthouse Update Changes How PageSpeed Insights Simulates Loading

### Google, Microsoft & OpenAI Plan To Honor A Shared AI Training Opt-Out

Google , Microsoft , and OpenAI announced on Oct. 30 that they plan to honor a shared robots.txt control for AI training preferences, based on an Internet-Draft by Anthropic’s Kevin Kelley.

Key facts:

The control is a normal robots.txt group under a policy token called __usage_ai-training , that has both Allow & Disallow rules; at this time none of these three organizations support the control, according to their publicly announced timelines. Google’s post states that it plans to treat a shared opt-out as though a site opted out of Google-Extended, when the site does not have Google-Extended defined. In addition, Google’s crawler documentation states that Google-Extended also covers grounding in Gemini Apps. Microsoft will utilize the shared control for training purposes, will introduce a separate page-level AI Grounding preference, and will cease treating NoArchive and NoCache as training and/or grounding preferences after March 1, 2027.

#### Why This Matters

A site would be able to use one robots.txt group as replacement for many per-company training rules after the companies read it; however, opting out through that group would not cover the same uses at Google and Microsoft. The documentation provided by Google regarding its robots.txt controls does not separate Gemini training from Gemini Apps’ grounding. Companies using NoArchive and/or NoCache in conjunction with Microsoft have until March 1, 2027 to switch to the new preferences.

Read our full coverage: Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out

### Mueller Expects Technical SEO To Stay Relevant For AI Search

Google’s John Mueller said AI systems “build on SEO” and that he expects technical SEO in particular to stay relevant. He spoke with David Iwanow in an interview posted Oct. 29 from Search Central Deep Dive Europe 2026.

Key facts:

Mueller also stated that AI systems crawl sites in slightly different ways using intent based on things like training versus getting the latest content; he described this as “another flavor of technical SEO”. When asked about listicle formats Mueller indicated that when tactics are effective they are likely to be mimicked poorly until the algorithms adapt and therefore establishing a solid foundation for a website is your best bet.

#### Why This Matters

Mueller placed AI crawling within technical SEO, so you can include how AI crawlers request your pages in the technical audits you already run. Just be sure to check each crawler’s access and robots.txt rules individually.

Read our full coverage: Google Says Technical SEO Remains Key For AI SEO

### OpenAI Puts ChatGPT’s Search-Like Queries At A Fifth Of Google’s

ChatGPT consumer product lead Adam Fry told Big Technology that ChatGPT’s “volume of search-like queries is now roughly one-fifth the volume of queries of Google”.

Key facts:

Fry noted each question that sends ChatGPT to the web is considered a search by ChatGPT’s developer; however, according to the article, there is no Google figure, period or market given for this comparison. Ahrefs’ referral tracker measures the source of referrals at the site level and shows Google accounts for 24.74% of tracked traffic across 118,671 sites during October with ChatGPT accounting for 0.36%.

#### Why This Matters

OpenAI’s ratio counts questions that send ChatGPT to the web, while referral data tracks visits sent to websites. To keep your channel plan clear, name the measure behind any ChatGPT size figure, because search counts and referral shares describe different things.

Read our full coverage: Google’s Search Volume Is About 5x ChatGPT’s, OpenAI Says

### Theme Of The Week: Check The Method Before The Number

A number of statistics reported by SEO teams this week require an assessment of how these statistics are collected prior to being viewed as information regarding performance for a website or channel. This week’s issue with rank data is the collection of one word results and redirect URLs; a simulated PageSpeed lab score will be affected when using a new simulation versus the previous simulation; and the size of ChatGPT will depend upon if you use search volume or total visits to determine its size. On the other hand, the planned shared opt-out would cover different uses based upon which company reads it; Mueller defined AI crawling, with its different intents, as technical SEO. When reporting changes in metrics or data from reports, this is where you should document which tracking tool or version of a tool was used as well as the criteria used (definition) to produce the report.

Top Stories Of The Week:

- Rank Trackers Find Google Results About One Word Of A Query

- SERP Data Providers Say Google Is Throttling Goto Result Links

- Google Lighthouse Update Changes How PageSpeed Insights Simulates Loading

- Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out

- Google Says Technical SEO Remains Key For AI SEO

- Google’s Search Volume Is About 5x ChatGPT’s, OpenAI Says

More Resources:

- How Rank Trackers Say They Handle Suspect Google Results

- Google Explains The Limit Of Robots.txt For AI Content Use

- Google Adds Experimental Soft Navigation Metrics To CrUX

Featured Image: Cast Of Thousands/Shutterstock

Category SEO SEO Pulse

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/seo-pulse-rank-data-problems-pagespeed-scores-ai-training-opt-out/596104/)
