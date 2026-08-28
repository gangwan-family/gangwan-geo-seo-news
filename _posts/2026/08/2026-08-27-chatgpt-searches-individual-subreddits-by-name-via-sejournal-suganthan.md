---
layout: post
title: "ChatGPT Searches Individual Subreddits By Name via @sejournal, @suganthan"
date: 2026-08-27T12:00:30+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-27/ChatGPT Searches Individual Subreddits By Name via @sejournal, @suganthan.md"
original_url: "https://www.searchenginejournal.com/chatgpt-searches-individual-subreddits-by-name/586925/"
author: "Suganthan Mohanadasan"
categories:
  - "AI Search"
  - "Reddit"
  - "_src_search-engine-journal"
---

# ChatGPT Searches Individual Subreddits By Name via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-08-27
- URL: https://www.searchenginejournal.com/chatgpt-searches-individual-subreddits-by-name/586925/
- Author: Suganthan Mohanadasan
- Categories: AI Search, Reddit

## RSS 摘要

Reddit still wins ChatGPT citations where a forum is the best source. Two captures, four days apart, show what actually decides the credit. The post ChatGPT Searches Individual Subreddits By Name appeared first on Search Engine Journal .

## 原文正文

ChatGPT Searches Individual Subreddits By Name Skip to content

- SEJ

- ⋅

- AI Search

## ChatGPT Searches Individual Subreddits By Name

ChatGPT targeted one subreddit with a 3,650-day window and gave it six of eight citations. Reddit's citation drop is query-dependent, not a shutdown.

Here is a search line ChatGPT wrote for itself this week, straight out of the traffic.

fast|site:reddit.com/r/whatnotapp seller tips Whatnot live selling|3650|reddit.com

Look at the path. It reads r/whatnotapp , one subreddit, chosen by name before anything was fetched.

Image Credit: Suganthan Mohanadasan

In the teardown I published on the 21st , I documented ChatGPT asking for Reddit at the domain level, reddit.com in the targeting slot with a 365-day window.

This goes a level deeper.

The model picked the community, not the site, and gave it 3,650 days, a decade of threads.

It came back with 48 Reddit threads out of 71 results in that conversation. 68% of everything it retrieved.

reddit.com/r/whatnotapp/comments/1vqdlaq/tips_for_a_new_seller/ reddit.com/r/whatnotapp/comments/1r6mws8/advice_on_selling_on_whatnot/ reddit.com/r/whatnotapp/comments/1tzv075/new_to_whatnot_best_tips_for_selling_smocked/

Then it cited them.

Six of the eight citations in that answer went to r/whatnotapp threads. One went to Whatnot’s own help centre.

A Reddit chip sits next to the advice about not starting valuable items at $1, next to the point about treating a stream as entertainment, and next to the one about scheduling shows ahead.

### Reddit Citation Is Query-Dependent, Not Switched Off

That matters because four days earlier I captured the opposite on the same account.

Query

Pages fetched

From Reddit

Citations

Won by Reddit

whatnot seller tips

best ai live chat support software

221

Four days apart, same account, both commercial questions. One gave Reddit three quarters of the visible credit. The other fetched 84 threads and credited none of them.

I published the second one on the 21st and read it as Reddit becoming an invisible input , feeding the verdicts while vendor pages collect the citations.

This capture says that reading is too broad. It holds for that conversation. It doesn’t hold as a rule.

What separates them is worth a guess, and it’s only a guess. Whatnot is a niche marketplace, and the practical seller knowledge sits in one subreddit and nowhere else. Live chat software is a vendor category with pricing pages, documentation and comparison sites competing for the same claims. When the honest best source is a forum, the forum still wins the citation .

Last week, I wrote that Reddit fell out of ChatGPT’s citations rather than out of the model , and that everything else needed another experiment.

This capture is that experiment, and it has consequences for the two explanations doing the rounds.

### Ryan Jones On Bing

Ryan found that Bing has stopped ranking Reddit for ordinary commercial queries, and reasoned that since Bing sits behind ChatGPT’s retrieval, Reddit went with it.

Image Credit: Suganthan Mohanadasan

His observation checks out, and it goes wider than his four examples. I ran them plus two of my own through Bing, reading the rendered SERP rather than an API.

Query

Reddit in Bing’s results

best tv for sports

none

best toothbrush

none

whatnot seller tips

none

transformers movie review

none

best running shoes

none

best crm for small business

none

Not “not in the top 10.” The string reddit.com appears zero times in the HTML of all six pages, while Google puts Reddit at position 2 for two of them.

Whatever has happened at Bing is real and worth knowing on its own.

Image Credit: Suganthan Mohanadasan

The step that doesn’t survive is an assumption the whole industry has carried since 2023, that ChatGPT’s web results are Bing’s results .

I’ve repeated it myself in talks. A pool can’t contain what the index doesn’t have, so if 68% of that pool is Reddit and Bing’s page for the same query has none, the two aren’t one source.

Something reaches Reddit another way, whether that’s OpenAI’s own index or the licensed feed from the Reddit deal.

Ryan’s Bing finding stands either way. It may well be the same decision playing out in two places rather than one causing the other.

### Jenny Halasz On Access

Jenny pointed at Reddit’s paid-access wall, and asked whether OpenAI’s user agents are now getting the restricted robots.txt and losing access to the content.

