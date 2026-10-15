---
layout: post
title: "How to do an SEO audit with Claude & the Semrush MCP"
date: 2026-10-15T12:32:00+00:00
source: "Semrush Blog"
source_slug: "semrush-blog"
generated_from: "GEO-SEO News/Semrush Blog/2026-10-15/How to do an SEO audit with Claude & the Semrush MCP.md"
original_url: "https://www.semrush.com/blog/semrush-seo-audit-with-claude/"
author: "Zach Paruch"
categories:
  - "AI"
  - "_src_semrush-blog"
---

# How to do an SEO audit with Claude & the Semrush MCP

- Source: Semrush Blog
- Published: 2026-10-15
- URL: https://www.semrush.com/blog/semrush-seo-audit-with-claude/
- Author: Zach Paruch
- Categories: AI

## RSS 摘要

Scan your website in Site Audit, connect Semrush’s MCP to Claude, and have Claude analyze the audit data.

## 原文正文

How to do an SEO audit with Claude & the Semrush MCP

Find new opportunities across AI search and SEO.

AI search and SEO.

Try free for 7 days

Login Sign up

Outperform your search competitors. Search now spans Google, ChatGPT, and beyond—and Semrush gives you the SEO and AI visibility tools to stay visible everywhere:

See how AI platforms talk about you

Discover valuable topics to cover

Get AI-powered strategy suggestions

Build keyword plans with personalized insights

Identify fixes to improve technical health

Benchmark yourself against competitors

Try for Free

10M marketing professionals have already used Semrush

## How to do an SEO audit with Claude & the Semrush MCP

Author : Zach Paruch

7 min read

October 15, 2026

Contributor: Faizan Ali

Semrush’s Site Audit scans your website for 140+ technical issues that could be hindering search visibility. Once you have these findings, you can use Semrush’s Model Context Protocol (MCP) server to pull them into Claude and get clear, actionable next steps for improving your website’s performance.

Let’s explore what an SEO audit with Claude involves, what you can learn from it, and how to run one yourself.

### How does conducting an SEO audit with Claude work?

When you conduct an SEO audit with Claude, Claude uses the Semrush MCP to pull website audit data from Site Audit for analysis. In this setup, Site Audit crawls and checks your site, and Claude analyzes the results.

The Semrush MCP is a server you can connect to AI assistants like Claude. These assistants can then access Semrush tool functions and data via the Semrush application programming interface (API) without navigating the Semrush dashboard.

For Site Audit specifically, the Semrush MCP lets AI assistants retrieve data from completed website audits. Your AI assistant can't start new audits or change audit settings through the MCP. You'll need to do both from the Semrush dashboard.

### What can you learn from conducting an SEO audit with Claude?

By conducting an SEO audit with Claude, you can turn raw website audit data into a prioritized action plan, complete with causes, fixes, and team ownership, just by asking in plain language instead of digging through reports manually.

Claude can obtain several types of Site Audit data. They include technical issues impacting your website’s performance, like missing and duplicate title tags , broken links , 4XX errors, missing meta descriptions , and llms.txt formatting issues.

Claude can also pull Site Audit’s categorization of issue severity: “errors” (most severe), “warnings” (moderate severity), and “notices” (least severe). Finally, Claude can list the pages affected by each issue.

Once Claude has retrieved Site Audit’s data, it can analyze the data in ways like:

- Identifying the most common or severe issues

- Spotting trends in the surfacing of certain issues over time

- Suggesting likely causes and fixes for an issue

- Prioritizing which issues to fix first

- Recommending which team should own the fix

Together, these outputs tell you not just the issues impacting your website’s performance, but also what to do about them.

### How to conduct an SEO audit with Claude

Here’s how to analyze Site Audit data with Claude, step by step:

#### 1. Meet the prerequisites

Before analyzing Site Audit data with Claude, make sure you have the following:

- A Claude account on any plan . Claude’s web, desktop, and mobile apps all work, but we recommend using the web app or desktop app for easier navigation.

- A Semrush account with Site Audit and Semrush MCP access . Both are included with Semrush One Starter and Pro+ and SEO Classic Pro and Guru plans. Semrush One Advanced and SEO Classic Business plans need an added API units package. Learn more about MCP access.

- Available Semrush API units . Each request you make via the Semrush MCP for Site Audit data uses between 100 and 10,000 API units, depending on the request type. The plans above come with 50,000 API units, which reset when your subscription renews. Check your remaining units in the “ API Units ” tab of your subscription information page, and your past requests in your API query log .

- At least one completed audit of your website by Site Audit . Claude can only retrieve data from completed audits — it can’t start new ones. From the Semrush dashboard, go to Site Audit and set up a campaign , or audit configuration, for your website if you haven’t already. The tool will automatically start a new audit once you complete the campaign setup.

You can optionally check when Site Audit last scanned your website to see how fresh your audit data is. To do this, go to Site Audit’s project page and look at the “Last Update” column for your website.

If you prefer to analyze more recent data with Claude, re-run your website’s campaign to start a new audit manually.

#### 2. Connect the Semrush MCP to Claude

Connect the Semrush MCP to your Claude account. The connection instructions we share below apply to Claude’s web and desktop apps. The steps for the mobile app may differ.

Open Claude and log in if you haven’t already. Then, click your name at the bottom left of the app, followed by “ Settings .”

