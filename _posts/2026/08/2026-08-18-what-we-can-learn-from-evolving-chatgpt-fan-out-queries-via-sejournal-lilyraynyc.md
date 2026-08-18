---
layout: post
title: "What We Can Learn From Evolving ChatGPT Fan-Out Queries via @sejournal, @lilyraynyc"
date: 2026-08-18T13:01:30+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-18/What We Can Learn From Evolving ChatGPT Fan-Out Queries via @sejournal, @lilyraynyc.md"
original_url: "https://www.searchenginejournal.com/what-we-can-learn-from-evolving-chatgpt-fan-out-queries/586254/"
author: "Lily Ray"
categories:
  - "AI Search"
  - "SEO"
  - "_src_search-engine-journal"
---

# What We Can Learn From Evolving ChatGPT Fan-Out Queries via @sejournal, @lilyraynyc

- Source: Search Engine Journal
- Published: 2026-08-18
- URL: https://www.searchenginejournal.com/what-we-can-learn-from-evolving-chatgpt-fan-out-queries/586254/
- Author: Lily Ray
- Categories: AI Search, SEO

## RSS 摘要

ChatGPT's search behavior is starting to look like E-E-A-T. Here's the data behind that theory, and what to do about it. The post What We Can Learn From Evolving ChatGPT Fan-Out Queries appeared first on Search Engine Journal .

## 原文正文

What We Can Learn From Evolving ChatGPT Fan-Out Queries Skip to content

SEJ Live : Boost Your Local Business Visibility Across AI Search

Register Now

- SEJ

- ⋅

- SEO

## What We Can Learn From Evolving ChatGPT Fan-Out Queries

ChatGPT is scoping its fan-out searches to sites it already trusts, and I think the site: operator is a method of reducing spammy results. See what the recent industry research reveals.

Over the past few months, I’ve been paying close attention to how ChatGPT’s fan-out queries have been evolving, as some interesting developments have taken place that I believe are changing the quality of ChatGPT’s responses. I’ve been working on this article for a while, but this one has been particularly difficult to write, because as with all things in AI search, the information changes more quickly than I can finish writing about it. That’s definitely been true for how OpenAI appears to be tweaking and refining its process of retrieving information via web search (RAG), and especially for how heavily ChatGPT has started relying on site: searches in fan-out queries, potentially using them to curate results from higher-quality sources.

The TL;DR: I think OpenAI is using fan-out queries, and the site: operator in particular, as one method of reducing spammy outputs in their answers derived from internet content. I believe it’s their effort to improve the quality of retrieved sources while taking early steps to combat spam and low-quality information in their results. It reminds me of what Google has tested with E-E-A-T, but ChatGPT style.

I think analyzing fan-out queries matters because ChatGPT is using search engines to retrieve the results it uses to formulate an answer, which means this is fundamentally an SEO problem. Every word the model chooses to put into a fan-out query, and every search operator it uses, tells us something about what the model is looking for and where in the search results it expects to find it. When it scopes a search with site:, adds the word “official,” or points at a specific subreddit, the model is telling us what kind of content it believes will best answer the user’s question. Those queries are the closest thing we have to understanding why ChatGPT pulls in the information that it does, and I think there is a lot we can learn from unpacking them.

There are a few folks in the industry who have done great work sharing their findings on the inner workings of ChatGPT: reading the raw traffic, scraping the conversation files, and pulling fan-outs out of the API. Their datasets have started to converge on the same findings, and this article combines the learnings from their research with my own observations from watching fan-out behavior over time, using a combination of Peec AI, Profound, the Resoneo plugin , FanoutFox , and Google Search Console. So I aim to do two things with this article: First, lay out what everyone has actually found, in one place, with the numbers attributed to whoever ran them. Then give you my read on what’s evolving and why I think it’s important.

### The Mechanics Of How ChatGPT Fan-Out Queries Work

Not all searches on ChatGPT use web search. Anything contained in its training data can be answered quickly without using RAG, and OpenAI’s free or cheaper models are more likely to rely on training data to answer questions quickly, as it costs them less money to generate. When the question requires up-to-date knowledge, ChatGPT will use web search (retrieval-augmented generation or RAG) to pull information from a variety of sources, including external search engine data and its own internal index (Labrador).

