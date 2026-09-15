---
layout: post
title: "Anthropic Shares Power Prompts That Improve AI Results via @sejournal, @martinibuster"
date: 2026-09-15T10:14:18+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-15/Anthropic Shares Power Prompts That Improve AI Results via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/anthropic-shares-power-prompts-that-improve-ai-results/589448/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
  - "SEO"
  - "_src_search-engine-journal"
---

# Anthropic Shares Power Prompts That Improve AI Results via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-09-15
- URL: https://www.searchenginejournal.com/anthropic-shares-power-prompts-that-improve-ai-results/589448/
- Author: Roger Montti
- Categories: AI Search, News, SEO

## RSS 摘要

Anthropic shares prompting upgrades that save tokens, improve how AI writes, code more efficiently, and handle longer tasks. The post Anthropic Shares Power Prompts That Improve AI Results appeared first on Search Engine Journal .

## 原文正文

Anthropic Shares Power Prompts That Improve AI Results Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- AI Search

## Anthropic Shares Power Prompts That Improve AI Results

Anthropic shares prompting upgrades that save tokens, improve writing & coding, and get the most from the least expensive effort settings.

Anthropic recently published prompting techniques for Claude Fable 5.1 that may also help users of other models save tokens and get better results.

### Writing Density

Claude provides an extremely simple prompt that improves all writing and helps to overcome some of the annoying tics that AI writing contains. Anthropic calls this kind of writing, “mannered prose.”

The way it works is very simple: Define the kind of writing behavior you don’t want and explain what that pattern looks like. Then define what you want instead. Define the bad writing pattern, then give the model an example of what to do instead. Anthropic says that even a very short and general prompt can work.

Anthropic provides two versions of the writing prompt upgrade.

#### The Long Version Of Writing Prompt

“Mannered prose substitutes metaphor and flourish for direct statement. Instead of “a parameter worth varying,” the mannered writer produces “a dial worth turning.” Instead of “this point still matters,” they write “this point earns its keep.” The phrases exist to display the writer, not to convey the idea, and readers can tell. That is why mannered prose irritates: it makes the reader work harder so the writer can perform. It is also imprecise. Metaphors drag in connotations the writer did not choose and cannot control. The fix is to say what you mean. When a literal phrase is available, use it.”

#### The Short Version Of Writing Prompt

“Please remove all mannered prose.”

### Formatting In Chat

Anthropic explains that Fable 5.1 uses less formatting, including bold, headings, lists, and quotation marks, than previous models. This means that users with anti-formatting rules may have to adjust their prompts to account for this new behavior. Anthropic recommends removing those rules altogether or to create new rules that explain when to use them.

While this is a prompt specific to Fable 5.1, users of other AI systems may benefit from refreshing old prompts because AI models are constantly changing.

Anthropic offers this example prompt to use for formatting:

“Use lists and bullet points when asked to, or when the content is multifaceted enough that they help with clarity. If the person explicitly requests minimal formatting, always format your responses without bullet points, headers, lists, or bold emphasis, as requested. In conversational, personal, or emotional exchanges, keep to plain prose.”

### Search Triggering At Low Effort

Claude Fable 5.1 has multiple effort levels, and Anthropic recommends starting at the default high level and then testing the others. Anthropic says the “low” level is comparable in cost to Claude Opus and Claude Sonnet models while scoring higher than both.

The issue with low effort, though, is that Fable 5.1 relies less often on search and retrieval tools and leans more on its parametric memory. So if you’re using the low setting to save on cost, this prompt can provide a bump in performance without moving to a more expensive setting.

#### Low Effort Nudge Prompt

“When a query centers on a name you do not confidently recognize, or recognize from a fast-moving area like AI models and developer tools where the landscape shifts within months, the name itself is the thing to verify: search before answering, and include the name as the user wrote it in at least one query alongside any reformulations. This holds even when you have some background on it — partial background is exactly what makes an out-of-date answer sound authoritative, so familiarity is not a reason to skip the search.”

### Prefer Targeted Edits Over Whole-File Rewrites

This power prompt may be useful to users who code, including WordPress developers, because it instructs the AI to make the smallest necessary change instead of rewriting an entire CSS/PHP/JavaScript configuration or template file. Anthropic describes this as a solution to a Fable 5.1 behavior, but the prompt should prove useful across a wide range of AI coding tools and agents.

#### Targeted Edits Prompt Upgrade

“The number of tokens used to edit files is best minimized, all else being equal. Therefore, when it will not affect the end result, try to surgically edit a file rather than rewrite the entire thing.”

### Finish The Whole Task

This prompt is specific and particular to Claude Fable 5.1. Anthropic says that Fable is able to complete long tasks without much detailed guidance when there is a clear goal. But on “asynchronous workloads” Fable can sometimes need a “nudge” to not end its turn but to keep going until it’s done.

If you find that the AI is needlessly pausing to ask permission to proceed to the next step when it’s not necessary then this is the prompt to use. These are actually two combined prompts.

#### Finish The Whole Task Prompt:

“You are operating autonomously. The user is not watching in real time and cannot answer questions mid-task, so asking ‘Want me to…?’ or ‘Shall I…?’ will block the work. For reversible actions that follow from the original request, proceed without asking. Stop only for destructive actions or genuine scope changes the user must decide. Offering follow-ups after the task is done is fine; asking permission before doing the work is not.

Exception: when the user is describing a problem, asking a question, or thinking out loud rather than requesting a change, the deliverable is your assessment. Report your findings and stop. Don’t apply a fix until they ask for one.

Before ending your turn, check your last paragraph. If it is a plan, an analysis, a question, a list of next steps, or a promise about work you have not done (‘I’ll…’, ‘let me know when…’), do that work now with tool calls. That includes retrying after errors and gathering missing information yourself. Do not stop because the context or session is long. End your turn only when the task is complete or you are blocked on input only the user can provide.

Before running a command that changes system state (such as restarts, deletes, or config edits), check that the evidence actually supports that specific action. A signal that pattern-matches to a known failure may have a different cause.”

### Takeaway

Anthropic’s guide for powering up prompts shows how to save tokens, unlock high performance from low effort settings, and obtain the best output from Fable 5.1 and also from other AI tools.

Featured Image by Shutterstock/Thrive Studios ID

Category News SEO AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-shares-power-prompts-that-improve-ai-results/589448/)
