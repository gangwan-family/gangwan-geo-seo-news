---
title: "Q3 AI Visibility: AI Citations, Brand Mentions & Content Refreshes That Work via @sejournal, @AirOpsHQ"
source: "Search Engine Journal"
published: 2026-07-29T19:41:37+00:00
fetched_at: 2026-07-29T22:28:19.968691+00:00
url: "https://www.searchenginejournal.com/rundowns/q3-ai-visibility-ai-citations-brand-mentions-content-refreshes-that-work/"
guid: "https://www.searchenginejournal.com/rundowns/q3-ai-visibility-ai-citations-brand-mentions-content-refreshes-that-work/"
author: "AirOps"
categories:
  - "Generative AI"
  - "SEO"
---

# Q3 AI Visibility: AI Citations, Brand Mentions & Content Refreshes That Work via @sejournal, @AirOpsHQ

- Source: Search Engine Journal
- Published: 2026-07-29
- URL: https://www.searchenginejournal.com/rundowns/q3-ai-visibility-ai-citations-brand-mentions-content-refreshes-that-work/
- Author: AirOps
- Categories: Generative AI, SEO

## RSS 摘要

Five articles explain why AI citations fluctuate, where they come from, what makes them persist, and how to audit content for stronger AI visibility. The post Q3 AI Visibility: AI Citations, Brand Mentions & Content Refreshes That Work appeared first on Search Engine Journal .

## 原文正文

What It Takes to Get Cited, and Stay Cited in AI Search

## Q3 AI Visibility: AI Citations, Brand Mentions & Content Refreshes That Work

Reading Now

### AI Visibility Rankings Aren’t Stable – New Research Shows It’s Mostly Statistical Noise

AI visibility numbers move between runs, so a single reading can mislead. A new paper offers a stopping rule for when rankings are finally trustworthy.

Matt G. Southern 1.7K Reads

AI visibility tracking data isn’t entirely reliable. Because generative models often produce different responses, the citation shares and rankings on your dashboard are merely snapshots of a continuously changing target, not fixed facts.

A difference between you and a competitor could be genuine or just fluctuation between measurements. A new IQRush paper released on April 11, provides a method to distinguish these, showing that no fixed amount of data can definitively settle the question.

The paper is by Ron Sielinski, who co-founded IQRush, who sell software that measures AI visibility the way the paper argues you should. The reason it’s worth your time is that a separate team published a similar repeated-measurement finding in April, so IQRush is not the only one making this case.

### How Much These Numbers Move

Repeatedly querying SearchGPT, Gemini, or Perplexity with the same question can produce different sources each time. They’re built to add some randomness to each response, so each citation is just one of many possible URLs it could have pulled. A prior paper by the same author explored this variability, showing that, for example, when testing SearchGPT on running gear, Tom’s Guide made up about 9.5% of citations, while Runner’s World accounted for roughly 6.0%. On the dashboard, Tom’s Guide appeared more often, but the large margin of error meant the figures overlapped. With only one sample, it wasn’t accurate to say Tom’s Guide outperformed Runner’s World, as the 3.5-point difference was within the margin of error. The new paper aims to prevent this mistake by addressing a simple yet often overlooked question: How much data is needed before rankings are truly meaningful?

### When A Ranking Is Worth Trusting

The answer has two parts, and both need to be true for a ranking to be reliable. First, the order must stop changing.

In the beginning, rankings may change frequently as new answers are added because no site has a clear edge yet. It’s only after enough answers are collected that the top sites start to stand out clearly, allowing the order to stabilize. Also, it’s important that the top sites are well apart; if they’re very close, the ranking might not be meaningful, as a tight competition doesn’t really show who’s truly ahead. The paper looks at whether the difference between the top sites is bigger than the margin of error for each. When it is, the ranking reflects a real difference. When it isn’t, it’s probably just statistical noise. Both conditions need to be true at the same time, neither alone is enough. In 30 platform-topic tests, the number of answers needed for both conditions to be met ranged from 33 to 94, counting only answers with citations.

Three out of 30 didn’t reach this point even after 125 questions, all on SearchGPT, where top sites were too similar to tell apart. There is no single cutoff applicable everywhere; what works for one platform and topic may not suit another.

### We’ve Been Circling This

In January, I discussed SparkToro’s discovery that AI tools give a different list of recommended brands more than 99% of the time you ask the same question. That article left one question unanswered: how many times do you need to ask before the results stabilize? This paper offers the clearest answer I’ve come across.

Rand Fishkin, who led that study, shares some helpful advice. Before spending any money on tracking AI visibility, he suggests making sure your provider “shows their math.” The IQRush paper is a great way to do this because it provides a simple stopping rule, so you don’t have to rely solely on intuition about how many runs are enough.

It also fits a run of studies SEJ has covered over the past year, each reporting AI citation numbers as if they were fixed. This one turns around, examines the measurement itself, and asks whether those numbers are stable enough to compare in the first place.

### What This Changes For Your Reporting

The number on your dashboard is just a single sample. Before trusting it, check whether your tracker performs the same check repeatedly and reports a range, or if it pulls data once and shows a clean figure. The clean figure can actually be a warning sign, not reassurance.

