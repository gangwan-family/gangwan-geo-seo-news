---
title: "I Tested DeepSeek’s New Search Api, Here’s How It Ranks And Scores Websites via @sejournal, @suganthan"
source: "Search Engine Journal"
published: 2026-10-20T14:00:13+00:00
fetched_at: 2026-10-20T23:59:08.859444+00:00
url: "https://www.searchenginejournal.com/i-tested-deepseeks-new-search-api-heres-how-it-ranks-and-scores-websites/593408/"
guid: "https://www.searchenginejournal.com/i-tested-deepseeks-new-search-api-heres-how-it-ranks-and-scores-websites/593408/"
author: "Suganthan Mohanadasan"
categories:
  - "SEO"
---

# I Tested DeepSeek’s New Search Api, Here’s How It Ranks And Scores Websites via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-10-20
- URL: https://www.searchenginejournal.com/i-tested-deepseeks-new-search-api-heres-how-it-ranks-and-scores-websites/593408/
- Author: Suganthan Mohanadasan
- Categories: SEO

## RSS 摘要

DeepSeek’s date filters dropped every undated page, 11% of results. Six practical checks for SEOs testing the new Search API, from localization to logs. The post I Tested DeepSeek’s New Search Api, Here’s How It Ranks And Scores Websites appeared first on Search Engine Journal .

## 原文正文

I Tested DeepSeek’s New Search Api, Here’s How It Ranks And Scores Websites Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- SEO

## I Tested DeepSeek’s New Search Api, Here’s How It Ranks And Scores Websites

DeepSeek opened its search API with authority scores and a promise to filter SEO and GEO spam. I spent $0.08 testing what it actually returns.

DeepSeek has opened access to its own search engine through a public Search and Fetch API. It returns an authority score for every result and says it filters out SEO spam, GEO manipulation , and low-quality AI content.

That is a significant release for SEOs.

The announcement on Oct. 17, 2026 came alongside an update to its Flash model. DeepSeek says the search engine already powers search on its website and through its API, indexes hundreds of billions of pages and handles hundreds of millions of searches a day.

Screenshot from X , October 2026

We can now query that system directly, inspect the sources it returns, and see some of the scores attached to them. That gives us something concrete to investigate before an AI model turns those sources into an answer.

Naturally, I wanted to see what it thought of my site. And whether the spam filtering held up.

I spent $0.08 finding out.

My site came back with an authority score of 1. Spam PDFs on government and university hosts came back with authority 4. The Fetch API also presented itself as Firefox from Hong Kong and returned content from URLs disallowed by robots.txt .

These are my preliminary findings.

### What I Tested

I ran 110 calls on Oct. 17, 2026 from Dubai: 93 Search calls and 17 Fetch calls . Around 103 were billable under the documentation’s billing rule, costing approximately $0.08.

The tests covered score distributions, authority across different hosts, six queries related to my own tools and research, localization, date filters, and fetch behavior.

I used the Search and Fetch documentation as the reference. Where the responses differed from the documentation, I’ve kept the observed results clear.

### DeepSeek Gives You 2 Scores

Each search result includes two fields worth paying attention to:

Field

What DeepSeek says it means

authority

An authority tier from 0 to 4, with -1 meaning unknown. Values of 3 or above indicate highly authoritative sources.

rerank_score

A score from 0 to 3 combining signals such as relevance, authority, and freshness. Scores of 1.5 or above are considered high quality.

These definitions come from the Search API reference . The authority tier is DeepSeek’s own assessment, and the documentation describes it as a property of the page.

Across 20 SEO and GEO queries at count=50 , I collected 1,000 results . Their rerank scores ranged from 0.75 to 2.70 , with a median of 1.63 . Results were consistently sorted by that score, and 68% scored 1.5 or above .

Only 196 distinct scores appeared across those 1,000 results. The returned values looked bucketed, although that alone doesn’t tell us whether the underlying scores are rounded or calculated in fixed steps.

### Authority Looked Tied To The Host. Mine Was 1

Across all 4,322 results in the run, authority tiers -1 and 0 never appeared. The distribution looked like this:

Authority

Share of results

Median rerank score

0.95

32%

1.45

60%

1.83

1.98

Higher authority tiers came with higher median rerank scores in this sample. That doesn’t isolate the effect of authority from the other ranking signals, but it makes the field worth investigating.

I then ran 16 site: probes across 16 hosts . On every host, every returned URL had the same authority score. Here are some examples:

Host

Authority

suganthan.com

growth-memo.com

ipullrank.com, brodieclark.com, medium.com, reddit.com

ahrefs.com, moz.com, searchengineland.com, aleydasolis.com, linkedin.com

zenodo.org

So although the documentation calls this a page authority tier, it behaved like a host score in my tests.

The Reddit subdomains were especially useful here: qh.reddit.com scored 1, while www.reddit.com scored 2 . That points towards the host being the relevant unit, rather than the entire registrable domain sharing one score.

