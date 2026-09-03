---
layout: post
title: "When AI Has Nothing On Your Company, It Describes Someone Else via @sejournal, @DuaneForrester"
date: 2026-09-03T14:30:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-03/When AI Has Nothing On Your Company, It Describes Someone Else via @sejournal, @DuaneForrester.md"
original_url: "https://www.searchenginejournal.com/when-ai-has-nothing-on-your-company-it-describes-someone-else/587876/"
author: "Duane Forrester"
categories:
  - "AI Search"
  - "SEO"
  - "_src_search-engine-journal"
---

# When AI Has Nothing On Your Company, It Describes Someone Else via @sejournal, @DuaneForrester

- Source: Search Engine Journal
- Published: 2026-09-03
- URL: https://www.searchenginejournal.com/when-ai-has-nothing-on-your-company-it-describes-someone-else/587876/
- Author: Duane Forrester
- Categories: AI Search, SEO

## RSS 摘要

Publishing more content won't fix AI substitution. Retrieval repeats the same popularity bias that thinned your presence in the weights. The post When AI Has Nothing On Your Company, It Describes Someone Else appeared first on Search Engine Journal .

## 原文正文

When AI Has Nothing On Your Company, It Describes Someone Else Skip to content

- SEJ

- ⋅

- AI Search

## When AI Has Nothing On Your Company, It Describes Someone Else

The substitution arrives at full confidence, it happens in a place you do not own, and no content audit you run will ever find it.

When an AI model has nothing on your company, it does not tell anyone. It does not decline, it does not hedge, and it does not mark the spot where its evidence ran out. It reaches for the nearest well-documented thing, which is usually a competitor, a category average, or a version of you from three years ago, and it delivers that substitution in the same confident register it uses when it actually knows.

That much has been discussed. What has not been discussed is the part that should worry anyone running this work: You cannot find this by auditing your own content. Every content audit ever built inspects what exists: pages, structure, coverage, accuracy, freshness. This failure lives in what does not exist, in a place you do not own, and it only becomes visible at the moment somebody asks a question you will never see.

So the audit comes back clean. The pages are fine. The schema validates. The coverage looks reasonable against the competitive set. And the model is still telling people something about your company that no page of yours supports and no page of yours could have prevented.

Image Credit: Duane Forrester

### Why The Model Fills The Gap Instead Of Leaving It

The mechanism is well documented, and I have leaned on Mallen and colleagues enough times in this newsletter that regular readers can skim this part: Models struggle specifically with less popular factual knowledge, and making them bigger mainly improves recall of popular facts while doing very little for the tail. Scale is not coming to rescue the mid-market manufacturer or the regional services firm. The thin part of the distribution stays thin.

What happens in that thin part is the interesting question. Longpre and colleagues, in their EMNLP 2021 work on knowledge conflicts , measured how heavily models lean on memorized information rather than reading what is actually in front of them, and framed the practitioner question as whether a model tends to hallucinate rather than read. The behavior is not abstention. It is confident production from whatever the weights happen to hold.

Separate this from hallucination as the term is normally used, because the industry has flattened the two and the flattening costs you the diagnosis. Generic hallucination is random. It produces a fake case citation , a fabricated statistic, a plausible-sounding paper that does not exist, and it does so unpredictably enough that better models measurably reduce it. What I am describing is not random. It is systematic, directional, and predictable from the shape of the evidence. Given a sparse entity and a dense neighbor, a model will reliably drift toward the neighbor, and it will do so in the same direction every time because the gradient pointing that way is a property of the training distribution rather than a glitch in sampling. That is why the usual reassurance about newer models hallucinating less does not apply here. The models are getting better at not inventing things. They are not getting better at knowing about companies nobody wrote about.

### A Worked Example, Published This June

There is a vendor article circulating right now about AI hallucinating product details, aimed at brand teams, warning them that models invent claims about their products. It is competent writing on a real problem.

It opens its argument with a direct quotation attributed to Percy Liang, named correctly as director of Stanford’s Center for Research on Foundation Models, on how models confabulate in commercial contexts. I cannot find that quotation anywhere else. Not in a paper, not in a talk, not in an interview, not on any other page on the web. The same article carries attributed quotations from two well-known media figures that I also cannot locate. It credits a hallucination rate range to the Stanford HAI AI Index , linking to the report’s front door rather than to any page inside it. Then it does the same thing roughly a dozen more times. A Nielsen consumer trust report. A Gartner risk report. An IAB task force report. An MIT Sloan evaluation study. Every title sounds exactly like a real report. Every link points at an organization’s homepage and never at a document.

Read that again in light of what the piece is about. It is an article warning brands that AI systems invent confident claims about them, and it invents confident claims about researchers and institutions to make the case. The mechanism did not stay in the machine. It came out the other side, got published, got indexed, and is now in the corpus the next generation of models will learn from.

The fair objection is that a lot of that research sits behind a paywall, and a writer without a Gartner or Forrester subscription genuinely cannot deep-link it. That covers some of the list. It does not cover the Stanford index, which is a free public download. It does not cover the ACL Anthology, which is free, open, and fully indexed, and where the taxonomy paper credited with sorting brand hallucinations into four named types does not appear to exist. And it does not cover a quotation, because a person either said something in public or did not, and no subscription changes that. There is also a convention for citing gated work: name the report, the author, and the date, so a reader with access can find it and a reader without can confirm it is real. What is on that page instead is a title that fits the claim perfectly and nothing underneath it.