A gain after a content change is easy to misinterpret. For example, a three-point increase in your SearchGPT citation share might seem like proof that your effort paid off, but such a change can fall within the natural variability of successive runs, according to the original paper’s data.

To claim the win, measure before and after more than once each. A single before-and-after reading cannot separate your change from ordinary noise.

The platform you are measuring changes how much data you need, and not in the way you would guess. It comes down to how much independent information each answer carries, not how many citations it hands you. Gemini piles citations onto the same handful of sites within a single answer, so many of those citations tell you the same thing. SearchGPT gives fewer citations per answer but spreads them out, so each answer carries more independent information than the raw count suggests. The same number of answers on two engines does not buy the same confidence, and a budget that settles Gemini can leave you guessing on SearchGPT.

Sometimes the honest answer is that you cannot say yet. Three of the 30 tests never cleanly separated their top sites within the budget. For those, the right call is to hold, not to publish a ranking the data cannot support. A tracker that can tell you “not enough data” is worth more than one that prints a confident order every time you ask.

The top of the ranking is the part you can most defend. With enough answers, the leaders pull away from the middle and tail, though even they are not exact. The margins of error widen fast below the front, until neighboring positions are a coin flip, and even the top 10 were not spotless, with the typical margin of error on a top-10 site running about five positions and one in five wider than 10. Trust the leaders, treat the middle and bottom as rough, and do not report exact positions past the front of the list.

### What The Paper Doesn’t Prove

None of this comes from a finished, peer-reviewed study. It is a preprint built on 30 platform-topic tests across three engines, using questions generated by ChatGPT rather than real user searches, over a single stretch of collection. The exact numbers will not transfer cleanly to your topics, so treat them as the shape of the problem, not a lookup table.

Those counts include only answers that carried citations, which matters most on SearchGPT, because a share of its questions return no citations at all. In one topic, 125 questions produced 104 usable answers, a 17% miss, so you would need to submit more questions than those totals suggest.

The check on the method is internal, too. The paper compares a ranking it calls early against that same collection’s final ranking, not against any outside ground truth. That tests whether the stopping rule is consistent with itself, which is why the matching result from the unaffiliated team does real work here. The authors of that April paper, Julius Schulte, Malte Bleeker, and Philipp Kaufmann, are researchers at the University of St. Gallen. They ran a separate dataset and reached the same verdict, that a single reading is unreliable and you have to sample an engine repeatedly to trust what it tells you.

### Where This Goes

The paper stops short of the thing most people will want, which is a way to know your run budget before you start collecting. Sielinski leaves that for later work and notes that the number depends on the shape of each platform’s citation pattern, so a single universal budget probably is not coming.

The bigger change is that AI visibility reporting is headed the way ad and analytics reporting already went, toward numbers that carry a margin of error instead of a false decimal point. That is happening while the basic plumbing is still missing, since Search Console still won’t tell you which clicks came from AI . Until it does, the job falls on you to run the check more than once and report the range, not the single number your dashboard hands you.

### More Resources

- Rank And AI Citation Aren’t The Same Number

- How ChatGPT Actually Picks Sources (I Read The Network Traffic, Not The Outputs)

- 68 Million AI Crawler Visits Show What Drives AI Search Visibility

Featured Image: Stokkete /Shuttertstock

### Reddit Tops Search Results Across All Niches After May Core Update

SE Ranking found Reddit gained top 3 share across all 20 niches after Google's May core update, with smaller moves in YMYL categories.

Matt G. Southern 2.2K Reads

An SE Ranking analysis of 100,000 keywords found Reddit grew its top 3 presence in all 20 niches tracked after the May core update .

For transparency, SE Ranking sells rank-tracking and AI visibility tools, and the data comes from its own keyword-monitoring platform.

Data suggests Reddit grew most in niches where people look for personal experience. Here’s a closer look at the data broken down by category.

### Reddit’s Niche-Level Gains

Reddit’s overall top 3 share rose to 10.24% after May, up from 8.56% after March and 9.19% after December. That’s about one in every ten top 3 spots in their data.

Reddit also took the #1 spot more often. It held the top result for 13,872 keywords after May, up 54% from 8,993 after March.

The biggest gains came in experience-led niches, including:

- Pets: +3.18 points (14.87% → 18.05%)

- Education: +3.03 points (10.46% → 13.49%)

- Sports and Exercise: +3.02 points (9.75% → 12.77%)

- E-Commerce and Retail: +2.61 points (11.50% → 14.11%)

YMYL niches barely moved:

- Healthcare: +0.40 points (0.93% → 1.33%)

- Real Estate: +0.06 points (3.67% → 3.73%)

- News and Politics: +0.78 points (2.75% → 3.53%)

That contrasts with what happened after the March core update, where Amsive found Reddit and similar UGC sites lost US search visibility while brand sites gained.

SE Ranking’s March data showed Reddit’s top 3 share declining from its December level, but moved back the other way in May data.

### YouTube’s Regular Organic Presence Fell

YouTube’s top 3 organic share dropped to 2.14% after May, down from 2.50% after March and 2.40% after December.

Data indicates that YouTube results may be appearing more often in video SERP features and less often in regular organic positions. The analysis covers organic blue links only, so any YouTube presence in video carousels or other features isn’t counted.

