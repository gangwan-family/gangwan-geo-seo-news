---
layout: post
title: "Good Vs. Bad pSEO: Learnings From A Decade Of Building Scalable Content Engines via @sejournal, @_nitman"
date: 2026-11-10T15:00:54+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-10/Good Vs. Bad pSEO Learnings From A Decade Of Building Scalable Content Engines via @sejournal, @_nitman.md"
original_url: "https://www.searchenginejournal.com/good-vs-bad-pseo-learnings-from-a-decade-of-building-scalable-content-engines/594204/"
author: "Nitin Manchanda"
categories:
  - "AI Search"
  - "Content Strategy"
  - "SEO Strategy"
  - "_src_search-engine-journal"
---

# Good Vs. Bad pSEO: Learnings From A Decade Of Building Scalable Content Engines via @sejournal, @_nitman

- Source: Search Engine Journal
- Published: 2026-11-10
- URL: https://www.searchenginejournal.com/good-vs-bad-pseo-learnings-from-a-decade-of-building-scalable-content-engines/594204/
- Author: Nitin Manchanda
- Categories: AI Search, Content Strategy, SEO Strategy

## RSS 摘要

Build programmatic SEO pages that earn their place with unique data, clear publishing standards, and pruning rules that keep scale from becoming spam. The post Good Vs. Bad pSEO: Learnings From A Decade Of Building Scalable Content Engines appeared first on Search Engine Journal .

## 原文正文

Good Vs. Bad pSEO: Learnings From A Decade Of Building Scalable Content Engines Skip to content

Ebook: State Of Search 2027

Download The Report

- SEJ

- ⋅

- Content Strategy

## Good Vs. Bad pSEO: Learnings From A Decade Of Building Scalable Content Engines

Build programmatic SEO pages that earn their place with unique data, launch checks, and pruning rules that keep scaled publishing from becoming spam.

Generative AI has removed the barrier to publishing at scale. A brand can produce thousands of pages in an afternoon, and even be bold enough to call it programmatic SEO. For many brands, it worked, bringing in massive search traffic and organic revenue.

Management teams also buy in easily, because time to market is short and production costs are low.

Those same two things are now what make it fail. Aggressive programmatic SEO initiatives like these are collapsing or drawing manual penalties, because no one asks whether these pages deserve to exist.

Google has been clear about this. On March 5, 2024, it strengthened its scaled content abuse policy to apply whether automation, humans, or a combination produces the pages, and later reported 45% less low-quality, unoriginal content in results.

On Sept. 7, 2026, John Mueller replied on Bluesky to a site that generated pages from every combination of domain names, technologies, and attributes. He wrote that programmatic SEO of that kind often leads to a site that’s spam, borderline spam, or low quality, and that pages already published may keep shaping how Google judges the whole site.

Screenshot from Bluesky, November 2026

I have been building programmatic SEO systems since 2016, from static templates to natural language generation engines such as Rosae NLG to AI-assisted pipelines. Some compounded for years and became true case studies for me. Some failed fairly quickly. I have taken that work to conference stages along the way, most recently in a session on scaling pSEO at the Shenzhen SEO Conference .

What we see today is mass AI publishing disguised as programmatic SEO. The real thing starts with a dataset that gives every page something a visitor can use. This article draws the line between the two.

### pSEO Is A Publishing Method, Not A Content Type

Programmatic SEO is a way of publishing, not a kind of content. It has three parts: a repeatable search pattern, a structured dataset that makes each page unique and value-driven, and a template that answers the query for every variation.

Take a currency converter. The pattern is “convert X to Y,” the dataset is a live rate for every currency pair, and the template turns each row into a page. Nobody writes thousands of pages by hand. The data makes each page different. And you publish only as many pages as your data can support.

Lucia Lecesne , the Marketing Lead of Wise, which runs exactly that kind of program, says:

“At Wise, we focus on genuine customer utility: solving a problem that users face on their journey to become customers. Programmatic SEO can then make that solution relevant and accessible across the many search queries and modifiers that share the same problem, in other words, tailoring it to each customer’s specific search context. It should never be a shortcut to publishing large volumes of low-quality pages.”

Mass AI publishing looks the same from the outside, which is why the two get confused. It keeps the template and the publishing system, but what makes each page different comes from a prompt. Swap the city name, and you have a new page with nothing new on it.

Google’s policies draw the same line. The word “programmatic” does not appear in its spam policies . What does appear is scaled content abuse : many pages generated mainly to manipulate rankings rather than help users, no matter how it’s created . Using generative AI to generate many pages without adding value is one of its named examples.

A template isn’t what gets penalized, and neither is automation. The core question worth evaluating is whether each page adds value.

Here is a quick test. Picture two pages for “cost of living in Lisbon,” built from the same template and the same search pattern. The first shows rent ranges, transport passes, and grocery prices pulled from a maintained dataset, and it updates when the numbers change.

The second looks just as complete, with a rent figure, a monthly budget, and a confident summary, but the numbers are the model’s best guess. They carry no source and no date, and the same sentences appear on every other city page with only the name changed. Only the first is programmatic SEO. To tell them apart, ask where each number on the page came from and when it was last updated. The first page can answer. The second can’t.

See also: How Do You Fix Thin Content Across Similar Ecommerce Product Pages? – Ask An SEO

### Good pSEO Vs Bad pSEO

Most teams can’t say whether their pages are programmatic SEO or mass publishing, because the output looks the same from the outside. These six checks look underneath it.

Image from author, November 2026

None of these checks ask whether AI wrote the page. A page built on real data and drafted with AI can still perform well, while a hand-written page with no real data behind it has no more claim to rank. Treat the comparison rubric as a diagnostic: if one of the rows fails, you have a workflow problem to fix. If several parameters fail, then you are mass publishing, whatever you call it.

