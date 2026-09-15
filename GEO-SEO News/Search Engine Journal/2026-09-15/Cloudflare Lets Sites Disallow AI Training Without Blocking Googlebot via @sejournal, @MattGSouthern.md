---
title: "Cloudflare Lets Sites Disallow AI Training Without Blocking Googlebot via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-15T21:29:41+00:00
fetched_at: 2026-09-15T23:33:47.182666+00:00
url: "https://www.searchenginejournal.com/cloudflare-lets-sites-disallow-ai-training-without-blocking-googlebot/589559/"
guid: "https://www.searchenginejournal.com/cloudflare-lets-sites-disallow-ai-training-without-blocking-googlebot/589559/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Cloudflare Lets Sites Disallow AI Training Without Blocking Googlebot via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-15
- URL: https://www.searchenginejournal.com/cloudflare-lets-sites-disallow-ai-training-without-blocking-googlebot/589559/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Cloudflare's Disallow AI Training keeps mixed-use crawlers available for search. Google and Apple honor training opt-outs; Bing robots.txt support is pending. The post Cloudflare Lets Sites Disallow AI Training Without Blocking Googlebot appeared first on Search Engine Journal .

## 原文正文

Cloudflare Lets Sites Disallow AI Training Without Blocking Googlebot Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- AI Search

## Cloudflare Lets Sites Disallow AI Training Without Blocking Googlebot

- Cloudflare announced a Disallow AI Training setting that publishes applicable no-training preferences in robots.txt.

- Googlebot, Applebot, and Bingbot stay allowed to crawl for search under that setting.

- The Block setting now stops those crawlers entirely, including for search.

Cloudflare's Disallow AI Training keeps mixed-use crawlers available for search. Google and Apple honor training opt-outs; Bing robots.txt support is pending.

Cloudflare has announced a new Disallow AI Training setting, and it says it will move sites that already block AI training onto it. This setting adds a no-training preference in robots.txt, while still allowing Googlebot, Applebot, and Bingbot to crawl for search purposes.

This differs from the plan I mentioned back in July . At that time, Cloudflare explained that from September 15, sites that block AI training would also block those three crawlers, since they are used for both search and training. Now, choosing Block will completely stop Googlebot, Applebot, and Bingbot, including for search.

### What Changed On September 15

Disallow AI Training is a new feature on Cloudflare’s Training control, which is part of a trio of controls including Search and Agent. The company first described it in August . When enabled, mixed-use crawlers that crawl for search and training stay allowed for search if the company labels them as “Accountable.” Other training crawlers, however, will be blocked.

Block and Block on pages with ads now apply to mixed-use crawlers too. The company says it previously left them out of both settings because blocking them could affect search visibility.

The company says most customers don’t need to change anything. Existing Training selections of Block or Block on pages with ads will migrate to Disallow AI Training. Sites that used either blocking option under the older Block AI Bots toggle will get Allow for Search, Disallow AI Training for Training, and Block on pages with ads for Agent.

Block AI Bots and Cloudflare’s Managed Robots.txt feature are set to be deprecated. To keep mixed-use crawlers off a site entirely, the company says you now have to select Block.

New domains that monetize with ads are offered Disallow AI Training as their Training preset.

### Which Crawlers Keep Search Access

Mixed-use crawlers keep search access under Disallow AI Training only if Cloudflare labels them Accountable, a designation it created after talks with crawler operators that began in July. To qualify, an operator has to meet or commit to meeting four requirements.

A way to opt out of AI training through robots.txt or a similar standard.

A way to opt out of AI summaries, set with the operator now and through Cloudflare next year.

URL-level visibility into which pages were made available for training, plus metrics on how content appeared in search.

An assurance that opting out of training won’t affect traditional search results.

The company says Apple, Google, and Microsoft meet those requirements, each with features available now plus commitments with deadlines for the rest.

It also lists the relevant crawlers from Amazon, Anthropic, Meta, and OpenAI as Accountable because those companies run separate search and training crawlers. Their training crawlers are still blocked under Disallow AI Training.

### What The Setting Covers At Google, Apple, And Bing

At Google, Disallow AI Training works through a Disallow rule for Google-Extended, the robots.txt token Google provides for opting content out of Gemini model training. Google’s crawler documentation says Google-Extended doesn’t affect a site’s inclusion in Google Search or its ranking.

A separate Search Console setting controls whether a site appears in AI Overviews, AI Mode, and Discover’s generative AI features. Google’s help page says that setting doesn’t affect AI training.

At Apple, the setting works through a Disallow rule for Applebot-Extended. Apple’s documentation says Applebot-Extended doesn’t crawl pages and isn’t considered in search ranking. Keeping content out of AI-generated answers to broad knowledge questions in Siri and Search takes the nosnippet meta tag.

Choosing Disallow AI Training won’t send Bing a no-training preference through robots.txt just yet, as Microsoft still needs to add support for it. Cloudflare mentioned that this feature is still in the works. Also, the earlier Training block on Cloudflare didn’t affect Bingbot either.

Bing’s current training opt-out is the NOARCHIVE meta tag. According to Bing’s documentation , content marked with NOARCHIVE isn’t used to train Microsoft’s generative AI models, and it’s not linked in Chat and Copilot.

### Why This Matters

Selecting Block instead of Disallow AI Training on Cloudflare not only blocks AI training crawlers but also stops Google, Apple, and Bing from crawling your site.

Disallow AI Training maps to the training opt-outs provided by Google and Apple. It doesn’t determine whether your pages will appear in AI Overviews and AI Mode, as Google manages this through Search Console. On Bing, the training opt-out is still indicated by the NOARCHIVE tag, which also means that links from Copilot won’t be included.

### Looking Ahead

Cloudflare shares that Google is planning to roll out URL-level transparency tools for Google-Extended in the coming weeks. Meanwhile, it says Apple is working on its own URL-level tool for next year. Additionally, Cloudflare says Microsoft’s support for a robots.txt no-training preference is targeted for early 2027.

Cloudflare’s upcoming focus is on AI summaries. The company says its goal is a way to control the amount of content included in summaries through a single setting on Cloudflare, rather than adjusting settings individually for each operator, by early next year.

Featured Image: Remo_Designer/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/cloudflare-lets-sites-disallow-ai-training-without-blocking-googlebot/589559/)
