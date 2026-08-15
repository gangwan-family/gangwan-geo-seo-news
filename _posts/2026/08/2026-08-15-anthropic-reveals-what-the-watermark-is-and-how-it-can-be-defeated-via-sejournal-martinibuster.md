---
layout: post
title: "Anthropic Reveals What The Watermark Is And How It Can Be Defeated via @sejournal, @martinibuster"
date: 2026-08-15T10:46:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-15/Anthropic Reveals What The Watermark Is And How It Can Be Defeated via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/anthropic-reveals-what-the-watermark-is-and-how-it-can-be-defeated/585930/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
  - "SEO"
  - "_src_search-engine-journal"
---

# Anthropic Reveals What The Watermark Is And How It Can Be Defeated via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-15
- URL: https://www.searchenginejournal.com/anthropic-reveals-what-the-watermark-is-and-how-it-can-be-defeated/585930/
- Author: Roger Montti
- Categories: AI Search, News, SEO

## RSS 摘要

Anthropic offers more details about its watermark including how it can be defeated. The post Anthropic Reveals What The Watermark Is And How It Can Be Defeated appeared first on Search Engine Journal .

## 原文正文

Anthropic Reveals What The Watermark Is And How It Can Be Defeated Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- SEO

## Anthropic Reveals What The Watermark Is And How It Can Be Defeated

Anthropic provides more details about its text watermark and reveals how it can be defeated.

Anthropic announced how its watermark works, confirming virtually all of the details previously reported about a similar watermarking method called MirrorMark. Similar to MirrorMark, the watermark is the randomness pattern itself which mirrors the randomness of the LLM when it generates text.

### How The Watermark Works

Contrary to what some AI influencers say, there are no Unicode characters that are embedded into the text. So it’s not something that you can copy and paste into a text file to remove or to identify.

Also, it’s not about em dash use and neither is it about patterns that LLMs tend to use, like “It’s not this, it’s that” style of writing. It’s not looking for the likelihood that something was written by an AI.

What it’s looking for is a specific watermark pattern.

LLMs generate the next likely text in a sequence but with randomness built in. It doesn’t always pick the most likely next word; there is an element of randomness to the word that’s chosen. SynthID uses that randomness to set a pattern that’s dictated by a watermark key plus the context of preceding words. Because a SynthID-style watermark subtly alters the word choice randomness, the text that’s generated is indistinguishable from regular generated text. Users can’t identify the watermark without the watermark key.

Anthropic explains:

“That pattern is undetectable to the reader, but is detectable to anyone who has a key that encodes it. When watermarking is used, choices are still made at random, but the source of the randomness is different. Instead of using an arbitrary random number generator to pick the next word, watermarking uses the key and a few words that come before to settle what word the model should pick. That is, the words that Claude picks are still random, but now, one can check the sequence of words and see if it’s consistent with the choices Claude would make if it was using the key.”

### A Version Of SynthID

The announcement said that the new watermark is a version of SynthID-Text which was developed by Google DeepMind in 2024. It’s not SynthID, it’s a version of it. The state of the art for this kind of watermarking has significantly improved in the intervening two years.

The announcement states:

“Claude’s text watermark is a version of the SynthID-Text approach published by Google DeepMind in a Nature paper in 2024. It belongs to a family of approaches that go back to a proposal by Scott Aaronson in 2022, all of which share the same design principle that we described above—the watermark only changes the source of the randomness used to pick among words.”

### Can Anthropic’s Watermark Be Defeated?

Yes, it can be defeated through paraphrasing. According to Anthropic, light editing probably won’t defeat it.

According to Anthropic:

“Can’t someone just edit the text to get around the watermarking?

To some extent, yes. Light editing probably won’t remove the watermark completely; a complete rewrite where every word is replaced will. In the latter case, of course, it’s arguable whether the text can any longer be described as AI-generated.”

SynthID looks for the watermark word pattern that was inserted at the time the text was generated. So if you paraphrase or edit enough of the document it’s going to erase the words that act as a watermark.

### It’s Not SynthID

SynthID was developed in 2024 and the state of the art has moved on over the past two years.

A recent version of SynthID, called MirrorMark, extends SynthID by spreading the watermark across the generated text and using the surrounding words as context for determining where each part is placed, which makes it more resistant to editing.

SynthID is a zero-bit watermark, which means it’s detecting watermark or no watermark. MirrorMark can encode multiple bits of information, essentially spreading the watermark across the generated text.

Here’s what a 2026 version like MirrorMark can do:

- It adds multi-bit encoding.

- It mirrors the randomness of the LLM’s text generation.

- It uses CABS, a Context-Anchored Balanced Scheduler, which decides where the different watermarks are embedded.

- It’s specifically designed to be resistant to editing (like Anthropic’s, which is resistant to light editing).

I am not saying that MirrorMark is what Anthropic is using. But I am saying that before you put all your eggs into the SynthID basket, which is two years old, it may be useful to see what a 2026 version of SynthID can do.

### Major Takeaways From Anthropic’s Watermark Reveal

Here are the major takeaways from what Anthropic revealed :

Claude will watermark future text outputs.

- Anthropic says future Claude models will generate watermarked text as part of its compliance with the EU AI Act.

The watermark is a pattern created during text generation.

- It is not Unicode, metadata, or hidden characters. The watermark is created through the word-selection process itself.

Claude’s watermark is a version of SynthID-Text.

- Anthropic says its method is based on Google DeepMind’s 2024 SynthID-Text approach.

The watermark changes the source of randomness used to select words.

- Claude still makes random choices among plausible words, but the watermark key and preceding words are used to determine that randomness.

The watermark creates a detectable pattern in Claude’s word choices.

- Someone with the key can check whether the sequence of words is consistent with the choices Claude would have made using that key.

Nothing is added to the text.

- Anthropic explicitly says there are no hidden characters, no extra tokens, and no visible additions.

Watermarked text cannot be distinguished from non-watermarked text.

- Anthropic says the watermark has no effect on quality or the generated content.

The watermark does not cause Claude to make unusual word choices.

- Anthropic says it does not bias Claude toward particular words.

Less words make it less detectable.

- Anthropic says watermark detection performs poorly on small samples. It works better with more words.

The watermark is weaker in factual content.

- It’s less reliable when there are fewer words to choose from because of constraints based on factual type of content.

The watermark is weaker when used for proofreading type edits.

- Anthropic says if you “ ask it to edit only the grammar and punctuation and nothing else, the watermark can only live in the handful of corrections, which might be too few to register .”

- Anthropic plans to release a watermark detection API.

- Non-text image files like JPG, PNG, and SVGs will use C2PA metadata.

- Watermarking has a trivial impact on speed and adds no additional token cost.

Featured Image by Shutterstock/Thaspol Sangsee

Category News SEO AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-reveals-what-the-watermark-is-and-how-it-can-be-defeated/585930/)
