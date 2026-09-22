---
layout: post
title: "Which Data Sources Should You Care About For AI Search? via @sejournal, @chrisgreenseo"
date: 2026-09-22T19:00:31+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-22/Which Data Sources Should You Care About For AI Search via @sejournal, @chrisgreenseo.md"
original_url: "https://www.searchenginejournal.com/which-data-sources-should-you-care-about-for-ai-search/590086/"
author: "Chris Green"
categories:
  - "AI Search"
  - "_src_search-engine-journal"
---

# Which Data Sources Should You Care About For AI Search? via @sejournal, @chrisgreenseo

- Source: Search Engine Journal
- Published: 2026-09-22
- URL: https://www.searchenginejournal.com/which-data-sources-should-you-care-about-for-ai-search/590086/
- Author: Chris Green
- Categories: AI Search

## RSS 摘要

AI search pulls from more sources than most SEOs track. Here's a tiered view of which data sources deserve your attention first. The post Which Data Sources Should You Care About For AI Search? appeared first on Search Engine Journal .

## 原文正文

Which Data Sources Should You Care About For AI Search? Skip to content

- SEJ

- ⋅

- AI Search

## Which Data Sources Should You Care About For AI Search?

Search is more than “is it in Google” or “Bing”? Where should you ensure you’re getting mentioned?

If you’re new to “search,” or one of the “old guard,” there’s a risk of some kind of search source myopia. A short-sightedness around what sources really matter for your day-to-day work.

This isn’t new in AI search, but it’s another bruise that’s getting punched again, and again (and again). As AI chatbots and different tools like AI Overviews, Copilot, etc., pull from a more and more diverse range of data sources , our job gets a lot harder. And more interesting!

### It’s Hard When You Need To Be Focused On Everything

When anything is hard or challenging, that is the place you have an opportunity to really get ahead. So this is the opportunity to really start reviewing the different data sources that could be preferenced or relied upon by AI tools in the future.

I have built a table of search sources and categorised them by how useful I think they’ll be to you right now.

Using This Data

Tier

Meaning

Confirmed + current — RAG / grounding / actions

Confirmed + current — training / licensing

Confirmed historical — pretraining

Strong evidence / highly likely

Approach the Tier 1 sources with the most interest – as they’ll more-than-likely be worthwhile. Tier 2 and 3 may be less easy to achieve or even be confident they’ll be beneficial and Tier 4 are highly likely, but lacking confirmation.

AI Data Sources Reference

Tier

Typical use

Source

Evidence status

What the evidence says

Reference

Web & search discovery

Google Search

Confirmed + current

Grounding with Google Search connects Gemini to real-time web content, returning inline citations to source URLs.

Google — Gemini API docs, Grounding with Google Search

Bing Search

Confirmed + current

Microsoft documents Bing results being used to enhance Copilot responses. Not re-verified in this pass.

Microsoft Bing

Common Crawl

Confirmed historical

GPT-3 used filtered Common Crawl as roughly 60% of its sampling mixture; LLaMA 1 reported 67%.

Common Crawl

Historical web corpora (C4 etc.)

Confirmed historical

C4 is a cleaned derivative of Common Crawl; LLaMA reported C4 at 15% of its pretraining mixture.

TensorFlow Datasets — C4

Web grounding services

Strong evidence / likely

Category inference covering third-party grounding/retrieval intermediaries. No single canonical source.

Products & shopping

Google Merchant Center

Confirmed + current

Merchant feed data underpins Google’s shopping surfaces. Retained on user instruction; Google Shopping removed as it is a surface, not a source.

Google Merchant Center Help

Merchant / retail feeds (OpenAI)

Confirmed + current

Merchants share a secure, regularly refreshed CSV/JSON feed of identifiers, descriptions, pricing, inventory, media and fulfilment so ChatGPT can surface products accurately. Refreshes accepted as often as every 15 minutes.

OpenAI Developers — Agentic Commerce, product feeds

Microsoft Merchant Center

Strong evidence / likely

Equivalent commercial feed infrastructure; inferred parallel to Google Merchant Center rather than separately evidenced.

Marketplace feeds

Strong evidence / likely

Category inference. Shopify catalog data is already integrated into ChatGPT, which supports the pattern.

OpenAI Help — Shopping with ChatGPT Search

Local & places

Google Maps

Confirmed + current

Grounding with Google Maps is a documented tool alongside Search grounding, giving models geospatial context.

Google Cloud — Grounding API

Google Business Profile

Confirmed + current

Business profile data feeds Google’s local surfaces. Carried from the source table; not separately re-verified.

Yelp

Confirmed + current

Yelp licenses reviews, photos and business information to OpenAI for real-time local recommendations. Beyond grounding it also drives actions: ChatGPT users can book a table or join a waitlist, and Request a Quote lets users contact providers in-chat. Yelp’s 10-Q confirms it is live.

Axios; Yelp blog; Yelp 10-Q FY2026

OpenStreetMap

Strong evidence / likely

Widely used open geospatial corpus; inferred rather than confirmed for any named model.

