---
title: "Llms.txt V2 Adds Formal Markdown Linking For AI Agents via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-08-17T16:06:23+00:00
fetched_at: 2026-08-17T21:47:12.415274+00:00
url: "https://www.searchenginejournal.com/llms-txt-v2-formal-markdown-linking-ai-agents/586119/"
guid: "https://www.searchenginejournal.com/llms-txt-v2-formal-markdown-linking-ai-agents/586119/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Tools"
---

# Llms.txt V2 Adds Formal Markdown Linking For AI Agents via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-08-17
- URL: https://www.searchenginejournal.com/llms-txt-v2-formal-markdown-linking-ai-agents/586119/
- Author: Matt G. Southern
- Categories: News, Tools

## RSS 摘要

A v2 update to the llms.txt spec has shipped, adding formal link relations that help AI agents locate Markdown versions of pages. The post Llms.txt V2 Adds Formal Markdown Linking For AI Agents appeared first on Search Engine Journal .

## 原文正文

Llms.txt V2 Adds Formal Markdown Linking For AI Agents Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- Tools

## Llms.txt V2 Adds Formal Markdown Linking For AI Agents

- llms.txt creator Jeremy Howard shipped a v2 spec update, its first revision.

- V2 adds link relations and an HTTP header for pointing AI agents to Markdown versions.

- Google's Search and Lighthouse teams still provide different guidance on the file, and it's unchanged by v2.

A v2 update to the llms.txt spec has shipped, adding formal link relations that help AI agents locate Markdown versions of pages.

Jeremy Howard, the Answer.AI developer who created llms.txt, published a version 2 update to the spec on August 10. It’s the first revision since the format launched, and it adds standard ways for agents to discover Markdown versions of pages.

The 2024 proposal included the llms.txt file and Markdown versions of individual pages, which are published at the same URL with .md added to the filename. V2 keeps this but introduces a second URL pattern for Markdown pages and formal ways for agents to locate them. For sites already using the file, updating it to V2 requires only a minor change rather than a complete rebuild.

### What Changed In V2

V2 now supports two URL patterns for Markdown pages. Sites can either add .md to the full filename, which was the only pattern supported before, making /docs/tutorial.html become /docs/tutorial.html.md, or they can replace the extension altogether, turning the same page into /docs/tutorial.md.

To make it easier for agents to discover Markdown pages, the V2 update introduces two link relations. A rel=”alternate” attribute with type=”text/markdown” provides a direct link from a page to its Markdown version. Additionally, a rel=”describedby” attribute points to the llms.txt file that covers it, because a single llms.txt file can describe all pages under its path.

Sites can include link relations either as standard HTML link elements within the page head or through an HTTP Link response header. The header option is versatile, as it can be used on files that aren’t even HTML, like Markdown pages. Plus, it can be added via server or CDN setup, so there’s no need to change a site’s templates or code.

How V2 Connects Pages, Markdown, And llms.txt

An HTML page uses two link relations to point to its Markdown version and the llms.txt file that covers it.

HTML Page

/docs/tutorial.html

This page points to

rel="alternate" type="text/markdown"

Markdown Version

/docs/tutorial.html.md or /docs/tutorial.md

rel="describedby" Points to the file covering this page

llms.txt

/llms.txt

Delivery methods: HTML <link> elements or HTTP Link header

Source: llms.txt v2 specification

### Why Howard Made The Change

Howard said the update is based on two years of practical experience. Now, thousands of sites are publishing an llms.txt file, and platforms like Mintlify help by creating one for every site they host. Google’s Chrome team has even added a check for this file to Lighthouse’s Agentic Browsing category, which we discussed when it was introduced in May. Additionally, Anthropic , OpenAI , and Google’s Gemini team now publish their own llms.txt files for their developer documentation.

As adoption grew, a real gap showed up. The llms.txt file pointed agents toward pages, but nothing in the spec told them where the Markdown versions actually lived.

### Where This Leaves Google’s Guidance

The update doesn’t change the positions of Google’s two product teams. Google’s Search team has said for over a year that support for llms.txt isn’t on their agenda, and the company’s AI optimization guide states that Google Search itself doesn’t utilize these files. The guide also notes that maintaining one of these files “will neither harm nor help your site’s visibility or rankings” because Google Search ignores them.

Chrome’s Lighthouse tool has an Agentic Browsing check that attempts to retrieve the llms.txt file and flags server errors. A missing file that returns a 404 is treated as N/A instead, because providing the file is optional. The tool views this as a way to help browser agents read a site’s layout more quickly. However, it doesn’t specifically test for new link relations or Markdown-page discovery.

### Why This Matters

The update to V2 involves adding two link relations as HTML link elements or using one HTTP header. What’s really important is what this update indicates about who the format is designed to serve.

Coding agents and document tools are already reading llms.txt files to help speed up API lookups. This use case isn’t related to whether Google uses the file as a ranking input. V2 clarifies this behavior rather than making a new case for search visibility.

Websites that maintain an llms.txt file primarily to influence AI Overviews or AI Mode citations still have no data or Google statement backing that goal.

Those who keep it because coding agents, IDE tools, or documentation platforms already use it now have a clearer spec to reference and a defined way to direct tools to Markdown content when available.

### Looking Ahead

Howard’s changes page shows every addition to the llms.txt spec along with the reasoning behind it. V2 is still open for feedback on GitHub , so if you’re using the link relations now, remember that the syntax might still change before everything is finalized as a stable version.

Featured Image: EyeFound/Shutterstock

Category News Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/llms-txt-v2-formal-markdown-linking-ai-agents/586119/)
