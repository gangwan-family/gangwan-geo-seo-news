---
title: "How to do an SEO competitor analysis with the Semrush MCP"
source: "Semrush Blog"
published: 2026-11-13T12:24:00+00:00
fetched_at: 2026-11-14T01:31:15.977411+00:00
url: "https://www.semrush.com/blog/competitor-analysis-semrush-mcp/"
guid: "https://www.semrush.com/blog/competitor-analysis-semrush-mcp/"
author: "Chris Hanna"
categories:
  - "AI"
---

# How to do an SEO competitor analysis with the Semrush MCP

- Source: Semrush Blog
- Published: 2026-11-13
- URL: https://www.semrush.com/blog/competitor-analysis-semrush-mcp/
- Author: Chris Hanna
- Categories: AI

## RSS 摘要

Learn how to use the Semrush MCP to analyze your competitors’ keywords, pages, and backlinks.

## 原文正文

How to do an SEO competitor analysis with the Semrush MCP

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

## How to do an SEO competitor analysis with the Semrush MCP

Author : Chris Hanna

13 min read

November 13, 2026

Contributor: Carlos Silva

An SEO competitor analysis helps you understand where and why your rivals are winning in search.

In this article, I’ll show you how to analyze your competitors faster by combining Semrush data with the power of AI tools.

### How to set up the Semrush MCP

The Semrush MCP (Model Context Protocol) connects your AI tool to your Semrush account to provide access to helpful competitive analysis data. This lets you analyze competitor domains, keywords, and backlinks.

Connect the Semrush MCP to Claude by clicking the “ + ” icon in any chat. Then click “ Connectors ” > “ Add connector ” > “ Browse connectors .”

Search for Semrush and click the “ Connect ” button next to the Semrush connector. Then, follow the on-screen instructions to connect your Semrush account.

The Semrush connection uses API units when you prompt Claude to access Semrush data via the MCP. The prompts below are designed to minimize API unit usage while still providing useful competitive analysis data.

You can see your API units in your Semrush account under “ Subscription info ” > “ API Units .” I ran the prompts below and used around 16K API units, but this will vary depending on how much data you request per run, how you word the prompts, and how many you send.

I’ve suggested numbers to use in each prompt as a starting point. I recommend keeping these numbers to begin with and only scaling up when you need to, as this will help keep your usage low.

Next, click the “ Projects ” option on the left and then click the “ New project ” button at the top right-hand corner.

Creating a project will let you add context files (see below) and keep all your competitor analysis tasks in one place.

Give your project a name and a description, then click “ Create project .”

Next, create a business context file to give Claude information about your business to help improve its outputs. Include information about your business’s industry, any specific products you sell, and the topics you already cover on your website.

Use the prompt below to let Claude build your context file for you, with the help of Semrush’s MCP to add your current organic search performance data:

Create a business context file for [yourdomain.com] that I can add to this project. Target country: [country].

Important information about my business: [What you sell, who you sell to, competitors you know of, topics you want to rank for, topics to avoid, and your content resources (team size, budget, whether you can do original research or build tools)]

Use Semrush data to add information about my business’s organic traffic, organic keywords, Authority Score, referring domains, top 10 pages by traffic, and the main topics we already rank for.

Write it in Markdown. Add "Last updated: [today's date]" at the top. Label anything you inferred with "(inferred)" so I can check it, and ask me about anything you can't fill in.

Here’s an example output of this context file:

Download this file, then navigate to your project and click the “ Library ” icon on the top right-hand side of your project window, select “ + Add ” in the Library, click “ Upload files ,” and upload the context file you just downloaded.

Your Claude project will use this business context for each of the four use cases below to return more relevant competitor, keyword, topic, and backlink outreach guidance.

### 4 ways to use the Semrush MCP for SEO competitor analysis

Follow the four steps in order below to use the Semrush MCP for a comprehensive SEO competitor analysis. Or, use any of the methods individually at any time to analyze your rivals.

