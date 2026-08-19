---
layout: post
title: "How To Track Google AI Mode Traffic In Search Console via @sejournal, @suganthan"
date: 2026-08-19T12:00:51+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-19/How To Track Google AI Mode Traffic In Search Console via @sejournal, @suganthan.md"
original_url: "https://www.searchenginejournal.com/how-to-track-google-ai-mode-traffic-in-search-console/586194/"
author: "Suganthan Mohanadasan"
categories:
  - "AI Search"
  - "Analytics & Data"
  - "SEO"
  - "_src_search-engine-journal"
---

# How To Track Google AI Mode Traffic In Search Console via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-08-19
- URL: https://www.searchenginejournal.com/how-to-track-google-ai-mode-traffic-in-search-console/586194/
- Author: Suganthan Mohanadasan
- Categories: AI Search, Analytics & Data, SEO

## RSS 摘要

Search Console hides AI Mode query data by default. This breakdown compares four extraction methods, including a free ML-powered tool. The post How To Track Google AI Mode Traffic In Search Console appeared first on Search Engine Journal .

## 原文正文

How To Track Google AI Mode Traffic In Search Console Skip to content

SEJ Live : Boost Your Local Business Visibility Across AI Search

Register Now

- SEJ

- ⋅

- AI Search

## How To Track Google AI Mode Traffic In Search Console

Four ways to surface AI Mode and AI Overview queries hiding in Search Console, from a custom regex to a free classifier that labels 100,000 queries per run.

On June 3, 2026, Google introduced Search Generative AI performance reports in Search Console, dedicated views of impressions within generative AI features on Search, such as AI Overviews and AI Mode. At last, there’s official AI Overviews reporting showing how often those features involve your pages. What it doesn’t include is the queries behind the AI activity, and the report is UI only. I re-verified on my own property on 11 August 2026 that neither the Search Analytics API nor the BigQuery bulk export exposes the generative AI data, so there’s no official way to track AI Mode traffic at query level.

Except the queries turn up anyway. Fragments of real AI conversations, replies like “yes go on,” follow-ups, and whole pasted prompts, started appearing as ordinary queries in the performance report. Anastasia Kourou posted about the strange strings on LinkedIn, and Google’s John Mueller replied, confirming this data had always been available in the performance report and pointing to Google’s documentation.

I’ve written the full account with 16 months of my own data separately and deployed my method of extracting these queries via my Google Search Console MCP, so what follows is just the practical ways to pull the AI queries in Search Console out into the open plus a free tool powered by my own custom-trained machine learning model that does it for you.

### The Scramble For The Queries

Once the leak was public, SEOs started building ways to pull those queries out.

The early wave, back in June 2025, was word count regex, surfacing long conversational queries by length alone, anything of 32+ words, for example. Barry Schwartz rounded up those early attempts , crediting Metehan Yeşilyurt, Vijay Chauhan, and David Konitzny. The approaches have got a lot more specific since.

### Method 1: Glenn Gabe’s Full Inventory In Excel

The performance report UI caps any table at 1,000 rows, so on a big site most of your query data stays hidden before you start. Glenn Gabe’s answer is to skip the UI. He pulls the complete query set through the Search Analytics API using Analytics Edge in Excel, then has Claude organize the list and flag likely AI Mode queries. If you already live in Excel, this puts the full inventory inside the workflow you know.

Image Credit: Suganthan Mohanadasan

### Method 2: Jean-Christophe Chouinard’s Custom Regex

Jean-Christophe Chouinard went after the same problem from inside the report. On August 14, 2026 he published a regex on LinkedIn that flags conversational strings directly in the performance report’s Query filter, using the Custom regex option. He built it by comparing prompts people commonly type into LLMs, from data he has access to, against strings rarely seen in GSC before AI Overviews.

The result is one long alternation covering prompt verbs (write, draft, generate, summarize, explain, act as), greetings, acknowledgements (yes, ok, sounds good, yes go on), refusals and follow ups (more, continue, show me more, any other options). Paste it into the filter and you get an instant look, free, inside the report you already have open.

Image Credit: Suganthan Mohanadasan

Separately, his January 12, 2026 case study showed AI Mode clicks are tracked in Search Console , but the queries behind them are almost exclusively anonymized, a caveat that hangs over every method here.

### Method 3: Amin Foroutan’s Advanced GSC Visualizer

Amin Foroutan’s Advanced GSC Visualizer is a free Chrome extension that bolts advanced charting, annotations, and an AI assistant onto your Search Console data, with one-click API access. There’s no AI Mode-specific filter in it.

Image Credit: Suganthan Mohanadasan

### Method 4: My MCP Servers

My Search Console MCP has the conversation detector built in as a tool called genai_conversation_queries, and my BigQuery MCP runs the same detector against the bulk export, which is where the anonymized pool of queries lives. Both run locally, so your data moves only between you and Google. What they do well is automation and scale with query-level labels on every row. The limit is setup rather than detection, since you need an MCP client and a config, so they suit technical users.

Image Credit: Suganthan Mohanadasan

### The 4 Methods Side By Side