I am not actually interested in the vendor here, and I am deliberately not naming them, because the specimen matters and the company does not. What matters is that this is exactly the failure operating one level up. Whoever assembled that piece needed authoritative support for claims about brand-level hallucination rates, and authoritative support for those specific claims does not exist in the volume the argument required. So the gap got filled with things shaped like evidence. Real institution names, plausible report titles, a correctly identified Stanford director, working links that resolve to real organizations. Every surface signal of rigor, none of the substance.

And consider the marketing director who reads it, believes the numbers, and repeats them in a board deck. The substitution has moved from a model, to an article, to a person, to a decision, without anyone along the chain doing anything obviously wrong.

### 4 Shapes, 1 Behavior

Substitution does not show up the same way twice, which is part of why it stays invisible. It takes four recognizable forms, and each one usually gets misdiagnosed as something else.

The first is silent analogy , where the model reaches for the nearest well-documented neighbor and describes it as you. Your pricing model becomes your largest competitor’s pricing model. Your implementation timeline becomes the category’s implementation timeline. Nothing in the answer signals that a swap occurred, because from the model’s side no swap occurred. It produced the most probable description of a company like yours .

The second is staleness presented as currency . The model holds a version of your company that was accurate at some point and states it in the present tense. Discontinued products, departed executives, an old positioning statement, a market you exited. There is no timestamp on parametric memory and no expiry warning attached to it.

The third is thin evidence handled with the confidence of thick evidence. One trade write-up and forty independent sources produce answers that read identically. The model does not surface how much material it is standing on, so a claim resting on a single blog post arrives sounding like consensus.

The fourth is category knowledge applied to a specific company. The model knows a great deal about your industry and very little about you, so it answers the industry question and attaches your name to it. This one is the hardest to spot because the answer is usually true about the category, which means it survives a casual accuracy check.

### Why Every One Of Those Clears A Content Audit

Here is the part that matters operationally. A content audit examines your pages against a standard. None of these four failures has anything to do with your pages. The evidence that would have prevented each of them was mostly written by other people, over years, and not by you. No amount of inspecting your own material reveals that shortfall, because the shortfall is not in your material.

The natural response is to publish more. Write the pages, cover the gaps, get retrieved, let retrieval fix what the weights got wrong. That instinct is understandable, and it is weaker than it sounds. Sciavolino and colleagues, in EMNLP 2021 work on entity-centric questions , found that dense retrievers underperform sparse methods badly on entity-rich questions and generalize reliably only to common entities. The same popularity gradient that thins out your presence in the weights reappears in what gets retrieved. Retrieval is a second application of the bias rather than a correction of it, which means the escape hatch most tactical advice is currently selling runs through the same narrow door as everything else.

So the audit is clean, the content is fine, more content is a partial answer at best, and the failure is happening anyway, once per query, in private, at a volume nobody is counting.

### The Only Place This Becomes Visible

You find substitution by watching outputs, not by inspecting inputs. That is the whole shift, and it is uncomfortable, because the diagnostic surface is something you do not own and cannot fully sample.

What you are looking for is specific, and it is not accuracy in the ordinary sense. It is any claim a model makes about your company that no source of yours supports. Not wrong claims, though those count. Claims with no traceable origin in anything published by you or about you. A capability you do not have, described in confident detail. A timeline you never quoted. A competitor comparison drawn on terms you never set. Each of those is a place where the model needed evidence about you, did not have it, and produced something anyway.

How you sample matters more than how much you sample. Asking a model to describe your company by name is the least informative test available, because your name in the prompt is itself a retrieval cue that pulls whatever thin material exists straight into context. The substitutions surface on the questions where your name is absent and has to be supplied by the model. Category questions with a qualifier. Comparison questions naming only your competitor. Questions about a capability rather than a company. Those are the conditions under which a model decides whether you belong in the answer at all, and what to say about you once it decides. That decision is where the neighbor gets borrowed from.

Run that across a real spread of the questions your buyers actually ask , repeatedly, because the substitutions move. Then treat the results as a map of where third-party description is missing rather than a list of pages to fix, because that is what it is. I will say plainly that I run a company in the measurement side of this, so I’m vested in all of this and see things from a unique perspective. It does not change the underlying point, which is that a discipline built entirely around auditing what you own is structurally blind to a failure that happens entirely outside what you own.

The uncomfortable version: the cleanest content audit you have ever run tells you nothing about this, and it never did.

If you have caught a model saying something about your company that traced back to nothing you could find, I would like to hear about it. Leave a comment with what it said and how you noticed, or reach out directly. The examples are more useful than the theory here, and there is no good public collection of them yet.

I go further into how these systems build and hold their picture of a company in The Machine Layer , available here .

More Resources:

- AI Search Runs On Two Memory Systems. The Platforms Don’t Use Them The Same Way

- Why AI Recommends Your Competitor & What To Do About It

- How To Measure AI Search Visibility

This post was originally published on Duane Forrester Decodes .

Featured Image: fizkes/Shutterstock; Paulo Bobita/Search Engine Journal

Category SEO AI Search

Read Full Bio

Duane Forrester Founder and CEO at UnboundAnswers.com

Duane Forrester is the Founder and CEO of UnboundAnswers.com, a consultancy helping businesses adapt to the realities of AI-powered search ...

## 原文链接

[Read original](https://www.searchenginejournal.com/when-ai-has-nothing-on-your-company-it-describes-someone-else/587876/)