The prompts assume you’ve created a project and added a business context file from the previous section. If you haven’t, modify the prompts accordingly.

I recommend running each step in the same chat, or pasting in results from previous chats. This gives Claude the context from each step to provide better results.

#### 1. Identify and prioritize competitors

The first step of any SEO competitor analysis is to identify and prioritize which competitors to assess. You likely have a couple of competitors in mind, but it’s important to focus on your closest rivals to ensure you make the most of your resources.

Use the prompt below to identify and prioritize your competitors to analyze in steps two, three, and four, based on their search performance, keyword overlap with your domain, and more:

Using Semrush data for [country], find the top 10 organic competitors for [yourdomain.com]. Add any business competitors from my business context file that aren't already on the list.

Only include real competitors. Exclude forums, social platforms, video platforms, and reference sites (e.g., Reddit, YouTube, Wikipedia), even if they share a lot of keywords with us.

For [yourdomain.com] and each competitor, pull:

- Organic traffic

- Organic keywords

- Common keywords with [yourdomain.com]

- Keyword overlap % (common keywords divided by [yourdomain.com]'s total organic keywords)

- Authority Score

- Referring domains

- Organic traffic trend over the last 12 months (growing, flat, or declining)

If my business context file already has these figures for [yourdomain.com], use those.

Return one table with [yourdomain.com] as the first row. Include these columns: Competitor, Type (Direct competitor or Content competitor), What they do (one line), and the metrics above.

Below the table, recommend 3-4 competitors to analyze in the next steps, with a one-sentence reason for each.

Here’s an example of the table output for the beard care brand Mad Viking Beard Co:

Claude then provided some context, along with the top four competitors based on business relevance, keyword overlap, and website authority :

Use the list of prioritized competitors for the next three prompts.

#### 2. Analyze competitor keywords

Analyze your competitors’ keywords using AI to find content gaps you’re missing, and to quickly check whether you should create a new piece of content to fill that gap, or optimize an existing page.

Use the prompt below to find keywords your rivals rank for that you don’t, and terms they rank for higher than you, and to organize them into topic clusters :

Using Semrush Keyword Gap data for [country], compare [yourdomain.com] with the competitors identified in Step 1.

Part 1:

Find keywords that one or more competitors rank for in the top 20 but [yourdomain.com] doesn't rank for at all. Limit to the top 10 by search volume.

Part 2:

Find keywords where [yourdomain.com] ranks 11-50 and at least one competitor ranks in the top 10. Limit to the top 10 by search volume.

Rules:

- Run each part as a single Keyword Gap call covering all competitors at once. Don't run competitors one at a time.

- Sort by search volume and request 10 rows at a time. Only request the next 10 if fewer than 10 keywords qualify after applying the rules below.

- "Top 10" means the top 10 across all competitors combined, not per competitor.

- To check for existing pages, pull [yourdomain.com]’s list of ranking pages once and use it for every cluster.

- Omit branded keywords.

- Don't include keywords that aren't relevant to my business, based on my business context file.

Group the keywords into topic clusters. Each cluster should share a topic and search intent, so one page could target it.

For each cluster, check whether [yourdomain.com] already has a page targeting it.

Return one table with these columns: Cluster, Primary keyword, Secondary keywords, Total search volume, Average keyword difficulty, Intent, Competitors ranking, Our existing page (or "None"), Action (Create new or Update existing), Priority (High, Medium, or Low).

Set priority based on relevance to my business and potential to drive conversions. Within each priority level, sort by search volume and keyword difficulty.

This step is typically the heaviest in terms of API usage, so I recommend limiting the number of keywords that the tool analyzes across all competitors to 10 as a starting point.

Once you've tested the prompt and made sure you get decent results, you can then increase this number.

Below is an example output table with the topic clusters, keywords, and relevant metrics.

You can see in the existing page column that even where there is no existing page, Claude highlighted the closest alternative. For example, in the first row, Claude flagged the collections page for beard oil, even though there is no page specifically for “beard growth oil.”

Further down, Claude provided notes on the keyword selection. Where several keywords had the same volume, Claude looked at the business context file and opted for “beard oil vs balm” since it was most relevant to one of the products specified in that file.

This is an example of how adding context to your project gives the AI tool more to work with than a simple seed keyword. In turn, the AI tool is able to use its reasoning capabilities to make decisions tailored to your brand, rather than just return a list of generic terms.

#### 3. Find and analyze competitor content that performs well

Analyze your competitors' top-performing content to understand how you can improve your own content's search performance.

Use the prompt below, along with the keywords identified in step two, to find the pages that drive rankings for your rivals:

For each of the top 3 priority clusters from Step 2:

1. Use Semrush to find the highest-ranking competitor URL for the primary keyword in [country]. If two of my competitors rank in the top 10, analyze both pages. Ignore forum results.

2. Visit each page using your web fetch tool. Note:

- Content type (e.g., how-to guide, listicle, comparison, template, free tool, product or category page)

- Angle and target reader

- Main sections (H2s)

- Approximate length

- Standout elements, such as original data, examples, visuals, templates, tools, expert quotes, or video

- Last updated date, if shown

3. Pull the top 10 organic keywords for each URL from Semrush. Flag any that weren't in the Step 2 cluster.

4. If [yourdomain.com] already has a page for this cluster, visit it and pull its top 10 keywords too. Compare it side by side with the competitor page(s) and identify: subtopics they cover that we don't, keywords they rank for that we don't, and differences in format, depth, and freshness.

For each cluster, give me:

- A summary table of the pages you analyzed

- What the top-ranking pages have in common

- If we're creating a new page: a short brief with target keyword, secondary keywords, recommended content type, suggested H2s, and 1-2 ways we could make our page more useful than theirs, based on my business context file

- If we're updating an existing page: a prioritized list of changes

This prompt will yield multiple outputs. The first of these is a list of pages within a specific cluster, along with information about the content itself and why the AI tool thinks it performs well.

For example, for madvikingbeard.com, the first cluster was for the term "best beard oil." Claude recommended updating an existing page based on its assessment of the competitor page that ranks well for this term.

Claude’s assessment included information about the angle of the piece of content, what the main sections looked like, how long it was, and even specific design decisions on the page. This provides a good starting point for you or your team to create or update your own piece of content.

Further down, Claude outlined the top 10 keywords for the competitor page, along with position, volume, and keyword difficulty metrics. It then summarized the rankings and explained why targeting the keyword with a category page makes sense over a blog post.

While the final decision still rests with you (the human), this analysis, performed automatically and at scale, makes it much easier to quickly categorize clusters into new content and updates to existing pages.

One thing I noticed on this run is that Claude looked at two different pages on madvikingbeard.com's website: a blog post (which may at first seem like a good candidate for the keyword) and the collections page.

In this case, since the competitor's ranking page is a collection page, that's the one Claude recommended updating. Claude then performed a side-by-side analysis of both collection pages, outlining subtopics that the competitor targets that Mad Viking doesn’t, and even specific information about the product cards on the page and which FAQs to use.

One of the specific recommendations was to add scent notes to every product card. I went to the collections page on the competitor’s website to verify that the rival was actually doing this.

I suggest visiting competitor pages yourself to verify any specific recommendations the AI tool makes. Remember that this is just a tool designed to flag potential actions you may want to take. Don’t skip the human review step before making any decisions.

#### 4. Look at your competitors’ backlinks

Look at your competitors' backlinks to understand which of their pages earn links from the most referring domains. These are the pages that may be contributing the most to your rivals' authority and helping them show up in search.

Use AI to take your backlink analysis further by automating the research and prioritization stage using the prompt below:

Using Semrush backlink data, find the top 20 pages on [competitor.com] by number of referring domains. Only include URLs in [e.g., /blog/], and skip the homepage.

For each page, note the number of referring domains and backlinks. Then visit the page using your web fetch tool and note the content type (e.g., original research, statistics roundup, free tool, template, guide, definition, case study) and what it covers in one sentence.

Return one table with these columns: Page, Referring domains, Backlinks, Content type, What it covers.

Then find 5 pages we could realistically create or improve a version of, based on my business context file. Work through the table, starting with the most-linked, until you have 5. For each one, check whether [yourdomain.com] has a page on the same topic and recommend:

- Create: we don't have a page on this. Say what we'd need to make a better one (e.g., original data, design help).

- Improve: we have a page on this. Say what it would need to compete.

If you run out of pages before finding 5, tell me how many you found.

Here's an example output for one of madvikingbeard.com's competitors, Live Bearded. You can see it organizes the top 20 pages by referring domains and notes the content type, along with a brief explanation of what it covers.

The output is useful for getting at-a-glance information about your rivals’ pages that get the most links, beyond just numbers. When performing link analysis at scale, this is much faster than visiting every page manually to learn what they cover.

Further down, Claude provides recommendations on pages to create or improve, checking your site’s ranking pages and drawing on your business context file. For example, it recommends creating a page on beard mistakes, which earned links from the most referring domains on the competitor’s website.

Claude also provides guidance to create a better version of the page by backing it with original data, including before-and-after illustrations, and by using the tone it recommends.

Madvikingbeard.com actually already had a post on this topic, but Claude didn’t pick it up since it doesn’t have any rankings in the Semrush data. To account for this, I recommend manually uploading a list of all your site’s pages to your Claude project.

Since the page doesn’t rank, the recommendations would still apply to improving the current page, rather than creating a new one.

I wouldn't make any changes to your site just based on the guidance of the AI tool. But this is a very quick way to flag pages you may want to create or improve, without having to manually search through your competitors' pages and match them up with your own pages.

You can perform this analysis regularly and keep your business context file up to date with your own new pages as you add them.

#### Turn these steps into an interactive dashboard

A final optional step is to turn the competitor analyses above into a single interactive dashboard. This is helpful for your own organization, but it also makes it easy to share your plans and why you're going to take those actions with key stakeholders and other members of your team.

Use the prompt below to turn the analysis into an interactive dashboard within Claude:

Turn the results from this [conversation/project] into an interactive dashboard with five tabs: Competitors, Keyword clusters, Content analysis, Linkable assets, and Action plan.

Make every table sortable. In the Action plan tab, combine the recommendations from each step into one list with these columns: action, page or topic, effort (Low, Medium, or High), impact (Low, Medium, or High), and the step it came from. Sort by impact, then effort.

Show the date the data was pulled in the header. Only use numbers from this conversation.

Below is an example output for madvikingbeard.com. You can see a summary of metrics like organic traffic and how that changed year over year, along with information about the top 10 competitors below that. Keeping the dashboard up to date is as simple as prompting Claude each month to update the numbers, since it uses Semrush data.

The “Keyword clusters,” “Content analysis,” and “Linkable assets” tabs all provide helpful summaries of the findings of each relevant step. However, the “Action plan” tab is the most important, as it provides a prioritized list of actions that you or your team could take based on your AI SEO competitor analysis.

It estimates the effort and impact level to help you prioritize tasks. And because it's interactive, you can sort by whichever column is most important to you.

### Perform SEO competitor analysis at scale with the Semrush MCP

Using AI for competitive analysis is all about performing analyses more efficiently. You still need a human to make the decisions based on the data you find, but gathering insights is so much faster when you connect your favorite AI tool to a reliable data source like Semrush.

Start performing your own AI competitive analysis using the Semrush MCP today.

Chris Hanna

Chris is a content writer, editor, and strategist with 6+ years of experience turning complex ideas and processes into clear, engaging content.

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

[Read original](https://www.semrush.com/blog/competitor-analysis-semrush-mcp/)
