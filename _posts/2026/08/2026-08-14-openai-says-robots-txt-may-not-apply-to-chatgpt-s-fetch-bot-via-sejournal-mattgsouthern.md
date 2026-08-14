---
layout: post
title: "OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot via @sejournal, @MattGSouthern"
date: 2026-08-14T19:10:07+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-14/OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-08-14
- URL: https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

New data shows ChatGPT's page-fetching bot is reaching sites that have disallowed it, and OpenAI's own documentation explains why the file may not stop it. The post OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot appeared first on Search Engine Journal .

## 原文正文

Some AI Agents Reach Pages Sites Told Them To Skip Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- AI Search

## OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot

- One AI bot reached disallowed pages on more sites than any other tracked.

- OpenAI says robots.txt may not apply to bots a person triggered.

- A disallow line is a request, and some agents are documented as ignoring it.

New data shows ChatGPT's page-fetching bot is reaching sites that have disallowed it, and OpenAI's own documentation explains why the file may not stop it.

ChatGPT’s page-fetching bot is disallowed by more sites than any other AI bot of its kind. It also reached disallowed pages on more sites than any other bot. OpenAI says robots.txt rules may not apply to it because a person asked for the page.

TollBit’s latest State of the Bots report has the numbers for the first half of 2026. Here’s what else the data shows about how these crawlers behave and what it means for your site.

### Where The Bypasses Land

In the European sites discussed in the report, about 15% of identified AI page-fetchers reached URLs that the sites had marked as disallowed.

This happens mostly with a few specific agents. For example, ChatGPT-User, Bytespider, and Youbot each accessed disallowed pages on nearly half of the European sites that had explicitly listed them. Among these, ChatGPT-User reached the most sites.

### Sites Did Disallow It

Many of the newer page-fetching agents are hardly blocked at all. Only 9% of European websites disallow Claude-User, compared to 26% in North America. Perplexity-User sits at 13% versus 26%.

Most of the newest agents have disallow rates in the single digits across Europe, but ChatGPT-User stands out as an exception.

### What OpenAI Says About The Rule

OpenAI’s crawler documentation says ChatGPT-User visits a page when a ChatGPT user asks a question, and that because those actions are initiated by a user, robots.txt rules may not apply.

Perplexity says Perplexity-User generally ignores the file for the same reason, but Anthropic has a different view and states that all three of its bots respect it, as we reported in February . TollBit treats any request to a disallowed URL as a bypass, regardless of what the operator claims.

### Why This Matters

A disallow line for ChatGPT-User is a request that OpenAI’s documentation says may not apply.

It’s important to look at a different aspect here. According to OpenAI’s documentation, the agent responsible for deciding if a site shows up in ChatGPT search results is called OAI-SearchBot, not ChatGPT-User. Sites that block both agents to prevent AI traffic have traded away the visibility half of that deal and kept a fetching control that carries a carve-out.

Server logs or CDN records show what actually arrived. The file only shows what you asked for.

### Looking Ahead

Cloudflare is making some updates to how it manages its crawler controls, moving the decision to the network layer. When it comes to the bots it recognizes, compliance is no longer left up to the crawler itself. Starting from September 15 , new domains added to Cloudflare will have their Training and Agent crawlers blocked by default on pages with ads, while Search crawlers remain allowed.

Whether the user-initiated loophole survives is the open question. It rests on the argument that requesting a page differs from a crawler taking it, and now all major assistants fetch pages this way.

Featured Image: Net Vector/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/)
