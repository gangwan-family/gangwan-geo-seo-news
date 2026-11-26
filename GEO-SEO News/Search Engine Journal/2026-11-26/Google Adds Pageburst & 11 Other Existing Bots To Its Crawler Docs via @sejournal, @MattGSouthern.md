---
title: "Google Adds Pageburst & 11 Other Existing Bots To Its Crawler Docs via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-11-26T03:22:22+00:00
fetched_at: 2026-11-26T03:40:40.847232+00:00
url: "https://www.searchenginejournal.com/google-adds-pageburst-11-other-existing-bots-to-its-crawler-docs/599120/"
guid: "https://www.searchenginejournal.com/google-adds-pageburst-11-other-existing-bots-to-its-crawler-docs/599120/"
author: "Matt G. Southern"
categories:
  - "News"
  - "PPC"
---

# Google Adds Pageburst & 11 Other Existing Bots To Its Crawler Docs via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-26
- URL: https://www.searchenginejournal.com/google-adds-pageburst-11-other-existing-bots-to-its-crawler-docs/599120/
- Author: Matt G. Southern
- Categories: News, PPC

## RSS 摘要

Google's crawler docs now list pageburst, which renders pages for Google Ads and ignores robots.txt, plus more existing user agents to check in server logs. The post Google Adds Pageburst & 11 Other Existing Bots To Its Crawler Docs appeared first on Search Engine Journal .

## 原文正文

Google Adds Pageburst & 11 Other Existing Bots To Its Crawler Docs Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

- SEJ

- ⋅

- PPC

## Google Adds Pageburst & 11 Other Existing Bots To Its Crawler Docs

- Google documented pageburst, which renders pages for Google Ads and ignores robots.txt rules.

- Several newly listed strings look like browsers, so filters keyed on Googlebot miss them.

- Check logs and bot rules for these strings, and verify requests by Google's IP ranges.

Google's crawler docs now list pageburst, which renders pages for Google Ads and ignores robots.txt, plus more existing user agents to check in server logs.

Google identified pageburst as a user agent that renders pages to measure Google Ads quality and landing page safety and ignores robots.txt rules. Its two strings look like a browser’s and do not contain “Googlebot”; a bot rule created using “Googlebot” will not capture them.

Pageburst is one of 12 existing user agents Google added to its crawler documentation on Nov. 23, along with a corrected entry for APIs-Google. Google’s crawling documentation changelog explains:

“These crawlers and fetchers are not new; we’re documenting existing high-volume clients that are more likely to show up in server logs and that we’ve received questions about.”

The 12 belong to Google products other than Search, such as Google Ads, Gmail and Google Cloud.

### What Pageburst Does

Google’s special-case crawlers page , which lists crawlers used by specific Google products, says pageburst “renders web pages for Google Ads quality, landing-page safety, and page understanding.” The entry adds that “it’s unaffected by crawling preferences.”

The desktop string identifies as Chrome on Linux and the mobile one as Chrome for iOS on an iPad, and both include “compatible; pageburst.”

AdsBot, which checks web page ad quality for Google Ads, has its own robots.txt token. Pageburst’s entry lists no token and says the user agent “ignores robots.txt rules.”

The highlights show what to look for in server logs and where Google states its robots.txt policy.

Screenshot from Google for Developers ( CC BY 4.0 ), with highlights added.

Google’s documentation says user-agent strings can be faked. Special-case crawlers use the IP addresses defined in Google’s special-crawlers.json ; these have a reverse-DNS match of rate-limited-proxy-***-***-***-***.google.com . The pageburst entry does not say what occurs when a website blocks the Google Ads check.

### The Other 11 User Agents

Besides pageburst, each of the five other newly documented special-case entries says the user agent “ignores robots.txt rules.”

- Google-analytics-postbacks sends Google Analytics attribution postbacks to ad networks when conversions happen.

- Google-Calendar-Importer refreshes .ics feeds that Google Calendar users subscribe to.

- GoogleDocs powers Google Sheets functions such as IMPORTHTML.

- Google-Edu verifies domains submitted for Google Workspace for Education.

- PlayStore-Google checks developer-submitted URLs in Google Play Store listings.

Google’s user-triggered fetchers page covers the six newly documented fetchers and says that because a user requested the fetch, these fetchers “generally ignore robots.txt rules.” Three of those (AppEngine-Google, Google-Apps-Script and Google-Cloud-Tasks) send requests for code running within Google’s platform-based products. The remaining three are GoogleImageProxy, which is used to load image content into email applications such as Gmail, along with Google Web Preview and the PageSpeed Insights fetcher, both with strings ending in Chrome-Lighthouse.

Several of the newly listed user agents seem to use standard browser strings. For example, a string from GoogleImageProxy appears similar to Firefox 11 on Windows NT 5.1; the strings for Google Web Preview and PageSpeed Insights, and one of PlayStore-Google’s, were created using Chrome strings. A filter that only identifies “Googlebot” would miss all of these.

### Google Moves APIs-Google To The Fetchers List

Google has moved APIs-Google, which makes requests to the webhook notification systems developers create within Google Cloud and Google Workspace APIs, from the list of special-case crawlers to the list of user-triggered fetchers. APIs-Google’s push requests, the changelog says, “come from the user-triggered fetcher IP ranges and ignore robots.txt rules.” Google added a missing semicolon after “APIs-Google” in its documented string and tells developers to modify any code that was previously using a hardcoded version of the earlier string.

Prior to the Nov. 23 update, Google had included robots.txt as a method to block requests from APIs-Google in its documentation. In an Oct. 21 capture , the robots.txt token was present on the special-case page. On Oct. 30, a capture of the APIs-Google page showed “Use robots.txt” as one of two methods to block requests from APIs-Google. Now the APIs-Google page says that it “ignores robots.txt rules”; for controlling the delivery of notifications, the page points to either the developer who created the notification system or Google Cloud’s abuse form for unexpected requests.

### Why This Matters

Pageburst renders pages for ads in Google and does not follow robots.txt. Check for “pageburst” in the log entries for your servers and CDNs, verify with Google’s procedures that the IP addresses are in its special-crawler ranges, and see if your pages were delivered to the verified requests, or if a challenge or a 403 was returned.

Roger Montti covered Google’s advice on Nov. 18 that general bot blocking may keep Googlebot from crawling content when moving a CDN; the same advice should be applied to other Google clients that do not have the name Googlebot.

### Looking Ahead

Google’s special-case and user-triggered pages both say their lists aren’t exhaustive and cover the requestors “more likely to show up in log files.” The crawling documentation changelog, which is where Google logs additions like these, has an RSS feed.

Featured Image: BalkansCat/Shutterstock

Category News PPC

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-adds-pageburst-11-other-existing-bots-to-its-crawler-docs/599120/)
