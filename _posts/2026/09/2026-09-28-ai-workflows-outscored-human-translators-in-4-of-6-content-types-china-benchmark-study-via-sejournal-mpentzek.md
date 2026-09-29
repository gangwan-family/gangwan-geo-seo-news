---
layout: post
title: "AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study via @sejournal, @MPentzek"
date: 2026-09-28T12:00:01+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-28/AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study via @sejournal, @MPentzek.md"
original_url: "https://www.searchenginejournal.com/humans-lost-4-of-6-content-types-in-our-localization-benchmark/589294/"
author: "Marcus Pentzek"
categories:
  - "AI Search"
  - "Content"
  - "International Search"
  - "_src_search-engine-journal"
---

# AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study via @sejournal, @MPentzek

- Source: Search Engine Journal
- Published: 2026-09-28
- URL: https://www.searchenginejournal.com/humans-lost-4-of-6-content-types-in-our-localization-benchmark/589294/
- Author: Marcus Pentzek
- Categories: AI Search, Content, International Search

## RSS 摘要

Stop evaluating "Chinese LLMs" as a category. A 774-output localization benchmark shows why model choice beats post-editing, and what to test yourself. The post AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study appeared first on Search Engine Journal .

## 原文正文

AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study Skip to content

SEJ Pro Sign In

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- International Search

## AI Workflows Outscored Human Translators In 4 Of 6 Content Types – China Benchmark Study

Human translators lost four of six content types to post-edited AI in a 774-output English-to-Chinese benchmark and model choice beat post-editing

We conducted a benchmark study of English-to-Chinese localization, evaluating content types, task types and workflow models to compare human performance against machines.

Professional human translators scored outside the top five on four of six content types. On marketing copy, they finished 10th of 15, 22.2 points behind the best AI workflow. Where humans did win, the margin over the best machine workflow was 2.8 points.

We measured 774 localized outputs across six content types, seven workflow models (human, Chinese LLM*, Chinese LLMPE**, Western LLM*, Western LLMPE**, MT*, MTPE**), and three task types (translation, transcreation, creation). Each output was scored on accuracy and consistency, fluency and language quality, and style and cultural adaptation – each dimension weighted equally at one third of the total. Scoring was performed blind*** by Chinese native-speaking professional localizers.**** This measured localization quality only. No ranking, traffic, or conversion data was collected.

Disclosure: The benchmark discussed here is a joint research project by EC Innovations, a localization services provider, and Jademond Digital, where I am a Partner and Director. Both firms sell services related to the practices this research evaluates.

### Humans Lost 4 Of 6 Content Types

Professional human localization was tested against fourteen machine and hybrid workflows across six content types. It finished first on two of them. On the other four, it finished outside the top five – 7th, 7th, 9th, and 10th out of 15.

Content type

Human score

Human rank

Top workflow

Informational

76.9

1st

Human (76.9)

SEO

74.1

1st

Human (74.1)

Technical

64.8

7th

PE-Qwen (79.6)

Product UI

63.0

7th

PE-Qwen (73.1)

UGC

64.8

9th

PE-Doubao / PE-Qwen (75.9)

Marketing

53.7

10th

PE-Qwen (75.9)

Table 1: Human localization finished first on two content types and outside the top five on four. Ranks are competition ranks out of the 15 workflows tested.

Human professionals won two of six categories and finished 10th of 15 on marketing content, 22.2 points behind post-edited Qwen. PE-Qwen won three categories outright, tied a fourth, and placed second on the remaining two.

This is the actual shape of the finding, and it is more interesting than “humans win SEO.” Human expertise is decisively better at a specific thing: content where factual precision and terminological consistency dominate, and creative latitude is near zero . That describes informational and SEO content. It does not describe marketing copy, UI strings, or social content – and on those, paying professional translation rates buys a worse result.

EC Innovations’ reading of the marketing result is worth repeating:

Human translators appear to over-correct the language, smoothing copy toward formal correctness and stripping out the contemporary register that marketing content depends on. The same instinct that makes a linguist excellent at terminology discipline makes them a poor fit for writing that needs to sound like the internet.

### Nothing Here Demonstrates A Ranking Effect

We measured localization quality. We did not track a single SERP position, and no one should present a 22-point – or a 2.8-point – quality gap as a ranking outcome. The published evidence connecting content quality metrics to ranking is thinner than the industry generally concedes. Portent’s crawl of 756,297 ranking pages found no correlation between readability and Google ranking position ( Portent, 2021 ), and specifically called out the circularity of firms that sell content quality asserting that content quality drives rankings. That criticism lands on research funded by localization companies too. Treat everything in this article as an input hypothesis to test, not a demonstrated ranking effect.

### Where Humans Still Win And By How Little

Humans won two categories. Both wins are narrower than the headline suggests.

Here is the full per-model ranking for SEO content – meta descriptions, headlines, keyword-carrying body copy – from a dataset that has not been published at this granularity:

Rank

Workflow

Score

Human professional

74.1

PE-Doubao

71.3

PE-Qwen

71.3

PE-DeepSeek

66.7

