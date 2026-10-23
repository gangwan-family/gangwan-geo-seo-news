---
layout: post
title: "OpenAI Details How ChatGPT’s LLM Ad Stack Selects And Serves Ads via @sejournal, @brookeosmundson"
date: 2026-10-22T16:58:09+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-22/OpenAI Details How ChatGPT’s LLM Ad Stack Selects And Serves Ads via @sejournal, @brookeosmundson.md"
original_url: "https://www.searchenginejournal.com/openai-details-chatgpt-llm-ad-stack/593857/"
author: "Brooke Osmundson"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# OpenAI Details How ChatGPT’s LLM Ad Stack Selects And Serves Ads via @sejournal, @brookeosmundson

- Source: Search Engine Journal
- Published: 2026-10-22
- URL: https://www.searchenginejournal.com/openai-details-chatgpt-llm-ad-stack/593857/
- Author: Brooke Osmundson
- Categories: AI Search, News

## RSS 摘要

OpenAI explains how a custom LLM orchestrator interprets multi-turn conversations, nominates ads for auction, and drops placements that miss response deadlines. The post OpenAI Details How ChatGPT’s LLM Ad Stack Selects And Serves Ads appeared first on Search Engine Journal .

## 原文正文

OpenAI Details How ChatGPT's LLM Ad Stack Selects And Serves Ads Skip to content

SEJ Pro Sign In

Webinar: AI Shopping: Get Your Products Found in Google & ChatGPT

Save Your Spot

- SEJ

- ⋅

- AI Search

## OpenAI Details How ChatGPT’s LLM Ad Stack Selects And Serves Ads

OpenAI details how the ChatGPT ad stack uses a custom LLM orchestrator to interpret multi-turn intent, run auctions, and serve sponsored placements.

OpenAI has shared how its ChatGPT advertising system interprets conversations, selects relevant ads, and keeps ad serving separate from organic answers.

The technical breakdown explains how a dedicated language model coordinates ad selection as a user’s needs develop across messages. It also describes why an ad can win an auction and still never appear.

OpenAI says ChatGPT Ads reached $1 billion in annualized revenue run rate less than 200 days after launch. More than 100,000 advertisers have run ads since launch, although the post does not include performance benchmarks for those advertisers.

### Ads Run Separately From Answer Generation

OpenAI says the system choosing ads runs separately from the one writing ChatGPT’s answers. Each uses its own models and code.

Both can use the conversation, but they do different jobs. As ChatGPT writes a response, the ads system checks whether there’s a relevant ad to show below it. Choosing that ad doesn’t feed back into what ChatGPT writes.

ChatGPT doesn’t wait for the ads system to choose an ad. If the ads system is slow or stops working, the answer still comes through. An ad that arrives too late won’t appear with that response.

Separate models and code give some support to OpenAI’s promise that ads won’t influence answers. To be clear, this is how OpenAI describes its system, rather than independent evidence that the separation holds in practice.

When an ad appears , it carries a sponsored label below the response. The advertising system also writes a short introduction explaining how the ad connects to the discussion. That introduction stays separate from the advertiser’s headline, description, and call to action.

To choose a relevant ad, the system can look beyond the user’s latest question. Details shared earlier in the conversation help it work out what the person needs.

### How Conversation Context Changes Ad Matching

OpenAI uses race training to explain how commercial intent can develop during a conversation. Someone might start with general training questions and ask about shoes several messages later.

Its ads system keeps track of relevant details as that discussion develops. OpenAI calls these “stateful” sessions, meaning each new message doesn’t require the system to start from scratch.

Let’s use the example of someone comparing project management software. They might explain that they run a small agency, need client approvals, and want to avoid paying for guest accounts. A later question about pricing would carry more context than a search for “project management software pricing.”

An advertiser offering free guest access could test that detail against a general message about improving productivity. The landing page would need to support the offer, and results would show whether the more specific message attracts qualified leads or customers.

When users choose personalized ads, the system can also consider available nonsensitive information from past conversations. That adds context to the conversation, but creates another challenge: recognizing which needs still apply.

OpenAI says the model must distinguish current intent from old information and hypothetical questions. Even a well-matched ad could reach someone researching a purchase months away, so relevance alone won’t tell advertisers how likely that person is to convert.

### How OpenAI’s Orchestrator Finds And Evaluates Ads

OpenAI calls the model managing ad selection the “orchestrator.” It reads the conversation and calls tools to find potential ads, check their relevance, and submit suitable options to an auction.

