---
layout: post
title: "Google Gets The Thank-You via @sejournal, @pedrodias"
date: 2026-10-26T14:00:54+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-26/Google Gets The Thank-You via @sejournal, @pedrodias.md"
original_url: "https://www.searchenginejournal.com/google-gets-the-thank-you/594108/"
author: "Pedro Dias"
categories:
  - "Ecommerce"
  - "SEO"
  - "_src_search-engine-journal"
---

# Google Gets The Thank-You via @sejournal, @pedrodias

- Source: Search Engine Journal
- Published: 2026-10-26
- URL: https://www.searchenginejournal.com/google-gets-the-thank-you/594108/
- Author: Pedro Dias
- Categories: Ecommerce, SEO

## RSS 摘要

Referral reports show who sent the visit, not who shaped the decision. Why GEO’s real job is what a model learns, not what it retrieves. The post Google Gets The Thank-You appeared first on Search Engine Journal .

## 原文正文

Google Gets The Thank-You Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- SEO

## Google Gets The Thank-You

A buyer can arrive through Google after making the important part of the decision somewhere else.

Imagine a buyer asks an AI assistant which supplier fits a particular problem. Your business makes the shortlist. The buyer discusses the alternatives, checks a concern, then opens Google and searches for your company.

They visit and buy. Depending on the attribution setup , Google may receive the credit. The assistant need never have sent a visit at all.

What happened before the visit we managed to record?

In GEO is a distraction , Marie Haynes reports that ChatGPT sessions amounted to 0.62% of Google organic sessions across her sample of 100 sites. Her conversion analysis also favours Google on total volume. Those are useful observations about the properties she examined. I haven’t inspected the underlying GA4 data.

Marie also recognizes the prospect of transactions happening without a site visit and argues for preparing for agentic commerce. I share her concern about chasing mentions or treating weak evidence as the basis for a new discipline. Where I disagree is how far referral figures can take us in judging the broader effort to influence how AI represents a business.

A report about arrivals cannot, by itself, settle what influenced the people arriving.

### The Visit Happens After The Question

Around me, I see people increasingly asking an assistant first and using Search afterwards. That’s an observation about the people I encounter, rather than evidence that everyone behaves this way.

It does make me question what a Google visit means. Someone searching for a company could be starting their investigation. They could also be following a recommendation or checking a shortlist made during an earlier conversation.

A buyer might use an assistant to understand a problem before they even know which category of product they need. The assistant could introduce a company, or describe an alternative so poorly that the buyer rules it out. In either case, the answer could influence the decision without sending the buyer to a website.

That gives us a reason to investigate. It doesn’t tell us how often this happens or how much business it creates.

I’m also wary of treating difficult attribution as evidence that a large amount of invisible value must exist. The gap leaves us with a question about what happened before the visit. It doesn’t give us a revenue estimate, however plausible the journey sounds. I’d want to see that evidence before putting a revenue number in the proposal.

### What The Model Learned, And What It Looked Up

I’ve been skeptical of using new initialisms for work SEO already covered. When someone asks what GEO does that SEO doesn’t , I think that’s a fair question. If we’re going to use a separate name, I want to know what work I couldn’t already describe as SEO.

The distinction that makes GEO useful to me is parametric memory : the knowledge and associations a model has learned through training , represented in its numerical weights. Influencing what it learns about a brand, and how it can use that knowledge in relevant searches and answers, is the separate job I mean by GEO.

Retrieval supplies external information while the system is answering. In retrieval-augmented generation , or RAG, the model uses retrieved material alongside what it has already learned. The original RAG paper explicitly combines the two.

Imagine asking a specialist colleague for advice. They bring what they’ve already learned, and they can open a reference folder to check something they need for your question. Changing the folder changes the information available for that consultation. Changing what the colleague has learned involves a different process.

A model’s weights don’t work like a person’s memory, and its answer doesn’t neatly identify which contribution came from which source.