Top 3 monopolies, where one domain holds all three top spots for a keyword, dropped to 1.99% of keywords after May, down from 3.24% after March. YouTube is still the domain most likely to hold a monopoly, but its share of those keywords dropped from 15.5% after March to 15.4% after May.

### Volatility & Recovery Data

For overall volatility, SE Ranking found May landed between March and December. After May, 76.03% of top 3 URLs changed position and 88.39% of top 10 URLs changed. Both figures were lower than March but higher than December.

About one in five top 10 pages (19.87%) disappeared from the top 100. That’s lower than the 24.10% that dropped out after March but higher than December’s 14.70%.

Only 32.20% of domains that lost their top 10 positions after March made it back into the top 10 after May. The other 67.80% still haven’t returned. At the same time, 17% of domains currently in the top 10 are new, not showing up in any of SE Ranking’s three snapshots.

### What The Analysis Doesn’t Show

SE Ranking’s data covers organic blue links for 100,000 keywords tracked from one US location (New York). The company has used the same keyword set across three core updates . That makes cross-update comparisons more consistent than a one-off analysis, though other regions or keyword sets could look different.

The figures also don’t capture SERP features, so the real picture is probably bigger than these numbers show, especially for YouTube.

In SE Ranking’s dataset, the “March” comparison combines the March spam update and core update, which rolled out within days of each other. SE Ranking’s data can’t separate which update caused which changes in that window.

### Why This Matters

The niche-level breakdown is what tells the story here. Hearing “Reddit is growing in SERPs” doesn’t register the same if you work in healthcare, where Reddit’s top 3 share went from 0.93% to 1.33%. But it matters a lot if you work in pets, where Reddit now holds 18% of the top 3 positions.

The recovery figures are also telling. Two-thirds of domains that dropped in March didn’t come back in May. For sites still recovering, data shows another core update doesn’t guarantee a rebound.

### Looking Ahead

The comparison after the next core update, whenever that hits, will help us see if the gap between YMYL and experience-led niches stays consistent.

Featured Image: frank333/Shutterstock

### The 2026 State of AI Search: How Modern Brands Stay Visible

New AirOps research identifies the content, authority, and measurement signals that help brands earn more consistent visibility in AI search.

AirOps

### TL;DR

AI search reshaped how people discover and evaluate brands in 2025. Visibility now depends on freshness, off-site credibility, content clarity and how clearly content can be interpreted inside answers—not just how it ranks.

- Brand visibility is in a constant state of fluctuation. Only 30% of brands stay visible from one answer to the next, and just 20% remain present across five consecutive runs.

- Fresh, structured content wins. Pages not updated quarterly are 3× more likely to lose citations. Sequential headings and rich schema correlate with 2.8× higher citation rates.

- Mentions and citations together create stability. Brands earning both signals show 40% higher likelihood of reappearing across answers, but only 28% of answers include brands with dual visibility.

- Credibility is earned off-site. About 48% of citations come from community platforms like Reddit and YouTube, and 85% of brand mentions originate from third-party pages rather than owned domains.

- AIO citations bypass rankings. Roughly 60% of AI Overview citations come from URLs not ranking in the top 20 organic results.

Across millions of datapoints, one message is clear: AI search rewards brands that keep content up-to-date, structured, and supported by strong off-site validation.

The way people discover information has shifted with the rise of the answer-first web. Instead of scanning a list of links, millions now ask AI assistants for direct answers. That changed how categories form, how options are evaluated, and how brands earn visibility in search.

AI search does not behave like a traditional results page. There is no fixed ranking, no predictable position drops, and no stable “page one.” Visibility moves according to signals that update in real time. Brands drift in and out of answers based on freshness, authority, community validation, and how clearly their content can be interpreted as relevant and trustworthy.

Understanding these patterns gives teams an advantage. This report brings together research from AirOps and Kevin Indig to map the signals that mattered most in 2025 and show where brands need to invest to stay visible and competitive.

### Fresh, Up-to-Date Content Drives Visibility in AI Search

AI models prioritize fresh, accurate content when generating answers. Models treat recency as a key signal of trust, especially when users compare options or make decisions. Maintaining fresh, up-to-date content is now non-negotiable for earning visibility in AI search.

#### Pages Not Updated Quarterly Are More Than 3× as Likely to Lose AI Citations

Stale pages fall out of rotation quickly. Once a fresher alternative is available, older content loses ground and rarely regains visibility without a direct update.

- Quarterly updates reduce citation loss: Pages that go more than three months without an update are over 3× more likely to lose visibility compared with recently refreshed pages.

- Annual updates mark the minimum bar: More than 70% of all pages cited by AI have been updated within the past 12 months.

- Six-month updates reflect an accelerating norm: More than 50% of pages earning citations were refreshed within six months.

#### Commercial Search Demands a Higher Bar for Freshness

For buying-intent queries, freshness becomes a necessity, not a negotiable. When users compare options, models prioritize pages that reflect the latest pricing, features, and claims.

- Commercial queries favor recent updates: About 83% of commercial citations come from pages updated within the last year.

- Six months defines competitive freshness: More than 60% of commercial citations surface pages refreshed within six months.

- Fast industries have <3-month windows: In SaaS, finance, and news, pages older than three months see steep drops in citation likelihood.