When you do ask ChatGPT a question that triggers a web search, it starts by deconstructing your prompt into a set of its own background searches (fan-out queries), runs them in parallel, and synthesizes an answer from whatever comes back. Monitoring how fan-out queries change over time tells us a lot about how OpenAI is tweaking the model’s search behavior to try to produce better results. I think watching this space gives us a big clue about what they were hoping to achieve with each model update.

It’s important to start by defining two words commonly thrown around in our space, without it always being understood what the nuance is between them. Retrieved means a page ChatGPT fetched while running its fan-out queries. Cited means a page that made it into the visible answer as a link. Citation and retrieval can behave differently, and right now they appear to be moving in opposite directions: the number of “retrieved” URLs in ChatGPT’s responses is growing, while independent measurements show the number of unique domains cited per response falling over the same period . While more pages are being considered for the answer, fewer pages get cited and credited.

While reading any study about AI search, it’s worth asking whether the article refers to retrieved URLs or cited URLs, and if it’s discussing citations, for which prompts those citations are appearing. In many cases, the discrepancies I’ve seen between fan-out studies come down to one measuring retrieval and the other measuring citations.

To read the actual fan-out queries (not just the final answer), I’ve been using a combination of a few tools: Peec AI and Profound both offer fan-out queries for tracked prompts, and the free Resoneo ChatGPT Chrome plugin and FanoutFox (shown below) both surface the queries the model runs and the sources it pulls. These plugins make it easier to watch the model “think” through its searches in real time.

Image Credit: Lily Ray

Timing matters here too: it’s essential to consider how and when ChatGPT releases new models, and which models and tiers are most commonly used by the majority of its users. ChatGPT 5.6 ships in more than one variant: Sol is the standard version, and the cheaper “Luna” variant is what rolled out around the start of August as the new default model for Free and Go users . That distinction is important when you read the studies below, because they aren’t all measuring the same model or tier. And according to Olivier de Segonzac’s breakdown in Search Engine Land , more than 90% of ChatGPT’s weekly users are on the free plan . So whatever the free default does when it searches, it’s now most likely what the large majority of ChatGPT users get.

### Part 1: What Industry Research Currently Shows

#### What I Saw In My Own Research

A few patterns stood out to me early on, before I went looking at anyone else’s data:

- The better models search more, and lean on site: more. In my testing, ChatGPT 5.4 Thinking would fire 10-plus searches for a single prompt , including multiple site: queries, while 5.3 Instant often did just two to three fan-outs.

- The type of site: search appears to depend on the query. For opinions and product reviews, it leans heavily on Reddit, including querying specific subreddits. For YMYL-style questions, it appears to prefer authoritative sources, often .gov domains or sometimes .org. In one batch of roughly 20 prompts in the legal space, every single one returned citations only from .gov domains . The below screenshot from the Resoneo plugin shows this process at work:

A screenshot from the Resoneo plugin showing how the prompt “tell me about legal benefits for disabled veterans” generated ChatGPT fan-out queries all limited to specific .gov sites (Image Credit: Lily Ray)

- For specs and pricing, the model goes to the brand. Searches like site:sephora.com or site:costco.com showed up regularly. And if you ask about a product or service, ChatGPT will often run site: searches against the most well-established brands in that space, even when you didn’t name them in your prompt . It also often names specific products and does site: searches for individual product pages from the brand within the fan-out queries.

The net effect, at least in what I looked at, appears to be more ChatGPT visibility for high-authority sites and trusted brands, and fewer citations for everyone else.

Below, I’ll highlight a few recent studies on this topic and what they found.

#### Useful Findings From SEO & AI Search Industry Experts On ChatGPT Fan-Outs

Several awesome folks in our space have been measuring this independently, with different tools and different collection methods. David Konitzny at Peec AI ran the numbers the day ChatGPT 5.6 became the default: the share of prompts with only a single fan-out query dropped from 94.0% to 43.5%, average retrieved sources roughly doubled from about 12 to 24, prompts needing a second fan-out iteration went from about 5% to 33.5%, and the site: operator went from appearing in roughly 0.3% of fan-outs to about 23%. Basically, ChatGPT is becoming more precise and robust in its searching process.