Foursquare

Strong evidence / likely

Left in Tier 4 deliberately: the OpenAI deal is Yelp’s, and no equivalent evidence exists for Foursquare.

Tripadvisor

Strong evidence / likely

Category inference for review/travel data. No confirmed deal identified in this pass.

Knowledge & reference

Wikipedia

Confirmed + current

Explicitly present in GPT-3’s disclosed mixture and LLaMA (June-Aug 2022 dumps, 20 languages); also widely used as a live reference/RAG corpus.

Wikimedia dumps

Wikimedia

Confirmed + current

Same corpus family as Wikipedia. Licensing is unusually clear: principally CC BY-SA with attribution/share-alike obligations.

Wikimedia dumps

Wikidata

Strong evidence / likely

Structured entity layer; strongly implied by knowledge-graph use but not separately confirmed.

Community / Q&A / social

Reddit

Confirmed + current

The Google deal gave access to the Reddit Data API for ‘real-time, structured, unique content’, and allows Reddit content to be displayed across Google products — i.e. live grounding, not only training.

Tom’s Guide (Google/Reddit deal)

Reddit

Confirmed + current

Same deal, training side: Google may use Reddit posts to train its AI models and improve services such as Search; reported at roughly $60m/yr. NOTE: Reddit is reportedly weighing whether to renew — treat as unstable.

Fortune; Neowin/WSJ on renewal doubt

Social platforms

Strong evidence / likely

Category inference covering platform-wide social corpora.

Forums / communities

Strong evidence / likely

Category inference. Overlaps Reddit but generalised to non-Reddit forums.

News & publisher content

Live publisher pages

Confirmed + current

Reached at inference time via search grounding rather than pretraining; retrieval selection and crawlability govern inclusion.

Google — Grounding with Google Search

Licensed publisher content

Confirmed + current

OpenAI has multiple explicit licensing partnerships (FT, Axel Springer, AP, News Corp). Terms differ per partner on training vs grounding vs attribution.

OpenAI — FT content partnership

Publisher partnerships

Confirmed + current

Axel Springer’s deal includes otherwise paywalled material in answers; AP licensed part of its text archive.

OpenAI — Axel Springer partnership

Historical news corpora

Confirmed historical

Archive material absorbed in pretraining; distinct from live licensed access.

Developer / technical

GitHub

Confirmed + current

LLaMA used GitHub’s public BigQuery dataset, restricted to Apache/BSD/MIT projects; The Pile separately includes GitHub. Public visibility is not an open licence.

GitHub

Stack Overflow

Confirmed + current

Named in licensing-deal mapping alongside Reddit and Shutterstock as a data platform powering multiple buyers.

LLM Pulse — AI content licensing deals mapped

Technical docs

Confirmed + current

Vendor documentation corpora; widely used but not tied to a single disclosed agreement.

npm / PyPI registries

Strong evidence / likely

WEAKEST ENTRY IN THE TABLE. Relabelled from ‘package registries’ to name examples. No disclosed agreement or documented retrieval use found — consider cutting.

Travel & commerce actions

Google Hotel Center feeds

Confirmed + current

When Gemini or AI Mode show hotel options with real-time prices, that data comes from the Google Hotels feed. In Aug 2026 Google added hotel booking inside AI Mode completed with Google Pay, so this is grounding plus actions.

TechCrunch — AI Mode travel update

Booking / partner feeds

Strong evidence / likely

Booking Holdings and IHG are reported as participants in Google’s agentic booking pilot, which supports the direction but stops short of a documented feed spec.

InfosTourisme (IHG/Booking pilot)

OTA / commerce sources

Strong evidence / likely

Category inference. OTAs run their own rate feeds into these surfaces.

Reservation / inventory APIs

Strong evidence / likely

Category inference covering booking/inventory endpoints exposed to agents.

Source: Chris Green.

There is a chance this table may date badly – an occupational hazard of “AI Search” at the moment. But another thing you could try is look ahead to where may be good sources of data AI providers will be looking for in the future.

If you’re in a niche or a country (even) where the above data sources have less traction (i.e., Yelp isn’t huge in the UK), perhaps there are other “big players” you may want to look into, even if there isn’t a confirmed relationship yet.

The most meaningful research you can do as to which of these data sources are most likely shaping AI results today. That’ll require some work studying generated results from some queries your customers are likely searching for – look for the gaps, or the areas you can get ahead.

As always, any feedback or suggestions welcome. Good luck!

More Resources:

- New Data Finds Gap Between Google Rankings And LLM Citations

- Complete Crawler List For AI User-Agents [Dec 2025]

- Timeline Of ChatGPT Updates & Key Events

This post was originally published on Chris Green SEO .

Featured Image: Gorodenkoff/Shutterstock

Category AI Search

Read Full Bio

Chris Green Technical Director & Senior Consultant at Torque Partnership

## 原文链接

[Read original](https://www.searchenginejournal.com/which-data-sources-should-you-care-about-for-ai-search/590086/)