PE-Gemini

66.7

PE-Google MT

66.7

PE-ChatGPT

65.7

Qwen (raw)

65.7

ChatGPT (raw)

62.0

DeepSeek (raw)

61.1

PE-Kimi

61.1

Doubao (raw)

59.3

Gemini (raw)

59.3

Kimi (raw)

56.5

Google MT (raw)

55.6

TABLE 2: How authors, tools, and workflows compete on SEO content. “PE” stands for post-editing by a human professional; “Google MT” is Google Translate. The human lead over the best AI workflow is 2.8 points.

Humans still finish first, but the gap to the best available AI workflow is only 2.8 points and given that each score is an average of three equally weighted dimension ratings, a sub-three-point difference is inside the range where I would not want to make a six-figure sourcing decision without replicating it on my own content.

Post-edited Qwen or Doubao is roughly at parity with professional human localization for SEO content and raw output from any model is not.

There is also a finding here for anyone running legacy infrastructure. Post-edited Google Machine Translation (MT) scored 66.7 on SEO. Ahead of raw Qwen and ahead of every raw model in the study. If you have a mature MT pipeline with translation memory and an established termbase, adding a post-editing layer gets you further than replatforming onto a raw LLM would.

### Why The Category Average Hid All Of This

On SEO content, professional human translation scored 74.1 out of 100. Raw Chinese LLM output and raw Western LLM output both scored an average of 60.7. A 13.4-point gap in favor of humans. That number is as close to meaningless as a procurement input, and understanding why is the most useful thing an SEO can take from this dataset.

“Raw Chinese LLM: 60.7” is a straight average of four models: Qwen, Doubao, DeepSeek, and Kimi. Here is what those four actually scored on SEO content:

Model

SEO Content score

Qwen (raw)

65.7

DeepSeek (raw)

61.1

Doubao (raw)

59.3

Kimi (raw)

56.5

TABLE 3: Chinese LLMs scoring spread on SEO Content – Averaged: 60.7

A 9.2-point spread. And SEO is the tightest category in the study. On technical content, the same four models span 22.3 points, from Qwen at 70.4 to Kimi at 48.1. On marketing, 22.2 points.

Model

SEO Content score

Gemini (raw)

59.3

ChatGPT (raw)

62.0

TABLE 4: Western LLMs scoring spread on SEO Content – Averaged: 60.7

Nobody deploys “Chinese LLM.” They deploy Qwen, or Doubao, or DeepSeek. The category average describes a model that does not exist.

CHART 1: Spread within the “Chinese LLM” category: The category average conceals differences of up to 22.3 points between the models it contains. (Image by author, September 2026)

CHART 2: Spread within the “Western LLM” category: The category average conceals differences of up to 8.4 points between the models it contains. (Image by author, September 2026)

The two categories do not behave the same way. Across all six content types, the widest gap between the two Western models is 8.4 points, on informational content. Among the Chinese four, it reaches 22.3, on technical. If you have standardized on GPT or Gemini, “Western LLM” is a roughly honest description of what you will get. “Chinese LLM” is not a description of anything. It is the average of a field whose best and worst members sit more than twenty points apart, and the model you actually deploy could be at either end.

In the SEO numbers, both categories average 60.7. Identical summary statistic, entirely different distribution behind it.

Gemini leads the raw field on user-generated content at 67.6, the only content type in the study where a Western model finishes ahead of every Chinese one (without post-edit).

The same problem shows up from the other direction. Kimi finished last among the Chinese four in all six content types, and removing it, which is what any enterprise does the moment it runs a two-week bake-off, moves the “Chinese LLM” figure by between 1.3 and 4.9 points depending on the category. The category average is not merely imprecise. it is being dragged by a model most buyers would eliminate in week one.

This is not a criticism of how the study aggregated – equal-weight averaging across a defined model set is the correct way to characterize a category. It is a caution about how the resulting number gets used. If you read “Chinese LLMs score 60.7 on SEO content” and conclude Chinese LLMs are unfit for SEO work, you have drawn a conclusion the underlying data does not support.

### Post-Editing Is Not A Uniform Quality Layer

Post-editing is usually described as a quality layer you either buy or you don’t. The category view shows it is nothing of the sort.

CHART 3: Post-editing lift by model category, per content type. Post-editing almost always improves output, with the exception of marketing content drafted by Western LLMs. The largest improvement is on machine-translated UGC. (Image by author, September 2026)

On user-generated content, a post-editing pass over Google Translate output is worth +30.6 points. On marketing content, the same pass over a Western LLM draft is worth -0.9. The variable is not how much editing you buy. It is whether the draft you hand the editor is close enough to right that editing improves it, or wrong enough that the editor spends the budget fighting it.

That UGC figure – 33.3 raw to 63.9 post-edited – is the largest single movement in the study, and an unsurprising one. Raw machine translation of informal Chinese social copy starts from near-unusable.

The same unevenness holds model by model:

CHART 4: Post-editing lift by base model averaged across all content types. (Image by author, September 2026)

CHART 5: Post-editing lift by base model on Technical content: The same editorial process benefits some models more than others. (Image by author, September 2026)