Chris Long at Nectiv , comparing roughly 4,000 prompts on 5.6 Sol against his own 2025 baseline, found average fan-out queries per prompt went from 2.17 to 7.61, the longest query chain went from 4 searches to 29, and “site:,” “official,” and “gov” all landed as top unigrams, with site: in 64% of queries. There’s a big gap between the site: search figures in David’s and Chris’s articles, and it could be explained by the fan-out query collection method: Chris’s consultancy pulls fan-outs from OpenAI’s API , while several of the other tools in this space extract them from the ChatGPT consumer interface. While the API is clean and repeatable, the UI method may be closer to what real users actually get (with certain limitations like personalization, which no tool can track effectively). It’s worth checking which method a study used to understand why different studies may show discrepancies. In both studies, however, the share of site: searches in query fan-outs increased substantially.

David also found product pages now make up 16.39% of retrieved pages, moving ahead of listicles, which tracks with what I’d been seeing anecdotally: ChatGPT 5.6 appears to go straight to brands and manufacturers for specs and pricing rather than routing everything through roundup articles and other listicles, which can be self-serving and prone to manipulation . The page types losing share of retrievals (listicles, how-to guides, and comparison pages in particular) also happen to be the formats most heavily spammed for GEO over the past year or two . In my talks throughout this year, I’ve shared how these exact page types cause SEO and AI search problems.

Olivier de Segonzac and the Resoneo team , who have done some of the most detailed reverse-engineering of the retrieval architecture out there, found that the unique domains cited per response dropped from 19 to 15 after the 5.3 update, confirming the pattern from the other direction: retrieval counts grew while citation counts dropped . Ahrefs’ most-cited-domains data shows where the surviving citations land most frequently: Reddit, Wikipedia, Forbes, Merriam-Webster, Consumer Reports, Healthline, and Walmart.

Suganthan Mohanadasan has been coming at it from the network-traffic side, and his findings are useful to understand: ChatGPT decides before it searches. Across 57 conversations and 3,554 retrieved pages, 21 of 27 initial queries contained brand names the user never mentioned in their prompt , across 11 of 13 product categories. For example, when searching “the best AI note-taking app,” the first fan-out query already contained the words “Granola,” “Notion AI,” “Otter,” “Fireflies,” “Fathom,” “Mem,” and “Limitless.”

Below is a snippet from Suganthan’s recent article, shared with permission:

Image Credit: Lily Ray

Being the brand mentioned in that first query is the real goal: brands named in the fan-out were cited 68.9% of the time , while pages that were only fetched were cited 2.1% of the time, and only 110 of the 3,554 retrieved pages, about 3.1%, made it into an answer at all. Suganthan also explained ChatGPT’s routing logic within fan-out queries: facts route to official pages, and opinions route to reviews and Reddit. So ChatGPT will look to different types of sites, and distinct pages within them, depending on which information helps to best answer the user’s question.

As with all studies, it’s helpful to read his methodology alongside those numbers, which he states himself: a single account, based in Dubai, sampled in July 2026, weighted toward software and AI tools, with the brand-injection pattern measured across 27 initial queries. That’s a relatively small sample size, but it’s worth citing because the direction also matches what the larger datasets show, and what I see in my own testing.

#### The Consensus Between Recent ChatGPT Fan-Out Query Studies

Although the above researchers used different tools, different models, and different collection methods, their findings still line up across four common patterns:

- ChatGPT is running substantially more searches per prompt than it was a year ago, including for free and cheaper tiers.

- A meaningfully large share of those searches are now scoped with the site: operator.

- The domains it scopes to skew high-authority : official and manufacturer pages, established review platforms (G2, Clutch, Capterra, Consumer Reports, Wirecutter), Wikipedia, .gov and regulatory sources, major retailers, and Reddit.

- Retrieval is going up while the number of unique domains cited is going down.

The skew is toward surfacing higher-quality, recognizable sites , and that trend is continuing with newer ChatGPT models.

### Part 2: My theory On One Reason Why This Is Happening