Eli Schwartz draws the line in the same place, and argues:

“Spinning up pages just because you can isn’t SEO; it’s programmatic spam. If you create pages because they benefit many users, that is good SEO, whether you create them programmatically or manually.”

Danny Sullivan, then Google’s Search Liaison, shared a way to test this at a 2025 event. The question, in his words as Search Engine Journal reported , is whether the intent was “‘I’m going to get that traffic’ and not ‘some user actually expected it'” if they came to your site directly. Ask that of your own pages: would a visitor who arrived straight at your site ever land on this one on purpose?

### From Static Templates To AI Pipelines: What Changed

The pages I built in 2016 and the ones I build today look very similar. Shipping a bad one is the part that got easy. I walked through that early scaling playbook at BrightonSEO in 2022 .

Image from author, November 2026

The middle era is the one I think about most. A rule-based engine like Rosae NLG writes sentences from structured data, and it only says what the data and the template author allow. It was slow to build, and that slowness was doing useful work.

Language models took that limit away. A model will write a fluent, confident paragraph about a row with nothing in it, and a reader cannot tell. I covered where AI belongs in a pSEO pipeline, and where it does not, at ISS Barcelona in 2024 .

So the checks evolved. People do the research and decide each page’s structure, the model drafts the sections from that structure, and a subject matter expert reviews the facts and brand fit before anything goes live.

Language models did not make programmatic SEO better or worse. We used to be stopped by the tools. Now we have to stop ourselves, and the checklist below is how I do it.

### The pSEO Checklist I Use Before Any Page Ships

#### Before The First Page

- Find a unique data source. If you cannot name it, you do not have a pSEO program.

- Define the minimum data completeness for a row to generate a page, and enforce it in code.

- Confirm each template maps to a distinct intent, not a keyword variant.

- Write the metadata rules – titles, descriptions, schema – with the same care as body content.

- Decide your disclosure line: how these pages are built, how often the data refreshes.

- Ask what you can add that nobody else has, such as your own measurements or two datasets combined into a new one.

Image from author, November 2026

#### At Launch

- Ship a test batch of 25-50 pages, not the full set. Publishing 10,000 pages before you know the index rate is the most common failure in this discipline.

- Instrument indexation tests from day one – log-based, not Search Console alone.

- Sample-review by hand. Ten pages read end to end will tell you more than any score.

#### Ongoing

- Track crawl hits per URL by template, monthly.

- Write the kill rule before launch: If a set share of a page set earns no impressions, including in AI features, within a set window, prune or merge it.

- Re-review whenever the template changes – a template edit changes every page at once.

- Prune on a schedule, not after an update. By the time a core update forces it, the site-level trust problem may already be in play.

In my experience, the programs that have survived and thrived across multiple Google updates had a written rule for deleting pages before they needed one.

That is close to how Kevin Indig describes the failure mode in a direct message with me:

“Programmatic SEO usually goes wrong when it is ‘spray and pray: publishing a lot of pages at once with no experimentation, no refreshing, and no look at engagement.’ The fix is the one worth underlining: treat pSEO like its own product, not like a content batch.”

### Building A pSEO Program For AI Search

Search is changing underneath these programs. In the first four months of 2026, 68% of U.S. Google searches ended without a click, according to SparkToro’s analysis of Similarweb data. That’s up from about 60% in 2024 and about 45% in 2016. SparkToro points to AI Overviews , which it says now appear on more than 20% of searches, and Ahrefs estimates they cut clicks on the top result by 58% .

For a programmatic page, that changes the goal. Traffic can’t be the only test of whether a page earns its place, because the click may never come. What stays is influence: Rand Fishkin notes that your content still shapes AI answers and Google’s other zero-click features even as visits fall.

That leaves three habits:

- Build fewer pages, each holding data nobody else has. If an AI answer needs a source for Lisbon’s rent ranges, it can link the page that holds them. It has no reason to link a page that repeats what a dozen other pages already say.

- Decide the query pattern before you build the template. If the searcher only wants one fact, Google will likely give it to them. If they need to compare, calculate, book, or find a local business, your page can still be where they end up. SparkToro says branded, local, and high-intent transactional searches still benefit from SEO.

- Measure by template, not just by site. Search Console’s generative AI performance report shows how often links to your pages appear in AI Overviews and AI Mode . Export the pages, group them by template, and set each group against its clicks in the regular performance report. A template with plenty of AI impressions and few clicks may be earning influence without visits, while one with neither is a candidate for your kill rule.

Dominik Schwarz puts the trade plainly:

“pSEO doesn’t fail because it’s programmatic; it fails when scale replaces substance. The hard part isn’t the tech; it’s the discipline to never trade quality for volume, because pSEO makes that trade tempting for every decision maker.

The test hasn’t changed. If a page’s only value was that it ranked, zero-click search takes away its reason to exist. If the value was the data, an AI answer still has to point to it. Before you scale anything, pick one page and ask where each number on it came from.

More Resources:

- Why Publishing More Content Is Making Your SEO Worse

- You’re Not Scaling Content. You’re Scaling Disappointment

- The Content Framework That Worked In 2019 Is Now Working Against You

Featured Image: RoseRodionova/Shutterstock

Category AI Search Content Strategy SEO Strategy

Read Full Bio

Nitin Manchanda Founder and Chief SEO / AIO Consultant at Botpresso

Nitin Manchanda is a renowned international SEO expert, speaker, and Founder of Botpresso. With over a decade of experience, Nitin ...

## 原文链接

[Read original](https://www.searchenginejournal.com/good-vs-bad-pseo-learnings-from-a-decade-of-building-scalable-content-engines/594204/)
