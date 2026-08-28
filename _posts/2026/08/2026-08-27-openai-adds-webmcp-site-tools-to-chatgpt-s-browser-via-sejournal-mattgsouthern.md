---
layout: post
title: "OpenAI Adds WebMCP Site Tools To ChatGPT’s Browser via @sejournal, @MattGSouthern"
date: 2026-08-27T15:18:34+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-27/OpenAI Adds WebMCP Site Tools To ChatGPT’s Browser via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/chatgpt-adds-webmcp-support/587237/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# OpenAI Adds WebMCP Site Tools To ChatGPT’s Browser via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-08-27
- URL: https://www.searchenginejournal.com/chatgpt-adds-webmcp-support/587237/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

OpenAI added WebMCP support to ChatGPT’s desktop browser, letting supported webpages expose structured actions to ChatGPT Work and Codex. The post OpenAI Adds WebMCP Site Tools To ChatGPT’s Browser appeared first on Search Engine Journal .

## 原文正文

ChatGPT Adds WebMCP Support For Interactive Websites Skip to content

- SEJ

- ⋅

- AI Search

## OpenAI Adds WebMCP Site Tools To ChatGPT’s Browser

- ChatGPT Work and Codex can use structured actions exposed by supported webpages.

- Site tools require GPT-5.6 Sol or Terra and aren’t available in Enterprise or Edu workspaces.

- OpenAI doesn’t connect WebMCP with search rankings, citations, or recommendations.

ChatGPT’s desktop browser can now use WebMCP site tools, giving supported websites a structured way to let agents search, edit, and complete tasks on-page.

OpenAI is adding WebMCP support to the built-in browser in its ChatGPT desktop app, letting websites expose actions that ChatGPT and Codex can use directly from the page.

This is separate from the server-based Model Context Protocol support ChatGPT has offered since 2025. WebMCP lets the webpage you’re visiting provide tools automatically, without setting up a separate MCP connector.

### How Site Tools Work

Site tools assist with tasks like searching documents, editing files, exploring dashboards, comparing travel options, and updating shopping carts. The selection of tools varies depending on the website, so options might differ from page to page.

An arrow appears in the address bar when site tools are available, showing whether a tool can read data or make changes. ChatGPT can automatically find a suitable tool, which remains linked to the page where it was accessed and disappears when you close that page.

### What WebMCP Changes

Without site tools, ChatGPT uses its standard browser capabilities, such as clicking and typing. WebMCP offers developers an additional choice. It’s different from the server-based Model Context Protocol, or MCP, which links an AI application to a local or remote server and can operate without an open webpage.

WebMCP makes available specific tools from the webpage the agent is visiting. A webpage can register JavaScript functions as tools, including their names, descriptions, and structured input schemas.

OpenAI shared this goal in its challenge announcement:

“Instead of leaving agents to guess their way through your UI, you define exactly how they can use your app.”

Site tools operate within the current page and signed-in session. Developers can connect them to existing application logic and permissions.

OpenAI calls WebMCP an experimental open standard. The specification is a draft from the W3C Web Machine Learning Community Group and isn’t on the W3C Standards Track.

### Availability And Limits

Site tools are accessible within the built-in browser of the ChatGPT desktop app when available for an account. According to OpenAI’s documentation, this feature requires GPT-5.6 Sol or Terra; GPT-5.6 Luna has WebMCP disabled. Site tools aren’t available in Enterprise or Edu workspaces.

Access depends on rollout status and available tools. Although the feature doesn’t work in Chrome via ChatGPT, developers can test WebMCP in Chrome by enabling an experimental flag or joining its origin trial . Some websites might not support site tools, and embedded content may lack these tools. Tools used on one page won’t automatically be available on others.

### Security Checks

Site tools can work while you’re signed in and might change website data. OpenAI asks for your permission before ChatGPT interacts with a site and confirms actions like making purchases, deleting data, changing account settings, sending messages, or sharing personal info.

They also warn about risks such as data exfiltration and prompt injection. While each tool invocation receives a safety review, these checks don’t guarantee the website or its responses are trustworthy. Previously, SEJ reported that Chrome’s guidance identifies malicious tool descriptions and contaminated outputs as prompt-injection risks for browser-based agents.

### Why This Matters

SEJ mentioned back in May that Google’s website guidelines encourage designing sites that are agent-friendly. Now, OpenAI has added WebMCP support to ChatGPT’s desktop browser. This new feature lets website managers choose which actions are available, rather than depending solely on ChatGPT.

### Looking Ahead

While WebMCP gives sites a structured way to expose actions to agents, the documentation doesn’t explain how it might affect rankings, citations, or discoverability.

Featured Image: Tetiana Yurchenko/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/chatgpt-adds-webmcp-support/587237/)
