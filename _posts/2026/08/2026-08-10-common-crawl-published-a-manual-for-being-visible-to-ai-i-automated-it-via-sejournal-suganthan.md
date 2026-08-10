---
layout: post
title: "Common Crawl Published A Manual For Being Visible To AI, I Automated It via @sejournal, @suganthan"
date: 2026-08-10T12:00:21+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-10/Common Crawl Published A Manual For Being Visible To AI, I Automated It via @sejournal, @suganthan.md"
original_url: "https://www.searchenginejournal.com/common-crawl-published-a-manual-for-being-visible-to-ai-i-automated-it/584466/"
author: "Suganthan Mohanadasan"
categories:
  - "Generative AI"
  - "SEO"
  - "Technical SEO"
  - "_src_search-engine-journal"
---

# Common Crawl Published A Manual For Being Visible To AI, I Automated It via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-08-10
- URL: https://www.searchenginejournal.com/common-crawl-published-a-manual-for-being-visible-to-ai-i-automated-it/584466/
- Author: Suganthan Mohanadasan
- Categories: Generative AI, SEO, Technical SEO

## RSS 摘要

Check captures, robots.txt history, block fingerprints and a live CCBot probe for any domain, free, straight from Common Crawl's own archives. The post Common Crawl Published A Manual For Being Visible To AI, I Automated It appeared first on Search Engine Journal .

## 原文正文

Common Crawl Published A Manual For Being Visible To AI, I Automated It Skip to content

🔥[Live 8/12 with Loren Baker] Ecommerce SEO : Own your "brand +promo code" search.

Register Now

- SEJ

- ⋅

- SEO

## Common Crawl Published A Manual For Being Visible To AI, I Automated It

Your CDN may be blocking CCBot without telling you, keeping your pages out of the archive that trains most models.

Every month, a non-profit called Common Crawl fetches over 2 billion webpages and gives the copy away to anyone who wants it.

That free archive is where most AI training data starts.

When Mozilla audited the LLMs released between 2019 and 2023, 64% had trained on Common Crawl data in some form, and GPT-3 was roughly 60% filtered Common Crawl by training weight.

If a model already knows your brand without searching the web , odds are this is part of where it learned.

The crawler behind it is called CCBot, and whether it can read your site decides whether you exist in that archive at all.

This is how it looks in your logs.

