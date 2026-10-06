---
title: "OpenAI To Watermark ChatGPT Text In The EU, Opens API Opt-In via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-06T01:07:32+00:00
fetched_at: 2026-10-06T01:48:26.774888+00:00
url: "https://www.searchenginejournal.com/openai-to-watermark-chatgpt-text-in-the-eu-opens-api-opt-in/592014/"
guid: "https://www.searchenginejournal.com/openai-to-watermark-chatgpt-text-in-the-eu-opens-api-opt-in/592014/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# OpenAI To Watermark ChatGPT Text In The EU, Opens API Opt-In via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-06
- URL: https://www.searchenginejournal.com/openai-to-watermark-chatgpt-text-in-the-eu-opens-api-opt-in/592014/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

OpenAI will add an invisible watermark to ChatGPT and Codex text in the EU. Its tests show editing can weaken it. The post OpenAI To Watermark ChatGPT Text In The EU, Opens API Opt-In appeared first on Search Engine Journal .

## 原文正文

OpenAI To Watermark ChatGPT Text In The EU, Opens API Opt-In Skip to content

SEJ Pro Sign In

Ebook: State Of Search 2027

Download The Report

- SEJ

- ⋅

- AI Search

## OpenAI To Watermark ChatGPT Text In The EU, Opens API Opt-In

- OpenAI will add a hidden watermark to eligible ChatGPT and Codex text in the EU.

- API users can opt in on select models, and detector access starts with approved researchers.

- OpenAI's own tests show synonym edits and short passages make the mark harder to detect.

OpenAI will add an invisible watermark to ChatGPT and Codex text in the EU. Its tests show editing can weaken it.

OpenAI will introduce an invisible watermark to qualifying ChatGPT and Codex texts within the European Union over the coming weeks. Their testing indicates that replacing certain words with synonyms can weaken the watermark’s effectiveness. In one test, substituting 25% of the words in 400-token English passages with synonyms lowered detection rates from approximately 92% to 17%.

From today, API users worldwide can opt to activate watermarking for select models, though it stays off by default. The text detection tool is not publicly accessible at launch; it is currently limited to approved researchers and expert organizations.

### What’s Rolling Out Where

OpenAI states that the ChatGPT and Codex watermark will reach eligible users across all plans within the EU only. Initially, text watermarking won’t be a default feature globally.

The Oct. 5 update does not specify which models are part of the API opt-in or whether EU ChatGPT users can disable the watermark. The company says it is working with cloud partners to add watermarking to outputs from its models via their services in the coming weeks.

### Why The EU, And Why Now

The transparency rules under Article 50 of the EU AI Act began applying on Aug. 2, 2026. The European Commission states that AI systems placed on the market before this date have until December 2 to meet the marking and detection obligation. The voluntary Code of Practice on Transparency of AI-generated Content provides organizations with an optional way to show their compliance. By the end of July, about 190 organizations had signed, and OpenAI publicly supported the Code in June.

The company says the EU-only rollout gives it room to learn from real-world use and feedback. I covered its decision against text watermarking for ChatGPT in August 2024, after a company survey found almost 30% of ChatGPT users said they would use the service less if watermarking was implemented.

### What OpenAI’s Tests Show

OpenAI’s method, called textGrain, adds a statistical signal to the model’s word choices that a detector can look for. At a target false positive rate of 1%, the detector found the watermark in about 80% of 200-token passages and about 95% of 400-token passages, for content such as psychology. The company reported much lower rates for content such as math, where word choice is less flexible.

I noted in August that the Code doesn’t require watermarking of free-form text shorter than 200 tokens . Two hundred tokens is the shortest length in the post’s results.

Editing the text weakened the signal in a separate scenario with 400-token English passages. Replacing 10% of words with synonyms reduced detection from approximately 92% to 66%. Increasing the replacement to 25% further decreased detection to 17%. Both tests used responses to questions from the ELI5 dataset.

The company reports that textGrain matched or exceeded the performance of other methods it tested, including SynthID for text. However, they highlight that successes under ideal conditions do not guarantee reliability in everyday situations. In their benchmarks, they saw minimal to no difference whether watermarking was enabled or disabled.

### Who Can Check A Watermark

Researchers and expert organizations can request access to OpenAI’s text detector, initially on a case-by-case basis according to the Code. The tool reports whether it detects an OpenAI watermark but does not disclose user identities or show their prompts and chats. OpenAI notes that due to the risk of missed watermarks and potential false positives, it is not available to the public at launch. In contrast, image and audio verification tools via openai.com/verify and the Content Provenance API stay open to all.

In a 2024 update , the company wrote that even with a low false positive rate, “applying it to large volumes of text would lead to a large number of total false positives.”

According to the post , a watermark doesn’t measure how much a person contributed, and a missing one doesn’t prove a person wrote the text.

### How It Compares With Claude

Anthropic marks text from supported Claude models worldwide, according to its support article . Its explainer says that’s because it doesn’t yet have a durable way to scope watermarking by region.

OpenAI vs. Anthropic: How Their Text Watermarking Compares

Different rollout scopes, methods, and access approaches

Apps

OpenAI Eligible ChatGPT and Codex text, EU only, over the coming weeks

Anthropic Supported Claude models, worldwide

API

OpenAI Opt-in for select models, off by default, models not named in the post

Anthropic Marked on supported models, which the support article lists by name

Method

OpenAI textGrain, OpenAI’s own

Anthropic A version of Google DeepMind’s SynthID-Text

Detector access

OpenAI Approved researchers and expert organizations, by application

Anthropic Private preview for eligible organizations, including regulators, media, and researchers, plus enterprises verifying their own compliance

Published editing results

OpenAI Detection rates after 10% and 25% synonym swaps

Anthropic No figures in the explainer. Light editing probably won’t fully remove it, and a complete rewrite will

Sources:

OpenAI, “Our approach to EU text provenance rules,” Oct. 5, 2026

Anthropic, “How Claude’s text watermark works,” Aug. 14, 2026, updated Sept. 1, 2026

Anthropic, “How Claude marks AI-generated content,” accessed Oct. 5, 2026

### Why This Matters

An agency with writers in both Berlin and Toronto, all sharing the same ChatGPT plan, might soon find that some of their copy has OpenAI’s watermark from one office but not the other. A contract clause or AI policy that considers a detection result as proof of who authored the copy is essentially asking the watermark a question that OpenAI has said it can’t answer.

### Looking Ahead

OpenAI says it is planning to expand detector access whenever it feels “results can be interpreted responsibly.” As watermarking begins in the EU over the next few weeks, teams working with EU staff on ChatGPT might start creating marked content that only approved researchers and expert organizations will have the ability to review.

Featured Image: daily_creativity/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/openai-to-watermark-chatgpt-text-in-the-eu-opens-api-opt-in/592014/)
