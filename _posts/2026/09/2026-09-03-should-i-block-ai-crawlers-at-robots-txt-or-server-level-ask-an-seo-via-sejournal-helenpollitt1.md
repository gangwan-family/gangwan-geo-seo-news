---
layout: post
title: "Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO via @sejournal, @HelenPollitt1"
date: 2026-09-03T12:00:18+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-03/Should I Block AI Crawlers At Robots.txt Or Server Level – Ask An SEO via @sejournal, @HelenPollitt1.md"
original_url: "https://www.searchenginejournal.com/ask-an-seo-should-i-block-ai-crawlers-at-robots-txt-or-server-level/586390/"
author: "Helen Pollitt"
categories:
  - "AI Search"
  - "Ask an SEO"
  - "Technical SEO"
  - "Web Dev SEO"
  - "_src_search-engine-journal"
---

# Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO via @sejournal, @HelenPollitt1

- Source: Search Engine Journal
- Published: 2026-09-03
- URL: https://www.searchenginejournal.com/ask-an-seo-should-i-block-ai-crawlers-at-robots-txt-or-server-level/586390/
- Author: Helen Pollitt
- Categories: AI Search, Ask an SEO, Technical SEO, Web Dev SEO

## RSS 摘要

Robots.txt relies on bot compliance, while WAF, CDN, and server-level blocks enforce it. A breakdown of which layer stops AI crawlers for good. The post Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO appeared first on Search Engine Journal .

## 原文正文

Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO Skip to content

AMA with Reddit Experts: what's working, and how to get into AI-cited threads. Exclusive for SEJ Pro members.

Save 20% with OGS20

- SEJ

- ⋅

- Technical SEO

## Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO

Robots.txt relies on bot compliance, while WAF, CDN, and server-level blocks enforce it. A breakdown of which layer stops AI crawlers for good.

Deciding to block AI crawlers is a business decision that many search professionals are currently discussing. But once you’ve made the decision, what’s the best way to go about blocking those bots?

There are two main approaches to blocking crawlers to consider: through robots.txt and at the server stack.

### The Two Approaches

Both of these approaches have their pros and cons. Let’s start by examining how they work and the differences between the two.

#### Blocking Through The Robots.txt

Blocking AI crawlers using robots.txt is exactly the same process as you would use for blocking any type of bot.

Each AI bot has its own identifying name, for example, OpenAI’s GPTBot and OAI-SearchBot. To block them, you simply need to add a disallow rule specifying the crawler’s name. For example, to prevent GPTBot from crawling any part of your website, you would add:

User-agent: GPTBot

Disallow: /

If there are only certain parts of your website you want to prevent the AI bots from crawling, you can call those out in the same way. For example, to prevent GPTBot from crawling your product pages you would include the folder those pages sit in, e.g.:

User-agent: GPTBot

Disallow: /products/

#### Blocking At The Server Level

There are a few ways you can block bots at a server level: through the server itself, the CDN or the WAF.

In this instance, the server will read the incoming request, like the bot’s IP, header, etc., and apply the specific rules you have configured for that agent (deny, allow, redirect). For example, you can specify that GPTBot receives a “deny” command. This would prevent the bot from accessing the content on your site.

For Content Delivery Network (CDN), the concept is the same but it happens at an earlier stage of a bot’s visit. The CDN intercepts a request for content from a bot before it hits the server. This essentially saves server bandwidth as the bot never actually interacts with it. Some CDNs offer this technology natively without you having to do much to configure it. For example, Cloudflare offers preset blocking based on whether a bot is a search crawler, an agent or used for training, as well as allowing finer-tuning on a bot by bot basis.

At the Web Application Firewall (WAF), bots are scrutinized more than the CDN does. The WAF acts as a security layer that can analyze request behavior, not just the headers used by the bots. This means it is capable of detecting bots that are spoofing other user-agents. It is the most competent way in most tech stacks of identifying more sophisticated AI crawlers that are looking to slip under the radar of blocking attempts. The WAF your company is using may be part of your CDN, for example, Cloudflare WAF, or a standalone application like AWS WAF.

### Robots.txt: Pros And Cons

The robots.txt is possibly the most accessible way for search professionals to control bots. Typically, SEOs have access to alter the robots.txt for their domains, or can easily request a quick update by the development team.

However, there are some other benefits to using this method.

#### Pros