The “Settings” modal will open. Click “ Connectors .”

Click the “ Discover ” tab. Then, type “semrush” into the “ Search connectors ” search bar. Click “ + ” next to the Semrush connector search result.

If you haven’t already logged in to your Semrush account, you’ll be asked to do this. Claude will then request access to your Semrush account. Click “ Approve .”

If the connection is successful, you’ll be redirected to the “Connectors” modal and see a checkmark under the Semrush connector’s “Status” column.

#### 3. Test Claude’s Semrush MCP connection

After connecting your Claude account to the Semrush MCP, test the connection. In a new Claude chat, click “ + ” > “ Connectors ” and confirm the “Semrush” toggle is enabled.

Next, run a simple prompt containing the term “Semrush” or “Site Audit” to test if Claude can get Site Audit data from your Semrush account.

For example: “Use Semrush to get the latest Site Audit results for [domain].”

In the process, Claude may ask for permission to access relevant Semrush tool functions. Click “ Always allow ” or “ Allow once ” depending on your preference.

If Claude’s response includes Site Audit data from your Semrush account, the connection works.

#### 4. Pull Site Audit data into Claude

You’re now ready to pull Site Audit data into Claude. Here’s a list of Site Audit data Claude can retrieve and sample prompts for surfacing this data:

Site Audit data

Sample prompts

A list of completed website audits, including their IDs and completion dates, so you can reference the IDs in future prompts

“Give me a list of website audits for [domain] in Site Audit”

Summaries of completed website audits, including:

- The audit’s date

- The website’s Site Health score

- The number of issues found and Site Audit’s categorization of their severity

- The number of audited pages

- The number of unaudited pages

“Summarize Site Audit’s latest audit of [domain]”

Explanations of specific issues surfaced during the latest website audit, including when these issues were detected and the URLs of pages affected by them

“Get me information on the ‘[issue]’ issue for [domain] in Site Audit”

Information about a single audited page, including all issues found on it

“What issues did Site Audit find on [page URL]?”

The ID of any audited page, so you can reference the ID in future prompts

“Find the page ID for [page URL] in Site Audit”

Results of multiple audits over a period

“Get me [domain]’s Site Health scores for the latest 2 audits”

Claude can pull data from every technical SEO audit that Site Audit has run, starting from when you first set up your website’s campaign in the tool. But pull data from past audits only when necessary, since each past audit you pull uses 10,000 API units. Most other Site Audit requests use between 100 and 1,000 API units.

#### 5. Analyze your Site Audit findings

Ask follow-up prompts to have Claude analyze the Site Audit data it’s retrieved. For example, after Claude displays the issues Site Audit has detected on your website, you can have Claude:

- List every page affected by an issue : “Show me every page affected by [issue]”

- Track trends : “How has the number of pages affected by [issue] changed between the latest audit and the previous one?”

- Share possible causes of an issue : “What are likely causes for [issue]?”

- Surface your website’s biggest problem areas : “Which are the most common issues?”

- Compare issue severity : “Which is worse, [issue one] or [issue two]?”

- Recommend fixes for an issue : “How do I fix [issue]?”

- Prioritize which issues to fix : “Rank the issues from this audit by impact, the number of affected pages, and the effort needed to fix them, so I can decide which to work on first”

- Assign ownership : “Should my SEO, content, or development team be in charge of fixing [issue]?”

If you’ve set up Site Audit campaigns for multiple websites, Claude can also flag shared issues across them with a prompt like “Identify issues common to [domain one] and [domain two] in their latest Site Audit reports.” Helping you spot broader trends in how you maintain your websites.

### Act on Claude’s Site Audit analysis

Act on the findings from your SEO audit with Claude to improve your website’s technical performance.

Assign each issue to the right person or team, using Claude’s recommended priority and solutions as a guide. Semrush’s Site Audit issues list provides fixes if your team needs more input.

Or, ask Claude to help draft fixes directly, like:

- Writing meta descriptions for pages that lack one

- Rewriting duplicate title tags

- Correcting invalid structured data

Claude can also take other actions with the analyzed Site Audit data using another connector or skill . Here are some ideas:

- Create a report of your website’s latest audit results as a Microsoft Word document

- Post a summary of critical Site Audit issues to a Slack channel

- Email a prioritized list of fixes to a team member via Gmail

Ready to get started? Set up a Site Audit campaign for your website to gather audit data for Claude’s analysis.

Zach Paruch

Zach Paruch is a data-driven SEO strategist with 10+ years of experience driving organic growth through scalable search strategies. He specializes in on-page and technical SEO, content strategy, AI search optimization, and AI-driven processes.

Tells Google to show you more from Semrush in AI, Search, and Discover.

### Most popular pages

#### What Is Keyword Search Volume? (& How to Check It)

Keyword search volume is the average number of monthly searches for a search term in a particular location.

Keyword Research

Rachel Handley 3 min read January 10, 2025

#### How to Use Google Keyword Planner

Google Keyword Planner is a free tool that lets you research the queries people type into Google.

Keyword Research

Rachel Handley 7 min read July 23, 2024

#### How to Get Backlinks: 10 Realistic Methods

Learn how to get backlinks by responding to media requests, creating link bait, finding broken links, & more.

Link Building

Rachel Handley 10 min read October 17, 2024

## 原文链接

[Read original](https://www.semrush.com/blog/semrush-seo-audit-with-claude/)
