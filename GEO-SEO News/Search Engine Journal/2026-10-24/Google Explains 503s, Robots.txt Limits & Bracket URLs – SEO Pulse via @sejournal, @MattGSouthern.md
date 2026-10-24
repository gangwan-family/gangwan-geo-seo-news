---
title: "Google Explains 503s, Robots.txt Limits & Bracket URLs – SEO Pulse via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-24T12:00:00+00:00
fetched_at: 2026-10-24T23:28:42.720709+00:00
url: "https://www.searchenginejournal.com/seo-pulse-google-explains-503s-robots-txt-limits-bracket-urls/594085/"
guid: "https://www.searchenginejournal.com/seo-pulse-google-explains-503s-robots-txt-limits-bracket-urls/594085/"
author: "Matt G. Southern"
categories:
  - "SEO"
  - "SEO Pulse"
---

# Google Explains 503s, Robots.txt Limits & Bracket URLs – SEO Pulse via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-24
- URL: https://www.searchenginejournal.com/seo-pulse-google-explains-503s-robots-txt-limits-bracket-urls/594085/
- Author: Matt G. Southern
- Categories: SEO, SEO Pulse

## RSS 摘要

Google reminds sites to use 503s during PHP patch downtime. Other updates cover robots.txt controls, bracket URLs, and JPEG XL in Google Images and Discover. The post Google Explains 503s, Robots.txt Limits & Bracket URLs – SEO Pulse appeared first on Search Engine Journal .

## 原文正文

Google Explains 503s, Robots.txt Limits & Bracket URLs – SEO Pulse Skip to content

SEJ Pro Sign In

Webinar: AI Shopping: Get Your Products Found in Google & ChatGPT

Save Your Spot

- SEJ

- ⋅

- SEO

## Google Explains 503s, Robots.txt Limits & Bracket URLs – SEO Pulse

Google reminds sites to use 503s during PHP patch downtime. Other updates cover robots.txt controls, bracket URLs, and JPEG XL in Google Images and Discover.

Welcome to the Pulse: This week, we’re looking at how to use a 503 during brief PHP patch downtime, what robots.txt controls for AI crawlers and agents, and how Google handles bracket URLs and JPEG XL images.

Here’s what matters for you and your work.

### Google Says Serve A 503 When Taking Sites Down For PHP Patches

In a LinkedIn post on Oct. 21, Google Search Central reminded anyone taking servers offline for PHP patches to return a 503 status code. The post went up the day PHP released emergency fixes for two critical flaws .

Key facts:

The post stated the 503 “ensures already indexed URLs are preserved in Search while you work” and noted to avoid general 404 or 200 error pages, and John Mueller of Google also shared a reminder on Bluesky saying that the 503 does not have to be served through PHP. In their crawl-rate documentation , Google advises users to limit serving 503 status codes to no longer than 1-2 days, as they may drop a URL from their index if it is returning a 503 for multiple days.

#### Why This Matters

If your site returns a 503 error due to downtime caused by a PHP patch, it will have to be triggered via an entity that remains available (i.e., during the time your PHP is unavailable), e.g., a CDN routing rule or a temporary server your DNS points to. According to Google’s guide to pausing a site , if you trigger a 503 in response to robots.txt requests, all crawling is blocked.

Read our full coverage: Google Reminds Sites To Serve A 503 During PHP Patch Downtime

### Illyes Says Standard Robots.txt Rules Cover Crawling, Not Later Use

Gary Illyes of Google stated in an Oct. 21 Search Central video that according to RFC 9309 , the standard robots.txt directives (robots.txt rules) only dictate what compliant crawlers are allowed to crawl. These directives do not control how systems use content after it’s crawled.

Key facts:

Illyes called robots.txt “an access preference protocol” and said that keeping one AI crawler out while allowing others means targeting that crawler’s user-agent token. Google’s list of common crawlers documents Google-Extended as the token for managing whether content Google crawls may be used for training future Gemini models and for grounding in Gemini Apps and on Vertex AI, and says the token doesn’t affect inclusion in Google Search. Google-Extended isn’t a separate crawler and doesn’t have its own HTTP user-agent string. A draft that Illyes co-wrote for the Internet Engineering Task Force would add a Content-Usage rule to robots.txt for stating usage preferences, but it’s still a working group document and hasn’t been approved.

#### Why This Matters

A Disallow rule under a crawler’s token can help keep that crawler away from the listed paths. To limit how Google uses crawled content for Gemini, you can use Google-Extended. A standard way to express a training preference separately from crawl access is available only as a draft.

Read our full coverage: Google’s Illyes: Robots.txt Covers Crawling, Not AI Training

### Cloudflare And OpenAI Say A Pilot Found New Pages For ChatGPT Search

Cloudflare and OpenAI say a research pilot helped OpenAI discover and index hundreds of millions of new web pages, giving ChatGPT even more information to draw on.

Key facts:

The pilot drew on a participating group of approximately 1% of Cloudflare’s network through signals which assist the OpenAI crawler in identifying pages; bypassing non-existent pages and indicating if a page is updated. The Oct. 15 blog post (co-authored by two OpenAI employees) states that finding new pages “can initially increase crawling,” and does not report how frequently those newly identified pages are being cited, nor does it provide data regarding the number of visits generated from the pages. Additionally, the post stated, “A signal about a page doesn’t grant permission to access it.”

