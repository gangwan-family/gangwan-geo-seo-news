---
layout: post
title: "November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports via @sejournal, @marie_haynes"
date: 2026-11-05T18:00:28+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-05/November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports via @sejournal, @marie_haynes.md"
original_url: "https://www.searchenginejournal.com/november-click-spikes-in-google-search-console-are-bot-traffic-how-to-filter-your-reports/595834/"
author: "Marie Haynes"
categories:
  - "SEO"
  - "_src_search-engine-journal"
---

# November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports via @sejournal, @marie_haynes

- Source: Search Engine Journal
- Published: 2026-11-05
- URL: https://www.searchenginejournal.com/november-click-spikes-in-google-search-console-are-bot-traffic-how-to-filter-your-reports/595834/
- Author: Marie Haynes
- Categories: SEO

## RSS 摘要

Seeing a vertical jump in Search Console clicks? Bots, not humans, are behind it. Here’s how to spot it and filter your reports. The post November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports appeared first on Search Engine Journal .

## 原文正文

November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports Skip to content

- SEJ

- ⋅

- SEO

## November Click Spikes In Google Search Console Are Bot Traffic – How To Filter Your Reports

That sudden click spike in Search Console isn’t real traffic. Here’s what my data shows, what’s causing it, and how to filter it out.

Earlier this week, I saw Barry Schwartz’s post on X (and his write-up on Search Engine Roundtable ) sharing a screenshot from Joy Hawkins. Joy noticed that several sites were seeing sudden, massive vertical spikes in Google Search Console clicks while impressions stayed flat, and Barry asked a great follow-up question: “Anyone else seeing this? If so, how are you filtering the report…”

Screenshot of Barry Schwartz and Joy Hawkins’ post on X highlighting the sudden click spike in Google Search Console. (Image Credit: Marie Haynes)

When I saw Barry’s tweet, I immediately thought this would be the ultimate real-world test for Marie’s Brain – my soon-to-be-launched agentic SEO and AI search analysis system.

Over the past several months, I have been building Marie’s Brain to combine my 15+ years of research on Google’s ranking systems with live, programmatic access to the Search Console and analytics data of the sites I monitor. Instead of manually clicking through Search Console property by property to see if any of my clients were affected, I asked my system to scan across all of the sites I monitor, check the unfinalized fresh data through Nov. 2, 2026, and flag any property showing a sudden anomaly in clicks.

Within seconds, Marie’s Brain surfaced the exact same vertical spike across multiple sites in completely different industries – and pulled the raw page, query, device, and country dimensions so I could see what was actually happening under the hood.

#### Key Takeaways

- Not real human searchers: Between Oct. 31 and Nov. 2, 2026, several sites saw sudden 2x to 6.5x spikes in Search Console clicks while impressions and rankings stayed flat. Whether this is external bot/agent retrieval or a Google logging bug counting automated fetches as clicks, it is not human traffic.

- Why it looks so strange: Pages ranking on Pages 2 to 6 (Positions 12 to 54) suddenly logged 45% to 100% CTR across dozens of one-off query variations (mostly on Desktop).

- How to filter it: There is no single button in GSC to strip out only the bot clicks if dozens of pages were affected. However, you can exclude a single spiked URL with a top-bar Page filter, or check Device: Mobile to see your unaffected mobile trendline. You can filter the Pages tab by Position > 10 to see which deep-ranking URLs were affected.

### What I Found Across The Sites I Monitor

Just like Glenn Gabe and Joy Hawkins mentioned in Barry’s Search Engine Roundtable post, the majority of properties I monitor showed completely normal traffic. However, while some SEOs saw the wave begin over the weekend (Oct. 31 to Nov. 1), a distinct subset of sites I monitor experienced a dramatic vertical spike on Monday, Nov. 2, 2026 that mirrors Joy’s screenshot:

Six-month daily Google Search Console clicks (Search type: Web, including fresh unfinalized data through Nov. 2, 2026) across three affected properties I monitor. Image Credit: Marie Haynes

Here is how those three anonymized properties behaved on Nov. 2, 2026 compared to their prior seven-day baseline (Oct. 26 – Nov. 1, 2026):

Anonymized Property

Prior 7-Day Avg Clicks

Nov. 2, 2026 Clicks

Spike Multiplier

Where the Anomaly Concentrated

Site A (Multi-Location Service Business)

~50 / day

327

6.5x (14.1x Desktop)

United States ; 91% Desktop ( 297 of 327 clicks across 120 pages )

Site B (Regional Service Business)

~16 / day

4.1x (7.9x Desktop)

United States ; 83% Desktop ( 55 of 66 clicks across 36 pages )

Site C (Technical Q&A Site)