Freshness shapes visibility across every category, but the expectation tightens as intent becomes more commercial. Pages that stay current remain inside the window models rely on when evaluating trust and relevance, while stale content quickly loses ground to fresher competitors.

##### Where to Start With Refreshing Your Content

- Refresh pages that are losing visibility or showing declining citations, traffic, and conversion.

- Update outdated claims, pricing, features, and examples to reflect up-to-date positioning and messaging.

- Prioritize updates across commercial and comparison pages that influence conversion and high-intent searches.

- Strengthen thin or outdated sections with updates that match evolving user search intent.

Maintaining fresh and up-to-date content provides users and LLMs strong signals of trust and relevance, while improving your brand visibility in both traditional search and AI-generated answers.

### Structured Content Shows Up More Consistently in AI Search

AI models cite pages they can interpret quickly and accurately. Well-structured content with clear headings, rich schema, and organized lists gives AI systems strong relevance cues, making those pages more likely to appear in answers.

#### Sequential Heading Structures Correlate With 2.8× Higher Citation Likelihood

Heading clarity shapes how models understand what a page covers. Pages that follow a clean, sequential hierarchy are cited far more often than pages with fragmented or inconsistent structure.

- Sequential headings correlate with visibility: 68.7% of pages cited in ChatGPT follow logical heading hierarchies.

- Single H1 strengthens structure: 87% of cited pages use a single H1 as the primary anchor.

- Poor hierarchy reduces interpretability: Skipped levels or multiple H1s make it harder for models to understand section relationships.

#### Well-Structured Content Improves User & Model Readability

Well-structured content helps both users and LLMs understand what a page covers. Schema clarifies meaning and intent, while lists make information easier to scan and extract. Pages that combine both show significantly higher citation rates.

- Schema provides strong relevance cues: About 61% of cited pages use three or more schema types, and pages with 3+ schema types have a 13% higher likelihood of being cited.

- FAQ and QA schema improve relevance signals: FAQ schema appears in 10.5% of cited pages, helping search engine indexation and models map answers to queries more directly.

- Ordered and non-ordered lists enhance user and model readability: Nearly 80% of pages cited within ChatGPT include lists to structure key information.

Together, these patterns show that structure is a core retrieval signal. Pages built with clear hierarchy, richer schema, and consistent list organization give LLMs the strongest cues to interpret content accurately and cite it more often.

##### Where to Start With Structuring Your Content

- Use a single H1 and follow a clean, sequential heading hierarchy.

- Add multiple schema types that reflect the page’s purpose and content.

- Break dense sections into short lists and scannable chunks.

- Include FAQ schema when your page answers direct user questions.

These actions help your pages stay clear, scannable, and easier for models to understand. Structured pages give both users and LLMs clearer signals, improving readability and increasing the likelihood that your content is understood and cited.

### Community and User-Generated Channels Have Become the Trust Layer of AI Search

Community and user-generated channels now act as a core trust layer in AI search . Models look to user-generated domains like Reddit, LinkedIn, YouTube, Wikipedia, and other community spaces to understand what people experience, recommend, and question about brands.

#### User-Generated & Community Content Influence 48% of AI Search Results

Instead of relying primarily on brand-owned pages, AI systems often cite UGC domains where people compare options, share outcomes, and validate claims in public.

- Community platforms drive nearly half of citations: About 48% of AI search citations come from user-generated and community sources.

- A concentrated set of UGC domains anchor validation: Reddit, LinkedIn, Wikipedia, YouTube, and arXiv are among the most cited for brand mentions across models.

- Models vary widely in how much they lean on community: Perplexity references community platforms in more than 90% of answers, while Gemini does so in as few as 7%.

#### Reddit Serves as a Signal of Peer Validation During Answer Generation

When people want firsthand comparisons or challenges to claims, models often treat Reddit as a credible reflection of peer insight.

- Appears in roughly 1 in 5 AI answers: Models treat Reddit as a proxy for authentic user experience.

- Shapes early category exploration: About 88% of Reddit citations come from category-level queries.

- Guides deeper brand evaluation: For branded queries, one-third check features, one-third ask how to use something, and one-quarter seek factual detail.

#### YouTube Citations Support Learning and Category Evaluation

LLLMs favor YouTube for its ability to help users understand concepts, processes, and category differences in multimodal contexts.

- A main UGC source across LLMs: YouTube is the #2 most-cited source in Gemini and Perplexity and #3 in Google AI Mode.

- Queries driving visibility to YouTube support educational intent: 75% come from non-branded queries where users want explanations, tutorials, or conceptual clarity.

- Supports category evaluation: For non-branded queries, 59% of citations seek factual detail and 34% focus on how-to guidance.

Community and user-generated platforms now shape how models understand trust, experience, and evaluation across categories. Participate in forums, Q&A platforms, and niche communities where your audience asks questions—engage authentically by answering questions and providing context, not just promoting. A brand’s off-site presence increasingly influences how users discover, learn, and compare options inside AI search.

### Off-Site Presence Influences Early Brand Discovery in Commercial Search

Visibility in AI search is shaped by how the wider web talks about a brand. During early discovery, models lean on third-party pages that define categories, compare options, and reflect consensus—not just what brands publish on their own sites.