The robots.txt disallow mechanism is officially supported by the largest, reputable AI companies. For example, OpenAI’s GPTBot and OAI-SearchBot, Anthropic’s ClaudeBot, Claude-User and Claude-SearchBot, Google’s Google-Extended, and Perplexity’s PerplexityBot.

This method allows you to selectively choose which pages to prevent the bots from visiting, and also to fine-tune the blocking based on each crawler.

#### Cons

There are some cons to this method, however. The greatest risk is that compliance with the robots.txt is completely voluntary and not centrally monitored. That is, although AI bot creators may claim their bots respect the robots.txt, it is just a set of requests, not an actual block. Think of it as a no-trespassing sign in front of an open gate. There is nothing actually stopping the bots, only their being coded to respect the rules of the robots.txt.

The robots.txt can be configured to disallow bots from certain pages very easily if there are robots.txt controls in the website’s CMS. This means that non-technical stakeholders can accidentally block more bots than anticipated with a mistaken disallow rule. This can be catastrophic if the robots.txt is updated to disallow all bots, for example, by implementing:

User-agent: *

Disallow: /

The robots.txt isn’t automatically updated when new user agents are released. This means that someone will need to manually add new disallows whenever you want to prevent a new AI bot from accessing your site.

### Server Stack: Pros And Cons

Blocking bots at a server, CDN, or WAF level has different pros depending on the implementation.

#### Pros

The CDN and WAF implementations will stop bot requests before they hit the server. This will save server bandwidth, reducing the strain on the server and saving associated costs.

The biggest pro for the server stack implementations, no matter which you choose, is that they are a definite block. If the robots.txt is a polite “no trespassing” sign, the server, CDN, and WAF blocks are a padlock on the gate. These implementation methods do not require a crawler’s compliance; they detect the bots and stop them from accessing content, whether the bot is compliant or not.

Another benefit of this method is that the software that sits at these levels will often give reports on the bots that have been blocked. The “padlock” records the attempts to unlock it. This can be helpful in analyzing which bots are trying to access your website. For sites that are receiving a lot of unwanted AI bot attention, this can be used in discussions, sometimes legal, with the owners of those bots.

#### Cons

The cons of the server stack implementation methods are primarily the maintenance overhead. Most website servers are fairly locked down, so only those who really know what they are doing with them will be allowed to access the server files, WAF or CDN. This means changes to the blocks will likely need to go through a developer, rather than be implemented directly by an SEO. This need for an intermediary comes with time, resource, and cost implications, especially if the server is managed by a third party like a development agency.

For each layer of security, bot spoofing is possible. Although the WAF is the strongest line of defense, it is still possible that highly advanced bots can bypass its validation checks. This means that there is no completely foolproof method of blocking rogue AI bots via the server stack. However, they are still highly effective for most.

### So Which Should We Use?

There is no one answer to this. It is dependent on your website’s set-up, costs, and management structure.

In an ideal world, you would block the bots at each level of the server stack. The server is a good way to block known user-agents and can detect simple patterns in bot behavior. The CDN blocks are largely effective and will prevent the bots from consuming server bandwidth. WAF is the most effective at spotting spoofed bots and preventing advanced AI scrapers from accessing the site. However, you may not have easy access to configure your WAF, if your site has one at all.

The robots.txt is the simplest method of declaring a desire for certain bots to not access your website, and it is effective for responsible bots. However, it can simply be ignored, and therefore is a deterrent, not a prevention method.

In summary, if you have a strong need to block certain AI crawlers, I would recommend going as high up the server stack as possible; blocking via the WAF if you can, the CDN if you can’t, and via the server as a last resort.

If you only need to block one or two of the most reputable AI crawlers, you are likely able to just rely on the robots.txt as a deterrent. However, I would also suggest monitoring your server logs to see if any of those bots are slipping past your robots.txt disallow.

More Resources:

- OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot

- Google Says Why It May Ignore Robots.txt And Negatively Impact SEO

- Google Explains Why URLs Blocked By Robots.txt Can Still Be Indexed

Featured Image: Paulo Bobita/Search Engine Journal

Category AI Search Ask an SEO Technical SEO Web Dev SEO

Read Full Bio

VIP CONTRIBUTOR Helen Pollitt Head of SEO at Getty Images

Helen manages the SEO team at Getty Images. She has a passion for equipping teams and training individuals in SEO ...

## 原文链接

[Read original](https://www.searchenginejournal.com/ask-an-seo-should-i-block-ai-crawlers-at-robots-txt-or-server-level/586390/)
