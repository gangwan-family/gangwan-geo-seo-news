---
title: "How to build an AI visibility dashboard with Semrush"
source: "Semrush Blog"
published: 2026-10-12T09:45:00+00:00
fetched_at: 2026-10-13T02:38:28.308888+00:00
url: "https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/"
guid: "https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/"
author: "Carlos Silva"
categories:
  - "AI"
---

# How to build an AI visibility dashboard with Semrush

- Source: Semrush Blog
- Published: 2026-10-12
- URL: https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/
- Author: Carlos Silva
- Categories: AI

## RSS 摘要

Learn how to build an AI visibility dashboard that shows whether the pages AI cites are the ones earning Google clicks.

## 原文正文

How to build an AI visibility dashboard with Semrush

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

## How to build an AI visibility dashboard with Semrush

Author : Carlos Silva

14 min read

October 12, 2026

Contributor: Faizan Ali

An AI visibility dashboard shows you whether AI platforms cite and recommend your brand.

We’ll help you build one that puts your prompt-level AI data from Semrush next to your page-level Google data from Search Console, so you can see whether the pages AI cites are also earning clicks.

On our test site, the first refresh surfaced a guide that AI answers cited for 50 prompts and that earned zero Google clicks.

To build your own brand visibility dashboard for AI search, you’ll need Semrush's AI Visibility Toolkit , Google Search Console (GSC), Google Sheets, and a paid Claude plan. The Sheet holds your data. Claude turns it into a live, interactive dashboard. It took me about 90 minutes to build out this dashboard the first time and it takes 20 minutes to update each week with fresh data.

### What this AI visibility dashboard will show

This dashboard shows two measurements side by side: how visible your brand is in AI answers (from Semrush) and how your pages perform in Google (from GSC). Specifically, it tracks:

- AI visibility rate: the share of your tracked prompts where your brand appears

- Mentions and cited pages from Semrush's prompt tracking

- Generative AI impressions from GSC's Generative AI performance report

- Clicks, impressions, click-through rate (CTR), and average position from GSC

- A list of SEO and answer engine optimization (AEO) opportunities based on your real data

There are two constraints to be aware of before you begin:

- The dashboard runs as a Claude artifact that pulls live data from your Google Sheet through the Google Drive connector. The connector itself is available to everyone, but artifacts that call connectors require a paid Claude plan (Pro, Max, Team, or Enterprise).

- You can't share it by public link. On Team and Enterprise plans, you can share it inside your organization, and each viewer sees data only if their Google account can open your Sheet and their Claude account has the Drive connector. On Pro and Max, it stays private to you.

This is a working dashboard for whoever owns reporting, not a link you send to leadership. For stakeholder reporting, you can ask Claude to turn the dashboard’s report into an HTML file they can open in any browser even without the connections.

### Step 1: Decide what you want to measure

Before you open any tool, decide what you want to measure:

- Your target domain, plus brand-name variations AI might use