#### Brands Are 6.5× More Likely to Be Cited Through Third-Party Sources Than Their Own Domains

For early brand discovery in commercial search, about 85% of brand mentions come from external domains. Brands that invest in a strong off-site presence are 6.5× more likely to earn visibility in AI search than through their owned content.

- Structured formats are a source of credibility: Nearly 90% of third-party mentions originate from listicles, comparison pages, and review roundups.

- Placement inside third-party content matters: Roughly 80% of mentioned brands appear within the first three positions of the page.

- Owned domains appear later in the journey: First-party mentions show up in roughly 25% of generated answers–primarily when users shift from broad exploration to verification.

#### Nofollow and Image Backlinks Correlate as Strongly With AI Visibility as Dofollow Links

AI models treat links and visual references as signals of recognition, making off-site presence more important than link type alone .

- Nofollow links show similar correlation strength: Nofollow links (0.509 Spearman) nearly mirror dofollow links (0.504 Spearman).

- Visual assets expand brand reach: Charts, infographics, and product images generate image-based links that correlate strongly with AI mentions.

- Breadth of recognition matters most: Content cited across many domains appears more often than content with a narrow off-site footprint.

Off-site environments teach models which brands define a category well before they reference owned domains. Brands that invest in both on-site clarity and broad off-site recognition gain stronger visibility in AI search.

### Visibility in AI Search is in Constant Fluctuation

Visibility in AI search shifts continuously as models rebuild answers from scratch. The recurring patterns behind these shifts show how brands cycle in and out of results and which signals help them stay present.

#### Brands That Are Mentioned & Cited Have a 40% Higher Likelihood of Consistent Visibility

LLMs rebuild the answer from scratch each time, reassessing which pages best match the query. That reconstruction drives continual reshuffling, which often contributes to visibility appearing unstable at the single-answer level.

- Dual signals improve recurrence: Brands that earn both a mention and a citation are 40% more likely to resurface across consecutive runs than citation-only brands.

- Most brands disappear between answers: Only 30% of brands stay visible across back-to-back answers, making single snapshots unreliable indicators of performance.

- LLMs rarely cite & mention the brand: Only ~28% of answers include brands that are both mentioned and cited, making dual-signal visibility a high-impact but relatively uncommon pattern.

#### Around 50% of Brands That Lose Visibility Resurface Quickly

Most visibility loss isn’t permanent. Brands rotate in and out as models rebalance for diversity, freshness, and category coverage, and strong signals help them re-enter quickly.

- Disappearance is often temporary : More than 50% of brands that drop from an answer resurface within two runs.

- Short gaps are the norm: Across repeated runs, most brands reappear in results within one to three answers as models diversify their source mix.

- Fast return correlates with stronger signals: Brands that reappear quickly tend to have fresher content, deeper citation presence, and clearer off-site validation compared with those that stay absent longer.

These patterns show that visibility is less about staying present in every answer and more about building signals that help models bring the brand back quickly. Brands should focus on earning both mentions and citations—strengthen on-site clarity through structured content while building off-site validation through community participation and earned media. This dual-signal consistency helps models confidently resurface your brand when rebuilding answers.

### The Impact of Zero-Click Search on User Behavior

AI Overviews changed both user behavior and traffic distribution. Zero-click interactions increased as more answers resolved directly in the Overview, while non-AIO queries continued to drive the most website visits.

#### Google’s Role in Accelerating Zero-Click Search

The rollout of AI Overviews shifted more user behavior into zero-click interactions by making it easier to complete tasks directly inside the results page without visiting a website.

- Zero-click activity rose after AIO launch: Google searches ending without a click, have increased by 2.5x since the initial rollout of AI overviews.

- Google usage shifted toward quicker task completion: From May 2024 to February 2025, US visits to Google increased ~9% while time-on-site and pages-per-visit declined, reflecting faster resolution through AIOs.

- AIO citations are more diverse but far fewer overall: Google surfaces a wider mix of sites in Overviews, yet only about 23% as many URLs appear in AIOs as in traditional results, which concentrates user attention inside the Overview and reinforces zero-click behavior.

#### Page Views From AI Overviews Rose ~22% After Launch

AI Overviews continue to reshape how users engage with search results. AIOs resolve more questions directly on the page, which increases zero-click interactions while still contributing meaningful exposure and early discovery for brands surfaced inside the Overview.

- Most AIO citations come from pages outside traditional rankings: About 59.6% of AI Overview citations come from URLs not ranking in the top 20 organic results.

- AIO-triggering queries are driving stronger engagement: Page views from AI overviews grew 21.5% since the May 2024 rollout, compared with just 1.3% growth for non-AIO searches.

- AIOs prioritize top funnel searches : AIOs appear mostly on informational, top-funnel queries that resolve on the page, while non-AIO queries drive ~2× more traffic by capturing higher-intent users.

These shifts make it clear that AI Overviews influence early understanding, while traditional SERPs remain the primary source in driving higher-intent traffic. Prioritize visibility in both layers: strengthen your presence in AI Overviews to build awareness, while securing traditional SERP positions to capture high-intent traffic downstream.

### The Shifts in Search That Defined 2025

2025 marked a clear turning point in how people search and how brands are surfaced in AI answers. From zero-click behavior to multimodal prompts, new patterns shaped the way categories form and how decisions begin.

