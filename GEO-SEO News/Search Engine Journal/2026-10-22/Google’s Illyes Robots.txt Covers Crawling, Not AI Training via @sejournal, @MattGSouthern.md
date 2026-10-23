---
title: "Google’s Illyes: Robots.txt Covers Crawling, Not AI Training via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-22T10:58:04+00:00
fetched_at: 2026-10-23T00:02:35.809394+00:00
url: "https://www.searchenginejournal.com/google-illyes-robots-txt-crawling-ai-training/593957/"
guid: "https://www.searchenginejournal.com/google-illyes-robots-txt-crawling-ai-training/593957/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Google’s Illyes: Robots.txt Covers Crawling, Not AI Training via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-22
- URL: https://www.searchenginejournal.com/google-illyes-robots-txt-crawling-ai-training/593957/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Google's new robots.txt video says the standard covers crawling, not how content gets used, and recommends percent-encoding non-English robots.txt paths. The post Google’s Illyes: Robots.txt Covers Crawling, Not AI Training appeared first on Search Engine Journal .

## 原文正文

Google's Illyes: Robots.txt Covers Crawling, Not AI Training Skip to content

SEJ Pro Sign In

Webinar: AI Shopping: Get Your Products Found in Google & ChatGPT

Save Your Spot

- SEJ

- ⋅

- AI Search

## Google’s Illyes: Robots.txt Covers Crawling, Not AI Training

- Google says robots.txt, as the standard defines it, governs crawling, not later use.

- Keeping out one AI crawler while allowing others means targeting its user-agent token.

- An IETF draft would add a robots.txt rule for stating AI usage preferences.

Google's new robots.txt video says the standard covers crawling, not how content gets used, and recommends percent-encoding non-English robots.txt paths.

Robots.txt, as the internet standard RFC 9309 defines it, governs which URLs a crawler may request, not what happens to the content afterward, Google’s Gary Illyes said in a Search Central video published Wednesday. To keep one AI crawler out while allowing others, he said, you have to target that crawler’s user-agent token in the file.

The video is the second episode of The Non-Canonical Cabinet , where Illyes and Cherry Prommawin of Google Search Relations take edge-case questions from the community. Illyes is also co-author, with Mozilla’s Martin Thomson, of an IETF Internet-Draft that would give robots.txt a standard way to state usage preferences. Prommawin recommended writing non-English rule paths in percent-encoded form for crawlers other than Google’s.

### What Illyes Said About AI Training

The episode’s question was whether robots.txt can allow AI crawling of a website and keep that same information out of generative model training. According to Illyes, “So as defined by RFC 9309, robots.txt is an access preference protocol.” He went on to say robots.txt “doesn’t dictate what a system does with the data after it has already crawled it.” If you want to completely block a specific AI crawler from accessing your entire website, Illyes stated, you need to “target their specific user agent tokens explicitly in the file.”

The episode illustrated a fictional directive (e.g., No-AI-Chicken-Training) which was shown on-screen and would be ignored by a parser. Google’s robots.txt specification page states that the four elements supported are User-Agent, Allow, Disallow, and Sitemap; invalid lines will be ignored by Google.

As for RFC 9309 specifically (Section 2.2.4), it allows crawlers to decide how they’ll process a record outside the scope of this protocol. Therefore, whether or not an additional line accomplishes something depends on the crawler interpreting it.

### What Google-Extended Controls

Google-Extended is a robots.txt token with no user agent of its own. Google crawls under its existing user agents, and Google’s list of common crawlers says the token is “used in a control capacity.” It manages whether content Google crawls can be used to train future Gemini models and for grounding in Gemini Apps and Grounding with Google Search on Vertex AI. The page says it doesn’t affect a site’s inclusion in Google Search and isn’t a ranking signal.

Google-Extended’s meaning as a usage control comes from Google’s documentation for its own products, rather than RFC 9309. The hosts didn’t discuss it on air, but the video’s description links to the same list.

### The Draft That Would Add A Usage Rule

The current version of the IETF draft Illyes co-wrote, dated Aug. 19, would update RFC 9309, if approved, with a Content-Usage rule for robots.txt and a matching HTTP header. Neither the episode nor its description mentions the draft.

Under the draft, Allow and Disallow would continue to govern which URLs can be crawled. Content-Usage would then define preferences as to how crawled content should be used. Those preferences would only relate to paths where a crawler has permission to fetch content. A Content-Usage field of “train-ai=n” is added to the draft’s example robots.txt file, which allows crawling.

The draft is still a Working Group Document. At present, its IETF Datatracker entry shows that the Working Group has not yet submitted the document for review by the IETF’s Steering Group (IESG). The Working Group’s planned date for sending it to the IESG was Aug. 2026. The ‘train-ai’ Label referenced above appears in a separate Vocabulary Draft , dated Sept. 14. That document states that it reflects no consensus within the Working Group.

### Percent-Encode Non-English Paths

Cherry Prommawin’s advice for paths with non-English characters or emoji was that “you should use the encoded version in your robots.txt rules.” Google’s parser handles raw characters by encoding them, she said, but “other or older crawlers on the web might get confused.”

The on-screen example labeled a raw emoji path “Works for Google, might break others” and its percent-encoded form “The Safe, Standard Way.” Google’s spec page says its parser treats raw UTF-8 and percent-encoded paths the same way, and RFC 9309’s grammar allows UTF-8 characters in paths.

### Why This Matters

The method you would need in robots.txt to limit AI use of your content while keeping your site visible in Google Search depends on what bot or product you are working with. Disallow statements may prevent specific AI crawlers from accessing particular webpages. For Gemini, the documented control of Google is Google-Extended and includes both training and grounding. There currently is no standard way of expressing a training preference independent of the bots allowed to crawl the webpage; one exists only as a draft.

Websites that use URLs with languages other than English will want to encode their robots.txt paths using percent encoding. Percent encoding is safer because, although Google treats both raw and encoded versions of the same robots.txt rule path equally, other crawlers could potentially interpret raw characters differently.

### Looking Ahead

According to the video description, the next Non-Canonical Cabinet episode will cover the 404 status code. The current Content-Usage draft is set to expire on Feb. 20, 2027, unless a new revision replaces it sooner.

Featured Image: Alicia97/Shutterstock

Google wordmark: Source: Google.

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-illyes-robots-txt-crawling-ai-training/593957/)