A search for site:suganthan.com filled the 50 result cap . It returned my homepage, /resources/ , notes and blog posts. DeepSeek was finding content across my site. Those pages all carried authority 1.

Being indexed was clearly only part of the story.

Image Credit: Suganthan Mohanadasan

### I Lost My Own Tool Queries To Registries And App Stores (Lol)

I ran six target queries with count=50 from the UAE.

Query

My best result

Who appeared at the top

Find out who Gemini cites for your query

#48 for my Gemini citations article , rerank 1.14

Apify actors, Chrome Web Store

ChatGPT fan-out queries Chrome extension

#32 for FanoutFox , rerank 1.37. Outside the top 50 with UK or US localization.

Chrome Web Store ×3, Writesonic, Resoneo

Track Google AI Mode traffic in Search Console

Outside the top 50

support.google.com, developers.google.cn, SEJ, Bounteous

AI crawler access checker

Outside the top 50

wordpress.org plugins, PyPI, Apify

Google Search Console MCP

Outside the top 50

PyPI ×3, n8n, mcpworld

x402 pay per crawl AI agents

Outside the top 50

Akamai, npm, pkg.go.dev

Package registries, app stores, and marketplace listings did well on these tool queries. PyPI, npm, Apify, the Chrome Web Store, WordPress.org, and GitHub were the kinds of hosts surfacing.

My Gemini article and FanoutFox both had authority 1. Their rerank scores of 1.14 and 1.37 also fell below DeepSeek’s documented 1.5 high-quality threshold.

For my site, having content directly about the thing being searched for wasn’t enough to beat those hosts. The low authority tier is a plausible part of the explanation, although these tests don’t tell us its exact weighting.

Image Credit: Suganthan Mohanadasan

### The Spam Filtering Still Let Some Questionable Stuff Through

DeepSeek explicitly says its engine filters SEO spam, GEO manipulation, and low quality AI content. I wanted to see how that claim lined up with the results.

Here is what still appeared:

Host

What I found

Scores and rankings

oig.dc.gov

Webform PDFs titled “Free Robux Generator in 2025” on a US government inspector general’s host

Authority 4, rerank 1.42

business.columbia.edu

Webform uploads titled “BEST CBD GUMMIES EXPOSED: The ‘Forbidden’ Gummy…”

Authority 4, rerank 1.50

damiangreen.co.uk

A former MP’s domain serving “Minimum Deposit Casinos UK”

Authority 3, ranked #2 for “best casino sites uk”

I also saw self-published “frameworks” on zenodo.org receive authority four and rank #one and #three for “generative engine optimization.” That is another observation about how authority behaved. Self-publication alone doesn’t make a page spam.

The government and university examples are hard to square with the promise of filtering this stuff out. Those uploads still received the highest authority tier.

This is why the apparent use of a host score matters. A system that carries a host’s authority across its pages can end up giving parasite content the same treatment as legitimate material on that host.

The results don’t tell us how much spam DeepSeek removed. They do show that these examples got through, and that a high authority tier wasn’t a reliable judgement of the individual page’s quality.

Image Credit: Suganthan Mohanadasan

### How To Run The Same Kind Of Search

Here is a request using an API key stored in an environment variable:

curl -s https://api.deepseek.com/v1/tools/search -H "Authorization: Bearer $DEEPSEEK_API_KEY" -H "Content-Type: application/json" -d '{"query":"find out who Gemini cites for your query","count":50}'

A trimmed result from that query:

{ "url": "https://suganthan.com/blog/gemini-citations/", "rerank_score": 1.14, "authority": 1 }

Search and Fetch each cost $0.75 per 1,000 successful requests . Under the billing rules , failed requests, empty search results, and timeouts are not billed. Returning 50 results costs the same as returning fewer.

There is a separate temporary exemption for the server-side Search and Fetch calls already made when using the DeepSeek API through Claude Code or Codex. Those remain free until one November 2026 at 00:00 Beijing time , which is 31 October at 8:00 PM GST . Per request, billing starts then. My direct API tests were billable.

### 3 Things To Account For When Testing

#### 1. Set Your Localization

Leaving out localization produced the same results as specifying a UAE IP across all six target queries. I was calling from Dubai, which is consistent with DeepSeek using the caller’s IP as the default.

Set this field explicitly to an IP address in the market you want to test. Otherwise, your audit may reflect wherever the script happens to run.

Using a UK or U.S. IP changed the rerank scores of 26 to 41 of the 50 results and swapped 4 to 15 URLs . The mean score delta was small, around ±0.05 . It mostly reshuffled the results, without substantially changing the score scale.

A Chinese IP, 114.114.114.114 , behaved similarly to the UK and US settings. I didn’t see a clearly separate Chinese result set in these tests, although this doesn’t establish how DeepSeek organizes its indexes.

#### 2. The Original Question Made Very Little Difference

The ori_question field lets you supply the user’s original question alongside the search query. DeepSeek says this can improve query understanding.

