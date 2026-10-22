---
title: "Google Crawls Raw And Encoded Bracket URLs Separately via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-21T12:06:29+00:00
fetched_at: 2026-10-22T00:03:56.030283+00:00
url: "https://www.searchenginejournal.com/google-crawls-raw-and-encoded-bracket-urls-separately/593765/"
guid: "https://www.searchenginejournal.com/google-crawls-raw-and-encoded-bracket-urls-separately/593765/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Technical SEO"
---

# Google Crawls Raw And Encoded Bracket URLs Separately via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-21
- URL: https://www.searchenginejournal.com/google-crawls-raw-and-encoded-bracket-urls-separately/593765/
- Author: Matt G. Southern
- Categories: News, Technical SEO

## RSS 摘要

Google's John Mueller says raw and percent-encoded brackets are different URLs and recommends using one form across links, canonical tags, and sitemaps. The post Google Crawls Raw And Encoded Bracket URLs Separately appeared first on Search Engine Journal .

## 原文正文

Google Crawls Raw And Encoded Bracket URLs Separately Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- Technical SEO

## Google Crawls Raw And Encoded Bracket URLs Separately

- Raw and percent-encoded brackets in a URL count as different URLs.

- Mueller cites the URL standard's reserved characters and says he probably answered this wrong before.

- Linking both forms can leave Google choosing which version it keeps.

Google's John Mueller says raw and percent-encoded brackets are different URLs and recommends using one form across links, canonical tags, and sitemaps.

Raw square brackets in a URL and their percent-encoded version, %5B and %5D, are different URLs, Google Search Advocate John Mueller said on Bluesky Monday. He wrote that he would have assumed they were equivalent and that he “probably gave people the wrong answer on this in the past.”

Google will crawl both versions, he said; if it finds they contain identical information it will eliminate duplication and pick one version; he recommends you choose one format to utilize across all links, canonical tags, sitemaps, and your structured data. The rules for duplicate formats apply equally to spaces, plus signs, and “%20,” he said.

### Why Encoded Brackets Are A Different URL

Mueller traced the difference to RFC 3986 , the internet standard for URI syntax, which puts brackets and plus signs in its reserved set of characters. Under Section 2.2, URIs that swap a reserved character for its percent-encoded version “are not equivalent.”

He was responding to Vanessa Fox, an ex-Google employee who developed Google’s Webmaster Central; she had asked in a Bluesky reply (after asking the question in the comments of the first Non-Canonical Cabinet episode) if Google treated the encoded form of a URL as a different URL. She provided examples by using both ?filter[]=123 and ?filter%5B%5D=123 (one in links; the other when identifying canonical versions). The JavaScript check he made then compared these two URLs and returned false .

He pointed out that the use of raw brackets in a query string is also technically invalid according to RFC 3986; this is because RFC 3986 restricts the use of brackets to the hostname, for wrapping raw IPv6 addresses.

He stated that letter cases within encoding do not make a difference, therefore “%5B” and “%5b” are equivalent; they adhere to the rules set forth by RFC 3986 regarding hex characters.

### What Google Does With Both Versions

Mueller described what Google does when a server returns the same page for the raw and encoded forms:

That said, *maybe* your server makes them “soft-equivalent” by serving the same content. We’d crawl both versions, if we see the same content (maybe even checksum level), we’d de-dupe them and pick one.

He also stated that a browser may encode brackets prior to sending an encoded version of what is typed by the user into the URL bar. However, if a bracketed URL is requested from JavaScript (or other code) then the brackets might be sent as is. He recommended encoding brackets when they need to be used within a URL: “always encode it, never show [].”

### What Google’s Documentation Already Says

Google’s URL structure documentation already calls for encoding characters like brackets. It says Google Search supports URLs as defined by IETF STD 66, the standard that contains RFC 3986, and that “Characters defined by the standard as reserved must be percent encoded.”

I covered the first Non-Canonical Cabinet episode last week. That episode dealt with emoji and non-English characters in URLs, which browsers percent-encode in a URL path. Brackets are a different case, because the standard reserves them as delimiters.

### Sites Already Using Raw Brackets

Vanessa Fox responded that she was thinking about a website which uses an invalid bracket notation throughout, does seem to be indexing just fine and has decided to leave it alone because it would be too much trouble to convert it into valid brackets.

Mueller stated he wouldn’t anticipate problems from using this structure but “wouldn’t set up a new site like this.” Mueller also indicated that he would pay extra attention to all internal links (including metadata related to rel=canonical and structured data) so they are uniform.

Additionally Mueller stated that based on problems they have encountered at Google with regards to how these characters functioned over 10+ years ago, other crawl / indexer / fetch programs may not be “as exact in this logic” when processing them.

### Why This Matters

Google will choose one version of the URL, Mueller said, if there are multiple versions available with the same content. If all your URLs use the same format (i.e. either raw or encoded) then this choice is more likely to go your way. The best solution is to encode the brackets in the URL as requested by Google’s own documentation. Mueller expects an existing site using raw brackets to still continue to work. Your task would therefore appear to be to make sure that your internal links and metadata point to the same version of the URL.

### Looking Ahead

Mueller suggested checking the crawlers and fetchers that matter to you for how they deal with bracketed URLs. Mueller didn’t name specifically what crawlers or fetchers could have a problem but he said that some crawlers/fetchers might not follow Google’s exactness when dealing with bracketed URLs.

Google had not yet posted their second installment of the Google Video Series titled “Non-Canonical Cabinet” regarding robots.txt as of October 20th.

Featured Image: Popartic/Shutterstock

Category News Technical SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-crawls-raw-and-encoded-bracket-urls-separately/593765/)
