---
layout: post
title: "ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them via @sejournal, @MattGSouthern"
date: 2026-10-26T12:24:23+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-26/ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/chatgpt-brand-mentions-cited-pages-graphite/594379/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-26
- URL: https://www.searchenginejournal.com/chatgpt-brand-mentions-cited-pages-graphite/594379/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Brands logged-out ChatGPT rarely named without search also showed up less when it searched, even with cited-page coverage, in new comparison-prompt data. The post ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them appeared first on Search Engine Journal .

## 原文正文

ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them Skip to content

SEJ Pro Sign In

AI Search Tracking Checklist: How to Attribute Calls From ChatGPT, Claude, and Perplexity

Download the Checklist

- SEJ

- ⋅

- AI Search

## ChatGPT Rarely Named Some Brands Even When Sources Mentioned Them

- In comparison prompts, brands ChatGPT rarely named without search rarely showed up with it.

- The pattern held even for brands mentioned on many of the pages ChatGPT cited.

- The agency behind the data argues brands should also target AI training data.

Brands logged-out ChatGPT rarely named without search also showed up less when it searched, even with cited-page coverage, in new comparison-prompt data.

Brands that ChatGPT rarely named when answering without using search results were generally the brands ChatGPT rarely named when it did a search (even when those brands were included in many of the web pages ChatGPT referenced). This is the primary result from an Oct. 16 analysis by Graphite comparing logged-out ChatGPT responses for comparison prompts with search versus without it.

Among brands substantially mentioned on at least 15% of cited pages, median visibility with search was 11% when ChatGPT named them in under a quarter of its no-search answers. Graphite, a growth agency that sells AEO services, argues brands should work on what AI models learn in training as well as on citations, and calls that parametric knowledge optimization (PKO).

### Search Visibility Rose With Visibility Without Search

Graphite’s comparison uses entity-comparison prompts, which ask ChatGPT to compare brands or products, from its Aug. 20 paper on prompt tracking . It covers 3,115 entity-question pairs across 57 questions, collected in August from logged-out ChatGPT. Visibility is the share of responses that mention a brand or product.

For answers that used search, Graphite also measured the share of cited pages that substantially mentioned each brand and split brands into three groups by that share. In all three groups, brands ChatGPT named more often without search were named more often with search.

There was an increase in visibility via search along with an increase in the share of cited pages mentioning the brand. According to Graphite, this suggests that both factors matter. Graphite states that there is the same relationship (with comparable strength) in two replications. The first replication used 100 prompts through the API with search explicitly enabled and disabled; the second used 200 prompts tracked through Graphite’s tracking tool during a different three-week time frame.

The 57-question comparison was based upon data from Graphite’s Aug. 20 paper comparing forcing ChatGPT to use search versus not forcing ChatGPT to use search. In the Aug. 20 paper, Graphite defined whether a response utilized search if a fan-out query or search result was included in the response. However, the Oct. 16 write-up does not explain how Graphite separated out responses that did not utilize search for the comparison. Graphite has described only the 100-prompt API replication as having been conducted while explicitly disabling search.

According to Graphite, early evidence exists that what a model learned during training affects how a model utilizes search results. Additionally, the write up does not include descriptions of control variables for the degree of awareness of each brand, and the data indicate that visibility of each brand with and without search increased together.

### Brand Names In ChatGPT’s Background Searches

Graphite also counted brand names in about 957,000 ChatGPT fan-out queries, the background searches it runs before answering. The queries came from 22,953 non-branded entity-comparison prompts collected from August to early October. Of those queries, 59.6% contained a brand, as labeled by Anthropic’s Claude Haiku 4.5 model, and 22.7% used a site: operator.

None of the prompts named a brand. Graphite says a brand in a fan-out query raises the chance that pages featuring that brand get retrieved.

Suganthan Mohanadasan found a similar pattern in a smaller test he wrote about for SEJ in August . In 21 of the 27 conversations on a single logged-in account, ChatGPT’s first search query included brand names he hadn’t typed.

### ChatGPT Citation Rates In Comparison Prompts

Between two weeks of entity-comparison prompts in Graphite’s tracking tool, where there is a fixed set of prompts, the percent of logged-out ChatGPT responses with citations rose from 56.6% (week of Aug. 3) to 88.5% (week of Sept. 28). At the same weeks, for logged-out Gemini, the percent was 79.0%, then 81.2%.

Graphite says this increase suggests increased frequency of search usage and states that these percentages have changed over time and could go down.

A citation alone does not necessarily indicate a search occurred. In an earlier paper by Graphite regarding prompt tracking, it noted that as of May, ChatGPT could add inline links without displaying any evidence of a search.

In its October fan-out report , which I covered on Oct. 12 , Ahrefs reported that 14.4% of 66.6 million free, logged-out ChatGPT responses in August and September included fan-out queries. These statistics do not correspond directly. Ahrefs counted responses with fan-out queries across general prompts based upon search volume for all topics and countries; Graphite counted responses including a citation for comparison prompts.

### Model Cutoffs And Training Data Controls

Graphite used the publication date of each model, along with the knowledge cutoff the vendor reported, to calculate the time period in days between each model’s stated knowledge cutoff and the release of that model. For Anthropic, Graphite used the training data cut-off instead of the earlier reliable knowledge cut-off, for comparison across all three AI vendors. For models released since July, the time periods for these vendors were approximately two to five months. Graphite states this difference is referred to as “the minimum time-to-impact for newly published content.” This calculation does not measure when an article is crawled into the training set or if the model’s answers change.

The methods that Graphite proposes are exploratory. One method involves checking brand visibility via an API, after searching has been turned off, when a new model has shipped. At least 50 responses need to be collected for a given prompt. A second method involves allowing training crawler access to a website; this includes checking whether there are any restrictions placed on the crawlers due to CDNs or firewalls.

Google’s crawler page says Google-Extended, its robots.txt token for Gemini, controls whether Google can use crawled content for training future Gemini models and for grounding in Gemini Apps and in Grounding with Google Search on Vertex AI. Google says the token doesn’t affect a site’s inclusion in Google Search and isn’t used as a ranking signal there.

### Why This Matters

Citation share and cited-page mentions are created based upon the references ChatGPT identifies in its responses, so they leave out how often it names a company for an item where it doesn’t conduct a search. For Graphite’s comparison prompts, brands ChatGPT rarely identified as a company name without conducting a search stayed low when it did, even when those companies were referenced on at least 15% of the cited pages. Tracking your prompts through the API using search set to off when there is a new model released provides a no search baseline. As shown in the data, visibility with search increased alongside both visibility without search and cited-page mentions; however, the data doesn’t show that increasing either will increase the frequency of a brand being mentioned by ChatGPT when it does search.

### Looking Ahead

Graphite says to expect at least the 2-5 months between cutoff and release for new material to appear in an AI model. Graphite adds that because AI labs do not publicly disclose what they used to train (their data), it isn’t known which pages were included. ChatGPT’s citation rate increased in Graphite’s comparison prompts from early August through late September. So, search-on tracking will need to be repeated as well.

Featured Image: Samuel Boivin/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/chatgpt-brand-mentions-cited-pages-graphite/594379/)
