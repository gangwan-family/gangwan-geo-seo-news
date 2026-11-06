---
title: "SERP Data Providers Say Google Is Throttling Goto Result Links via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-11-05T11:48:21+00:00
fetched_at: 2026-11-06T01:40:26.846492+00:00
url: "https://www.searchenginejournal.com/google-goto-result-links-throttling/595959/"
guid: "https://www.searchenginejournal.com/google-goto-result-links-throttling/595959/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Tools"
---

# SERP Data Providers Say Google Is Throttling Goto Result Links via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-05
- URL: https://www.searchenginejournal.com/google-goto-result-links-throttling/595959/
- Author: Matt G. Southern
- Categories: News, Tools

## RSS 摘要

SERP data providers say Google throttles goto links per results page, so some rank data may store Google redirect links in place of page URLs. The post SERP Data Providers Say Google Is Throttling Goto Result Links appeared first on Search Engine Journal .

## 原文正文

SERP Data Providers Say Google Is Throttling Goto Result Links Skip to content

Webinar: 9 AI Workflows For Better Content. Nov 18, 2 PM ET.

Save Your Spot

- SEJ

- ⋅

- Tools

## SERP Data Providers Say Google Is Throttling Goto Result Links

- Two SERP data providers say Google now throttles goto link lookups per results page.

- Some SERP data request modes may return Google redirect links instead of destination URLs.

- Check stored landing pages before reporting URL-level ranking losses from late October.

SERP data providers say Google throttles goto links per results page, so some rank data may store Google redirect links in place of page URLs.

Google is restricting the speed at which anyone can follow (google.com/goto) redirects for search results on each page, as per DataForSEO and Serper . Both sell Google search result API access. Due to this restriction rank data provided by these services may contain Google redirect URLs instead of actual URLs.

According to DataForSEO, the restrictions mean that they have seen some of their request modes only resolving part of the destination URLs. Serper’s status page first noted the issue at 1:30 a.m. UTC on October 30. SerpApi, another seller of search data, also logged goto links for organic results on the same date. Neither DataForSEO nor Serper links to a Google announcement regarding the restriction and the statements below are from their websites.

### How The Limit Works

DataForSEO stated in its November 2nd article that when you open multiple links from the same results page in rapid succession, Google will begin to throttle the redirect(s). Each link carries an identifier based on the results page it originated from.

When Google throttles your redirects, instead of sending your requests for resolution directly to the destination, Google will send back a page with a “Continue” button. That button will only become available after a waiting period. The amount of time the continue button is disabled grows the faster the previous links were resolved.

For example, take a results page that contains 18 goto links to other websites. If all 18 links are requested in quick succession, Google may allow the first 5-6 to be resolved immediately. However, the 7th link may result in a 1 second wait before being able to access the website. The 8th link may then take 3 seconds. And this process continues until the 15th link, where there could be a 40 second wait before accessing that website. DataForSEO reported that they had instances of waiting up to 120 seconds for 1 URL.

The limit is based on the results page and not based on the IP address or the search query used. Also, DataForSEO reports that simply switching IP addresses or search queries will not help bypass this limitation. Additionally, it says that even if you wait an hour or longer before resolving all of the links, Google still uses the same results page limits.

### What SERP Data Providers Are Doing

DataForSEO’s Standard Priority mode now resolves all goto URLs, although the added delays may mean execution takes longer. In High Priority and Live modes, the company says about half of goto URLs are resolved.

Serper’s status page says Google “limits how many /goto result links can be followed per results page.” Its first fix resolved the top three organic links and returned results four through 10 as goto links, which Serper said work about 30 seconds after the search. It added a /resolve endpoint to fetch the rest.

On Oct. 31, Serper said it had found another way to get the real URLs and that all result links had them again. It called that “likely temporary.”

SerpApi’s Status Page displays an October 30th event indicating that its Google Search API returned goto links instead of regular links for organic search results; it states that they had the issue fixed by November 2nd. However, there is a second incident reported on November 3rd reporting intermittent issues with the same problem. Neither incident gives a cause.

### How Goto Links Got Here

DataForSEO dates Google’s move to www.google.com/goto links in Search Results to late August. It says the links cannot be decoded, and therefore a tool will have to follow each link to find out where it goes. The link-following part is what the new limit slows down.

### Why This Matters

Some rank tracking services as well as in house reports using landing pages for URL-level reporting may display Google goto redirects (google.com/goto) in place of true destination URLs from approximately October 30th onward based upon the service provider and how the requests were made. If a specific URL is missing from a URL-level report it could still be showing up in a ranking position and have an unresolved redirect at the URL location. Prior to reporting a URL-level loss check whether the stored URL is a Google redirect, also contact your service provider and determine what method was used to collect the data.

### Looking Ahead

As of my check on Nov. 4, SerpApi’s Incident Report on goto links from Nov. 3 is still listed as Identified. Serper states that in the event that Google also puts a cap on the method it uses for retrieving actual URLs, it would revert to automatically resolving the top three results and use /resolve to fetch the remaining after approximately thirty seconds. DataForSEO stated it will continue to adjust its processing based on what it observes regarding how Google deals with goto resolutions.

Reports covering the last few days of October through early November should be reviewed again at some point when providers have determined how they will handle goto resolution.

Featured Image: Teodora ART/Shutterstock

Category News Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-goto-result-links-throttling/595959/)
