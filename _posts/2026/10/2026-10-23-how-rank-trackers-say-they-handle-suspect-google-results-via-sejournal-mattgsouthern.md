---
layout: post
title: "How Rank Trackers Say They Handle Suspect Google Results via @sejournal, @MattGSouthern"
date: 2026-10-23T12:00:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-23/How Rank Trackers Say They Handle Suspect Google Results via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/rank-trackers-suspect-google-results/594049/"
author: "Matt G. Southern"
categories:
  - "SEO"
  - "Tools"
  - "_src_search-engine-journal"
---

# How Rank Trackers Say They Handle Suspect Google Results via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-23
- URL: https://www.searchenginejournal.com/rank-trackers-suspect-google-results/594049/
- Author: Matt G. Southern
- Categories: SEO, Tools

## RSS 摘要

Rank trackers describe how they check suspect Google results, what customers see during checks, and what they say about reprocessing and past results. The post How Rank Trackers Say They Handle Suspect Google Results appeared first on Search Engine Journal .

## 原文正文

How Rank Trackers Say They Handle Suspect Google Results Skip to content

SEJ Pro Sign In

Webinar: AI Shopping: Get Your Products Found in Google & ChatGPT

Save Your Spot

- SEJ

- ⋅

- Tools

## How Rank Trackers Say They Handle Suspect Google Results

Rank trackers describe how they check suspect Google results, what customers see during checks, and what they say about reprocessing and past results.

SEO tool maker Ahrefs said Thursday that it’s “cleaning up any past results that may have been affected” by what it calls the “poisoning” of search results by Google, in which suspected SERP data providers are shown different results. Its post doesn’t say which dates, reports or metrics the cleanup covers.

Agency SEO platform SEOmonitor says in its help center that between Oct. 9 and 13, “some of the incorrect results were recorded in the platform” and that the affected keywords were reprocessed on Oct. 13, the day it put a new check in place.

Three other companies ( AccuRanker , BrightLocal and SerpApi ) have also described how each of them treats these results. These descriptions are side-by-side so you can see how each company describes the steps taken for an individual rank before storing that data, when displaying it to users and after recording it. A tool’s actions at each step during the weeks these vendors describe can affect what is said in your reports.

### What Nozzle Measured And What Changed On Oct. 21

An Oct. 10 article by rank-tracking company Nozzle looked at how Google’s results pages were showing up without many (or sometimes all) of the sites that normally show up for a particular search term. The Nozzle article was updated on Oct. 21. Roger Montti covered the original article on Oct. 14.

When determining if a result is poisoned, Nozzle’s first page poisoned count includes it if less than 50 percent of the normal first page sites for a keyword show up anywhere within the collected results. This test does not need those same sites to return in a follow-up review.

In this way, 8.7 percent of the Nozzle-determined first pages were poisoned between Sept. 13 and Oct. 21, while 0.17 percent of the Nozzle-determined first pages were poisoned from Aug. 20 to Sept. 9. Nozzle states this trend “is Google’s response to AI scraping, and rank trackers are caught in it.”

### What Vendors Say They Check Before Storing A Result

AccuRanker states they eliminate shortened Google results pages, then use another browser session to get the results page again. They will compare the new page 1 results to the sites that were listed for that keyword on page 1 of at least two of the previous three days. When less than half of those sites show up on that page, AccuRanker will go out and get the results page again.

If the second pull shows the same new sites in the results page, AccuRanker records this page as an actual change. According to AccuRanker, approximately one in every 20 desktop pages and about one in every 12 mobile pages do not have enough history data to run their change check.

In addition, SEOmonitor estimates that on average, around 8 percent of the results returned by Google each day will be either incomplete or incorrect and will be pulled again prior to being recorded. SEOmonitor does not say what period that average covers. On Oct. 13, the company switched to checking each result’s content against the keyword’s own recent history as results arrive.

Ahrefs says it has filters that detect and reject abnormal results and request replacements. It estimates that 5% to 20% of search results have been affected over the past few weeks, depending on the data provider. The post doesn’t say whether that share is measured before or after its filters.

BrightLocal, a company selling local search engine optimization (SEO) software, is taking steps to improve the way they gather their information, by engaging with their current data suppliers and adding additional suppliers of data so that if one provider was to fail, another would be available. BrightLocal CEO Myles Anderson’s Oct. 16 blog posting does not mention verifying every individual result, but also states there is “no single fix that solves it completely” for BrightLocal or anyone else in the industry.

### What Customers See While A Result Is Unconfirmed