Here are several key shifts that took place:

- AI Overviews went mainstream: Google’s launch of AI Mode and expansion of AI-generated overviews increased the share of queries resolved inside the results page, pushing traditional organic links further down.

- Google reinforced E-E-A-T as a core signal: Experience and trustworthiness became stronger retrieval cues across both AI answers and traditional SERPs as Google emphasized human expertise over scaled AI content.

- Models competed on three fronts: Open-source challengers grew fast, frontier models pushed deeper reasoning, and major platforms fought to control the answer layer across search, browsers, and productivity tools.

- Search became conversational and multimodal: AI Mode, Deep Research , and new AI browsers moved users from link-scanning to asking, chatting, and uploading images for instant answers.

- Off-site sources shaped brand visibility: Reddit, YouTube, comparison pages, and reviews guided which brands models considered credible, with citations appearing more directly inside answers.

- Freshness became table stakes: Google continued to roll out core updates that prioritized recent, high-quality content and reduced the visibility of outdated or low-value AI-generated pages.

- Crawling and licensing tightened: LLMs.txt entered the conversation, and major AI data licensing deals plus stricter crawler controls gave publishers more leverage over how AI systems access and use content.

These changes reflect a broader move toward real-time, answer-driven search that blends models, signals, and user behavior in new ways.

### The AI Search Content Playbook

With these trends reshaping user behavior and answer generation, visibility increasingly depends on a specific set of signals that models rely on.

This playbook gives teams a clear guide for strengthening visibility across traditional search and AI answers:

- Refresh content quarterly: Update key pages every three months so models treat your information as current, accurate, and aligned with how people search.

- Keep content well-structured: Maintain sequential heading hierarchies with a single H1, add schema types that clarify page purpose, and make sure each section aligns with the user’s search intent so content is easily understood by both readers and search engines.

- Create unique, authoritative content: Publish original research, proprietary data, and expert explanations that add real value and reflect your brand’s subject-matter expertise. Keep product and feature pages current so your information remains accurate, trustworthy, and easy for search engines and third-party sites to reference.

- Write for clarity and extraction: Lead with direct answers and use concise lists so content is easy for users and models to read, interpret, and reuse.

- Engage in real community conversations: Participate in subreddits, forums, and third-party channels where your users ask questions, share experiences, and provide unfiltered feedback.

- Track visibility patterns over time: Monitor how often your brand appears across models and identify patterns in when you show up, drop out, and return so you can understand how your visibility shifts and where to prioritize improvements.

As AI search reshapes how people discover and compare options, the teams that build upon these habits will be the ones positioned to win in 2026.

Ready to turn visibility into measurable growth? Book a demo to learn how AirOps helps teams manage onsite content, build offsite credibility, and track visibility in AI search with our all-in-one platform.

###### Your Rankings Don't Predict AI Visibility

New data: pages updated in 90 days get cited 3x more. 85% of AI mentions come from third-party sources, not your site.

Read the State of AEO 2026 Report

### A Smarter SEO Content Audit: Aligning For Performance, Purpose & LLM Visibility

Effective content audits prioritize impact, AI visibility, and actionable updates over purely technical metrics.

Corey Morris 4.6K Reads

A major category, focus, or pillar (as I have defined it for decades) of SEO is content. Influencing a range of on-page factors, but more so to develop authentic context and authority status over the years, content has been an engine of so much SEO and is a focal point in the shift from keyword-focused to visibility in the era of LLMs, AI search results, and organic search results in integrated thinking.

With a focus on content needs of today, combined with those from the past few years, a popular way to understand content’s effectiveness is to conduct SEO content audits . As we look at content auditing in a more versatile way for broader visibility, I believe it is important to address the fact that audits often fall into one of two extremes:

- Too shallow to be useful – using an automated tool and lacking data and a point of view.

- Too deep and detailed to be usable – so much data, so much crawling, and so many topics that it’s difficult for search engines and LLMs to understand the actual focus.

With AI and LLMs changing how content is discovered and interacted with, we can’t afford to rest on the content we have created in the past and to assume past performance will provide future positive results. I believe a better model is a performance and purpose-driven audit that prioritizes actions based on business impact and newer visibility models.

SEO content audits, which evolve to stay relevant in today’s search and AI environment, need to account for the fact that search behavior is shifting . I’m not going to unpack the stats or talk about search market share in this article, but trust that you’re seeing the impact in your stats and dashboards. As we shift with the market, we do have to think more about answers and authority signals.

Even if we have a finely tuned content machine that has every possible AI-driven efficiency built into it, we can’t afford wasted efforts and content bloat. Flooding search engines and LLMs with bloat, whether human-generated or AI-generated (or some combo), is wasted if it isn’t working for us. This is especially true for B2B and lead-generation-focused companies that have longer customer journeys and sales cycles.

Marketing and corporate executives expect performance and find out too late that outdated or ineffective content didn’t translate from keyword rankings to AI visibility. Leveraging a content audit that balances having enough depth, but being actionable and focused on business value, is as important as ever.

### How To Conduct A Performance-Driven, LLM-Aware Content Audit

I’m advocating a modern and repeatable framework that replaces traditional SEO content audits with one that is more useful and aligned to how things work today.

