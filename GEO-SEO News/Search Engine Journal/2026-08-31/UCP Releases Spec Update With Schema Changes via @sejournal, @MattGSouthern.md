---
title: "UCP Releases Spec Update With Schema Changes via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-08-31T10:00:27+00:00
fetched_at: 2026-09-01T00:41:30.291545+00:00
url: "https://www.searchenginejournal.com/ucp-releases-spec-update-with-schema-changes/587590/"
guid: "https://www.searchenginejournal.com/ucp-releases-spec-update-with-schema-changes/587590/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# UCP Releases Spec Update With Schema Changes via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-08-31
- URL: https://www.searchenginejournal.com/ucp-releases-spec-update-with-schema-changes/587590/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

The Universal Commerce Protocol's first spec release since April adds grocery readiness, lays groundwork for food and lodging, and brings schema changes. The post UCP Releases Spec Update With Schema Changes appeared first on Search Engine Journal .

## 原文正文

UCP Releases Spec Update With Schema Changes Skip to content

- SEJ

- ⋅

- AI Search

## UCP Releases Spec Update With Schema Changes

- The UCP project released its first update since April.

- The release adds grocery features and lays groundwork for food and lodging commerce.

- Anyone running the affected schemas needs updates before moving to the new version.

The Universal Commerce Protocol's first spec release since April adds grocery readiness, lays groundwork for food and lodging, and brings schema changes.

The Universal Commerce Protocol (UCP) project has released an updated specification . This new version includes features specifically designed for grocery shopping and paves the way for further development in food and lodging commerce, complementing retail.

This update includes breaking changes that require updates for affected schemas. It represents UCP’s fourth overall release and the first release since April. Google introduced the protocol at NRF in January , and I previously covered the Cart and Catalog features introduced in March.

The announcement was published on the project’s website and GitHub. Since then, UCP’s Governing Council has expanded, adding Stripe in April alongside permanent members Google and Shopify.

### What The Release Includes

The release notes describe structural changes to facilitate multi-vertical expansion, along with updates on payment security and grocery features. The grocery enhancements include location tools that enable agents to find physical stores and access information such as addresses, operating hours, and map coordinates. A standardized store hours format has also been introduced, and agents can now place orders by weight.

The payments feature has been updated to include vendor-neutral 3D Secure 2 authentication, payment schedules with deposits and installments, and support for splitting orders across various payment methods. Additionally, the specification has been reorganized into Shopping, Payment, and Common sections, with payment features positioned to be relevant across different categories, not just retail checkout.

### Breaking Changes For Adopters

The release notes say the breaking changes require schema updates. Fulfillment schemas have been modified to a new structure, and buyer consent now lives in a flexible map instead of fixed fields. Profile signing keys are now consolidated into a single JWK Set, a common key format.

UCP versions are labeled by dates instead of numbers, helping platforms and businesses agree on which versions to use. Businesses can still support earlier versions even as they update to the latest ones.

### The Push Beyond Retail

UCP’s growth into sectors beyond retail follows governance changes made earlier this summer. In July, the Governing Council set up a Food Technical Council with initial members Block (Square), DoorDash, Google, Toast, and Uber Eats. Later, on August 11, a Lodging Technical Council was created with Amadeus, Booking.com , Expedia, Google, Hilton, Marriott, and Trip.com .

According to UCP’s roadmap , new specifications are being developed in collaboration with industry leaders for both food and lodging sectors. The food developments involve processes like locating restaurants and menus, selecting dishes, and handling checkout with tipping and delivery notes. The lodging efforts focus on hotel searches, room selection, and reservations.

The project describes this release as laying the groundwork for these industries, with shared components like token binding being redesigned to support them.

### Why This Matters

If your company has implemented UCP, start by reviewing the breaking changes section in the release notes. Whether you need to update your schema depends on the features you are currently using.

The protocol for checkout in AI Mode and Gemini is expanding toward food, grocery, and travel, with the companies leading this effort being the platforms that already serve these industries.

The release doesn’t say grocery ordering or hotel booking is available through any AI interface. The food and lodging features included are basic steps, laying the groundwork for future updates that are still being worked on.

### Looking Ahead

As of publication, UCP’s announcements page doesn’t have a specific release timeline for the food or lodging specifications. On the retail side, news from Google I/O revealed that UCP-powered checkout is expanding to Canada and Australia, with the U.K. planned for later.

Featured Image: Natalya Kosarevich/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/ucp-releases-spec-update-with-schema-changes/587590/)