CCBot/2.0 (https://commoncrawl.org/faq/)

The July 2026 crawl holds 2.14 billion of those pages.

Three of its records come from bbc.com. CCBot asked for permission, read the refusal, and left.

As far as the training data pipeline is concerned, one of the biggest news sites on earth doesn’t exist.

The BBC robots.txt blocks 13 of the 14 AI crawlers the checker tracks, and other top news sites have been blocking training crawlers on purpose since 2023. BuzzStream measured it at 75% of the top U.S. and UK publishers.

The question that interests me is how many sites are missing from that crawl without ever deciding to be.

Chris Green posted HTTP Archive numbers on LinkedIn recently. Roughly 492,000 sites name CCBot in robots.txt, and about 95% of those mentions exist to block it.

His open question stuck with me.

How many of that half million meant it?

Since July 1 2025, Cloudflare blocks AI crawlers by default on every new domain it serves.

Its managed robots.txt reached 3.8 million more domains that never wrote one. Ad plugins add blocklists. In 2026, a CCBot block is as likely to be a platform default as a decision.

Common Crawl itself wrote a manual for auditing exactly this. But it’s all manual work. So I automated it.

The Common Crawl Visibility Checker is free, needs no signup, and answers one domain at a time, straight from Common Crawl’s own archives.

### Where Common Crawl Sits In The AI Pipeline

The crawling has run monthly since 2008, and the snapshots are the raw material for C4, RefinedWeb, RedPajama, Dolma, FineWeb and most of the other big training sets.

Labs rarely touch the raw crawl. They take a filtered derivative, so your page’s route into a model runs from CCBot through Common Crawl into one of those datasets, and each step keeps only what passed the one before it.

The pipeline is still moving, too. FineWeb added six fresh 2025 crawls last July, and NVIDIA hosts its Nemotron training set inside Common Crawl’s own bucket.

I covered the pre-training life of your content in the Three Lives of schema markup .

The short version is that CCBot is the one crawler whose visits compound.

GPTBot fetches your page for OpenAI alone. A CCBot visit ends up with everyone who’ll ever train on the open web.

### The Audit Common Crawl Expects You To Run By Hand

In June, Common Crawl published something interesting.

The AI Visibility Audit is an 18-page guide telling site owners how to check their standing in the dataset.

It’s a good guide with one catch.

Every check is manual.

You curl your homepage with CCBot’s user agent and compare the response to a browser’s.

Next comes the index API, where you eyeball your capture counts, and their web graph, where you look up your rank. Then you compile a scorecard per domain, by hand. lol!

I read the checklist and then automated it. Conveniently, Common Crawl opened its data to browser tools in May , which makes this the rare tool the data provider actually wants built.

I think they know exactly what they’re doing. Fair play to them.

### What The Checker Shows

Type a domain and the diagnosis comes back in four panels.

#### Captures Per Crawl

How many of your pages each of the last twelve monthly crawls took, as a trend.

My site went from two captured pages in last August’s crawl to 55 in July’s, which is the most flattering chart anyone has ever drawn of it.

A big domain gets an estimate instead. Type wikipedia.org and you’ll see roughly 3.7 million, labelled as an estimate, because the tool reads the index structure for huge sites rather than counting every record.

Image Credit: Suganthan Mohanadasan

#### Robots.txt History

Common Crawl stores the robots.txt it read before every crawl. The checker checks those stored copies backwards month by month and diffs the AI crawler rules, so a block gets a start date.

Run bbc.com and every month reads the same. CCBot blocked, 13 of 14 tokens, Disallow slash.

Image Credit: Suganthan Mohanadasan

#### Whose Block It Looks Like

When a block matches a known template, the tool says so. Cloudflare’s managed robots.txt has a distinctive license comment. Squarespace’s default has its own unique signature.

And when eight or more AI tokens go down in one sweep, that’s usually a plugin or a copied list.

Image Credit: Suganthan Mohanadasan

#### A Live Probe

History says what happened, so this one checks what’s true right now. It fetches your homepage as CCBot/2.0 next to a normal browser and a control bot, which catches the block robots.txt never shows, a firewall challenging the user agent at the edge.

Image Credit: Suganthan Mohanadasan

Those four are the diagnosis. The rest of the checker is what to do with it.

Every check ends in a panel of fix cards matched to what it found.

A Cloudflare template block gets the dashboard path and a warning.

Handwritten blocks get the two-line robots.txt stanza with a copy button.

When it’s an edge challenge instead, the card will show the firewall vendor and links CCBot’s published IP ranges.

Under the cards, it will show the date of the next crawl, because a fix made today shows up in next month’s data, and knowing when to look is important.

#### Sitemap Coverage

The sitemap panel is the feature I wanted for myself. The checker fetches your sitemap and diffs it against the captured URLs, which turns the headline number into a work queue. Mine reads 42 of 97 pages in the July crawl, and the other 55 download as a CSV.

Image Credit: Suganthan Mohanadasan

#### Tracking A Single Page

You can also paste a full page URL instead of a domain and get that single page’s history across the year. Doing that taught me two things about my own site inside a minute.

My ChatGPT sources teardown was captured in only 1 of the last 12 crawls. And the copy Common Crawl holds isn’t the clean URL at all.

Image Credit: Suganthan Mohanadasan

CCBot found the page through a newsletter link and stored it with the ConvertKit tracking parameters still attached. I stopped using Kit a long time ago.

The crawler doesn’t browse your site the way you imagine. It follows whatever links the web actually contains.

#### Stored Copy Check

The last piece is a stored copy check. The tool pulls the actual bytes CCBot archived for your homepage, extracts the text, and compares it against your live HTML.

Both sides are read before JavaScript runs, which is the point, because CCBot never runs it.

Image Credit: Suganthan Mohanadasan

### The Invisible Blocks

Two kinds of block never show up when you check a robots.txt by hand.

1. CDN default. A domain created on Cloudflare after July 2025 blocks AI crawlers unless someone turned that off, and the managed robots.txt reached millions of sites whose owners never touched a file.

2. An edge rule. A WAF challenging CCBot while robots.txt reads clean. Common Crawl’s own guide says to check your CDN dashboard before you touch anything on your server, and they’re right. It’s also the one place no classic SEO crawler looks.

### What Actually Moves Inclusion

If your result shows open but barely captured, blocking was never your problem.

Crawl priority was.

Common Crawl samples each site by how well connected the domain is, so a handful of things matter.

- Fix the CDN first. If the live probe shows a challenge, no robots.txt edit will help you.

- Let CCBot in. Absence of a rule already means yes. Mine allows it explicitly, and quotes The Matrix while doing it. (Check it out)

- Add a sitemap in robots.txt . CCBot follows the sitemap protocol.

- Render on the server. CCBot doesn’t execute JavaScript , so content that only exists after hydration leaves an empty shell in the training data. Size stopped being an excuse in March 2025 , when the stored limit went from 1 MiB to 5 MiB per page.

- Earn links from well-connected sites. Crawl priority follows harmonic centrality, which you can look up in Metehan Yeşilyurt’s web graph tool . (Don’t listen to the “SEO is dead” naysayers. Keep buying, sorry, I meant building, those links.)

### What This Tool Can’t Tell You

Being in Common Crawl doesn’t put you in a model .

Every training set filters the crawl, and the frontier labs stopped disclosing their mixes around 2023.

Thin coverage proves nothing on its own either, because Common Crawl is a sample of the web, not a copy of it.

That’s why the checker looks at captures, robots history, and the live probe together before it gives you a verdict.

When the three disagree, it says so.

### Run It

Check your domain .

Then check a client’s. If the robots.txt history shows a block that appeared the same month the site changed CDNs, you’ll know exactly what happened, and you’ll probably be the first person to tell them.

The access checker covers the rest of the AI crawler picture, GPTBot and ClaudeBot and friends, live.

More Resources:

- Complete Crawler List For AI User-Agents

- How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers)

- Cloudflare’s AI Crawler Rules Can Block Googlebot

This post was originally published on Suganthan .

Featured Image: Prostock-studio/Shutterstock

Category SEO Generative AI Technical SEO

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

I’m the Co-founder of Snippet Digital, A Search Journey Optimization agency helping brands win across every stage of modern discovery. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/common-crawl-published-a-manual-for-being-visible-to-ai-i-automated-it/584466/)