#### 1. Define Purpose

We have to start off by getting on the same page with what spurred us to do an audit and what our ultimate goal for the effort is. Whether we’re trying to clean up legacy content overall, to shift focus to LLM visibility that we want to improve, seeking to get more conversions out of existing content, or other noble goals.

It is important to understand what “good” looks like. Whether it is visibility, traffic, authority, engagement, or some other measurable outcome.

#### 2. Segment By Type And Funnel Stage

A challenge of content reviews and analysis is how specific content is prioritized. We want to avoid a one-size-fits-all approach.

That means we need to break down the categories of content for the audit by type. That can include blog posts vs. core landing pages vs. gated assets. However you look and classify the types of content on your site and that your team creates, you’ll want to use this as a filter.

Additionally, you want to look at your content in the same way that you consider your funnel. Whether it is top, middle, and bottom-of-funnel content, or if you look in a different way at customer journeys and classifications, use this as a second important filter and prioritize what you want to analyze and why (going back to the defined purpose of the content audit).

#### 3. Score Content 3P’s (Purpose, Performance, Potential)

This is where our audits and processes start to take a more custom approach based on the steps we’ve completed so far. You’ll need your own custom scoring system. It could be as simple as a 1-3 scale for the categories of Purpose, Performance, and Potential.

##### Purpose:

- What is this content meant to do?

Is it aligned with:

- Brand?

- Positioning?

- Goals?

##### Performance:

How does it drive:

- Traffic?

- Conversions?

- Citations?

- Engagement?

Does it actually:

- Bring people in?

- Move them forward?

##### Potential:

- Could it rank or be rendered in answers in AI with updates?

Could it be:

- Repurposed?

- Repositioned?

As third-party tools continue to add to their data sets and measurement capabilities, you could do your own checks, combining Google Analytics 4, Google Search Console, and ChatGPT to see what content feels useful for LLMs.

#### 4. Determine What Stays

At this juncture, it is time to add a business-focused or aligned lens. Considering content for things like it helps us get found for the right reasons, if it would resonate with our primary audience, and if it would be prominently perceived as expert and authoritative by further stakeholders (current client, journalist, industry colleagues).

For each piece of content that is reviewed within the audit and analysis, arrive at a final decision:

- Remove: With no performance, future, or purpose, this content can be removed.

- Combine: This category is typically for topics that are competing or have cannibalization.

- Update: Whether it is a topic that isn’t optimized, is misaligned in the current iteration, or needs some other type of identified improvement. LLMs prefer sources that are timely, so refreshing content on a regular basis to stay as up-to-date as possible can help improve the longevity of a piece being sourced by AI.

- Keep: This category is for content that needs no change and that you’ll keep as-is currently.

#### 5. Optimize For Search & LLM Visibility

For the content you have determined that stays or gets updated, you’ll want to consider both search and LLMs and what they reward for your content and brand to be found.

For search engines, starting with intent can often help to not get bogged down in old-school thinking about keywords and help with thinking of topics and the opportunity that exists for visibility in organic search results.

For AI, while this article isn’t a primer for what matters for being found in LLMs, there are things like content structure, clear and authoritative answers, brand signals, and external validation (PR, etc.) that are important here, too, in the edits and updates that you make.

#### 6. Create Prioritized Action Plan

While it might feel like, at this point, the heavy lifting is done and that you’ve got a solid spreadsheet, list, or way that you’ve organized the work so far, this is where the follow-through and implementation can get derailed quickly.

You need to work at this juncture to score or plan out what is required for implementation based on effort vs. impact. Additionally, you need to layer in your team’s capacity, skill sets, and cost (or opportunity cost) of resources. Lastly, you need to organize the effort into sprints or milestones to do over time so it doesn’t become a never-ending project or one that is too big to accomplish.

#### 7. Track Business (Not Search) Metrics

As the content audit work wraps up and turns to implementation of the action plan, you need to make sure you’re set up to look beyond rankings and traffic.

Deeper business-aligned metrics include conversions, form submissions, and demo requests as the bridge from online to sales processes. Quality metrics and key performance indicators (KPIs) still apply as you weave in conversion rate optimization (CRO) efforts and mapping to expected aspects of the customer journey or funnel.

And, as you evolve from SEO metrics to visibility, third-party tools or your own qualification and quantification efforts in customizing GA4 or other data capture and analysis work will be important in understanding the impact of your content auditing and update efforts.

### Final Thoughts

Content audits aren’t dead. However, the way we’ve done them in the past likely does need to change. There’s no such thing as a perfect process, tool, or spreadsheet, but we can leverage solid practices that integrate our own goals, potential, and value to our target audiences.

SEO this year and beyond is about visibility, usefulness, and what we can impact across search engines and LLMs.

Remembering that the right audit balances depth with being actionable, the steps I outlined and your team’s dedication and focus can help you see it through to measurable success.

More Resources:

- Create Your Own ChatGPT Agent For On-Page SEO Audits

- Agentic AI In SEO: AI Agents & Workflows For Audit (Part 2)

- Perfectly Optimized Content From Start To Finish

Featured Image: Roman Samborskyi/Shutterstock

### AI SEO: Writing That’s Specific May Get Cited More

AI SEO that prioritizes content that is specific may be a key to getting cited by AI search engines.