The process starts by turning relevant parts of the conversation into search queries. Those queries become “embeddings,” numerical representations of meaning that help the system find ads without requiring the same wording.

A conversation can generate several queries if the person has different needs. The orchestrator can also adjust its searches as it receives more information.

Once it finds potential ads, the system checks whether they’re eligible to run. These checks can include location targeting, policy restrictions, available budget, and pacing, which determines when a campaign spends its budget.

It then assesses how well each ad fits the conversation, its past performance, and the likelihood of a view, click, or conversion.

The orchestrator sends candidates to a separate auction tool, which handles final ranking, pricing, and selection. The language model helps decide which ads enter that auction; it doesn’t directly choose the winner or set the price.

OpenAI didn’t disclose how much weight each signal receives, so the breakdown offers limited guidance on how to improve an ad’s ranking. And even after the auction selects an ad, further checks determine whether it appears.

### Winning The Auction Doesn’t Guarantee An Impression

OpenAI applies another check after the auction to decide whether the selected ad fits the conversation. While an ad can meet advertising policies, its system may still find it inappropriate in a particular discussion.

An auction winner can also miss the delivery window described earlier, leaving the advertiser without an impression.

This means low impressions could reflect several issues, including relevance checks or delivery timing. Before changing bids or creative, advertisers would need to understand where their ads stopped progressing.

OpenAI says its internal logs help identify those points. They record outcomes such as searches that found no potential ads, ads that failed eligibility checks, and placements that appeared and received an interaction.

That information could help explain why a campaign has limited delivery. For example, a campaign excluded by location targeting would require a different response from one that enters auctions but rarely wins.

The post doesn’t explain how much of this information advertisers can see in their reporting. Without that visibility, they may have to test changes without knowing which part of the process is limiting impressions.

### Revenue Growth Still Leaves Advertiser Returns Unanswered

OpenAI’s $1 billion annualized revenue run rate and 100,000+ advertisers show how quickly the advertising business has grown. However, neither figure explains what advertisers earned from their spending.

The revenue figure projects a full year based on the pace of revenue at that point. It doesn’t mean OpenAI has already collected $1 billion from advertising.

The advertiser count also leaves some gaps. It doesn’t show how many advertisers remain active, returned after an initial test, or increased their spending .

Repeat spending would help show whether advertisers saw enough value to continue after an initial test. The post doesn’t provide CPA, ROAS, or conversion-rate benchmarks, either, including how results vary by industry or campaign objective.

It’s reasonable for an engineering post to focus on how the system works. But OpenAI also uses revenue and advertiser adoption to demonstrate its progress, without showing what advertisers received for that spending.

Advertisers would need to know who those results represent, how much they spent, and how OpenAI measured conversions. Averages alone could also hide substantial differences between accounts.

There’s also the question of how many sales the ads added. A campaign can receive credit for purchases from customers who would have bought anyway. The post doesn’t include controlled studies showing whether ChatGPT Ads generated additional purchases.

OpenAI’s figures establish that advertisers are spending on the platform. They leave unanswered how many are acquiring customers profitably, and how consistently.

### What This Means For Advertisers

OpenAI’s explanation gives advertisers a reason to look at the customer requirements their ads address. The project management example shows how a detail such as free guest access could become relevant during a conversation, even when the latest question only mentions pricing.

Customer research and converting search terms can help advertisers choose which requirements to emphasize. The post doesn’t suggest they need a new campaign for every variation of that discussion.

For advertisers already running ChatGPT Ads, the reporting gaps deserve attention. Before responding to low impressions with higher bids, they need to know whether their ads entered auctions, failed relevance checks, or encountered another delivery issue. OpenAI describes tracking these stages internally without explaining how much advertisers can see.

The engineering detail supports OpenAI’s explanation of how it protects answers and selects ads. Its revenue figures leave advertisers with less evidence about the return on their spending.

As more advertisers continue to test ChatGPT Ads, further disclosure from OpenAI would be most useful. Whether advertisers continued after testing, what they paid to acquire customers, and how widely those results varied is something the industry should keep an eye on in the coming months.

Featured image: Samuel Boivin / Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Brooke Osmundson Director of Growth Marketing at Smith Micro Software

Brooke serves as the Director of Growth Marketing at Smith Micro Software, with over 10 years of paid media experience. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/openai-details-chatgpt-llm-ad-stack/593857/)
