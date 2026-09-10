---
title: "Everyone Is Quoting The Same Number And Getting Different Answers via @sejournal, @DuaneForrester"
source: "Search Engine Journal"
published: 2026-09-10T19:00:21+00:00
fetched_at: 2026-09-10T23:17:04.219816+00:00
url: "https://www.searchenginejournal.com/everyone-is-quoting-the-same-number-and-getting-different-answers/588659/"
guid: "https://www.searchenginejournal.com/everyone-is-quoting-the-same-number-and-getting-different-answers/588659/"
author: "Duane Forrester"
categories:
  - "AI Search"
  - "SEO"
---

# Everyone Is Quoting The Same Number And Getting Different Answers via @sejournal, @DuaneForrester

- Source: Search Engine Journal
- Published: 2026-09-10
- URL: https://www.searchenginejournal.com/everyone-is-quoting-the-same-number-and-getting-different-answers/588659/
- Author: Duane Forrester
- Categories: AI Search, SEO

## RSS 摘要

Publishers are blocking AI crawlers on a metric whose denominator is missing an unknown share of referrals. The post Everyone Is Quoting The Same Number And Getting Different Answers appeared first on Search Engine Journal .

## 原文正文

Everyone Is Quoting The Same Number And Getting Different Answers Skip to content

- SEJ

- ⋅

- SEO

## Everyone Is Quoting The Same Number And Getting Different Answers

One metric, one publisher, one fully documented method, and figures that differ by a factor of 30. Nobody lied, and that is the part worth understanding.

Anthropic’s crawl-to-refer ratio has been reported as 70,900 to one, 38,000 to one, 23,951 to one, 11,122 to one, 10,300 to one, 4,580 to one, and 2,237 to one. Every one of those figures is attributed to Cloudflare. Every one was published inside about 13 months. Two of them claim the same month and differ by roughly a factor of 17.

If crawl-to-refer is not a number you track, the whole idea fits in a paragraph. Every AI company runs crawlers that fetch pages from your site. Some of those platforms also send you visitors when a person reads an answer and clicks through to the source underneath it. The ratio compares the two. How many pages a platform took, against how many people it sent back. Five to one means it fetched five pages and returned one visitor. Seventy thousand to one means it fetched seventy thousand and returned one.

It exists because the old arrangement broke. A search crawler took your pages and sent you traffic in return, and that trade was the economic basis for publishing anything on the open web . AI systems answer in place, so the taking continued and the sending back largely did not. The ratio is the cleanest single expression of how lopsided that exchange became, which is why it spread quickly, turned up in board decks, and started driving real decisions about which crawlers get through the door .

It is also still growing. Google said at its May developer conference that AI Mode had passed a billion monthly users and that its queries have “more than doubled every quarter since launch,” presented as a story about utility rather than about where those answers stop sending people. Keep that second figure in mind. A doubling every quarter with no base stated is a growth rate you can’t use. That is the same problem this article is about, sitting inside an announcement that sets its scale.

The obvious thought with the imbalance is that somebody was careless or somebody was spinning. That reading is wrong, and it is more comfortable than what happened. Cloudflare published a clear metric, documented the method in full, and disclosed its own limitations in the post that introduced it. The numbers are still scattered across an order of magnitude, because a ratio is a numerator over a denominator, and this one has four denominators stacked inside it that almost nobody carries forward when quoting the figure.

### The Method Is Not Where This Breaks

Last week, I wrote about vendor content citing sources that turned out not to exist . This is the harder version of that same problem, and I want to be clear about the difference up front. Here, every source is real, the publisher is credible, and the documentation is public. The failure happened anyway.

Cloudflare introduced the crawl-to-refer ratio in July 2025 and stated the calculation plainly. Take the total requests from user agents associated with a given platform where the response was HTML. Divide that by the total requests for HTML content where the Referer header contained a hostname associated with that platform. Normalize to a single referral. That is the whole formula, published, unambiguous, and reproducible by anyone with server logs.

They also published the parts that undercut their own metric, which is more than most companies do. What follows is what happens to a well-built number after it leaves the building.

### 4 Denominators Wearing 1 Coat

The first denominator is the window. In Cloudflare’s launch post, the sample period was June 19 to 26, 2025, one week, and Anthropic came out at 70,900 to one while Mistral came out at 0.1 to one, sending 10 referrals for every crawl request. In a separate post the same month , the June 2025 figure for Anthropic is 73,000 to one, with OpenAI at 1,700 to one and Google crawling roughly 14 times per referral. Same publisher, same month, different windows, different numbers. Downstream you now find quarterly figures, monthly figures, rolling 28-day figures, and single-week figures circulating side by side as though they are the same measurement.

How much does the window matter? Cloudflare reported Google’s ratio moving 19.4% week over week, attributing it to a drop in GoogleBot crawling that began on a specific day. A crawl scheduling decision moved the published number by a fifth in seven days. Two analysts choosing different windows in good faith will produce different answers and both will be right.

The second is which bot you counted. Cloudflare states that a platform’s training crawler and its user-request crawler, operating under different user agents, are aggregated under a single platform name for the analysis. Those two behaviors have nothing in common. One consumes at scale and returns nothing by design. The other fetches on demand and can produce a citation. Rolled together, the platform figure describes neither. It also makes the standard comparison against Google structurally unsound, because some operators run purpose-split crawler fleets and others run unified ones, so the aggregate is measuring a different kind of object on each side.