Image Credit: Suganthan Mohanadasan

She’s right about the architecture. I checked it. Reddit’s public robots.txt is Disallow: / for everyone, and the permissive version is the one served to verified partners, so the open file is the cloaked one.

I spoofed GPTBot and Googlebot, and both get a 403 rather than a robots.txt at all.

That 403 is the interesting part, because real Googlebot is obviously not blocked from Reddit.

It tells you Reddit verifies the requesting IP against the published crawler ranges rather than trusting the user agent string. Both OpenAI and Google publish those ranges, which is what makes the check possible.

The consequence is that nobody outside OpenAI’s IP ranges can see what verified OpenAI agents receive. Jenny says as much in her own post, that she can spoof a user agent but not an IP. So a user-agent test shows the outsider’s view no matter who runs it.

When I put this to her, she asked a good question. She still gets the user-facing robots.txt with no trouble, so was my test running from a US IP address?

It wasn’t. I’m on a residential connection in the UAE. That turns out to make the result cleaner rather than muddier, because every request came from that same address within the same minute and only the user agent changed.

Requested as

Response

Chrome on macOS

200, the public robots.txt

OAI-SearchBot

200

GPTBot

403

ChatGPT-User

403

Googlebot

403

Those all came from the same address within a minute, so geography can’t be the variable there. Her result and mine also agree, since a normal browser UA returns 200 for me too, so we were probably testing different things.

The row worth paying attention to is OAI-SearchBot at 200 while GPTBot and ChatGPT-User get 403. Reddit is treating OpenAI’s own agents differently from each other, which is a distinction no geographic explanation reaches.

Whatever robots.txt each agent receives, that content reached the model, current and in bulk, on a query asked this week. Worth adding that robots.txt governs crawling anyway, and a licensed data feed isn’t crawling.

### Auth On Old.reddit.com

A third version of the access idea has been going round too, that Reddit put a login wall on old.reddit.com and made scraping harder. That part is true. The r/whatnotapp thread ChatGPT cited redirects to /login/ on old.reddit.com , while the same thread on www.reddit.com returns 200 and serves normally.

Image Credit: Suganthan Mohanadasan

It doesn’t reach this, though, because every Reddit URL in the retrieval pool is www.reddit.com . A wall on a hostname ChatGPT never requested isn’t in the path. OpenAI’s licensing deal may make the whole question moot anyway, and I can’t tell from the payload whether those threads arrived through the Data API, OpenAI’s own index, or a crawl of www . The hostname I can tell you, and it isn’t the gated one.

Either way, six cited threads answer the access question from the other end. You can’t quote what you can’t reach.

There’s also a timing problem for access as the cause. The gating Jenny describes has been in place for around two years. The citation drop is three weeks old.

### On The Live Chat Query, The Drop Came After The Fetch

Both explanations are about fetching, and fetching is working on every query I’ve captured.

In the teardown, a live chat query pulled 84 Reddit threads out of 221 results and cited none of them. The pages arrived on that question and then went uncredited, which is the case that still needs explaining. It’s also the one that doesn’t repeat here, so whatever governs crediting varies by query rather than running one way.

That’s the step you can’t see from a SERP or a robots.txt. The experiment it needs is a different one again. Hold a query constant, capture the pool, and check whether the wording of the answer tracks the Reddit snippets that were fetched and never credited. That would test influence directly, which is the thing none of us can currently prove.

### A Falling Citation Share And A Winning Subreddit

Reddit is being searched deliberately, down to the individual community, with the widest freshness windows I’ve seen ChatGPT grant anything. It got cited heavily on the question where a subreddit is the best available source, and not at all on the vendor-category question I checked, where pricing pages and comparison sites answer the same thing.

That’s a different problem from the one being discussed. The aggregate citation share can drop sharply while Reddit keeps winning the queries it deserves to win, and both of those can be true at once.

### What I’m Not Claiming

Four queries, one account, one week. Two of the four didn’t pull any Reddit, and one didn’t trigger a search. The wider point that Reddit turns up less than it used to is not in dispute, and I can’t tell you where the line sits between a query that earns Reddit citations and one that doesn’t.

Jenny called it a yes-and situation with several contributing factors, and I think that’s closer to right than one explanation on its own, mine included. Bing’s rankings, Reddit’s access rules, and whatever governs crediting can all be happening at once.

The traffic changes where to look. The door is open, so the question moves to whatever decided that 84 fetched threads were worth reading and not worth crediting on the live chat query, when the 48 fetched here took six of the eight citations.

Whether those uncredited threads still form the answer is the part I can’t prove from traffic, because influence without a citation doesn’t leave a trace on the live wire.

More Resources:

- Why Reddit’s ChatGPT Citation Drop Isn’t Fully Explained

- Reddit Preserved The Part Of The Internet We Broke

- Reddit CEO Says LLMs ‘Would Not Exist’ Without Reddit Data

This post was originally published on Suganthan .

Featured Image: NONGNUCH VIKRUTHA/Shutterstock

Category AI Search Reddit

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

Suganthan Mohanadasan is the co-founder of Snippet Digital, an AI SEO agency, and Keyword Insights, an AI content intelligence platform. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/chatgpt-searches-individual-subreddits-by-name/586925/)
