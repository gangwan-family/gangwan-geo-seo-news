---
title: "Cloudflare Will Write Your Robots.txt, And It Has A Point via @sejournal, @slobodanmanic"
source: "Search Engine Journal"
published: 2026-09-18T14:30:00+00:00
fetched_at: 2026-09-18T23:25:06.353737+00:00
url: "https://www.searchenginejournal.com/cloudflare-will-write-your-robots-txt-and-it-has-a-point/589262/"
guid: "https://www.searchenginejournal.com/cloudflare-will-write-your-robots-txt-and-it-has-a-point/589262/"
author: "Slobodan Manic"
categories:
  - "AI Search"
  - "SEO"
  - "Technical SEO"
---

# Cloudflare Will Write Your Robots.txt, And It Has A Point via @sejournal, @slobodanmanic

- Source: Search Engine Journal
- Published: 2026-09-18
- URL: https://www.searchenginejournal.com/cloudflare-will-write-your-robots-txt-and-it-has-a-point/589262/
- Author: Slobodan Manic
- Categories: AI Search, SEO, Technical SEO

## RSS 摘要

Bot Preference Sync sets AI crawler policy per category, not per crawler. Allow GPTBot and block Bytespider, and no setting describes what you do. The post Cloudflare Will Write Your Robots.txt, And It Has A Point appeared first on Search Engine Journal .

## 原文正文

Cloudflare Will Write Your Robots.txt, And It Has A Point Skip to content

- SEJ

- ⋅

- SEO

## Cloudflare Will Write Your Robots.txt, And It Has A Point

Cloudflare's Bot Preference Sync writes your robots.txt for you, by default, from three settings that cannot express a per-crawler policy.

On August 20, I published a page arguing that a website’s robots.txt and its actual enforcement are two different things , and I used my website as the example of getting it wrong. My robots.txt had spent months welcoming Bytespider by name, long after I would have chosen otherwise, and I only caught it while writing that page.

The next day, Cloudflare announced Bot Preference Sync , a product that fixes exactly that.

Bot Preference Sync writes your robots.txt for you. Whatever bot policy you set in Cloudflare’s dashboard gets turned into robots.txt entries and prepended to your file, inside # BEGIN Cloudflare Bot Preference Sync and # END Cloudflare Bot Preference Sync markers, with your existing content preserved underneath. Cloudflare says it will run from the free tier up, and that for new customers it will be on by default.

As of September 13, there is no entry for Bot Preference Sync in Cloudflare’s bots changelog , which still ends at July 1, no mention of it anywhere in Cloudflare’s bots documentation, and no generated block on my robots.txt. So what follows is a product as announced.

Bot Preference Sync is good. My objection is that it hands a vendor the decision about what your website tells AI crawlers, in a shape that cannot express what many websites actually do, and it does that by default.

### A Robots.txt That Contradicts Your Edge Is An Argument For Ignoring It

Cloudflare’s announcement of Bot Preference Sync says that “when your stated preferences and your enforced rules disagree, some crawlers treat it as a basis to disregard your preferences or try to bypass your enforced rules.”

Cloudflare does not say which crawlers, or how many, or how it knows. It sits in front of a large share of the web and sees the traffic, which makes it the one party in a position to name them, and it names none. It sounds like something that could be true. A list would make it something I could check.

Cloudflare is confirming the argument I spent a whole reference page on in what courts say about blocking AI bots . A file that says one thing while your edge does another hands an argument to anyone who wants to ignore you.

That kind of gap is easy to create, because robots.txt and edge enforcement live in different places. The file is text you wrote once, probably a while ago. The enforcement is a dashboard you changed at some point since. Nothing keeps them honest with each other, and nothing keeps either of them honest with what you would decide today. My file drifted from what I would decide for months, and I write about this for a living.

I started fixing my robots.txt by hand on August 20, the day before Cloudflare announced Bot Preference Sync, and finished on August 26.

### Bot Preference Sync Sets Policy Per Category, Not Per Crawler

Bot Preference Sync generates your robots.txt from three settings, which live under Security Settings and Configure AI bot policies: Search, Agent, and Training . Cloudflare’s documentation gives all three the same options : block on all pages, block only on pages with ads, or allow. The Bot Preference Sync announcement describes Training differently, as a Disallow option that writes a no-training line into the file. Cloudflare’s tracked bot list decides which crawlers fall into which category, and the generated robots.txt entries follow from your three settings. You cannot exclude an individual bot from the sync. Cloudflare’s stated answer for anyone who wants finer control is to turn the sync off and maintain the file yourself.

My own crawler policy does not fit any of Bot Preference Sync’s three categories. I allow OpenAI’s GPTBot, Anthropic’s crawler and PerplexityBot. I block Bytespider and meta-externalagent . Every one of those companies trains models. My rule is a question I ask per company: What am I getting in return? The first three put my pages in front of people who ask assistants questions. The other two take and return nothing. That is a business decision made one crawler at a time .

Set Training to disallow and the file tells OpenAI not to train on content I am happy for OpenAI to train on. Set Training to allow and nothing in the file separates Meta and ByteDance from anyone else, while my edge returns 403 to both. There is no setting that describes what I actually do. Cloudflare’s documented remedy is to switch the sync off and go back to writing the file by hand, which I had already been doing the day before Bot Preference Sync existed.

### Cloudflare Published 4 Disclosure Conditions, And Attached Blocking To Them

