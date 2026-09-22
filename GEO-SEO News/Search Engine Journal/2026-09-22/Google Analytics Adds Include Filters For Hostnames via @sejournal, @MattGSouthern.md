---
title: "Google Analytics Adds Include Filters For Hostnames via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-22T08:06:17+00:00
fetched_at: 2026-09-22T23:40:24.283022+00:00
url: "https://www.searchenginejournal.com/google-analytics-include-hostname-filters/590336/"
guid: "https://www.searchenginejournal.com/google-analytics-include-hostname-filters/590336/"
author: "Matt G. Southern"
categories:
  - "Analytics & Data"
  - "News"
---

# Google Analytics Adds Include Filters For Hostnames via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-22
- URL: https://www.searchenginejournal.com/google-analytics-include-hostname-filters/590336/
- Author: Matt G. Southern
- Categories: Analytics & Data, News

## RSS 摘要

Google Analytics supports Include data filters for hostnames, so a property can keep event data from approved domains instead of excluding spam one by one. The post Google Analytics Adds Include Filters For Hostnames appeared first on Search Engine Journal .

## 原文正文

Google Analytics Adds Include Filters For Hostnames Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- Analytics & Data

## Google Analytics Adds Include Filters For Hostnames

- Google added Include data filters for hostnames, an allowlist of approved domains.

- Measurement Protocol events skip the filter, and events with no hostname get blocked.

- An active data filter permanently changes incoming data, so Google provides a Testing state before activation.

Google Analytics supports Include data filters for hostnames, so a property can keep event data from approved domains instead of excluding spam one by one.

Google Analytics now supports Include data filters for hostnames, letting a property list the domains it will keep event data from. The change appears in a Sept. 21 entry on Google’s What’s new in Google Analytics page.

Until now, hostname filters could only exclude. When Google added the filter type on June 11, its release note said it let customers “filter out (exclude) events based on their hostname.” With an Include filter, you define approved hostnames instead of adding unwanted hostnames to an Exclude filter.

### What’s New

Google’s release note frames the change as ending the upkeep an exclude list needs. It reads:

“Previously, filtering was limited to Exclude filters, which required ongoing manual updates to keep up with new sources of spam. By allowing you to define a list of approved hostnames, this feature simplifies configuration and helps ensure the integrity of your analytics data with minimal maintenance.”

The note says Include filters “will not be applied to events sent from the Measurement Protocol, ensuring this data remains unblocked.”

Events with no hostname at all go the other way and get blocked. The example given is gtag.js traffic, and the entry says “a missing hostname typically indicates spam or abnormal traffic.”

### What To Know Before Activating

Data filters act on incoming data only. Google’s data filters help page says Analytics evaluates them “from the point of creation forward,” so older data does not change.

Once a filter is Active, the effect is permanent. Matching events are never processed, and the same page says they “will never be available in Google Analytics or BigQuery.”

Google’s setup page for hostname filters advises testing a filter before activating it. The Testing state tags matching events with a “Test data filter name” dimension instead of dropping them. Google says a data filter can take 24 to 36 hours to apply.

### Why This Matters

An exclude list is only as current as the last unwanted hostname you noticed. With an allowlist, you list your production domains once and stop editing the filter every time a new one shows up. Because Active filters permanently change incoming data, the configuration should be tested before activation. Google’s release note doesn’t explain how Include matching works for subdomains or properties receiving data from several hostnames.

### Looking Ahead

The release note gives no rollout details, so it is not clear whether the Include option is in every property yet. For now, users can check the Data filters section in Admin to see whether the Include option is available in their property.

As of Sept. 22, Google’s setup page for hostname filters and its data filters overview still describe the feature as exclude-only. When I covered Google’s AI Assistant channel in May , the definitions page lagged the release note the same way.

Featured Image: Cast Of Thousands/Shutterstock. Google wordmark: Source: Google.

Category News Analytics & Data

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-analytics-include-hostname-filters/590336/)