I find all of this interesting because it aligns closely with one of the components of Google’s search ranking systems I’ve spent the most time studying: E-E-A-T (experience, expertise, authoritativeness, and trustworthiness) . I think OpenAI may be using fan-out queries as a method of ensuring users get high-quality, trustworthy, authoritative information, while suppressing spammy and highly manipulated articles (such as self-promotional listicles and other types of self-serving content).

I think the site: operator is functioning (at least in part) as a spam filter.

For a while, ChatGPT would frequently retrieve and cite the exact kind of spammy, self-serving, manipulative content that we’ve already become quite familiar with in the SEO world. Evaluating the quality of a random open-web page in real time is genuinely hard and expensive, and at ChatGPT’s volume you’d have to do it hundreds of millions of times a day. Narrowing fan-out queries to .gov domains, established review platforms, big recognizable brands, and official sources is presumably a much cheaper way to get most of the same outcome. Instead of judging whether an unknown page is trustworthy, the model appears to be sidestepping the problem entirely by only looking for information in places it already trusts.

Google spent years building systems to answer “is this source authoritative enough for this query?” and what OpenAI appears to be doing is a distilled version of this same process, relying heavily on the site: operator and other keywords that influence which sources get retrieved. For example: pure facts go to the brand’s own domain. Health and legal questions go to .gov sites. Opinions go to Reddit and established review platforms. While Google uses complex ranking algorithms to surface high-quality, trustworthy, and authoritative pages, ChatGPT can refine its fan-out queries to ensure the search results pull from those trusted sources.

Adding “.gov” to certain queries (YMYL, perhaps?) is what I find intriguing, because it reminds me of how Google elevates .gov (and other high-authority) sites in its results for certain queries or during times of crisis. For example, during the Covid era, I shared a lot of research showing how Google elevated the official FDA, CDC, and other high-authority and government sites in the search results for health-related queries:

Research from my 2022 MozCon presentation (Image Credit: Lily Ray)

The .gov-only pattern in that batch of legal prompts (shown below) feels like a big change on ChatGPT’s part, as it separates the most “popular” or “optimized” pages on the internet from the official authority sites. On almost any consumer legal topic, the popular, top-ranking pages shown in search come from law firm blogs, not government agencies. Combined with the page types losing retrieval share, that strikes me as a way for ChatGPT to cut through the noise and elevate official information instead.

Image Credit: Lily Ray

The refinement also appears to be moving down across the price tiers. The 5.4 Thinking model was already doing a version of this : lots of fan-out queries, site: operators aimed at trusted domains, a clear preference for official and authoritative sources. With 5.6 becoming the free default, those search behaviors seem to have also extended to free tier users, not just the users paying for the reasoning model.

#### The Use Of The Word “Official” In Fan-Out Queries

I found it very interesting that the frequency of the word “official” in fan-out queries appears to be climbing, and it shows up as a top unigram in Chris’s data alongside site: and gov. Similar research by Conductor , shown below, also shows the increase in site: searches and searches including “official.” ChatGPT seems to be actively trying to find the official source for a brand or product, which is exactly what you’d expect if the goal is to avoid citing unverifiable third-party pages.

Image Credit: Lily Ray

This could present a decent reason to revisit whether “Official” or “Official Site” belongs in your homepage title tag or meta description, especially for companies that share a name with other brands or entities, or where the search results may otherwise be confusing. While this has already been a fairly standard SEO recommendation for a long time, I think there are cases where making that language explicit can avoid confusion. And given how much ChatGPT now appears to be looking for official information in the search results, it could potentially help the model reconcile which brand you actually are, or which domain is officially yours.

#### The Risks Of Relying On Site: Searches

Heavy use of site: searches in fan-out queries can work well when the model knows which sites to pull from. But articles by Malte Landwehr and Netcraft found that if there is confusion about the correct domain for a given brand, ChatGPT appears to guess the domain, and sometimes it guesses incorrectly.

Malte Landwehr found examples where ChatGPT constructed site: queries against the wrong brand domain , and in some cases, a domain that doesn’t belong to the company at all. In one test, it repeatedly searched site:census.com for the startup Census (not the government bureau), when the startup’s official site is getcensus.com, and census.com is parked and available to buy. He saw the same pattern pointing at other parked domains like lago.io, persona.id, lightfield.ai, and mesa.com.

