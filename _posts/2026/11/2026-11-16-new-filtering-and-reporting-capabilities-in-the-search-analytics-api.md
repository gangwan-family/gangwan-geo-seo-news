---
layout: post
title: "New filtering and reporting capabilities in the Search Analytics API"
date: 2026-11-16T00:00:00+00:00
source: "Google Search Central Blog"
source_slug: "google-search-central-blog"
generated_from: "GEO-SEO News/Google Search Central Blog/2026-11-16/New filtering and reporting capabilities in the Search Analytics API.md"
original_url: "https://developers.google.com/search/blog/2026/11/search-analytics-api-update"
categories:
  - "_src_google-search-central-blog"
---

# New filtering and reporting capabilities in the Search Analytics API

- Source: Google Search Central Blog
- Published: 2026-11-16
- URL: https://developers.google.com/search/blog/2026/11/search-analytics-api-update

## RSS 摘要

Over the past year, we introduced several updates to the Search Console Performance report to help you better slice and understand your traffic, including the branded queries filter, web multimodal search reporting, and multi-country and multi-device filtering.

## 原文正文

New filtering and reporting capabilities in the Search Analytics API | Google Search Central Blog | Google for Developers Skip to main content

- Search Central

- English

- Deutsch

- Español

- Français

- Indonesia

- Português – Brasil

- Tiếng Việt

- Русский

- 中文 – 简体

- 日本語

- 한국어

- Google Search Central Blog

- Home

- Search Central

- Google Search Central Blog

## New filtering and reporting capabilities in the Search Analytics API

Monday, November 16, 2026

Over the past year, we introduced several updates to the Search Console Performance report to help you better slice and understand your traffic, including the branded queries filter , web multimodal search reporting , and multi-country and multi-device filtering .

Today, we're bringing all three capabilities to the Search Analytics API , following ecosystem requests to make this data available for custom reporting and automated workflows.

### How these updates help website owners and developers

These API features make it easier for site owners, international businesses, and third-party tool builders to automate reporting at scale. Instead of stitching together separate requests or maintaining complex keyword regex lists, you can now query a group of countries (such as EMEA, LATAM, or DACH) and device combinations in a single API call, and automatically segment branded from non-branded traffic in your dashboards.

You can also pipe search metrics directly into your dashboards and monitoring workflows to track multimodal performance alongside other Google Search results. Because these filters work together, you can slice your data even further, such as monitoring brand growth across specific regional hubs or seeing which pages perform best in multimodal search across key markets and devices.

### How to pull the new data from the Search Analytics API

We've added three new options to the Search Analytics API :

- Branded queries : Group or filter your data by brandedClassification to compare branded and non-branded performance. As in Search Console, this data is only available for eligible properties . For other properties, the response won't include any rows.

- Web multimodal : Set type to webMultimodal to get performance data from Google Lens, Circle to Search on Android, and image uploads in Google Search. This data will also be available in BigQuery for properties with an active bulk data export .

- Multi-country and multi-device filters : Use the new filterLists field to filter by several countries or devices in a single request.

For the full details, including supported values and combinations, see the Search Analytics API documentation .

We hope these additions make it easier to automate your search performance reporting. If you have any questions or feedback, please reach out to us on LinkedIn or post in the Google Search Central Community .

Posted by Daniel Waisberg , Nati Yosephian , Karin Gadasi , Search Console team.

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License , and code samples are licensed under the Apache 2.0 License . For details, see the Google Developers Site Policies . Java is a registered trademark of Oracle and/or its affiliates.

## 原文链接

[Read original](https://developers.google.com/search/blog/2026/11/search-analytics-api-update)
