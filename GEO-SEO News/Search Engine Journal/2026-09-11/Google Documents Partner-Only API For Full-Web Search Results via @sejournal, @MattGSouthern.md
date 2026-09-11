---
title: "Google Documents Partner-Only API For Full-Web Search Results via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-11T17:32:12+00:00
fetched_at: 2026-09-11T23:24:12.565053+00:00
url: "https://www.searchenginejournal.com/google-documents-partner-only-api-for-full-web-search-results/589194/"
guid: "https://www.searchenginejournal.com/google-documents-partner-only-api-for-full-web-search-results/589194/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Tools"
---

# Google Documents Partner-Only API For Full-Web Search Results via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-11
- URL: https://www.searchenginejournal.com/google-documents-partner-only-api-for-full-web-search-results/589194/
- Author: Matt G. Southern
- Categories: News, Tools

## RSS 摘要

Google's developer docs for the Web Search Service API show a partner-only path to full-web search results. The post Google Documents Partner-Only API For Full-Web Search Results appeared first on Search Engine Journal .

## 原文正文

Google Documents Partner-Only API For Full-Web Search Results Skip to content

Webinar: AI Cites Your Brand. Now What? Turn AI Visibility Data Into Actions

Register Now

- SEJ

- ⋅

- Tools

## Google Documents Partner-Only API For Full-Web Search Results

- Google documented its Web Search Service API, which returns Google Search results as JSON.

- Access requires a Google Cloud project, API key, and client ID from a partner agreement.

- Custom Search JSON API users needing full-web results must move by January.

Google's developer docs for the Web Search Service API show a partner-only path to full-web search results.

Google refreshed its public developer documentation for the Web Search Service API, a service that lets partners retrieve and display Google Search results in their websites and apps. Google updated the main overview page and four related pages on September 9, and every request needs a client ID tied to a partner agreement on top of a Google Cloud project and API key. The Custom Search JSON API, which ends in January 2027, is the backdrop. Back in January , Google told anyone needing full-web results to get in touch about a separate full-web solution.

### What The API Provides

Google documents one primary method, Search, which the reference page describes as performing a “full web search.” It returns results in JSON format through REST or gRPC. Each request must include a partner client ID, the user’s IP address, and the search query. As mentioned in the invoke guide , including the IP address helps with regional routing and also helps prevent misuse. You can receive up to 20 results per request, 10 by default, with an option to get more pages using a token. Users can filter results by language, country, date range, enable SafeSearch, or sort by date. The response provides fields such as title, URL, snippet, MIME type, file format, an estimated total results count, and a corrected query if Google recommends one.

### Access Is Restricted

The pages refer to users as “programmatic partners.” On the introduction page , it’s explained that requests are connected to the partner agreement through the client ID. This ID follows a standard format, including details like the partner, name, product, and feature set.

This differentiates the service from an API that a developer can enable in a Google Cloud project and start using right away. However, the pages don’t provide details on how a company can become a partner, what the service costs, or what query limits might be in place.

### How This Fits The Search API Transition

In January, Google announced that the Programmable Search Element, their site search widget, will now focus on searches across 50 or fewer domains. They pointed enterprise needs like conversational search and grounding to Vertex AI Search. For partners who want to look beyond a set of sites, Google said it has a full web search solution for “those requiring our entire index.” Interested partners can sign up by filling out a form. Google hasn’t shared detailed features or pricing yet. Search Element users who search on more than 50 domains or across the entire web will need to switch to a different solution by January 1, 2027. The same deadline applies to Custom Search JSON API users, and Google’s API overview page now says the API is closed to new customers and will be discontinued on that date.

The Web Search Service API matches the full-web use case from January on two points. It performs a full web search, and it is limited to partners. As of September 11, neither the January post nor the updated pages mention each other.

### Why This Matters

Google’s January announcement shared an interest form for developers who need full-web results, but it didn’t include many details about that offering. The updated Web Search Service documentation now provides a much clearer explanation of how Google’s partner-only API works and what a request must carry to be accepted. People using the Custom Search JSON API for full-web projects still don’t have a complete migration path. Google has documented a full-web API for partners, but it hasn’t said if current users can switch over or what requirements companies need to meet to become partners.

### Looking Ahead

Google’s January 1, 2027 deadline stands. Meanwhile, watch for updates on partner eligibility, costs, query limits, and whether Google names the Web Search Service API as the path for full-web Custom Search users.

Google’s January post still directs Custom Search users who need full-web results to its interest form. The Web Search Service documentation doesn’t explain how a company obtains the required partner agreement.

Google logo — Source: Google. Featured Image: Accogliente Design/Shutterstock

Category News Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-documents-partner-only-api-for-full-web-search-results/589194/)