Setting Training to disallow writes a no-training line into your robots.txt and blocks every AI crawler Cloudflare judges opaque. Cloudflare has published the conditions a crawler must meet to avoid that. For a bot that does both search and training, here are the requirements in Cloudflare’s own words:

- It “must respect, via any mechanism, a ‘no training’ preference in robots.txt”

- “They give site owners a way to opt out of AI summaries”

- “They provide URL-level visibility into which pages were made available for training, as well metrics on search results, so you can see how your content was used for search and for training”

- “They can show publicly that Disallowing Training does not hurt your traditional search results”

Miss those four conditions and Cloudflare treats the crawler as opaque, and opaque means blocked on every website that set Training to disallow.

No company is named anywhere in that list. Conditions two and four describe Google.

Condition four Google already meets. Its crawler documentation , last updated July 14 2026, says Google-Extended controls whether crawled content trains Gemini models and grounds their answers, and that it “does not impact a site’s inclusion in Google Search nor is it used as a ranking signal in Google Search.” That is the public statement condition four asks for, on Google’s own say-so.

Condition two is the one Google has no answer for. It asks for a way to opt out of AI summaries, and Google’s documentation on AI features says the controls are “nosnippet, data-nosnippet, max-snippet, or noindex,” every one of which limits what Search shows everywhere. The same page sets the rule that makes the two inseparable: to be shown as a supporting link in an AI Overview “a page must be indexed and eligible to be shown in Google Search with a snippet.” One switch governs both. There is no setting that takes you out of AI Overviews and leaves your ordinary search snippets alone, and Google’s crawler documentation does not mention AI Overviews anywhere.

Microsoft answered condition two in September 2023 . Content tagged NOARCHIVE “will not be included in Bing Chat answers,” and such content “will still appear in our search results.” The content stays out of the answer and stays in the index. The ask is reasonable and it is easy to meet. Cloudflare’s July 2026 post on AI traffic options names BingBot alongside Googlebot as the mixed-use crawlers these conditions govern.

So Cloudflare, which sits in front of much of the web, has written down what disclosure it expects from AI companies, and attached blocking to the answer. That seems fair to me. But the terms were written by a vendor, the enforcement is that vendor’s network, and the websites doing the blocking mostly clicked one toggle in a dashboard and never saw the conditions attached to it.

The accountability question publishers have been asking about AI companies now points at Cloudflare too.

### Cloudflare Says Bot Preference Sync Will Be On By Default For New Customers

On September 15, Cloudflare changes the defaults for all new domains: Training and Agent blocked on the pages that display ads , Search left allowed. Until then a new customer who sets nothing gets no blocks at all, and Cloudflare says “the starting point will not add any blocks on your behalf.”

Selecting “I monetize from pages with ads on this domain” during onboarding sets Training to Disallow for you. That is a question about your business model, and the answer to it becomes a published position on AI training in your robots.txt.

On defaults generally my position is unchanged: Do not go for them without knowing what they do. The websites at risk are the ones that never open robots.txt again and never read the position written for them. They will have a policy on AI training that they did not write, cannot see, and could not have expressed in three settings anyway.

Every default gets accepted by people who never see it, Cloudflare’s included. Cloudflare already writes its analytics script into free-plan websites unless you opt out, which its own blog announced in September 2025 and an August 2026 Hacker News thread rediscovered . The same on-by-default pattern now reaches robots.txt, a file people open even less often than a settings page.

### Robots.txt Stops The Crawlers That Want To Be Stopped, And Nothing Else

A robots.txt rule stops a crawler that chooses to be stopped and does nothing to one that does not . Bot Preference Sync will make some people feel protected.

The file is a request, and a request only works on the well-behaved. I have measured the other kind on my own website: the biggest so-called AI crawler in my logs was hunting for credentials , asking for /.env and SSH keys under a nonprofit research archive’s name. No line in a text file was ever going to inconvenience that.

So Bot Preference Sync is genuinely useful for the honest half of the internet, which is a real half. The enforcement is still the edge. The file is documentation of intent, which matters later, in a dispute, and not at the moment a request arrives.

### Compare Your Robots.txt To Your Cloudflare AI Bot Policies Before Bot Preference Sync Reaches You

Three checks take about 10 minutes and tell you whether Bot Preference Sync would change what your website publishes.

Read your robots.txt, including the parts you wrote in 2023. Then open Security Settings, Configure AI bot policies, and compare. If those two disagree, you have the mismatch I had, and you get to decide who fixes it.

Then decide whether the three categories can express what you want. If your policy is “open to everyone” or “closed to training,” they can, and Bot Preference Sync will save you a job you should not have to do by hand. If your policy is per company, they cannot, and the honest move is to turn the sync off and maintain the file yourself.

When Bot Preference Sync does reach your website, go look at what it wrote. A policy file you have not read is a statement someone else is making on your behalf.

More Resources:

- Should I Block AI Crawlers At Robots.txt Or Server Level? – Ask An SEO

- What Opting Out Of Google’s AI Search Features Means Now

- The Modern Guide To Robots.txt: How To Use It Avoiding The Pitfalls

This post was originally published on No Hacks .

Featured Image: PeopleImages/Shutterstock

Category SEO AI Search Technical SEO

Read Full Bio

Slobodan Manic Founder of No Hacks and machine-first website optimisation consultant at No Hacks

Slobodan “Sani” Manić is a website optimisation consultant with over 15 years of experience helping businesses make their websites faster, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/cloudflare-will-write-your-robots-txt-and-it-has-a-point/589262/)