SEO addresses the web discovery and retrieval work: making relevant sources discoverable, accessible and suitable for the question. A page being available, being retrieved and contributing to an answer are separate outcomes. SEO doesn’t own the entire answering system.

For Google’s AI search features, Google itself says established SEO practices remain relevant and no special optimization is required . Calling familiar SEO work GEO gives it a new label. I’d still like to know what changed in the work.

My working shorthand is AI visibility = SEO + GEO : information available through retrieval, alongside associations already learned. Instructions and user context also matter, so the shorthand doesn’t describe everything that shapes an assistant’s response.

A page could be retrieved today and become candidate training material later. Separating the two routes helps explain how the information reaches the answer, even when the same page might eventually contribute through both.

### Memory Can Shape The Search

When a language model generates search queries, its learned associations may influence where the search starts. Google describes query fan-out as issuing related searches across subtopics and data sources.

There is relevant evidence in What Drives AI Citations? . Researchers compared brands recommended without search with brands included in the system’s generated queries. In the OpenAI API configuration they tested, brands recommended without search appeared in queries in 67% of cases, against 11% otherwise.

Asking without search tells us what the model recommends under those conditions, rather than revealing everything it knows. The comparison is useful, though it leaves open whether changing the training would change the searches. That would need a different experiment.

For me, this adds another reason to care about parametric memory. An association between a brand and a buyer’s problem could give that brand a head start in the searches used to investigate the problem. Memory could therefore affect which evidence gets a chance to reach the answer.

The same study observed the system picking up niche-vendor names from an initial round of search results. A category search can introduce an unfamiliar brand, and a user can supply a name the model didn’t previously know. Instructions and retrieved information can also shape subsequent searches.

My interest is in testing whether learned associations change the searches a system makes. What a model recalls may affect the question it sends to Search, before any resulting visit appears in analytics.

### You Can Study The Learning

The Outlandish paper shows one way training can change associations.

Researchers inserted texts into controlled training runs. Learning an association could raise a keyword’s probability in other contexts, especially within the same theme. They call that spillover priming . Putting the text in a prompt produced substantially less of this effect than training on it.

A keyword appearing in an irrelevant answer could make the answer worse. I’d want to read the answer before celebrating the extra mention.

Repetition raises a different question. It can improve a model’s ability to reproduce a passage from its training data . That is a form of learning, but successful recitation doesn’t establish that the model can use the facts when asked a different question. In controlled biography experiments , researchers trained smaller models from scratch and found that changing how the same facts were presented during training improved factual answering.

That gives us something we can study. With open-weight models, whose learned parameters are publicly available, you can download a model and run controlled experiments. Where training code and data are available too, you can change the material, compare versions, and test what the model does differently. Research resources such as Pythia provide models saved at different stages of training, alongside code and data.

A well-controlled comparison can establish an effect within the experiment’s conditions without revealing its entire mechanism. What we test depends on what we want to establish: improved factual answers and different generated searches are distinct outcomes. When testing learned associations, we also need to control the information supplied through retrieval or the conversation.

In those experiments, the researchers control training. A business publishing pages doesn’t control whether a provider includes those pages in training or what the model learns from them. Seeing a page published, crawled, or cited therefore doesn’t establish that the model has learned something useful from it. An uncited reply alone wouldn’t establish a change in weights either.

My interest is commercial too. I work at geoSurge, which has been doing this kind of research for a couple of years now. That experience is part of why I take the possibility of influencing learned associations seriously.

We can’t assume that findings from open-weight models carry over to the closed models that OpenAI, Anthropic or Google use in production. The experiments give us evidence about the models and conditions tested. Whether those findings hold in a particular production system needs separate evidence.

The outcomes are statistical. I want to know how often a result holds across the questions and conditions tested, and how large the change is. A useful improvement needn’t mean every future answer will go our way. I’d want evidence across those conditions before drawing a conclusion, rather than relying on a few responses that happened to look encouraging.