- Which AI platforms you want to track (Semrush's Prompt Tracking supports ChatGPT, Google AI Mode, and Gemini)

- Location and language

- A stable set of prompts tied to how buyers actually talk to AI

- Your desired reporting period, such as the latest 28 days versus the previous 28 days

### Step 2: Set up AI prompt tracking in Semrush

To set up AI prompt tracking, create a campaign in the Prompt Tracking tool, which checks a fixed set of prompts against the chosen AI platform every day and records whether your brand appears.

#### Choose and add your prompts

Add prompts that mirror how your buyers talk to AI . If you can, mine customer support tickets, sales calls, and forum posts. You can feed transcripts and text posts into Claude to get better prompt options based on the patterns it sees.

Spread your prompts across the full journey rather than clustering on brand terms. I used 30 prompts, six in each of five groups:

- Customer problems : The issues your potential customers are dealing with (e.g., "I was just named executor of my dad's estate and have no idea where to start. What do I do first?")

- Product or category discovery : When your customers don’t know your product or service exists yet, and they’re trying to find a solution; e.g., "Is there software that helps executors settle an estate?"

- Comparisons : Comparing your brand to a competitor’s brand; e.g., "Which is better for [your ideal customer or one specific problem you help solve], [your brand] or [competitor]?"

- Product selection : Researching product or service options beyond direct comparison; e.g., "What are the best tools for an estate without a will?"

- Branded questions : Questions directly about your brand; e.g., "Is [brand] legit?"

Start with around 30 prompts. Monitored daily, that's roughly 200 observations a week, enough for a stable site-wide visibility rate. The entry AI Visibility Toolkit plan covers 25 prompts, so 30 means a higher tier or a prompt add-on.

Group-level numbers will swing. With six prompts per group, one prompt changing moves that group's rate by 17 points, so treat group changes as leads to investigate. If stakeholders want dependable group-level reporting, expand each group to 15 or more prompts over time, and only add prompts that mirror real buyer language.

Your branded prompts will almost always show your brand, which lifts your overall rate. Report on all prompts and non-branded only. The non-branded number tells you whether AI recommends you to people who don't know you yet.

Keep the same core prompts stable for at least a month once tracking starts. Every trend line in your dashboard depends on the prompt set staying constant. If you swap prompts mid-stream, you break the reporting.

#### Organize your prompts with tags

Tag each prompt with the group it belongs to, so you can compare visibility across meaningful segments instead of one blended score.

In your campaign, open the " Tags " tab and click " Manage tags " to create and assign them. I used one tag for each of my five prompt groups. The screenshot below is from my Google AI Mode campaign, which tracks a smaller set of prompts across the same five groups. Semrush also shows its own topic groupings in this view, and you can ignore those for the dashboard.

### Step 3: Export your Semrush AI visibility data

You’ll need to export two datasets from the AI Visibility Toolkit into Google Sheets: prompt-level performance from the tracking campaign you set up in step 2, and the pages AI platforms cite.

Neither dataset is available through the Semrush API yet, so the data gets to your Sheet by export. You can schedule those exports via email (more on that below).

#### Export prompt-level performance

Your prompt tracking campaign opens in a Position Tracking view with "AI Visibility" toggled on. Once the data is populated (it may take a few hours), scroll down to the “Top Prompts” section and click “ View all X prompts .” Then, click “ Export ” in the top-right corner and choose Google Sheets.

You should see one row per prompt, with a column group for each day showing your brand's position in the answer, the answer type, and the landing page cited. A position of "-" means your brand didn't appear that day. You'll reshape this in the master Sheet step.

#### Export cited pages and sources

In Visibility Overview , use the platform selector to pick the same AI platform your tracking campaign follows, so your citation data and prompt data describe the same platform. Then scroll down to the “Topics & Sources” section. You’re going to export the Google Sheets data for both the “ Cited Sources ” and “ Cited Pages ” tabs.

Visibility Overview holds months of history even if you created your prompt tracking campaign yesterday, because Semrush builds it from its own ongoing analysis of the AI answer space. My test site had a mentions trend going back six months on day one.

#### What to do if export is unavailable

If the export button is grayed out or missing, check your access to the campaign. If someone else owns it, ask them to export the reports for you or to change your permissions. Nothing else in this workflow needs owner rights.

Reach out to Semrush support if you encounter any difficulties here.

### Step 4: Export Google Search Console data

GSC data shows what your pages actually earn in Google, next to what AI answers say about you. Which report you use depends on whether the Generative AI performance report has data for your property.

#### If your Generative AI report has data

Open your property in GSC, go to " Performance ," and open the " Generative AI " report. Export it twice. Once with the date range set to the last 3 months, for the daily trend. Once set to the last 28 days, for the pages table, so it matches your standard GSC window.

The export is a ZIP of separate one-dimension tables (daily impressions, pages, countries, devices). Impressions are currently the only metric available.

There is no prompt-to-click attribution; Google currently does not give you queries, clicks, or CTR data. The pages table is aggregated across the whole date range rather than broken out by day.

#### If your Generative AI report is empty

The Generative AI report is available to every property, but it shows data only once your pages get enough impressions in AI Overviews and AI Mode. If yours is empty or thin, use the standard "Search results" performance report instead. Export page-level clicks, impressions, CTR, and average position for two matched 28-day windows.

End each export window 2-3 days before today, because the newest GSC data is incomplete and will undercount. Keep the windows the same length so period comparisons are consistent.

Note that this is overall Google Search performance, not AI-specific visibility, so label it that way in your dashboard.

### Step 5: Organize everything in one master Google Sheet

Put every export into one Google Sheet with a fixed tab structure. Mine ended up with seven data tabs, each holding one dataset:

- semrush_prompts : prompt-level results reshaped to one row per prompt per day, with columns for date, prompt, platform, tag, position, and cited landing page

- semrush_cited_pages : the cited pages export, stamped with a snapshot date

- semrush_source_domains and semrush_topics : the Visibility Overview exports, same stamping (topics is optional)

- gsc_genai_daily and gsc_genai_pages : the daily table from your 3-month Generative AI export and the pages table from your 28-day one

- gsc_pages : standard page-level GSC data, one row set per 28-day window

Here is a prompt you can feed to Claude along with all the exports to have it build the sheet for you:

On future weekly updates, I'll attach the current master sheet (downloaded as .xlsx) plus new exports.

### Step 6: Turn the Google Sheet into a live Claude artifact

Next, we’ll turn the Sheet into a dashboard by asking Claude to build a live artifact that reads the Sheet through your Google Drive connector.

#### Connect the Google Sheet to Claude

Connect Google Drive in Claude's connector settings , then confirm Claude can open the master Sheet before asking for anything visual. The connector lets the artifact re-read the live Sheet on demand, so it updates every time you add the new data.

#### Tell Claude what to include

Prompt Claude to build the visual dashboard connected to your master sheet. Make sure you replace [sheet name] with your Sheet’s name and [domain] with your domain:

The freshness warnings stop you from presenting stale data as current, and the "compare, never blend" instruction keeps data separate. The opportunity section in that prompt is how the dashboard makes recommendations based on the data.

On your first build, the prompt-tracking charts will show only a few days of data. That's expected.

On our test site, the first refresh flagged three things that went straight onto the content plan. Step 8 walks through each one.

### Step 7: Test that the dashboard updates correctly

The whole point of the dashboard is to track visibility over time , so you’ll want to make sure it updates properly. Test the connection by changing one number in the Sheet and confirming it moves in the dashboard.

Edit a clicks value in the “ gsc_pages ” tab, refresh the artifact, and check that the matching KPI card changes. Check the data-freshness stamp shows the current read, then undo the edit.

If a section of the dashboard goes empty after a Sheet edit, compare your column headers against the original structure. They need to match exactly.

### Step 8: Review the dashboard and prioritize actions

Use the dashboard to decide what to work on next. Here's how we read the three findings from our test site's first refresh:

- A page AI cites that earns no Google clicks : Our executor checklist was cited for 50 prompts and earned zero clicks. AI platforms already trust the page, so the work is on the Google side. Find a keyword it can realistically rank for, refresh the page around it, and build links to it .

- Competitors cited where you aren't : Our competitor list was led by domains cited for seven prompts each. Open those prompts and read what gets cited. That's your list of comparison and category content to create, and of listicles to get mentioned in.

- A whole prompt group with no presence : We had zero visibility across all six customer-problem prompts. One weak page doesn't explain that. It points to missing content, so those six prompts became the brief for new top-of-funnel pieces.

As your history builds, watch for these patterns too:

- A page ranking well in Google but rarely cited by AI usually needs clearer structure: direct answers, descriptive headings, and current dates that make passages easy to lift

- A page losing mentions after a content change is your early warning to review the edit

- Topics improving across both AI answers and Google search are your proof of what works, so document what those pages have in common

You’ll also see an “Opportunities” section, where Claude reviews the overlap between GSC and Semrush data and gives you suggestions on how to improve your AI visibility.

For example, a page can rank well in Google and still never appear in ChatGPT. ChatGPT pulls from its own web index , so a strong Google ranking doesn't guarantee a citation. Check whether the page answers the tracked prompt directly, and whether the sources ChatGPT does cite for that prompt mention you. If Bing and Copilot matter to you, Semrush's Position Tracking tool tracks Bing rankings, and you can add that data to the dashboard with one extra export.

### Step 9: Update the dashboard each week

You’ll need to update the Sheet on a fixed weekly routine to keep the data accurate. Each week, preferably on the same day:

- Export the latest prompt tracking data (or collect it from the scheduled export email)

- Export the latest Cited Pages and Cited Sources tables from Visibility Overview

- Export the latest GSC data, ending the window 2-3 days prior

- Append the new rows with the new snapshot date, then bring the updated file into the same Google Sheet with File > Import > Replace spreadsheet. If you import it as a new file, the dashboard can keep reading the old one.

- Refresh the artifact and confirm the freshness stamps updated

- Note any major content changes or campaigns in the Sheet, so next month you can connect movements to causes

When you update the sheet, keep these tips in mind:

- Keep the same headers

- Stamp every Semrush export batch with its snapshot date

- Append new rows rather than replacing old ones so you get comparison data

- Normalize URLs consistently across tabs

If you don’t normalize URLs, GSC can report some of your pages twice; once with a trailing slash and once without. If your page-level numbers ever look absurdly low, URL variants are the first thing to check.

### Build your AI visibility dashboard

A brand visibility dashboard for AI search shows you how often AI cites and mentions your brand, next to what those same pages earn in Google.

Open the AI Visibility Toolkit , create your first tracking campaign, and write 30 prompts the way your buyers actually ask. Then connect that data with your master sheet and build the dashboard in Claude.

And if you need to show the dashboard to stakeholders, ask Claude to turn the artifact into a shareable HTML file with the same data.

Carlos Silva

Carlos Silva leads the editorial pipeline for the English blog and builds AI workflows that boost content quality and AI visibility. 10+ years writing and editing across in-house and agency roles.

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

[Read original](https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/)
