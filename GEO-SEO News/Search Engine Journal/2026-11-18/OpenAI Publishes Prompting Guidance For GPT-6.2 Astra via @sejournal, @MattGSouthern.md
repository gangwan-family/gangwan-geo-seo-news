---
title: "OpenAI Publishes Prompting Guidance For GPT-6.2 Astra via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-11-18T22:26:21+00:00
fetched_at: 2026-11-19T02:41:06.811446+00:00
url: "https://www.searchenginejournal.com/openai-gpt-6-2-astra-prompting-guidance/597877/"
guid: "https://www.searchenginejournal.com/openai-gpt-6-2-astra-prompting-guidance/597877/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# OpenAI Publishes Prompting Guidance For GPT-6.2 Astra via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-18
- URL: https://www.searchenginejournal.com/openai-gpt-6-2-astra-prompting-guidance/597877/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

OpenAI's GPT-6.2 guide says Astra writes more concisely by default, suggests revisiting "be concise" prompts and flags an API change for edited history. The post OpenAI Publishes Prompting Guidance For GPT-6.2 Astra appeared first on Search Engine Journal .

## 原文正文

OpenAI Publishes Prompting Guidance For GPT-6.2 Astra Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

- SEJ

- ⋅

- AI Search

## OpenAI Publishes Prompting Guidance For GPT-6.2 Astra

- OpenAI published prompting guidance for its GPT-6.2 Astra and Sol models.

- It says Astra writes more concisely by default and suggests revisiting "be concise" lines.

- Apps that edit earlier turns can lose the model's saved reasoning.

OpenAI's GPT-6.2 guide says Astra writes more concisely by default, suggests revisiting "be concise" prompts and flags an API change for edited history.

OpenAI is suggesting that developers who are migrating to GPT-6.2 Astra should revisit instructions such as “be concise” when they update their system prompts. The guide for developers on how to use GPT-6.2 states that Astra produces output that is more direct and brief by default than prior GPT models.

The company’s guidance for GPT-6 Astra says the model tends toward detailed, formatted responses.

GPT-6.2 Astra and GPT-6.2 Sol launched Nov. 17. Developers can use both in the API as gpt-6.2-astra and gpt-6.2-sol.

### How The Guide Describes GPT-6.2 Astra’s Writing

Astra is described in the GPT-6.2 guide as “more concise and direct by default than earlier models,” with an adjustable overall tone that can range from a professional colleague to a more conversational assistant.

The GPT-6.2 guide provides an example prompt for apps that use the model as a collaborator in day-to-day work. This prompt tells Astra to stick with the terminology of the user and its sources and to address the key points at the outset of its response.

The GPT-6 guidance states, “GPT-6 Astra tends to use lists, tables and Markdown to make responses scannable.” The GPT-6 guide also contains an example prompt for apps that require prose with less formatting. This example prompt requests “clear, concise paragraphs” and directs the model to reserve lists for presenting parallel or sequential data.

The GPT-5.6 guide states that GPT-5.6 is generally more concise by default than GPT-5.5, and that brevity instructions (such as “Be concise” and “Keep it short”) may be unnecessary for some types of task.

### Prompts For Drafting, Editing And Final Answers

The GPT-6.2 guide advises asking the model to adjust for its target audience in emails, documents and any other writing intended for an external reader. It does this by suggesting a prompt which states that an external audience would probably have less understanding of the user’s context, so the model will need to provide the background information that audience needs.

The prompt also provides guidance on editing by instructing the model to “preserve the author’s content and wording” when reviewing or editing existing work and adhere to the user’s direction as to what changes are to be made.

When performing longer tasks, the model can retain abbreviations, jargon or shorthand from the reasoning process, or from other agents, in its final answers. The guide suggests a method to address this by having the model write a self-contained response for anyone who hasn’t been tracking progress updates. Additionally, the guide’s example prompt tells the model not to include such shorthand, jargon or abbreviations in the response.

### When The Model Pauses On Long Tasks

The guide says GPT-6.2 Astra may propose a next step and wait for confirmation when a user’s intent is unclear. For work that can run on its own, the guide’s advice is to spell out the outcome the model should complete and which decisions need the user’s input.

The guide’s suggested prompts tell the model to make reasonable, reversible assumptions and keep working, stating what it assumed. It should stop and ask only when the task’s scope changes in a big way, when it’s blocked, or when the user has to make a decision. It should also check in before irreversible or destructive actions.

The guide also points to an async question tool, which lets GPT-6.2 ask the user a question while it keeps working on anything that doesn’t depend on the answer. OpenAI’s async tool calling page says the app defines that tool and shows the question to the user, and that it isn’t a built-in tool in the Responses API.

### An API Change For Apps That Edit Earlier Turns

Starting with GPT-6.2, the API will drop reasoning items as soon as it identifies that the client has made an edit to prior history, dropped down to a lower model version, or changed the end-user account or organization, according to OpenAI’s API documentation. Reasoning items provide the model’s reasoning from earlier in the conversation. Dropping these can lead to a reduction in answer quality and increase the number of tokens used by the model to repeat previous work.

Examples on OpenAI’s page about the change include shortening a tool result, rewriting a developer message (which carries an app’s instructions), and replacing older turns with a summary. For new instructions, the page suggests appending a developer message that asks the model to ignore older instructions and follow the new ones, in place of editing the original.

### Why This Matters

Teams building drafting or editing tools on GPT-6 Astra have prompts to review prior to migrating to GPT-6.2 Astra. Developers need to revisit any instruction that asks GPT-6 Astra to produce briefer answers, according to the 6.2 guide. Some of these tools may rewrite their own instructions as well during a conversation. This could lead to GPT-6.2 Astra losing its earlier reasoning, and spending additional tokens to recreate this process.

### Looking Ahead

The GPT-6.2 guide calls its prompts a starting point, based on behavior seen with GPT-6.2 Astra and Sol. The GPT-6 guidance is still on the same page as the 6.2 guide, under its own tab, so teams can compare what each guide says about the model they’re moving from.

For reasoning effort, the 6.2 migration notes recommend medium for new integrations and low for apps that are currently set to none or minimal. Anthropic’s Claude Opus 5.5 guide, which I covered in September , also asked developers to retest effort settings carried over from Opus 5.

Featured Image: Tetiana Yurchenko/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/openai-gpt-6-2-astra-prompting-guidance/597877/)
