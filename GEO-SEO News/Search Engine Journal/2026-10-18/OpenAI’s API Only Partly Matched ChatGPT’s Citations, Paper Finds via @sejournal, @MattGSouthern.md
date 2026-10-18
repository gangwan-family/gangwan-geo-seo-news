---
title: "OpenAI’s API Only Partly Matched ChatGPT’s Citations, Paper Finds via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-18T08:00:00+00:00
fetched_at: 2026-10-18T23:25:02.799805+00:00
url: "https://www.searchenginejournal.com/openais-api-only-partly-matched-chatgpts-citations-paper-finds/593304/"
guid: "https://www.searchenginejournal.com/openais-api-only-partly-matched-chatgpts-citations-paper-finds/593304/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# OpenAI’s API Only Partly Matched ChatGPT’s Citations, Paper Finds via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-18
- URL: https://www.searchenginejournal.com/openais-api-only-partly-matched-chatgpts-citations-paper-finds/593304/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

A paper tested whether Google results and OpenAI's API can stand in for ChatGPT's citations. They matched cited sites more often than the exact pages. The post OpenAI’s API Only Partly Matched ChatGPT’s Citations, Paper Finds appeared first on Search Engine Journal .

## 原文正文

OpenAI's API Only Partly Matched ChatGPT's Citations, Paper Finds Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- AI Search

## OpenAI’s API Only Partly Matched ChatGPT’s Citations, Paper Finds

- Google results and OpenAI's API missed most of the pages ChatGPT cited in tests.

- The researchers found the stand-ins matched cited sites more often than exact pages.

- The authors suggest tracking by site, rerunning prompts, and re-testing after model changes.

A paper tested whether Google results and OpenAI's API can stand in for ChatGPT's citations. They matched cited sites more often than the exact pages.

Google search results and OpenAI’s Responses API together found 26.2% of the pages ChatGPT cited in a preprint’s tests of the GPT-5.5 Instant setting. They found 48.7% of the sites behind those citations.

Figures in this paper were posted on Oct. 11 by researchers at the National University of Singapore and Xi’an Jiaotong University. It included four versions of ChatGPT, from GPT-5.2 Instant to GPT-5.5 Instant, along with the majority of data collection from March 29 through July 29, 2026. The two stand-ins were able to be queried without having to open ChatGPT; the researchers compared both stand-ins’ results for similarity to the pages cited by ChatGPT’s web app.

### How The Researchers Watched ChatGPT

Researchers recorded the flow of data ChatGPT’s web application received during its writing process, by recording what was happening in their own signed-in sessions. In this data flow you can see the searches ChatGPT performed, which pages resulted from the searches and the pages ChatGPT chose to be sources. A page was counted as cited if ChatGPT selected it as a source; i.e., both pages that are individually listed as their own link and pages in groupings included as a single selection as a source.

There were 80 questions. These 80 questions originated from Search Arena. This is a public database of actual user interactions with search-enabled chatbots/AI models. There were two languages used in these 80 questions: 40 English and 40 Chinese. Four types of requests were made: recommendation, fact lookup, information synthesis and analysis. Each of the 80 questions was run 20 times on GPT-5.3 Instant and GPT-5.5 Instant. GPT-5.2 Instant and GPT-5.4 Thinking had fewer questions run due to being decommissioned prior to completion of data collection.

To create the substitutes, researchers retrieved up to five pages of Google’s organic results per question through SerpAPI for each of the 80 questions. On average they got about 43 results per question. For each question, researchers also sent 20 queries to gpt-5.3-chat-latest and gpt-5.5 via OpenAI’s Responses API, with web search enabled. All of this was done within three days of running ChatGPT for the exact same query. The paper is an arXiv preprint. arXiv does not do peer review of papers.

### Stand-Ins Matched Sites More Often Than Pages

Combined, Google’s results and the API found 28.3% of the pages GPT-5.3 Instant cited and 26.2% of the pages GPT-5.5 Instant cited. In terms of sites, the same combination found 50.3% and 48.7% of all cited sites (with subdomains being treated as different sites). The paper calls a page cited if it has been cited on ChatGPT in at least one run of the 20. The percentages are then the averages across the 80 questions.

The Google search results alone accounted for 9.4% and 6.4% of cited pages, and 26.1% and 22.8% of cited sites. The API’s entire source list accounted for more than that, showing 22.9% and 22.5% of all cited pages. The pages the API cited in its own answers covered less; however, when comparing them to ChatGPT’s citations, we can see that they were a closer match. When looking at averages over the 80 questions, GPT-5.5 Instant also cited 23.3% of the pages the API cited. This is higher than the percentage of API-cited pages that were cited by GPT-5.3 Instant (at 16.4%).

### ChatGPT Rewrote Questions And Changed Sources Between Runs

OpenAI’s help page explains that when ChatGPT search utilizes an external provider, it usually transforms a query into one or more specific search terms. In both GPT-5.3 Instant and GPT-5.5 Instant runs in which searches could be seen, ChatGPT never queried using the exact wording of the original question. However, in GPT-5.2 Instant, it did so in 5.5% of all runs.

Among the runs that included visible searches for questions written in Chinese, GPT-5.3 Instant (67.0%) and GPT-5.5 Instant (69.6%) utilized only the English language. Additionally, in February, I discussed results from Peec AI that found that in its tests, 43% of fan-out queries for non-English prompts ran in English.

Additionally, there was variation in results between individual runs. For example, 44.5% of the distinct pages returned for a given question were shown in only one of the 20 GPT-5.5 Instant runs. Similarly, 40.8% of the distinct pages returned for a given question were shown in only one of the 20 GPT-5.3 Instant runs. The degree of overlap between runs was greater at the level of site than at the level of page. Also, as noted by the authors, while pages that appeared in more of the other runs associated with a particular question had higher likelihoods of being referenced, they noted that this does not indicate that citing is influenced by the frequency of appearance of a given page.

I previously covered the CiteChoice preprint about how rerunning identical inputs flipped 15% of cite-or-not decisions. Here, two collection sessions transitioned to another model after running for 14 and 16 runs respectively, and the authors therefore suggest checking which model generated each response.

### Why This Matters

In the tests described here, neither of OpenAI’s API results nor of Google’s search results showed ChatGPT’s cited pages exactly as they were cited. This would mean that an OpenAI API or Google ranking-based test would find a larger share of the same site(s) than of the same page(s).

The authors’ suggestions for how to monitor are to monitor at both the level of individual webpages and of sites, run the same prompt multiple times, and take into account the fact that ChatGPT rewrites your prompts into its own searches. Check if any comparison of webpage-level results from a tracking tool versus what ChatGPT reports uses data collected through the API or directly through the ChatGPT application. The paper didn’t test any commercial tracking tool.

### Looking Ahead

Every setting in the paper predates GPT-5.6 and GPT-6. OpenAI’s model help page notes that GPT-6 is rolling out in Chat to eligible Plus, Pro, Business, and Enterprise users, while GPT-5.6 Luna is becoming the default for Free and Go users.

Around the GPT-5.5 change in May, Sistrix data showed day-to-day variation in German-language ChatGPT citations jump to 47%, against a normal 1% to 2%. The paper’s authors say monitoring strategies should be re-evaluated when the model behind ChatGPT changes. Until the comparison is repeated on GPT-6, the paper’s figures describe the models that were current from March to July.

Featured Image: Accogliente Design/Shutterstock

OpenAI wordmark: OpenAI.

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/openais-api-only-partly-matched-chatgpts-citations-paper-finds/593304/)