~68 / day

144

2.1x

Canada (jumped from ~11/day to 75 clicks while US stayed flat at 67 ); 40 clicks hit a single page across 23 reworded query variations

### The 2 Big Clues In The Data

When I had my system drill into the raw API rows for Nov. 2, two unmistakable patterns emerged across the affected sites:

Visual summary of why total impressions look flat while automated deep-SERP clicks create a vertical spike in Google Search Console. Image Credit: Marie Haynes

#### 1. 45% To 100% CTR On Page 2 To Page 6 Results (And Why Impressions Looked Flat)

Normally, organic clicks in Search Console are heavily concentrated in the top 3 to 5 results on Page 1. On Nov. 2, click-through rate (CTR) exploded on pages ranking between Position 11 and Position 55 (Pages 2 through 6 of Google):

- On Site A, desktop clicks jumped 14.1x over the six-month daily median (21/day median to 297 on Nov. 2), pushing sitewide Desktop CTR from 0.20% to 2.89%, while mobile clicks stayed completely flat (30 clicks on Nov. 2 vs. 25-40 on prior days).

- More than 40 inner city and service pages on Site A that had zero clicks all week suddenly logged three to 16 clicks each while ranking on Page 2 to Page 6 (for example, one city page logged nine clicks on 13 impressions = 69.2% CTR at Position 15.5; another logged five clicks on 11 impressions = 45.5% CTR at Position 53.8).

- Nearly every visible non-brand query on Sites A and B logged one click on one impression (100% CTR) on Desktop at deep ranking positions (Position 14, 21, 24, 28, 30, 34, 38).

Why did total impressions stay flat if every click also had an impression? It comes down to simple scale. When a site normally gets 18,000 impressions and 50 clicks per day (like Site A), adding 275 automated impressions is only a 1.5% bump on the impression line – completely invisible on a chart! Adding 275 clicks to a 50-click baseline, on the other hand, creates a massive 6.5x vertical spike.

#### 2. Synthetic Query Fan-Out Clusters

On Site C (a technical troubleshooting Q&A site), a single long-tail troubleshooting page that normally gets zero to one click per day (and never received more than seven clicks in a single day across the entire previous six months) suddenly jumped to 13 clicks on Nov. 1 and 40 clicks on Nov. 2.

While the spikes on Sites A and B came from U.S. searches, all 40 clicks on this Site C page came from Canada. From Oct. 28 to Oct.r 31, that page only had four to seven impressions per day in Canada (and 0 clicks) while ranking on Page 2. Then on Nov. 2, Canadian impressions on that page jumped by ~45 (to 50 impressions), and Canadian clicks jumped from 0 to 40 clicks – meaning almost every single one of those new impressions was clicked (an 80.0% CTR at average position 14.6 on Page 2, while U.S. clicks on that page stayed at 0)!

When I inspected the exact queries that clicked into that single URL on Nov. 2, there were 23 slightly reworded variations of the exact same troubleshooting question (including systematic number permutations like 3 times, 4 times, 5 times, 7 times, 10 times), almost every single one logging 100% CTR (1 click / 1 impression, 2/2, or 3/3) between Position 10.0 and Position 33.0. Other troubleshooting pages on the same site logged 1 click / 1 impression (100% CTR) at Position 45.5 to 54.0.

### What Could Be Causing This?

Normally, when a basic rank tracker or scraper loads a Google search results page, it only generates impressions – not clicks. For Search Console to record a click, a browser or bot has to actually follow (or trigger) Google’s click-tracking link on the search results page.

Looking at the data patterns across these sites, four possibilities stand out:

- Scrapers or Headless Browser Bots That Also Click Through: If a scraper network or automated crawler recently started clicking through SERP links on Pages 2 through 6 to scrape the underlying page content (or resolving Google’s click-tracking redirect parameters to grab the final URL, as one commenter suggested on Search Engine Roundtable ), Search Console will log a 1 click / 1 impression (100% CTR) event on every result it visits.

- CTR Manipulation Networks (“Cookie Warming” or Decoy Clicks): Even if a business would never pay for CTR manipulation, automated click-bot networks frequently hit innocent sites in the same niche. To make fake headless Desktop browser profiles look like “real humans” to Google’s user-signal systems , CTR manipulation bots are programmed to run searches and click random “decoy” results across Pages 2 to 6 to warm up browser cookies (or misfire across other listings on the page while hunting for their target URL).

- AI Agent / Query Fan-Out Retrieval: As we move deeper into the agentic web , automated research agents are increasingly browsing the web on behalf of users . On Site C, where a single troubleshooting page was clicked across 23 slightly reworded variations of the same question (including systematic number permutations like 3 times, 4 times, 5 times, 7 times, 10 times ), the query pattern looks remarkably like synthetic query fan-out from an AI agent or research tool using a headless browser to open candidate URLs and extract answers.

