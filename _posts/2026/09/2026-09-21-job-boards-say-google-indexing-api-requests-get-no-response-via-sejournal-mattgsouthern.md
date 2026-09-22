---
layout: post
title: "Job Boards Say Google Indexing API Requests Get No Response via @sejournal, @MattGSouthern"
date: 2026-09-21T20:30:43+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-21/Job Boards Say Google Indexing API Requests Get No Response via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/google-indexing-api-approval-job-sites/590316/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Web Dev SEO"
  - "_src_search-engine-journal"
---

# Job Boards Say Google Indexing API Requests Get No Response via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-21
- URL: https://www.searchenginejournal.com/google-indexing-api-approval-job-sites/590316/
- Author: Matt G. Southern
- Categories: News, Web Dev SEO

## RSS 摘要

Job site operators report months-long waits for Google Indexing API approval, with no stated review timeframe in Google’s documentation. The post Job Boards Say Google Indexing API Requests Get No Response appeared first on Search Engine Journal .

## 原文正文

Job Boards Say Google Indexing API Requests Get No Response Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- Web Dev SEO

## Job Boards Say Google Indexing API Requests Get No Response

- Job site operators report months without an approval or rejection from Google.

- Google's John Mueller said in May he imagined the team is more cautious now.

- Google describes the default quota as testing and says API use requires additional approval.

Job site operators say Google Indexing API approval requests go unanswered for months. Google's docs recommend the API but don't state a review timeframe.

Job site operators say their requests for approval to use Google’s Indexing API are going unanswered for months. Google’s documentation still recommends the API for job posting URLs.

SEO consultant Nick LeRoy, who runs SEOJobs.com and PPCJobs.com, drew new attention to the problem in a Sept. 19 thread on X . LeRoy wrote that neither job board has been approved or given a quota increase.

The reports go back to at least May, and three more appeared in Google’s help forum this month. For job sites, approval decides whether the API can be used beyond a quota Google describes as for testing. Google’s public Indexing API documentation does not state a typical approval timeframe.

### What Job Site Operators Report

In his Sept. 19 thread, LeRoy said he and job board consultant Alexander Chukovski have “100+ job boards as data points.” The two “hypothesize that Google hasn’t approved any submissions in 2026,” he wrote.

That is their hypothesis, and LeRoy has been open about its limits. In a July issue of his newsletter , he said he had resubmitted requests for both sites six months earlier.

“Not an approval. Not a rejection. Not a request for more information,” LeRoy wrote. He added, “Can I confirm the number is zero? No.”

Chukovski, who sells SEO consulting to job boards, wrote in July that he had “visibility over at least 50 different applications” since October 2025 and that none had gone through. He said in the same post that he has no inside information.

Other operators have shared similar wait times in the Google Search Central Community. On May 22 , a job board operator mentioned they had submitted the form multiple times over the past six to nine months but hadn’t received any response and still faced the default quota. Another job board’s post from September 8 reported the same.

On September 2nd , an operator said they hadn’t received any acknowledgment, reference number, or visible status on their request. Similarly, on September 10th , a Belgian job board shared that a request submitted on August 21st still hadn’t received any approval or rejection.

### What Google’s Documentation Says

Google’s job posting structured data guide tells site owners to use the Indexing API. It reads:

“For job posting URLs, we recommend using the Indexing API instead of sitemaps because the Indexing API prompts Googlebot to crawl your page sooner.”

That page doesn’t mention approval, but the Indexing API quickstart does. It says the API “provides a default 200 quota for API onboarding and submission testing, and it requires additional approval for usage and resource provisioning.”

Google clarified this on Sept. 4, 2024. Its documentation changelog gives the reason as “to better explain that the default quota is for initial setup and testing.” On Sept. 11, 2024, Google added a spam warning to the quickstart, which I covered at the time .

Site owners request approval through a Google Form linked from the quota page . On how requests are judged, that page says only that the “quota may increase or decrease based on the document quality.”

The quickstart, quota, and usage pages describe no way to check whether a request is pending, approved, or rejected. The quota page points to the Google API Console, which shows a project’s current quota.

### What Google Has Said

Google’s John Mueller responded in May, after LeRoy raised his stalled requests on Bluesky. Mueller replied :

“I’m not aware of any particular issues, but I know the indexing API is inundated by bloggers trying to act like legitimate sites, so I imagine they’re just a bit more cautious nowadays.”

The reply doesn’t describe the review process.

Search Engine Journal inquired with Google about whether job site requests are being reviewed, how long the review process usually takes, if applicants can check the status of their requests, and whether publish requests are handled differently before approval. As of the time of publication, Google had not responded.

### What An HTTP 200 Response Means

Google’s Indexing API usage page defines an HTTP 200 response narrowly, saying it “means that Google may try to recrawl this URL soon.”

Several operators report that a publish request returns HTTP 200, then a follow-up call for the same URL to the getMetadata endpoint returns 404. Google says that endpoint shows the last time it received a notification for a URL. Both the forum posters from September 2 and September 10 mentioned noticing the same pattern, and the Belgian site saw it through two different setups. LeRoy also shared similar findings in July.

The usage page doesn’t clarify if requests sent prior to approval are treated differently. Google’s errors page provides a generic description for 404 errors and doesn’t link them to approval status.

A Google Diamond Product Expert told the September 10 poster that the 404 was a strong sign the project hasn’t been approved, and mentioned that the first 200 response can be helpful for testing a setup. Keep in mind, Product Experts are volunteers, not official Google staff, so their insights aren’t official Google statements.

### Why This Matters

Google’s job posting guide recommends using the Indexing API as a quicker alternative to sitemaps. The API’s own documentation says using it beyond testing requires additional approval. Operators who have requested access report waiting months without any response, making it hard to tell if they are simply in a slow queue or have been rejected. The guide also still recommends submitting a sitemap for full site coverage.

### Looking Ahead

Short of a statement from Google, a change to the approval process would most likely show up first on the Indexing API quota page or in Google’s documentation changelog, where the 2024 clarification was logged.

Featured Image: Sahabzady/Shutterstock

Category News Web Dev SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-indexing-api-approval-job-sites/590316/)