Method

Strong at

Limits

Glenn Gabe, API into Excel with Claude

Full query inventory in an Excel workflow

Per-run sorting, pattern-based

Jean-Christophe Chouinard, custom regex

Instant free filter inside the report

English pattern list

Amin Foroutan, Advanced GSC Visualizer

Charting and exploring without exports

No AI Mode specific filter

My MCPs

Automation and scale, labels on every query

Needs an MCP client and config

Look down the Limits column and the first three share a gap. Pattern lists and per-run sorting can’t reliably catch edge cases like rank tracker probes, agent harness prompts, pasted strings, or “my location is” probes. They’re built for English too, so a reply in Tamil or a code-mixed Hinglish string sails through unlabelled. Method 4 will solve this problem with a custom ML model.

### Why This Needs An ML Model

Classifying every query into named buckets, across languages, with the weird machine-generated strings included is very hard to do accurately with conventional methods. Because there are so many edge cases, etc. So the only reliable way to get this working is to train a machine learning model.

So I decided to build one.

Image Credit: Suganthan Mohanadasan

### How I Built The Detector

The detector has two parts. Deterministic rules own the exact classes (reply artifacts, tracker probes, agent harness prompts), and a trained model owns the fuzzy boundary between conversational, long tail, and ordinary.

The model is FacebookAI’s xlm-roberta-base, pre-trained on 100 languages and fine-tuned on my own labelled Search Console conversation exhaust plus synthetic rows across eight languages, including code-mixed Tanglish and Hinglish. I validated it across just over 120,000 queries scored, and retrained it twice on whatever broke. It runs quantized on a scale-to-zero Cloudflare container, and the same model now powers a free tool anyone can use without any setup.

### The Tool

That tool is the AI Mode and AI Overview query classifier , free on this site, and you don’t have to sign up or give me your email.

If the GSC MCP route sounded like effort, this is the same detector with that effort removed.

Image Credit: Suganthan Mohanadasan

### How It Works

Drop in Search Console or BigQuery query exports as CSV, and several files stack into one run.

Image Credit: Suganthan Mohanadasan

Step 1: The model will classify your queries into one of seven buckets.

Step 2: If you add a Search Console generative AI report, the tool will extract page data and map this against your queries. (In your report, you’ll see an “AI page” column. You’ll see the full URL when you export the CSV.)

The deterministic rules label the obvious buckets right in your browser, and those queries never leave your device. I do this because I want to minimize the amount of data I process and to help speed things up.

Everything else goes to the model, gets classified in memory, and none of this is stored. Each query comes back with a bucket and a confidence score. In plain words, the buckets are full conversational queries, short replies like “yes go on,” follow-up pivots like “what about the pro plan,” rank tracker probes, agent harness prompts, pasted strings, and ordinary searches. You can filter by bucket, classifier and confidence, then export every labelled row to CSV with no row cap.

### How To Use It

Five steps, start to finish.

- Get your queries out. Under about 1,000 queries, the performance report’s normal export is already complete. Bigger sites can stack several filtered exports, pull the full list through the API with Search Analytics for Sheets or Looker Studio, or dump the BigQuery bulk export table to CSV. If you’re an SEO, you already know how to get more than 1000 queries off GSC.

- Drop the CSV or CSVs onto the page.

- Press Classify.

- Filter or search the labelled table.

- Export the labelled CSV.

### Limitations

The tool comfortably handles up to 100,000 unique queries per run in the browser, and a big run needs the tab kept open, which I accept is a very 2010 way to compute. The second limit applies to every way of tracking AI Mode in Google Search Console, mine included. Google anonymizes rare queries; conversation strings are rare, and part of the pool never shows, so treat the output results as an undercount. My BigQuery export shows 57.7% of my impressions sat in the anonymized pool over the last 59 days, measured on August 11, 2026.

The model costs me real money to run, and as you already know me, I do not sell anything, and none of my tools require any form of sign-ups or paywalls. So I have to put some limitations and caps so everyone can use this tool.

So, please play nice. You don’t want to be the person who ruins things.

The tool is in beta, and if loads of people start using it, it will slow down, and processing may take longer. In that case, wait and try again.

Also, kindly note I offer my time and expertise free of charge, so do not demand customer support, etc. Yes, I have to write this stuff because some people don’t act like reasonable adults.

### Over 100,000 Queries

Above 100,000 unique queries, we need to do a batch run instead. Send yours in, and my agency runs it as a proper batch job, then emails you the complete results. We can also turn the findings into a full, actionable report, or help with your wider AI SEO work.

More Resources:

- Google Now Reports AI Search Impressions. Here’s How To Read Them

- How To Track AI Traffic In GA4 Without Undercounting It

- AI Visibility Measurement: What To Track & What To Ignore

This post was originally published on Suganthan .

Featured Image: Roman Samborskyi/Shutterstock

Category SEO AI Search Analytics & Data

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

I’m the Co-founder of Snippet Digital, A Search Journey Optimization agency helping brands win across every stage of modern discovery. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/how-to-track-google-ai-mode-traffic-in-search-console/586194/)
