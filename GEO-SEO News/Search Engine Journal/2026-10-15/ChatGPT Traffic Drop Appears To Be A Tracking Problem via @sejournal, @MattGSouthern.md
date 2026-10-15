---
title: "ChatGPT Traffic Drop Appears To Be A Tracking Problem via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-15T21:48:30+00:00
fetched_at: 2026-10-15T23:43:55.433657+00:00
url: "https://www.searchenginejournal.com/chatgpt-traffic-drop-appears-to-be-a-tracking-problem/593157/"
guid: "https://www.searchenginejournal.com/chatgpt-traffic-drop-appears-to-be-a-tracking-problem/593157/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# ChatGPT Traffic Drop Appears To Be A Tracking Problem via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-15
- URL: https://www.searchenginejournal.com/chatgpt-traffic-drop-appears-to-be-a-tracking-problem/593157/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

ChatGPT-attributed traffic fell sharply in several analytics datasets this month, and analysts tie the drop to ChatGPT links that open without tracking tags. The post ChatGPT Traffic Drop Appears To Be A Tracking Problem appeared first on Search Engine Journal .

## 原文正文

ChatGPT Traffic Drop Appears To Be A Tracking Problem Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- AI Search

## ChatGPT Traffic Drop Appears To Be A Tracking Problem

- ChatGPT-attributed traffic dropped sharply in several datasets after GPT-6 rolled out.

- Analysts tie the drop to inline links arriving without a tracking tag or referrer.

- Some ChatGPT visits may now show up as Direct, making reports harder to compare.

ChatGPT-attributed traffic fell sharply in several analytics datasets this month, and analysts tie the drop to ChatGPT links that open without tracking tags.

The number of ChatGPT-attributed sessions in Google Analytics 4 fell by 22% to 57%, for sites tracked by Graphite with meaningful traffic in the AI Assistant channel, starting Oct. 9, stated Graphite CEO Ethan Smith in his LinkedIn post . Smith estimates this represents an approximate 45% fall from the previous baseline. LLM Pulse reported that, relative to the same days in the last two weeks, sessions from ChatGPT on the sites LLM Pulse has been monitoring were approximately 46% less during Oct. 9–11. Total traffic on those sites remained relatively constant over the same period.

Smith says that ChatGPT started opening links in the answer text without the utm_source=chatgpt.com tag or a referrer, therefore visits from these links can appear as Direct in GA4. There are other analyses suggesting the same change in tracking. However, there is not enough data yet to determine whether there was also some loss of visitation.

### Where The Visits Appear To Be Going

Cedric Huesler, a senior director of product management at Adobe, compared Oct. 9–13 with the week before on about 500 pages where ChatGPT drove at least 5% of visits. He reported on LinkedIn that ChatGPT visits to those pages fell by about 31,000 a day while Direct visits rose by about 26,000 a day. Search traffic fell 7%, in line with search elsewhere.

Direct rose on two of every three pages that lost ChatGPT traffic, compared with about half the week before. Huesler says the new Direct visitors also behave like ChatGPT visitors. On mobile, the share of Direct visitors who saw the consent banner, his sign of a first visit, went from 36% to 44%, moving toward the 55% he sees among ChatGPT visitors. He calls the findings early, based on four days of sampled data.

### What Changed In ChatGPT’s Links

Huesler says that after the GPT-6 rollout, ChatGPT began opening links in a new tab with a browser setting that withholds the referrer, and leaving off the utm_source tag that ChatGPT’s citations carried when its search launched in 2024.

Smith noted that inline links in answer text lost the tag, while links in the Sources panel and shopping links retained it. He also shared that 95% of mobile ChatGPT visits to Graphite’s sites relied on the tag alone, making app traffic the most exposed.

Profound ties the change to a new answer format. Among the ChatGPT answers with citations that it collected, the share with at least one tagged source link fell from about 98% on Oct. 8 to 66% by Oct. 14. Over the same days, Intelligent UI, ChatGPT’s format for charts, comparisons and small tools, went from 2% of all the answers Profound collected to about 35%. Links reached by opening a product or information panel still carried tags.

When I covered the GPT-6 rollout on Oct. 7, OpenAI’s announcement didn’t say how sources would appear in those formats. GPT-6 began rolling out to paid plans that day and to Free and Go users on Oct. 8, and LLM Pulse saw no drop on Oct. 7.

### Rudzki Measured More Direct Links In ChatGPT Answers

Tomek Rudzki at Peec AI ran the same 1 million prompts from October 2 through October 7 and then again from October 9 through October 13. He observed that ChatGPT put a direct URL for a webpage into 42% of the responses compared with a rate of about 8-10% previously; that 54% of these URLs point to home pages, he reports. He says there are also no tags or referrers associated with the links. The figures represent links displayed by ChatGPT but do not represent actual user click-throughs.

### What The Data Doesn’t Settle

The authors of LLM Pulse stated that the team did not observe an increase in site traffic for Direct. They said that Direct is much larger than ChatGPT and as such even an increase in a relatively small number of sessions would be difficult to detect. Additionally they stated that the aggregated data made it impossible to distinguish traffic that was lost from traffic that was no longer labeled as coming from ChatGPT.

Smith called the change a bug on OpenAI’s side and wrote that he expects OpenAI to fix it “very soon.” Huesler now says OpenAI confirmed to him on Oct. 14 that it was a bug. In a follow-up post , he wrote that a fix began rolling out early on Oct. 15 and that by 9 a.m. PT, tagged ChatGPT clicks were back to roughly 95% to 100% of the same hour a week earlier, across thousands of domains he tracks. SEO consultant Glenn Gabe replied that he wasn’t seeing the change yet on paid or free accounts. Profound says it hasn’t seen official word on a fix, and OpenAI’s ChatGPT release notes for Oct. 1 through Oct. 15 don’t mention link tracking.

Graphite, LLM Pulse, Profound and Peec AI sell SEO or AI search services and tools, and Huesler works at Adobe. The LLM Pulse and Profound posts don’t give sample sizes.

### Why This Matters

A 50% or so decline in GA4 referrals from ChatGPT in just one week may be an indicator that you are experiencing changes to how your tracking data is being reported more than a real change in visitor interest. Both Smith and Huesler suggest you annotate the October 8 date in your reporting prior to anyone interpreting it as a loss of traffic, and Huesler now puts the window at Oct. 8–15.

In addition, until further notice, review your ChatGPT and Direct traffic side-by-side for each page ChatGPT referred visitors to, and your homepage, where Rudzki has indicated more than half of the direct links he saw point.

At the time of the introduction of Google Analytics’ AI Assistant channel in May, I stated that if users accessed content via an AI assistant but did not have a referrer, their session would also report as part of the Direct channel. The ChatGPT tag provided a way to capture this additional traffic (especially on mobile). According to Smith, if you set your own UTM parameters within a click from ChatGPT Ads they should be unaffected.

### Looking Ahead

The open question now is how quickly the tags return for every account, since OpenAI hasn’t mentioned the fix in its release notes. Profound notes that restoring them could help with future reports, though it wouldn’t bring back attribution that’s already been lost. Gemini took a different direction two weeks ago, adding UTM parameters to its links, as Roger Montti covered .

Featured Image: Tetiana Yurchenko/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/chatgpt-traffic-drop-appears-to-be-a-tracking-problem/593157/)