The third is whose sites. Cloudflare sees the traffic that crosses Cloudflare. That is an enormous sample and still a sample, weighted toward the properties that sit behind it. When one analyst measured the same metric against Cloudflare’s network and against their own smaller commercial panel over the same period, one platform’s ratio roughly doubled. Panel composition alone moved it.

### The 4th One Is The One That Matters

The denominator is not referrals. It is referrals that announced themselves.

A referral only enters the calculation if the request carried a Referer header naming the platform. Cloudflare says directly that traffic referred by Claude’s native app does not include that header, that they believe the same is true of other providers’ native apps, and that because referral counts therefore capture only the web-based tools, the calculations may overstate the ratios. Their words on the size of that distortion: It is unclear by how much.

Read that again. The company publishing the metric said, in the post announcing it, that the denominator is missing an unknown quantity of what it is supposed to count, on platforms whose usage is increasingly happening in exactly the place that goes uncounted. That is not a footnote. It is a statement that the metric has an error bar nobody can size, disclosed by the only party positioned to know.

A fifth decision shows how much judgment lives inside a simple formula. Cloudflare excludes referral traffic from Google’s own network, on the grounds that prefetching driven by speculation rules is not a person consuming content. That is defensible. It is also a call, and another analyst could make it differently and produce a different Google figure without either being wrong.

### What Gets Stripped On The Way Down

So the caveats existed, published in plain language by the source at the moment of release. By the time these numbers reach a slide in a quarterly review, none of them are attached.

I am not naming the analyses I pulled those seven figures from. The pattern matters and the publishers do not, and most of them were summarizing in good faith. The mechanism is what is worth describing, because it is not fraud and it is not really error. Each retelling compresses. The first drops the native-app caveat because it complicates the headline. The second drops the window because the number is more quotable without a date range attached. The third reads the second, sees a clean figure with a credible attribution, and repeats it. Four steps from the source, you have a bare integer, a company name, and total confidence.

One of those seven did carry an explicit warning that ratios are tied to a specific window and must never be averaged across periods, and that the numbers were both real and neither universal. That one did the job properly. It sits in the same search results as the ones that did not, looking identical.

### Decisions Are Already Riding On This

This would be an academic complaint if the number were decorative. It is not. Publishers are using crawl-to-refer ratios to decide which AI crawlers to allow and which to block , which is what Cloudflare built the metric to support and a reasonable use of it. Marketing teams are using the same figures to argue AI referral traffic is not worth pursuing. Both decisions are difficult to reverse, because we all know that once a decision is made, it’s all too difficult to bring it up and have it examined again, for a variety of reasons.

Now put the four denominators against that. If a large share of a platform’s referrals arrive through a native app sending no Referer header, the ratio overstates the imbalance by an amount nobody has quantified. If the figure blends a training crawler with a user-request crawler, you may be blocking the one that could have cited you in order to stop the one that never would. If it came from a window where that operator was running a heavy training pass, you are making semi-permanent policy out of a temporary spike.

The spread should make anyone cautious about acting on a single figure. In the same week, one platform measured near 70,900 to one; another measured 0.1 to one, sending 10 referrals for every page it requested. That is not a rounding difference across a category. These ratios describe individual product decisions at individual companies at individual moments, and treating any one of them as a stable property of a platform is a category error.

### What This Actually Asks Of You

The general idea is uncomfortable because it applies well beyond crawler ratios, and it applies to numbers you may currently believe.

A figure without its window, its grouping, and its collection boundary is not a figure. It is a shape that resembles one. Those three things are not caveats attached to the number; they are what builds it, and a number separated from them has not been simplified. It has been made unusable while still looking usable, which is worse than being obviously wrong, because obviously wrong numbers get challenged in the room.

Which gives you a test that costs nothing and disqualifies quickly. When anyone hands you a measurement, ask what period it covers, what got grouped to produce it, and where the collection stopped. Not to be difficult. If those three answers are not immediately available, whoever is holding the number does not know what it means either, and you are both about to decide something on the strength of a shape.

I would extend that to an entire category. We are in a stretch where a lot of companies are shipping measurement products into AI visibility , and I am one of them, so weigh this accordingly. The ones worth your money will tell you their window, their grouping, and their boundary without being asked, the way Cloudflare did. The ones that will not are asking you to trust a number they have not defined. Cloudflare disclosed all three, and the ecosystem still managed to lose them in transmission. A vendor who never discloses them at all is not even giving you something to lose.

The question to carry out of this is not whether a number is accurate. Most of the numbers in this article are accurate (as far as I can determine). It is whether you know what the number counted, and what it could not.

If you have run into a metric in this space that fell apart once you asked what was in the denominator, leave a comment or reach out directly. I would like to see more examples of it, and the specific ones are more useful than the general argument.

More Resources:

- 81.8% Of My ‘AI Assistant’ Traffic Was Fake; The Googlebot Number Was Worse

- How To Track AI Traffic In GA4 Without Undercounting It

- How To Measure AI Search Visibility

This post was originally published on Duane Forrester Decodes .

Featured Image: voronaman/Shutterstock

Category SEO AI Search

Read Full Bio

Duane Forrester Founder and CEO at UnboundAnswers.com

Duane Forrester is the Founder and CEO of UnboundAnswers.com, a consultancy helping businesses adapt to the realities of AI-powered search ...

## 原文链接

[Read original](https://www.searchenginejournal.com/everyone-is-quoting-the-same-number-and-getting-different-answers/588659/)
