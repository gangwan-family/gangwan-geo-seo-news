---
layout: post
title: "Cloudflare: Machine Traffic Could Hit 1,000x Human Traffic In 5 Years via @sejournal, @slobodanmanic"
date: 2026-08-14T14:30:22+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-14/Cloudflare Machine Traffic Could Hit 1,000x Human Traffic In 5 Years via @sejournal, @slobodanmanic.md"
original_url: "https://www.searchenginejournal.com/the-biggest-ai-crawler-on-my-website-was-hunting-for-credentials/585159/"
author: "Slobodan Manic"
categories:
  - "SEO"
  - "_src_search-engine-journal"
---

# Cloudflare: Machine Traffic Could Hit 1,000x Human Traffic In 5 Years via @sejournal, @slobodanmanic

- Source: Search Engine Journal
- Published: 2026-08-14
- URL: https://www.searchenginejournal.com/the-biggest-ai-crawler-on-my-website-was-hunting-for-credentials/585159/
- Author: Slobodan Manic
- Categories: SEO

## RSS 摘要

One company measures the bot problem, frames it, and sells the fix. Cloudflare now owns both the meter and the valve. Check your own logs. The post Cloudflare: Machine Traffic Could Hit 1,000x Human Traffic In 5 Years appeared first on Search Engine Journal .

## 原文正文

Cloudflare: Machine Traffic Could Hit 1,000x Human Traffic In 5 Years Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- SEO

## Cloudflare: Machine Traffic Could Hit 1,000x Human Traffic In 5 Years

Cloudflare's CFO says machines will outnumber humans 1,000 to 1. My largest AI crawler was a credential scanner wearing a nonprofit's name.

The single largest AI crawler on my website over the past day was not an AI crawler. It arrived roughly 1,500 times under Common Crawl’s name ; it sent back nothing, and what it wanted was my SSH keys.

I went looking because of a number.

### Cloudflare’s CFO Told Analysts Machine Traffic Could Reach 1,000 Times Human Traffic

Cloudflare’s Chief Financial Officer, Thomas Seifert, told analysts on the company’s second-quarter earnings call that “if the current trends continue, we think in five years, non-human traffic will be as much as 1,000 times as much as human traffic.” Then the line that will capture the headlines: “humans will be a rounding error on the internet, not because human traffic goes down, but that’s just how fast we’re seeing non-human traffic grow.”

Two things worth saying before anyone reaches for the pitchforks. First, Seifert added his own caveat, unprompted: “with the big caveat that I have called it wrong at every point along the way.” Cloudflare previously expected machine traffic to pass human traffic in 2027, and it happened in May 2026. His errors have run toward under estimating, which is the strongest argument for taking the projection seriously.

Second, the underlying measurement is real. Cloudflare’s own post published the same week says fewer than half of all HTML page requests now come from a human. I have no argument with that. The machine visitors are real and they are the whole subject of this website.

The argument is about what the number counts.

### What One Day of Crawler Traffic on My Own Website Looks Like

I pulled Cloudflare’s AI crawler view for nohacks.co for the 24 hours ending the evening of August 7. About 3,000 requests, of which roughly a third were unsuccessful, a figure up more than 1,000% on the previous period.

By crawler: CCBot 1,510. ChatGPT-User 375. ClaudeBot 296. Googlebot 245. PetalBot 107. Thirteen others sharing 353 between them.

Image Credit: Slobodan Manic

CCBot is Common Crawl’s crawler, the long-running non-profit web archive whose corpus trained a good share of the models everyone now argues about. On paper, it being my largest visitor is unremarkable.

Then I exported the paths.

### It Asked for My SSH Keys, Not My Articles

Here are the most-requested paths in that AI crawler traffic, with request counts, exactly as they came out of the export:

- /.ssh/known_hosts (42 requests)

- /phpinfo.php (31 requests)

- /.boto (30 requests)

- /.env.production (29 requests)

- /.vscode/launch.json (28 requests)

- /.env.test (27 requests)

- /firebase-service-account.json (26 requests)

- /.gitconfig (24 requests)

- /server/.env (24 requests)

It continues like that for a hundred paths: /id_rsa , /id_ecdsa , /private-key , /ssl/localhost.key , /key.json , /serviceAccountKey.json , /.aws/config , /actuator/configprops , /api/v1/env , /Dockerfile , /values.yaml , and /@fs/proc/self/environ , which is an attempt at a known path-traversal bug in a development server.

Across those hundred paths: 1,028 requests, 6.7 MB transferred, and zero referrals. The number of requests to anything I have actually written rounds to nothing. The closest it came to my content was /blog/wp-login.php , a WordPress login probe aimed at a website that has never run WordPress, and two requests for /blog/null .

That last detail matters more than it looks. Whatever this is, it is not reading my pages before it asks for things. It is working through a list, the same list it works through everywhere, and my website is a row in a loop.

