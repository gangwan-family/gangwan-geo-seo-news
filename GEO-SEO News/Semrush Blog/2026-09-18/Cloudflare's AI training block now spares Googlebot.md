---
title: "Cloudflare's AI training block now spares Googlebot"
source: "Semrush Blog"
published: 2026-09-18T14:04:00+00:00
fetched_at: 2026-09-18T23:25:06.353737+00:00
url: "https://www.semrush.com/blog/cloudfare-blocks-ai-training/"
guid: "https://www.semrush.com/blog/cloudfare-blocks-ai-training/"
author: "Cecilia Meis"
categories:
  - "Industry News"
---

# Cloudflare's AI training block now spares Googlebot

- Source: Semrush Blog
- Published: 2026-09-18
- URL: https://www.semrush.com/blog/cloudfare-blocks-ai-training/
- Author: Cecilia Meis
- Categories: Industry News

## RSS 摘要

Cloudflare‘s Disallow AI Training setting blocks AI training crawlers but not Googlebot. Bing won‘t honor it until early 2027.

## 原文正文

Cloudflare‘s AI training block now spares Googlebot

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

## Cloudflare's AI training block now spares Googlebot

Author : Cecilia Meis

3 min read

September 18, 2026

Cloudflare released a setting on September 15 that lets website owners refuse AI training on their content without blocking the Google, Bing, and Apple crawlers that put them in search results. The setting is called Disallow AI Training, and it's available on every plan, including the free one.

Until now, Googlebot, Bingbot, and Applebot index pages for search and gather content that can be used to train AI models, so a site that blocked one of them lost its search listings too. Cloudflare says fewer than 1% of the sites on its network block search bots, whereas 17% have turned on some way to block training.

In July, Cloudflare said that from September 15, any site blocking AI training would block those three crawlers as well. Since then, the company has been in talks with Google, Microsoft, and Apple, and each has now added a training opt-out or promised one by a set date.

### How disallow AI training works

When you turn on the setting, Cloudflare's Bot Preference Sync adds two rules to your robots.txt file: one disallowing Google-Extended and one disallowing Applebot-Extended. Google and Apple use those tokens only for AI training.

Amazon, Anthropic, Meta, and OpenAI already run separate crawlers for training and search, and Cloudflare blocks their training crawlers outright. Your pages should still be readable by ChatGPT search and similar tools.

Googlebot, Bingbot, and Applebot stay allowed because Cloudflare now labels their operators "Accountable,” available by offering four things:

- A way for site owners to opt out of AI training through robots.txt or a similar standard

- A way to opt out of AI summaries

- URL-level visibility into which pages were made available for training

- Assurance that opting out of training won't affect search rankings

Google says its URL-level reporting will arrive in the coming weeks, and Apple's is planned for next year. Microsoft is furthest behind. Bingbot won't read the robots.txt rule until early 2027, which means that, for now, the only way to keep Bing from training on a page is to add a NOARCHIVE meta tag.

### What the early data shows

SeenSure tested how 1,046 websites responded to eight AI crawlers on September 14 and again on September 16. Of those sites, 746 used Cloudflare, and more of them refused training crawlers after the change. GPTBot refusals rose from 18.9% to 22.0%, and ClaudeBot refusals from 19.9% to 22.8%.

Cloudflare's announcement didn't mention any change for AI search crawlers or agents, but refusals of those fell by about 13 points each. OAI-SearchBot, which feeds ChatGPT search, was refused by 16.9% of the Cloudflare sites before the change and 3.0% after. The 300 sites that don't use Cloudflare stayed flat. If the pattern holds, ChatGPT search and Perplexity can now read many Cloudflare-hosted pages they were refused last week.

"Search moved the most of any category," SEO consultant Aleyda Solis wrote on X when she shared the findings.

### Opting out of training doesn't take you out of AI answers

The new setting decides whether your content can be used to train models, but of course doesn’t determine whether you appear in AI answers. That leaves site owners with separate choices about search indexing, AI training, and AI answers, and Cloudflare's setting covers only training. Cloudflare says AI summaries are next on its list, with its own controls planned for next year.

Opting out isn't the obvious choice for every site. For sites that don't run ads, Cloudflare's recommended default leaves training set to Allow. A brand that wants AI tools to know and mention it could benefit from being in the training data, though no AI company has said how much that matters. Cloudflare recommends Disallow AI Training for publishers that make money from ads on their content.

A robots.txt rule is a request, and a crawler can ignore it. Cloudflare can detect and block crawlers that do, but with Google, Apple, and Microsoft, it's relying on commitments made to a company that sells bot-blocking products and wrote the "Accountable" standard. Cloudflare says it will track their progress publicly on Cloudflare Radar.

### Check your AI crawler settings in Semrush

Site Audit's Blocked from AI Search check reads the file and lists which AI crawlers are blocked from which pages. Google-Extended is on its list, so it will show as blocked once Disallow AI Training is on. Googlebot, OAI-SearchBot, and the other search crawlers shouldn't appear as blocked.

Site Audit reads robots.txt only and won't detect a block made at Cloudflare's firewall. Your server logs will , so check that the search crawlers you want are still getting 200 status codes.

The AI Visibility Toolkit shows whether any of this changes how often you appear in AI answers. It tracks your brand and pages across ChatGPT, Google AI Mode, AI Overviews, and Gemini, and the Cited Pages tab in Visibility Overview lists which of your URLs get cited and by how many prompts. Record your numbers before you change the setting and compare them a few weeks later.

Cecilia Meis

Cecilia is a senior editor and strategist with 12+ years of experience spanning print, digital, and SEO. She’s passionate about optimizing editorial processes, upholding quality standards, and mentoring writers to deliver brand-aligned content.

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

[Read original](https://www.semrush.com/blog/cloudfare-blocks-ai-training/)