I’ve made this distinction before : counting an appearance and explaining it require different evidence. These studies give me reasons to investigate how facts are taught, beyond counting copies. They don’t establish a publishing recipe for brand recommendations; whether an approach produces a useful result for a business still needs commercial validation. Putting the paper on a sales slide doesn’t perform that study for you.

### When The Content Is The Product

Nati Elimelech recently posted publicly on LinkedIn about the economics of running a recipe site. Their Search traffic was rising after a successful refactor. They were questioning the business model even while the SEO was working.

For a service business, an assistant’s recommendation can still lead to someone being hired. With a recipe, the ingredients and instructions may be the whole thing the person wanted. Once those have been supplied elsewhere, the publisher can lose both the visit and the chance to turn that person into a regular reader. The recipe has already done its job for the reader. The publisher still has to pay for producing it.

In my reply, I focused on the production pipeline. I think the harder question is what gives someone a continuing reason to depend on the original source after consuming one of its answers.

Training, assistant fetches, and AI search each need their own case for what the publisher gives up and receives. I wouldn’t dismiss blocking as pointless. My doubt is that blocking alone can solve the longer-term business problem.

The direction I want to investigate is how producing and maintaining information could make the source worth consulting again. That might involve information whose value depends on continued testing or verification. I mean giving the source continuing value through that work, rather than simply increasing the volume of pages published.

I expect many websites to evolve towards fewer pages, with more of the business accessible through API endpoints and MCP connections that let assistants use its data and services. For some businesses, those interfaces could become the main way customers interact with them, leaving a smaller site for people to browse. An assistant could request current information or use a service on someone’s behalf without sending them to a page. If visits remain our default KPI, we’d be judging those interactions by a visit that never needed to happen.

A recipe doesn’t become obsolete simply because an assistant has read it. Some publishers may find no viable return from allowing a particular kind of access. Even a system that keeps consulting the source needn’t cite i t, send a visitor, or pay for it.

A publisher could remain useful as a source while losing the visit that funded the work. Keeping a system dependent on your information would still leave the question of how you get paid . Before choosing a visibility metric, the publisher needs a business case for continuing to supply that information.

### A Mention Still Has To Mean Something

For a supplier seeking qualified demand, I want to know whether relevant buyers encounter the business, understand what it offers, and become more likely to choose it. Observations about answers can help investigate that. They don’t automatically measure the resulting demand.

Asking an assistant about a named company supplies the name. Asking it to help solve a buyer’s problem leaves it to identify possible suppliers. A mention could then be a recommendation, a warning or a correction. A dashboard could color all three green because the name appeared. A warning about your company is a strange thing to put in the wins column.

Buyer research and self-reported discovery can help investigate journeys that referral reports miss. Where feasible, controlled comparisons can test whether an intervention improves an outcome. Neither a rise in branded searches nor a nicer answer, taken alone, proves incremental revenue.

I want to understand what happened in that earlier conversation. The weak pitches around AI visibility don’t make the question go away. An agent capable of completing a transaction still has to arrive at a choice.

In the journey I opened with, the supplier has to earn the sale, and Google helps the buyer reach it. The assistant also has a part in that journey: it helped decide whose name went into the search box.

Google gets the thank-you. I’d like to know who made the introduction.

More Resources:

- Google Announces New Query Fan-Out Framework: R4T-Diffusion

- AI Search Tools Cited A Made-Up Concept Within A Week, Paper Finds

- ChatGPT Access Tied To 9% Drop In Traditional Search

This post was originally published on The Inference .

Featured Image: Andrey Suslov/Shutterstock

Category SEO Ecommerce

Read Full Bio

Pedro Dias Independent Consultant at Visively

I help companies design systems that make their content findable — by both search engines and AI (Artificial Intelligence). I’m ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-gets-the-thank-you/594108/)