Across my six queries, it changed the rerank score for only zero to two of the 50 results and swapped at most one URL .

#### 3. Date Filters Removed Every Undated Result

The after: and before: operators produced zero date violations across four queries .

They also removed every undated page. 11% of the unfiltered results had date: null , and those URLs disappeared when a date filter was applied.

That matters if your content needs to appear in searches for recent information. Put an appropriate machine-readable date on the page, then check that DeepSeek actually recognizes it. A page it treats as undated can disappear from a date-filtered search.

Every returned date that was present ended in T16:00:00Z , which corresponds to midnight Beijing time. The filtering behavior pointed to Beijing calendar days in these tests.

I also found two differences between the documented and observed text lengths:

Field

Documented typical length

Observed median

snippet

100 to 200 characters

301 characters

summary

600 to 800 characters

About 3,570 characters

That is worth knowing if you are building a tool around these responses. The summaries I received were considerably longer than the documentation suggested.

### The Fetch API Arrived As Firefox From Hong Kong

The Fetch requests I inspected did not identify themselves as DeepSeek. They used this user agent :

Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0

The Accept-Language header was:

zh-CN,zh;q=0.9

There was no From header, bot token, Signature or Signature-Input . The requests presented themselves as Firefox, with no DeepSeek identifier to match in the user agent.

Five fetches came from five different IPs , all identified as AS136907, Huawei Cloud, Hong Kong :

121.91.172.54 183.87.40.160 119.8.239.43 27.106.106.73 159.138.131.203

In the rendering test, it loaded CSS. It did not run JavaScript, load images, or fire the XHR beacon. Content that required JavaScript did not appear in those fetches.

These observations concern the Fetch API. They don’t establish how the crawler that builds DeepSeek’s search index behaves.

#### It Returned Content From URLs Disallowed By Robots.Txt

The Fetch API returned full content from three URLs disallowed for User-agent: * :

- httpbin.org/deny

- Wikipedia’s Special:Search

- google.com/search

I could not confirm whether it ever requested /robots.txt . What I could confirm was that the disallowed URLs still returned content through the API. Those rules did not prevent the fetches I tested.

Image Credit: Suganthan Mohanadasan

#### What To Look For In Your Logs

If your access logs record Accept-Language , this will help surface requests matching the observed headers:

grep -E 'Firefox/149.0' access.log | grep 'zh-CN'

A more specific filter combines the Firefox version, language header, and ASN. A Cloudflare custom rule in that shape would be:

(ip.src.asnum eq 136907 and http.user_agent contains "Firefox/149.0" and any(http.request.headers["accept-language"][*] contains "zh-CN"))

Treat that combination as a fingerprint to investigate. It is based on what I observed in these requests and could change.

There is no DeepSeek-specific user agent here, and blocking the Firefox string alone can catch legitimate browsers. AS136907 is also a general Huawei Cloud network. Blocking the whole ASN can affect other tenants, so don’t assume every request from it belongs to DeepSeek.

### What I Would Do With This As An SEO/GEO/AEO/AI SEO

The useful part of this release is that we can inspect the search results and scoring directly.

Here is where I would start:

- Run your actual target queries against POST https://api.deepseek.com/v1/tools/search . Record rank, rerank score, and authority together.

- Check your site’s authority tier with site:yourdomain.com , including any relevant subdomains.

- Set localization explicitly so repeated tests represent the market you care about.

- Check your dates. Add appropriate machine-readable dates and verify whether DeepSeek returns them. Compare results with and without date filters.

- Test relevant distribution for your tools. PyPI, npm, Apify, the Chrome Web Store, WordPress.org, and GitHub performed well in these queries. If your tool belongs on one of those platforms, a legitimate listing is worth testing alongside your own site.

- Monitor the fetcher in your logs using the combined Firefox/149, zh-CN and AS136907 pattern, while checking matches before treating them as DeepSeek.

For me, the most interesting finding is the combination of visible authority tiers, weak rankings for some original tool content, and obvious spam receiving the highest authority tier. It gives us specific questions we can now test.

This was one day, 110 calls, six target queries, and one calling region , with additional probes for scores, hosts, filters, and fetching. I still couldn’t confirm whether the fetcher requested robots.txt. Treat the numbers as directional, please.

More Resources:

- How ChatGPT Actually Picks Sources (I Read The Network Traffic, Not The Outputs)

- The Technical Signals AI Search Uses That Most SEOs Still Aren’t Optimizing

- Checking A Page Is Part Of A Retrieval Pipeline For AI

This post was originally published on Suganthan .

Featured Image: Fahmi_Ruddin_Hidayat/Shutterstock

Category SEO

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

Suganthan Mohanadasan is the co-founder of Snippet Digital, an AI SEO agency, and Keyword Insights, an AI content intelligence platform. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/i-tested-deepseeks-new-search-api-heres-how-it-ranks-and-scores-websites/593408/)