This is a credential scanner. Common Crawl follows links and fetches pages, and it has no reason to ask a podcast website for its Firebase service account key.

I could not verify the source addresses to prove impersonation, because per-request IP data is not something I can reach on my plan. Common Crawl publishes the test: genuine CCBot traffic comes from documented address blocks and reverse-resolves to hostnames ending in crawl.commoncrawl.org . Someone with those logs can settle it in a minute. What I can say is what arrived, what it asked for, and how it was labelled: Cloudflare’s AI dashboard attributes this to Common Crawl as the operator, and counts every request toward my AI crawler totals.

Which leads to the part that unsettles me most. I went looking for these requests in my security events and found nothing at all, because the security log only records requests that trip a rule. I am not blocking this traffic, so it passes through, gets served, and leaves no mark. It appears in exactly one place on my whole dashboard: the AI crawler view, sitting in the list beside ChatGPT-User and Googlebot, under the name of a nonprofit research archive. A credential scanner is fully legible to me as agent traffic and completely invisible as a security event.

### 2 of Those Paths Are New, and They Are the Ones I Keep Thinking About

Buried in that list are /.mcp.json , requested 30 times, and /.continue/config.json , requested 24.

Those two are agent tooling configuration: an MCP server definition and a coding assistant’s settings file. Both routinely hold API keys and access tokens, because that is what you put in them to let an agent reach your services.

Someone has added agent credentials to the standard secret-scanning wordlist. The same automated sweep that has been asking every website on the internet for /.env since roughly forever now also asks for the file that lists which tools your agents can call and what they authenticate with. Nobody announced that, and it happened fast. If you run anything agentic, the wordlist arrived before most people finished writing their first MCP server .

### Cloudflare Published the Correction Itself, the Same Week

The strongest counterweight to the earnings-call framing is in Cloudflare’s own engineering writing from the same week.

Their agentic-internet post says a lot of traffic from well-behaved bots is re-fetching pages that have not changed, and that this runs to billions of requests. In their words, “an enormous amount of machine effort, attached to no outcome at all.”

Machine effort and machine demand are different quantities. My own logs are a sharper version of the same point than I expected to find: the largest single contributor to my machine traffic was not merely useless, it was hostile, and it still counted.

Meta crawling your website and never sending anything back is the definition of useless traffic if you are the person who owns the website. I wrote about that split on August 1 . A scanner wearing a research crawler’s name while it hunts for your cloud credentials is a category below that, and both land in the same bar on the same chart.

So when the graph climbs, the question for a website owner is what the traffic actually is.

### Help Create the Problem, Market the Problem, Sell the Solution

It is clear what Cloudflare is positioning itself as here, and it should be called out. Help create the problem, market the problem, sell the solutions. In the first week of August alone: a bot-traffic projection on the earnings call, a blog post quantifying how much of the web is no longer human, an agent-readiness scanner to tell you that you are not ready, an AI-visibility product to score you, a bridge to expose your website’s tools to agents, and a default that starts blocking some of those agents in September unless you decide otherwise.

Every one of those products is a reasonable response to something real. That is what makes the pattern worth noticing rather than dismissing. The company measuring the problem, framing the problem, and selling the fix is one company, and they now own both the meter and the valve.

I want to be careful here, because I have backed a lot of what Cloudflare has done. Pay-per-crawl was the right idea. Content Independence Day was the right idea. Giving website owners a real choice over which machines get in beats a court deciding it for them, which is what I argued when the Ninth Circuit took up that question on August 4.

All of that can be true at once. Cloudflare can do some good things, some directionally good things, and some things that look sketchy, at the same time. Most companies can. The mistake is deciding they are the good guys or the bad guys and then reading everything they do through it.

### Go and Look at Your Own Logs

Take the traffic numbers seriously and take the framing with the salt it deserves. Machines are the majority of requests. That is measured, and it is true.

Then open your own crawler analytics and read the paths, not the totals. Mine told me three things I did not know this morning: that my largest AI crawler was a scanner, that it was burning megabytes of my bandwidth on nothing, and that the wordlist it works from now includes the config files it thinks my agent tooling lives in.

None of that detail is in anybody’s projection. The volume is. Fifteen hundred of these arrived at one small website in a single day, every one of them counting toward the thousand-to-one Seifert described to analysts, and not one of them wanted anything I wrote.

More Resources:

- Complete Crawler List For AI User-Agents [Dec 2025]

- US Publishers Demand Common Crawl Stop Scraping Their Content

- Should I Block AI Crawlers Or Measure Their Value First? – Ask An SEO

This post was originally published on No Hacks .

Featured Image: Lightspring/Shutterstock

Category SEO

Read Full Bio

Slobodan Manic Founder of No Hacks and machine-first website optimisation consultant at No Hacks

Slobodan “Sani” Manić is a website optimisation consultant with over 15 years of experience helping businesses make their websites faster, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/the-biggest-ai-crawler-on-my-website-was-hunting-for-credentials/585159/)
