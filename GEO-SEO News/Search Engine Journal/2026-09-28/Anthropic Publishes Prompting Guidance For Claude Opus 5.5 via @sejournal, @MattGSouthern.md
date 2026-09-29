---
title: "Anthropic Publishes Prompting Guidance For Claude Opus 5.5 via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-28T20:48:12+00:00
fetched_at: 2026-09-29T01:05:54.844618+00:00
url: "https://www.searchenginejournal.com/anthropic-claude-opus-5-5-prompting-guidance/591278/"
guid: "https://www.searchenginejournal.com/anthropic-claude-opus-5-5-prompting-guidance/591278/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Anthropic Publishes Prompting Guidance For Claude Opus 5.5 via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-28
- URL: https://www.searchenginejournal.com/anthropic-claude-opus-5-5-prompting-guidance/591278/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Anthropic's Claude Opus 5.5 prompting guide asks developers to retest effort settings and reconsider chat prompt lines telling Claude to think carefully. The post Anthropic Publishes Prompting Guidance For Claude Opus 5.5 appeared first on Search Engine Journal .

## 原文正文

Anthropic Publishes Prompting Guidance For Claude Opus 5.5 Skip to content

SEJ Pro Sign In

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- AI Search

## Anthropic Publishes Prompting Guidance For Claude Opus 5.5

- Anthropic published a prompting guide for Claude Opus 5.5.

- It says to test effort levels again instead of reusing Opus 5 settings.

- In its tests, removing a "think carefully" instruction made chat replies start sooner.

Anthropic's Claude Opus 5.5 prompting guide asks developers to retest effort settings and reconsider chat prompt lines telling Claude to think carefully.

Anthropic’s prompting guide for Claude Opus 5.5 advises developers to test multiple effort levels instead of reusing the setting used in Claude Opus 5. It also suggests chat applications remove system-prompt lines instructing Claude to think carefully before responding.

Opus 5.5 launched Sept. 22 . The guide says Opus 5 prompts should still work well without edits, and that the company’s Opus 5 guidance is a reasonable place to start.

When the company tested this in a chat product, removing a think-carefully line made replies start sooner, with “no clear decline in the quality of the reply.”

### Opus 5.5 Defaults To Medium Effort

Opus 5.5 runs at medium effort by default, one level below the high default on Opus 5.

Thinking can’t be turned off on Opus 5.5, and requests that try get an error. Opus 5 allowed that at high effort or below. The guide calls effort the first setting to adjust when balancing quality against speed and cost.

In Anthropic’s testing, Opus 5.5 at medium effort matches or even surpasses Opus 5 at high effort when it comes to coding and knowledge work.

To cut thinking, the guide says to try lower effort settings before prompt changes, and save the higher levels like xhigh and max for tasks where they really make a difference in quality.

### Anthropic Suggests Reconsidering “Think Carefully” In Chat

The guide’s reason for suggesting chat apps reconsider think-carefully lines is that Opus 5.5 decides for itself how much to think, with effort as the main control.

Anthropic’s own docs include that kind of line. For Claude Opus 4.7, when effort has to stay low to keep responses quick, its page on effort suggests adding guidance such as “This task involves multistep reasoning. Think carefully before responding.”

### Agent Guidance Covers Time Budgets And Pasted Text

For agent teams, the guide recommends using a time budget based on how long tasks might take. With Opus 5.5, the software helps by tracking elapsed time.

Anthropic’s tests have shown that small agent groups, when using time signals, finish research tasks quicker than a single agent working without signals. Even under time budgets, these groups managed to achieve answer quality comparable to solo agents. The guide emphasizes that the time budget is just a suggestion, and setting a strict timeout can be quite helpful. The model might perform slightly less thoroughly under pressure.

For users who input text from sources like emails, the guide suggests using tags with a random ID and adding a system note on how to manage tagged text. This approach encourages careful handling and, since tags are plain text that can be copied, they provide only one layer of protection against prompt injection.

5 Claude Opus 5.5 Prompting Tips From Anthropic

What Anthropic says to retest, remove, and add when prompting Opus 5.5

Retest effort settings

Opus 5 Opus 5.5

Don’t assume your Claude Opus 5 setting is still the right one for Opus 5.5.

Lower effort before prompting for less thinking

Effort Prompt First

Anthropic says effort is the first setting to adjust when balancing quality, speed, and cost.

Consider removing ‘think carefully’ in chat prompts

“think carefully”

In Anthropic’s chat-product testing, removing that instruction made replies start sooner.

Anthropic said there was ‘no clear decline’ in reply quality.

Use time budgets for predictable tasks

For multiagent workflows with a sensible task estimate, Anthropic recommends passing elapsed time against that budget.

The budget is advisory, not a hard stop.

Tag pasted text from outside sources

Instructions <…> Pasted text </…>

Anthropic recommends marking pasted content and telling Claude how to treat it.

It describes this as one guardrail against prompt injection, not a full defense.

Source: Anthropic Claude Opus 5.5 documentation, accessed Sept. 28, 2026

Anthropic says existing Opus 5 prompts should still work well. These are Opus 5.5-specific tuning suggestions.

### Why This Matters

Several sections of the Opus 5.5 guide ask developers to re-check setup carried over from older models, such as workarounds for reading charts and screenshots, or instructions written for running with thinking off. The Fable 5.1 guide, which Roger Montti covered earlier this month , asked developers to revisit formatting rules.

An app that never sets effort runs at medium on Opus 5.5 without any code change.

### Looking Ahead

Using an output cap (max_tokens) for Opus 5 with ‘thinking off’ might cut responses off on Opus 5.5. The guide mentions that ‘thinking’ uses some of that cap even when you don’t see it.

For frontend projects, the Opus 5.5 guide recommends setting clear styles to avoid defaults like cream backgrounds and pill-shaped buttons. Vague requests to steer clear of a generic AI look often just switch one default for another.

Featured Image: Samuel Boivin/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-claude-opus-5-5-prompting-guidance/591278/)