CHART 6: Post-editing lift by base model on Marketing content: Both ChatGPT and Kimi lose quality after post-editing. (Image by author, September 2026)

More instructive than the averages are the three cases where post-editing made output worse: PE-ChatGPT on marketing (-3.7), PE-Kimi on marketing (-2.8), and PE-ChatGPT on technical (-0.9). On technical content, the spread runs the full width of the same pattern, from PE-ChatGPT at -0.9 to PE-Qwen at +9.3.

Post-editing is not a monotonic improvement. Applied with the wrong register in mind – formalizing marketing copy, or editing technical content without domain knowledge – a human pass destroys value. This is the same over-correction effect visible in the human-only marketing scores.

Which points at the thing I got wrong myself. Model choice matters more than the editing layer, not less. I have seen the opposite argued from the category averages, and I initially read the data that way too. Post-editing lift averages 5.6 points. The spread between the best and worst Chinese model runs up to 22.3 points within a single content type. Choosing Qwen over Kimi is a larger decision than whether you post-edit at all.

### Why Chinese SEO Changes The Calculus

Everything above measures content quality. For Chinese SEO specifically, content quality is rarely the binding constraint.

E-E-A-T is a Google framework and does not transfer cleanly to Baidu, which weights site-level signals – domain history, ICP filing status, and hosting geography – more heavily than page-level language quality. Hosting geography matters partly through latency : a site served from outside the mainland is slower behind the border, and Baidu treats slow sites unfavorably. An ICP filing, and mainland or Hong Kong hosting to go with it, can do more for visibility than the difference between a 60.7 and a 74.1 translation score.

That does not make localization quality irrelevant. It does mean the sequencing matters. If your ICP filing and hosting are not sorted, upgrading from post-edited Qwen to full human translation is an optimization layered on top of a constraint you have not removed – and it is the more expensive of the two fixes.

### What To Actually Do

- Stop evaluating “Chinese LLMs” as a category. Evaluate Qwen against Doubao against DeepSeek on your own content. The within-category spread is larger than the human-versus-AI gap that gets all the attention.

- For flagship SEO and informational content, use human translation or post-edited Qwen or Doubao. The difference between them is small enough that cost and turnaround should decide it.

- For marketing, UI, technical, and social content, stop paying for human translation. The data says you are buying a worse result at a higher price. Post-edited Qwen led all four.

- If you run a mature MT pipeline, add post-editing before you consider replatforming. PE-Google MT at 66.7 on SEO beat every raw model tested.

- Build the termbase. Terminology consistency is where raw model output fails most reliably on SEO content, and a glossary is the cheapest control for it. It also survives every model change you will make in the next two years.

- Tag localized pages by workflow and watch what happens. Within two quarters, your own analytics will answer the ranking question this study could not – on your verticals, your competitive set.

### When This Was Measured, And Why It Matters

A word on timing. The outputs were produced in December 2025 and January 2026. Blind evaluation ran until early March – Chinese New Year sits in the middle of that window and slows everything in China down. Analysis and report preparation took until the end of May, and the study was published on June 5th.

Every model in this study was tested at its December 2025 version, and in this field a months-old snapshot is a historical document. Qwen, Doubao, GPT, and Gemini have all shipped since. The specific ranking above may not survive contact with the current releases.

The durable finding is not “use Qwen.” It is that the differences between individual models, on your specific content type, are large enough to be worth measuring yourself. A benchmark that goes stale in months is an argument for running your own, not for waiting on someone else’s. A two-week internal bake-off across your three or four candidate models, on a representative sample of your own content, will tell you more than any published benchmark, including this one.

Run it. Then run it again in six months.

### What Was Measured:

* The LLM and MT systems tested were GPT-5.2 (via ChatGPT), Gemini 3.0, Doubao 1.6, Qwen 3, Kimi K2, DeepSeek-V3.2, and Google Translate – all accessed through their web interfaces.

** “PE” throughout stands for post-editing by human professionals.

*** Scoring was done by professional Chinese localizers who did not know which text was produced by which workflow. The scorers were different people from those who produced the human and post-edited versions.

**** Test window: localized outputs were produced from December 2025 to January 2026. Blind evaluation ran to early March 2026. Analysis and report preparation continued through May, and the study was published in June 2026. Every model version listed above is the version available in December 2025 and January 2026.

Full methodology and benchmark report . The per-model breakdowns in this article go beyond what the published report contains.

More Resources:

- How AI’s Geo-Identification Failures Are Rewriting International SEO

- APAC Search Strategy Goes Beyond Google & Baidu

- Scaling AI Content Is The #1 Enterprise Priority: How Do You Scale Without Penalty?

Featured Image: Summit Art Creations/Shutterstock

Category Content AI Search International Search

Read Full Bio

Marcus Pentzek

Marcus Pentzek, a seasoned SEO expert specializing in the Chinese market, has been at the forefront of SEO for China ...

## 原文链接

[Read original](https://www.searchenginejournal.com/humans-lost-4-of-6-content-types-in-our-localization-benchmark/589294/)