The data an individual user will see can be based upon the validation and display rules used by their SEO tool as well as the information it received.

SEOmonitor refers to this rule in another help article regarding rank volatility it states it observed since around May. For some unusually large drops on the same device (i.e. a drop from Rank #4 to Rank #14; a drop from Top 50 to Rank >99), it “may keep showing the previously recorded rank for up to two daily updates” until it determines if the lower rank continues to appear in the results.

Also included in that help article are links to a recrawling option as well as a Chrome extension to compare rank values.

AccuRanker states that when its history check applies and a page has lost most of its normal sites it has a secondary fetch before reaching the customer’s dashboard. AccuRanker does not state what appears at the dashboard during that re-check. Also, users can request a refresh of a keyword within the application that will cause a new page with a new session to be fetched.

### What Vendors Say About Rankings Already Recorded

SEOmonitor stated that it re-processed all keywords affected by incorrect September results for the period of Sept. 25 through 28. It also indicated that it prevented the entry of erroneous data into their product until Oct. 8.

Beginning around Oct. 9, according to SEOmonitor, many of the erroneous results no longer contained the signs upon which their quality control check depended. According to SEOmonitor, approximately 10% of the monitored keywords experienced issues with incorrect results during the time frame of Oct. 9 through 13; however, they report most of the movements in their Visibility metric were minimal. The article does not indicate which prior day’s values were revised as a result.

AccuRanker states that it uses a “sandwich check” when monitoring stored data for a given keyword. This check indicates if there is a day where less than 50% of the websites listed on page 1 are the same from the previous day and the next day. A fixed sample of one in every two hundred keywords was used for this check, resulting in a flag rate of 30.2% for desktop keyword-days on Sept. 25 and 0.58% on Oct. 17. The blog post does not state if flagged days will be revised within customers’ stored data.

### How SERP API Providers Describe Their Handling

On Oct. 14, SerpApi, which sells Google results through an API, wrote in a public issue that it had deployed an update that “should reduce the number of instances in which poisoned results are returned” and that it was still working on the problem.

An Oct. 13 comment in the same issue passed along a customer’s request for a field that would flag searches without relevant results. The comment said downstream services currently have to review each search response.

AccuRanker’s API, AccuSERP, returns the page Google sends for a single search, so it can’t run the history check. The company says AccuSERP shares a pool of browser sessions with its rank tracker and draws first on sessions that passed the rank tracker’s check and have stayed clean since.

### Why This Matters

Teams who are going to be reviewing potential late-September/October drops should first look at how the vendors reported out during that time. Because it has a volatility safeguard, SEOmonitor could show the previous rank for up to two days of updates until it verifies if the big drop persists. You can refresh a keyword at AccuRanker, and we have checks we discussed in the Oct. 17 Pulse for keywords and their typical page 1 sites and via Search Console.

Search Console will be useful as additional evidence in a dispute regarding a drop. According to Google’s performance reporting help page , average position is based on the average position of the highest-ranking result on your site and that search engine results can vary depending on what type of device was used; where the search took place; when the search occurred; and the user’s search history. According to SEOmonitor, having a high average position does not inherently mean that an incorrect rank exists in SEOmonitor.

If an agency sends data again from September/October, they can ask the vendor if data stored for those dates were updated. If the vendor confirmed they had been updated, older exports may not reflect the current tool and therefore compare the two before sending them to a client.

Teams using API pulls for Google results can determine which types of safeguards exist for the API endpoint being pulled from (e.g., screened sessions, history checks) and whether their internal systems require validation of API response.

### Open Questions

As of Oct. 22, none of these vendor statements include a statement from Google. The same can be said for AccuRanker as they write “Google has made no statement.” In addition, each of the vendors described their own systems; however, none cites independent testing of how well their checks work.

Several vendors provided figures for their check percentages; however, those figures represent a variety of items. For example, the 8% reported by SEOmonitor represents results Google returned to them. On the other hand, AccuRanker’s sandwich figures were based upon a sample of the keyword days stored.

### Looking Ahead

SEOmonitor says it will update its incident page as Google’s changes develop and as its own changes go live. Ahrefs says it will post updates in its dashboard.

Check those updates before using figures from an affected period in your next client or management report.

More resources:

- Rank Tracking Broke In September – The Future Is Measured By Brand & Revenue

- The Future Of Rank Tracking Can Go Two Ways

- Google Completes September 2026 Spam Update After Nearly 14 Days

Featured Image: Tetiana Yurchenko/Shutterstock

Category SEO Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/rank-trackers-suspect-google-results/594049/)