#### Why This Matters

OpenAI’s crawler documentation is split by search vs. training. A website may use robots.txt entries like Allow for OAI-SearchBot and Disallow for GPTBot to tell the crawler that its content shouldn’t be used for training purposes. Because OpenAI ranks pages on its own, the post says, just because your website was found through the pilot does not mean you will get a citation.

Read our full coverage: ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot

### Raw And Encoded Brackets Are Different URLs, Mueller Says

Square brackets in a URL and their percent-encoded forms, %5B and %5D, create different URLs, Google’s John Mueller said on Bluesky on Oct. 19. He added that he would have assumed they were equivalent and “probably gave people the wrong answer on this in the past.”

Key facts:

Mueller referenced RFC 3986 (the URI syntax standard, which reserves brackets and plus signs) as well as noting that if a site returned the same content in response to either version of the URL format Mueller stated that Google would crawl each and eliminate duplicates then select one. Mueller offered a solution, stating “pick one,” and recommended using it consistently across all pages, including links, canonical tags, sitemap entries, and structured data. This is consistent with the existing Google documentation on URL structure which states that reserved characters must be percent encoded.

#### Why This Matters

When links and canonical tags mix raw and encoded forms, Google may have to decide which version to keep. If your existing site uses raw brackets throughout, Mueller said he’d expect it to keep working, though he “wouldn’t set up a new site like this.”

Read our full coverage: Google Crawls Raw And Encoded Bracket URLs Separately

### JPEG XL Isn’t Supported In Google Images Or Discover Previews

JPEG XL images aren’t currently supported in Google Images or as previews in Discover, as Google’s John Mueller shared on Bluesky on Oct. 15.

Key facts:

His post followed JPEG XL support in Chrome 155, which Google began rolling out widely on Oct. 6 , and in Firefox 158 on Oct. 13. Google’s image SEO documentation lists BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF as supported formats for images in an img element’s src attribute, and didn’t include JPEG XL as of Oct. 22. Asked about fallbacks in a picture element, Mueller said the element includes an img element, “so that would work for any search engine.”

#### Why This Matters

Serving JPEG XL as a picture source, with a JPEG, WebP, or AVIF file in the img element, keeps a supported format in the src attribute, where Google’s documentation says Search reads images. Google’s Discover guide points to og:image and schema.org markup for preview images, so those should point to one of the listed formats too.

Read our full coverage: Google Images & Discover Previews Don’t Support JPEG XL

### Pichai Expects AI Agents To Reach Sites By Browsing And Through Protocols

In an interview with Alex Heath on the Sources podcast, Google CEO Sundar Pichai shared that he expects AI agents to access websites both by browsing pages like people do and through protocols designed specifically for agents.

Key facts:

“I think you have both ways and they’re going to develop,” Pichai said. He pointed to momentum behind agent and payment protocols, including the Universal Commerce Protocol that Google backs. He called protocols “a far more scalable approach” but said he expects them to take longer to develop. Later in the interview, he said he expects agents to provide a unifying experience across Search and Gemini.

#### Why This Matters

By Pichai’s account, agents that browse pages the way people do stay in the picture while protocols develop. Google’s own hosted agents browse as Google-Agent, one of the user-triggered fetchers that Google says generally ignore robots.txt rules.

Read our full coverage: Pichai Says AI Agents Will Click Through Pages And Use Protocols and Google CEO Sundar Pichai Views Search Absorbed Into Agentic Layer

### Theme Of The Week: What Each Signal Reaches

Each of the stories this week concerns a signal that crawlers and agents receive about a website and where they are allowed to reach. A 503 signals to Google that the outage is only temporary (within the recommended time frame for outages from Google’s documentation). A disallowed crawl directive keeps compliant crawlers from crawling through the content of your pages, but how it’s used later depends on controls like Google-Extended and GPTBot. However, a Cloudflare discovery signal does not provide OpenAI permission to access your web page. Whether Google views your page at one URL or two depends upon whether you mix raw and encoded brackets. Currently, a JPEG XL image file contained in the img element cannot be viewed by Google Images. Agents that fetch based on user input fall into an area partially outside of robots.txt as defined by Google regarding its user-triggered fetchers. Server logs track what crawler has been making requests to your server; however, the specific crawlers and which controls govern crawling and later use are explained in each respective company’s documentation.

Top Stories Of The Week:

- Google Reminds Sites To Serve A 503 During PHP Patch Downtime

- Google’s Illyes: Robots.txt Covers Crawling, Not AI Training

- ChatGPT Search Can Draw On More Pages After A Cloudflare Pilot

- Google Crawls Raw And Encoded Bracket URLs Separately

- Google Images & Discover Previews Don’t Support JPEG XL

- Pichai Says AI Agents Will Click Through Pages And Use Protocols

- Google CEO Sundar Pichai Views Search Absorbed Into Agentic Layer

More Resources:

- Google Launches A Video Series For Odd Technical SEO Questions

- Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO

- The Expert SEO Guide To URL Parameter Handling

Featured Image: Cast Of Thousands/Shutterstock

Category SEO SEO Pulse

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/seo-pulse-google-explains-503s-robots-txt-limits-bracket-urls/594085/)
