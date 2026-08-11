---
title: "Anthropic To Mark Claude Text & Files Under EU AI Act Code via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-08-11T16:03:35+00:00
fetched_at: 2026-08-11T22:10:16.282913+00:00
url: "https://www.searchenginejournal.com/anthropic-claude-watermarks-eu-ai-act-code/585355/"
guid: "https://www.searchenginejournal.com/anthropic-claude-watermarks-eu-ai-act-code/585355/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Anthropic To Mark Claude Text & Files Under EU AI Act Code via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-08-11
- URL: https://www.searchenginejournal.com/anthropic-claude-watermarks-eu-ai-act-code/585355/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Anthropic will embed invisible watermarks in Claude text and sign generated files. The post Anthropic To Mark Claude Text & Files Under EU AI Act Code appeared first on Search Engine Journal .

## 原文正文

Anthropic To Mark Claude Text & Files Under EU AI Act Code Skip to content

🔥[Live 8/12 with Loren Baker] Ecommerce SEO : Own your "brand +promo code" search.

Register Now

- SEJ

- ⋅

- AI Search

## Anthropic To Mark Claude Text & Files Under EU AI Act Code

- Anthropic will add hidden watermarks to text from new Claude models.

- The company says it signed the EU's AI content transparency code.

- Marks can appear on human writing that Claude only edited or translated.

Anthropic will embed invisible watermarks in Claude text and sign generated files. Detection tools are still unpublished, and marks can appear on edited human writing.

Anthropic will embed invisible watermarks in text produced by its new Claude models and include signed provenance metadata with generated files, as detailed in a support article . This marking is implemented worldwide, not just in the European Union. According to Anthropic, a detected mark indicates that Claude may have processed the content, but it does not confirm that Claude authored it.

These marks apply to outputs from supported models through the API, the Claude applications, Claude Code, Cowork, and Tag, as well as those accessed via AWS, Google Cloud, and Microsoft Foundry.

### What Anthropic Committed To

Anthropic signed the EU AI Act’s Article 50(2) Code of Practice on Transparency of AI-Generated Content, as a provider of both generative AI models and generative AI systems. Claude models launched in the EU on or after August 2, 2026 support machine-readable marking at launch. Models released earlier fall under a transition period, and the company says it’s working to add marking support to those as well.

The European Commission counted about 190 signatories by the end of July. Google, Meta, Microsoft, Mistral, and OpenAI joined Anthropic on the provider section, which covers machine-readable marking and detection.

I covered OpenAI’s decision to scrap its own watermarking plans in September 2024, after a company survey found almost 30% of ChatGPT users would use it less if watermarking was added.

### How The Marking Works

Text gets an embedded watermark that Anthropic says doesn’t change the meaning, quality, or readability of a response. Because the mark is embedded within the text, it stays intact when copying and pasting and, as Anthropic notes, “may persist through some editing.” This watermarking is implemented at the model level, so it appears in any Claude product the text comes from.

Generated files in .svg, .png, and .jpg formats include signed metadata that follows the C2PA open standard. This records how each file was created and shows whether it has been tampered with.

Anthropic’s limitations section states that proofreading, translation, summarizing, and file conversion may result in a mark even if the original ideas and text come from elsewhere. Moreover, content from Claude might lack a detectable mark if created by an older model, heavily edited, or too short to provide a clear signal.

Roger Montti discussed Article 50’s four exemptions on August 3. Two of them land on edited copy, under different obligations.

Systems that only assist with standard editing can fall outside the marking requirement, provided they don’t substantially alter the input or its meaning. Published text that has undergone qualifying human review or editorial control can be exempt from the disclosure requirement, when someone holds editorial responsibility for it. So a Claude mark can appear on copy that its publisher has no obligation to label.

What Claude Marks & What It Means

Text from supported Claude models

Hidden watermark

Supported generated files

C2PA signed metadata

.SVG, .PNG, .JPG

Human-written text Claude processes

Edits, translations, summaries, or conversions may also carry a mark.

Detected mark = possible Claude processing

It does not prove Claude authored the content.

No detectable mark does not rule Claude out. Older models, heavy editing, or short text may not produce a detectable signal.

Source: Anthropic support article

### Whether The Marks Survive Editing

The support article doesn’t specify how much editing is needed to remove a watermark. TechCrunch reported that it reached out to the company for clarification but hadn’t received a response by the time of publication.

Alex Cui, CTO and co-founder of GPTZero, published a technical explainer on X arguing that text watermarks can be defeated. GPTZero sells AI detection software that scores text by pattern rather than checking for watermarks, and the company has argued since 2024 that watermarking doesn’t remove the need for independent detection.

In his testing, Cui noted that watermarks can be lost through intense paraphrasing, and free tools have bypassed Google DeepMind’s SynthID. He was describing the general method frontier labs use, not Anthropic’s own version, which hasn’t been published. His tests ran against other systems, because Anthropic hasn’t published its detection mechanism yet.

Jonas Geiping leads a machine learning safety group at the ELLIS Institute Tübingen and studies watermarking. He said paraphrasing can remove a watermark, but not every paraphrase will. By his account, stripping one out of a long document takes more than a light pass, because enough of the original phrasing has to go.

### Why This Matters

A writer who drafts their own copy and runs it through Claude for a cleanup pass ends up with marked text. So does a translator working from someone else’s article. Anthropic names both in its limitations, which is why a positive check shows Claude was involved and nothing about who did the writing. Any policy that treats a hit as proof of authorship inherits that gap.

### Looking Ahead

Anthropic says it will extend marking to models released before August 2. No date is attached.

Cui argued that public detection cuts both ways, giving people a way to check content and giving anyone working on removal something to test against. Google keeps SynthID verification inside its own products, and I covered that expansion reaching Search in May . Anthropic has said it will support detection by users and third parties and publish technical documentation, without saying yet what that access will look like.

Featured Image: frank333/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-claude-watermarks-eu-ai-act-code/585355/)