Roger Montti 4.5K Reads

Someone posted on social media about their experience writing deep and insightful articles last year and was pleasantly surprised to see that AI was leaning on their articles and even referencing them. Their secret was to choose highly specific topics, which is a good idea.

### SEO And Natural Language AI

SEOs like to write articles based on keywords, and that’s actually how people did it in the relative caveman days of SEO, well over 25 years ago. Natural language processing has come a long way, and LLMs are now able to understand topics and questions in a conversational manner. So it’s truly outdated to proceed with SEO by focusing on keywords.

User behavior and what other sites and people are saying about a site or product are increasingly important. The best way to influence that is with content that’s insightful and gives users what they’re looking for and a lot of it, as often as possible.

### It’s Not Just About Being Insightful

The person who started the discussion pointed out that they chose a “specific enough topic” and wrote something insightful about it. That’s a deceptively simple tip, but it is one of the key points about writing for an audience of humans and machines that interpret content as if they were humans.

Choosing a specific enough topic is about keeping the article focused on a topic and not allowing it to stray. One of the hallmarks of good writing is the willingness to remove the bits that tend to wander off topic. This is an American style of writing, although Europeans as far back as Charles Dickens knew the value of staying on topic so that the effect is a constant stream of interesting sentences that pull a reader all the way to the end of the page.

Writing is an art, like painting and composing music. But you don’t have to have a literature or journalism degree to engage users with text.

### How Someone Got Lots Of Love From Claude AI

Bluesky user @danabra.mov posted about their experience writing an insightful article that subsequently began getting referred to by Claude AI.

He posted :

“If you write an insightful blog post on a specific enough topic, and people link to it, you have a real chance at influencing everyone’s LLM output in a year or so. it’s a bit wild.

I wrote some articles last year that I thought nobody would read because they’re super long. And now I see Claude regurgitating what I wrote in those articles in a perfectly condensed way (and occasionally explicitly referring to the posts). they took away exactly what I wanted the reader to take!

For me it’s a relief because i was worried about falling interest to longform blogs and declining readership. but in a sense maybe it has significantly expanded! It’s just that my reader is now infinitely patient and really wants to hear the entire thing.”

### Others Agree That Being Specific Is Key To Success With AI Citations

The response to Dan’s post was overwhelmingly positive, with one person commenting that it gave them hope.

One person named Tyler shared that they had a similar experience with content they published that was specific.

‪@tylergaw.com‬ responded :

“I’ve seen a couple of mine, not even that insightful, just specific, get pulled into them and used within like 6 months. Wild.”

The person who started the discussion, Dan, agreed :

“I mean yeah but I think being specific by itself is enough…”

### Why Is Being Specific Enough?

Based on my well over forty years of writing experience, including writing poems, short stories, one novel, blog posts, and articles for Search Engine Journal, my opinion on the matter is that focusing on being specific helps to keep a work focused in a way that matches the reader’s focus. The moment the article strays off topic is when the reader loses interest and jumps away.

Being insightful is not enough. Being witty or clever is nice in moderation, but in higher doses it becomes off topic and will, in my opinion, lose the reader. That’s why anyone who writes content must be willing to ruthlessly cut words out to keep it focused and specific (on topic).

### What Google Said About The Topic

Google’s John Mueller reposted Dan’s post with the comment :

“Make more insightful & useful stuff.”

There was one skeptic in the crowd who argued that the economics remove the incentive to put in the work.

They wrote :

“Why on earth would anyone put in the effort required at this point only to have it immediately stolen, receive no compensation and no credit. It’s never been more hostile environment to be a creative. The economics DO NOT WORK.”

Yes, it’s true that today’s environment is hostile to creators because of AI. Yet there is always an opportunity for success by writing about the topics that interest you because they will be sure to be of interest to someone else.

Featured Image by Shutterstock/Nur Alam sabuz

Q3 AI Visibility: AI Citations, Brand Mentions & Content Refreshes That Work

In partnership with

Getting cited by AI is one thing. Staying cited is another, when only about 30% of brands hold their visibility from one answer to the next. This stack shows what earns AI citations and what makes them stick.

This Rundown Answers:

- Why AI visibility is so inconsistent from one answer to the next

- Where AI answers actually pull their citations from

- The data on what gets mentioned and content that loses ground

- A step-by-step way to audit your content for performance, purpose & LLM visibility

By clicking the “Submit” button, I agree to the terms of the Alpha Brand Media content agreement and privacy policy .

Search Engine Journal uses the information you provide to contact you about our relevant content and promotions. Search Engine Journal will share the information you provide with the following sponsors, who will use your information for similar purposes: AirOps. You can unsubscribe from communications from Search Engine Journal at any time.

Unlock this exclusive article stack.

By clicking the “Submit” button, I agree to the terms of the Alpha Brand Media content agreement and privacy policy .

Search Engine Journal uses the information you provide to contact you about our relevant content and promotions. Search Engine Journal will share the information you provide with the following sponsors, who will use your information for similar purposes: AirOps. You can unsubscribe from communications from Search Engine Journal at any time.

## 原文链接

[Read original](https://www.searchenginejournal.com/rundowns/q3-ai-visibility-ai-citations-brand-mentions-content-refreshes-that-work/)