- A Gap in Google’s Bot-Click Filtering: Google normally filters known automated and bot clicks out of Search Console behind the scenes. Whether this is a brand-new wave of headless browser bots that bypassed Google’s filters or a temporary glitch in how Google filters automated click-throughs, those non-human clicks made it into our performance charts.

### How To Filter Your Google Search Console Reports

Because GSC does not let you filter the top performance chart by ranking position or CTR, there is no perfect one-click button to strip only the bot clicks out of your sitewide graph if dozens of pages were affected. However, these three approaches work well depending on how your site was impacted:

#### 1. Exclude A Specific Spiked URL (Or Filter By Country)

- If only one or a few pages spiked (like Site C): Click + Add filter > Page… > URLs not containing at the top of the report and enter that URL slug (or a subfolder like /locations/ ). This cleanly removes the spiked page from the top chart while keeping 100% of your legitimate traffic on the rest of the site intact.

- If the spike came from a specific country: While Sites A and B saw their spikes come from the U.S., Site C’s spike came entirely from Canada (where sitewide Canadian clicks jumped nearly seven times while U.S. clicks stayed flat at 67). Checking the Countries tab in GSC will quickly tell you if the bot wave hit you from a single country that you can filter out in the top bar.

#### 2. Use Device: Mobile To Sanity-Check Your Trendline

If dozens of pages across your whole site spiked on Desktop (like Sites A & B), you cannot exclude every page individually. While filtering the top bar by Device: Mobile obviously hides your legitimate Desktop traffic too, it is a great sanity check to show a client or stakeholder that your Mobile organic trendline is completely normal (on Site A, Mobile clicks were 30 on Nov 2 vs. 27-40 on prior days; on Site B, Mobile clicks were 11 on Nov 2 vs. 11 on Nov 1).

#### 3. See Which URLs Were Affected In The Pages Table (Position > 10)

To see the exact pages that were affected on your site:

- Check the boxes for Average CTR and Average position at the top of the chart so those columns appear in the table below.

- Click the Pages tab (use the Pages tab rather than the Queries tab, as GSC hides most one-off single-impression queries for privacy).

- Click the filter funnel icon inside the table header, select Position , choose Greater than , and enter 10 .

- Sort by Clicks descending to see every Page 2 to Page 6 URL that logged 30% to 100% CTR during the spike.

#### 4. Prompt To Run If Your AI Agent Or LLM Is Connected To The GSC API

If you have Claude, Gemini, ChatGPT, or an agentic coding environment (like Antigravity or Cursor) connected to the Google Search Console API or a custom MCP server , you can paste this exact prompt to check all of your sites in seconds:

Query the Google Search Console API for my site(s) from October 20, 2026 through the latest available date using dataState: "all" (so fresh unfinalized data is included): 1. Check daily sitewide clicks and impressions to see if any date between October 31 and November 2, 2026 spiked by more than 2x compared to the prior 7-day average. 2. For any spiked date, break down clicks and impressions by Device (DESKTOP vs. MOBILE) and Country. 3. Query the "page" dimension for the spiked date and list all URLs with average position > 10 and CTR >= 20% (or clicks >= 3), comparing their clicks on the spike date against the prior week. 4. For the top spiked URLs, pull the "query" dimension and check for clusters of reworded query variations logging 1 click / 1 impression (100% CTR) at positions 11 to 60.

### Should You Worry About This Traffic?

No. Because this is automated activity rather than human visitors, you do not need to change your pages, disavow anything, or panic when those clicks drop right back down to baseline. Just annotate early November 2026 in your reporting (right alongside GSC’s other recent reporting changes ) so you and your clients know why Search Console suddenly showed a vertical jump in clicks!

Disclaimer: This blog post was mostly generated by Gemini 4 Argon in the Antigravity harness in conjunction with Marie’s Brain – an OKF -driven system full of my knowledge. It has been fact-checked by me, Marie, a human (I think).

More Resources:

- Google Search Console Glitch Gives SEOs A Scare

- Google Says No AI Click Reporting News Yet, Ahead Of UK Deadline

- Google Admits Search Console Reporting For AI Search Is Inadequate

Read Marie’s newsletter, AI News You Can Use. Subscribe now .

Featured Image: TAMI IAKO/Shutterstock

Category SEO

Read Full Bio

Marie Haynes Owner at Marie Haynes Consulting Inc.

I like learning about Google. I’ve been obsessively learning and sharing everything I can about how Search works since 2008. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/november-click-spikes-in-google-search-console-are-bot-traffic-how-to-filter-your-reports/595834/)