A Netcraft study from 2025 also found that roughly a third of brand login links generated by LLMs pointed to domains the brand didn’t own, and about 29% pointed to unregistered, inactive, or parked domains, with smaller brands the most exposed.

As Malte discussed in his article, when the model misidentifies the trusted site for a lesser-known brand, someone could buy that parked domain, host content matching what ChatGPT is looking for, and quietly feed it wrong pricing or a fake support number. This could be problematic for brands where the official domain isn’t strongly encoded yet, or where any other reason prevents ChatGPT from identifying the right domain name.

It’s worth acknowledging that this narrowing could be as much about cost and latency as it is about quality. Checking a short list of known domains is cheaper and faster than evaluating the open web at ChatGPT’s volume, and from the outside, that would look identical to a deliberate quality filter. Malte’s finding also shows there is still room to improve: a model that was genuinely assessing whether a source is trustworthy and authoritative would be less likely to point a search at a parked domain. So there could be more than one reason why OpenAI is evolving how it constructs fan-out queries.

#### Site: Searches Appearing In Google Search Console

One site: query on the site below generated roughly 197,000 impressions and exactly one click. That’s not the only example: when I looked at site: searches for several major brands in Google Search Console , I found thousands of impressions for site: queries with almost zero clicks, and the volume of these queries is generally increasing over time. A click-through rate that close to zero is hard to explain with human searchers, and points instead to bots (LLMs, tracking tools, scrapers, and so on). You can see similar site: search patterns in Bing Webmaster Tools’ AI search query reporting.

Image Credit: Lily Ray

This got me thinking: ChatGPT is running far more site: searches than ever, and if it (or the partners it uses to scrape search engines for RAG) is still leaning on a major search index, it seems plausible that at least some of those searches would surface in our query reporting. There’s no official “ChatGPT Search Console,” so this is speculation based on looking at various accounts in both Google and Bing’s search console tools, and Google has had its own Search Console impression-related data issues muddying this exact kind of data, so it’s difficult to get a conclusive answer as to where these searches are coming from.

The practical tip: Check both Google Search Console and Bing Webmaster Tools queries for site: searches and other repeated patterns. In Search Console, use the Performance report and filter Query by “Queries containing” site: (or a regex). In Bing Webmaster Tools, use the Search Performance report and search the query table for site: strings.

While ChatGPT search has historically run on Bing (the OpenAI-Microsoft partnership), independent testing over the past year suggests it’s also pulling from Google’s index, possibly through third-party scrapers, so it genuinely isn’t clear which engine logged a given retrieval. This information is also evolving all the time, especially given Google’s lawsuit against SerpApi, which was believed to be the provider of scraped Google data to OpenAI. ChatGPT also appears to be increasingly building and leveraging its own index , which would give OpenAI more control over freshness and coverage without depending on its biggest competitor.

Bing has made it easier to monitor AI search performance: in February 2026, it launched an AI Performance Report inside Webmaster Tools that separates AI citations from traditional search and surfaces “grounding queries,” which are the topics derived from search phrases Copilot generates internally to retrieve content. That was big news: a search engine choosing to report fan-out sub-queries as their own category, which tells you this whole behavior is real enough that Microsoft is now building reporting around it (while Google continues to hide it from us).

### What I’d Actually Do About It

I see a lot of this as an indication that SEO matters more than ever. Because ChatGPT appears to lean on major search indices (directly or through RAG partners), ranking well in search is still what feeds the fan-out , along with ensuring your brand has the right information when its pages are directly searched for. Here are a few things I think are worth doing:

- Build your brand to the point where it’s the one ChatGPT thinks of first. While this one seems pretty obvious, this is where all the data points: you want your brand to be synonymous with its category , and to be naturally recommended enough to enter into the training data as one of the most trusted and well-known brands in the space. Without good branding, it’s likely that your brand won’t even enter the conversation. This is also impossible to win long-term via manipulative optimization tactics.

- Put your key facts in plain, crawlable HTML on your own domain. Information such as pricing, specs, model numbers, and support details needs to be readable to the model. If ChatGPT is running site:yourbrand.com looking for these, they need to be included as text it can actually read , not locked inside an image or client-side JavaScript-rendered content.

