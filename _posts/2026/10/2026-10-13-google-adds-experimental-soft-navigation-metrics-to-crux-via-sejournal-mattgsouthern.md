---
layout: post
title: "Google Adds Experimental Soft Navigation Metrics To CrUX via @sejournal, @MattGSouthern"
date: 2026-10-13T21:31:39+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-13/Google Adds Experimental Soft Navigation Metrics To CrUX via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/google-experimental-soft-navigation-metrics-crux/592820/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Tools"
  - "_src_search-engine-journal"
---

# Google Adds Experimental Soft Navigation Metrics To CrUX via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-13
- URL: https://www.searchenginejournal.com/google-experimental-soft-navigation-metrics-crux/592820/
- Author: Matt G. Southern
- Categories: News, Tools

## RSS 摘要

Experimental Core Web Vitals that count in-app page changes are now in the Chrome UX Report, with Search Console set to follow. The post Google Adds Experimental Soft Navigation Metrics To CrUX appeared first on Search Engine Journal .

## 原文正文

Google Adds Experimental Soft Navigation Metrics To CrUX Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- Tools

## Google Adds Experimental Soft Navigation Metrics To CrUX

- Chrome added experimental Core Web Vitals to CrUX that count soft navigations inside single-page apps.

- Most sites should see little change; SPA-heavy sites can expect higher pass rates.

- Stable scores are unchanged; Search Console switches after a targeted May 2027 graduation.

Experimental Core Web Vitals that count in-app page changes are now in the Chrome UX Report, with Search Console set to follow.

Chrome has announced experimental versions of all three Core Web Vitals in the Chrome User Experience Report (CrUX). These metrics count soft navigations, which refer to the in-app page changes a single-page application (SPA) makes without a full reload. They’re available in BigQuery, the CrUX API, and the History API as of the release published October 13, and CrUX Vis now includes a toggle to show them.

About 70% of origins in CrUX have little or no soft navigation traffic, so most sites probably won’t notice much of a difference. Sites that rely heavily on soft navigations are most likely to see a change, and their experimental scores tend to be higher.

Google’s stable scores are unchanged at this time. Chrome aims to conclude the metrics’ experimental status in May 2027, subject to the feedback it receives. Chrome says Search Console will adopt the new data once that happens.

### What’s In The Release

There have been three new fields added to CrUX, experimental_largest_contentful_paint_with_softnavs along with one each for INP and CLS. They track the exact same measurements as the stable versions of those fields; however, they count both hard loads and detected soft navigation events.

Prior to the inclusion of soft navigation tracking, CrUX only measured an SPA’s first load. Subsequent in-app changes were grouped together with that first load, all interactions and layout shifts attributed back to the landing URL. With the ability to detect and record soft navigation events, every time a user’s actions cause a change in both content and URL it is tracked individually, and the associated metrics are provided under the destination URL subject to the normal eligibility criteria.

This data has come from the Soft Navigations API which has been turned on by default since the release of Chrome Version 151 on July 28. When a user takes an action that results in both a visible change to the URL and a visible paint, then Chrome considers this a “soft navigation”. I wrote about the origin trial in August 2025 prior to the announcement that CrUX would be integrating this.

### Which Sites See A Change

Google’s post sorts CrUX origins by the share of their page views that are soft navigations. Between 66% and 75% of origins have fewer than 5%, depending on platform. Only 7.0% on Android and 10.6% on desktop have more than half.

Among the top 1,000 sites, 35% on Android and 42% on desktop rely on soft navigations for more than half of their page views.

Annie Sullivan, who wrote the post, puts it this way:

“If your site doesn’t use JavaScript to dynamically swap out page content and update the URL without a full browser reload, you shouldn’t expect to see any changes in your metrics.”

### How The Scores Move

For sites where more than half of page views are soft navigations, all three metrics improve. Among Android origins with 75% to 100% soft navigations, the share with good LCP is 26% on the stable metric and 87% on the experimental one. Sullivan writes:

“This isn’t because SPAs are faster than multi-page websites (MPAs) overall, but because follow-up clicks are faster on any site, bringing SPAs with many follow-up visits in line with MPAs with many follow-up visits.”

INP improves by measuring responsiveness per page view instead of using the slowest interaction across a session. The post says this roughly doubles Android pass rates for sites relying mainly on soft navigations. SPA-heavy sites still lag behind multi-page sites on INP, so heavy JavaScript during page changes can affect it.

The changes made to CLS have improved things as well, since all of the layout shift events are now grouped by view instead of session. The author states that this puts SPA-heavy desktop sites on par with multi-page sites; Android is still slightly behind.

The release notes for the September dataset state that 55.9 percent of all origins worked well on the Core Web Vitals test when soft navigations were not counted. When they were, that number was 59.5 percent.

### Why This Matters

Chrome’s new metrics show how an SPA performs by measuring each soft navigation separately, rather than charging the landing page for everything that happens afterward.

On an SPA-heavy site, you can turn on the new “Include soft navigations” toggle in CrUX Vis to compare both versions of each metric side by side. This makes it easier to see whether your site meets Google’s thresholds on the experimental numbers and which metrics change the most. Just keep in mind that these numbers may still change before Search Console picks them up. On a site that reloads with every click, turning on the toggle shouldn’t make any difference.

### Looking Ahead

Every metric is still experimental, and Chrome welcomes your feedback through the web-vitals feedback group and the soft navigations spec repository on GitHub. It advises readers to “expect some shifts from month to month as the measurement improves,” so it’s best to interpret the new numbers cautiously until they stabilize.

The November CrUX release will be the next checkpoint, with soft-navigation versions of FCP and navigation types expected. In the Web Vitals lifecycle , metrics move from experimental to pending for at least six months before becoming stable. Google says it will switch Search Console once the metrics leave the experimental stage, though the post doesn’t say which stage comes next. Check the release notes for updates to the May 2027 target or changes in how progress is described.

Featured Image: Tetiana Yurchenko/Shutterstock

Category News Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-experimental-soft-navigation-metrics-crux/592820/)