- Nail down which domain is “official.” Consider “Official Site” (or similar) in title tags or meta descriptions where it reads naturally and helps users (don’t spam this), and make sure your real domain is consistently reinforced across the web, particularly if you’re a smaller brand or share a name with other entities. This is the single best defense against the wrong-domain problem.

- Don’t play whack-a-mole with trying to target individual fan-out queries. They’re long-tail, low-volume, and vary between prompts and users. Generating many pages targeting the long-tail is a good way to get caught up in Google’s scaled content abuse spam trap. It’s more useful to aggregate the queries the model keeps running and find the core topics it consistently prioritizes. This is what I believe Microsoft does in the Bing Webmaster Tools AI search query report. I also think that aggregating fan-out queries and distilling them down into core keywords to use for traditional SEO rank-tracking is still a good method of approximating AI search performance: if you rank well for the topics generally asked about in fan-out queries (ideally tracked across both Google and Bing), you have a higher chance of ultimately being part of the AI response.

- Check whether you are in the query at all. Suganthan’s test is a good one: Run the prompts you care about five separate times and look at whether your brand shows up in ChatGPT’s initial searches , not just in the answer. If it never does, you likely have work to do to build up the notoriety of your brand in its niche, and that gets done with reviews, comparisons, digital PR, and media coverage over a long stretch of time, not with technical fixes alone. If your brand does show up, the goal is to convert retrievals into citations and to influence the AI response, and that is where on-page optimization can count: state claims clearly and early on the page, and ensure important numbers and business details are retrievable for LLMs .

- Take Reddit seriously. If the model is pulling opinions from specific subreddits, that’s part of your brand’s visibility now, whether you like the discussions or not. But retrieval and citation diverge here: Dan Petrovic found ChatGPT discards the Reddit pages it pulls roughly 99% of the time . That fact stood out to me next to Reddit topping Ahrefs’ most-cited-domains list, and both are true at once: Reddit gets retrieved so relentlessly that even a ~1% survival rate produces more citations than almost anyone else in absolute terms. It’s also the same phenomenon as Suganthan’s 3.1% overall citation rate, seen from a single domain’s point of view. So treat Reddit as something that shapes how the model understands your category rather than as a reliable citation path. And don’t use any of this as an excuse to spam Reddit with artificial recommendations of your brand : Reddit recently cracked down on this exact type of GEO spam , using its own LLMs to flag around 25,000 spammy posts and comments per day, and playing with fire can cause your account to be banned.

- Watch your site: impressions in both Search Console and Bing Webmaster Tools. This is another example of bot activity affecting our Search Console data, on top of the recent discussions around Google Search Console showing conversational prompts from AI Mode as individual queries in GSC . This is something to consider so the noise doesn’t distort your reporting, and it could potentially hold some information about how ChatGPT (and maybe other LLMs) is retrieving information about your brand, assuming that’s what that GSC data reveals.

I believe much of this is a response to the clear flaws in ChatGPT over the past year, such as referencing biased and promotional content , like listicles and comparisons that recommend the same brand writing the article. These changes appear to be doing the opposite, narrowing hard to .gov domains, big brands, Reddit, and official sources, and extending that approach down from the premium models to the free default that most of the world uses. While I don’t see this as anywhere near as sophisticated as Google’s mechanisms for achieving similar goals, it shows that OpenAI is innovating toward higher-quality results and working on solutions to the problem of manipulated content appearing in its responses.

More Resources:

- How LLMs Interpret Content: How To Structure Information For AI Search

- How ChatGPT Actually Picks Sources (I Read The Network Traffic, Not The Outputs)

- ChatGPT Already Knows Who’s In The Running Before It Searches

This post was originally published on Lily Ray NYC Substack .

Featured Image: CineVI/Shutterstock

Category SEO AI Search

Read Full Bio

VIP CONTRIBUTOR Lily Ray Founder of Algorythmic at Algorythmic

Lily Ray is the founder of Algorythmic, an SEO and AI search consulting practice focused on SEO, AI Search (AEO/GEO), E-E-A-T, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/what-we-can-learn-from-evolving-chatgpt-fan-out-queries/586254/)
