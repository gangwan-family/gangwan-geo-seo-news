---
title: "Google Now Has The Math To Rank Without An Index, And The Results Page Does Not Survive It via @sejournal, @DuaneForrester"
source: "Search Engine Journal"
published: 2026-10-08T14:30:43+00:00
fetched_at: 2026-10-09T01:17:51.840578+00:00
url: "https://www.searchenginejournal.com/google-now-has-the-math-to-rank-without-an-index-and-the-results-page-does-not-survive-it/591945/"
guid: "https://www.searchenginejournal.com/google-now-has-the-math-to-rank-without-an-index-and-the-results-page-does-not-survive-it/591945/"
author: "Duane Forrester"
categories:
  - "SEO"
---

# Google Now Has The Math To Rank Without An Index, And The Results Page Does Not Survive It via @sejournal, @DuaneForrester

- Source: Search Engine Journal
- Published: 2026-10-08
- URL: https://www.searchenginejournal.com/google-now-has-the-math-to-rank-without-an-index-and-the-results-page-does-not-survive-it/591945/
- Author: Duane Forrester
- Categories: SEO

## RSS 摘要

Google DeepMind proved one model can theoretically rank without a separate index. If it ships, visibility stops being a position and becomes inclusion or absence. The post Google Now Has The Math To Rank Without An Index, And The Results Page Does Not Survive It appeared first on Search Engine Journal .

## 原文正文

Google Now Has The Math To Rank Without An Index, And The Results Page Does Not Survive It Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- SEO

## Google Now Has The Math To Rank Without An Index, And The Results Page Does Not Survive It

A DeepMind paper closes a five-year research arc toward a model that ranks by generating results, which makes page two something that never happens.

Google’s researchers have now proven, on paper, that a single language model can rank an unlimited number of documents without a separate index, and the practical consequence is that the ranked list stops being something you see and becomes something the model computes on its way to an answer. That is the key takeaway after reading the paper, and it is the reason I think this research matters more for practitioners than its modest experiments would suggest.

Roger Montti covered the paper recently at Search Engine Journal , and his explanation of the mechanics is the one to read: how today’s two-stage pipeline pairs a fast, cheap dual encoder for retrieval with a slower, more accurate cross encoder for reranking, and how the DeepMind team proposes collapsing both into one generative model. I am not going to re-explain the encoders, because Roger did that well and there is no reason to do it twice. I want to go the other direction, forward and outward, into what this architecture does to the industry, to the work, to the people doing the work, and to the person typing the question.

One disclosure first. I founded CitationIQ, a measurement platform for AI data and visibility, so when I say measurement changes under this model, I have a stake in that change.

Everything that follows is informed speculation. The paper proves a theoretical capacity and demonstrates a training method on two small datasets. Nobody has replaced a web index with it. But Google does not publish five years of research pointed in one direction unless the direction is serious, and that history is where this needs to start.

### This Paper Finishes A Sentence Google Started In 2021

In 2021, four Google researchers published Rethinking Search: Making Domain Experts out of Dilettantes , which argued that a search system should answer directly from a corpus it can cite rather than hand the user a list of references. It carried a disclaimer that it was a research proposal and not a product roadmap, and that disclaimer still applies to everything downstream of it. In 2022, largely the same group published the Differentiable Search Index , which showed a single Transformer could map a query directly to document identifiers with the entire corpus encoded in the model’s parameters. That is the idea Roger’s article describes, four years earlier and without the theory.

The January 2026 paper supplies the theory. It proves that a dual encoder’s embedding dimension has to grow linearly with the number of documents in order to express every possible ranking of them, while an autoregressive model with a fixed hidden dimension can rank an arbitrary number. It then introduces a training loss, SToICaL, that teaches the model to care about the whole ranked list rather than just the top result. So the arc is proposal, prototype, proof. Google is not floating a new idea here. It is closing the theoretical gap on a bet it placed publicly five years ago.

Read the experiments honestly, though, because the piece I want to write here doesn’t work if I overclaim. The team fine-tuned Mistral-7B, not a frontier model. The ranking was done in-context, meaning the candidate document identifiers were placed in the prompt and the model chose among them, which is reranking rather than retrieval from an open corpus. WordNet has about 82,000 noun concepts. The shopping evaluation ran on 310 examples. One configuration got worse at putting the single best result first even as it improved the rest of the list. This is a foundation, not a deployment. Foundations are what you build on, and Google has been laying this one in public for half a decade. (WordNet is a Princeton database that arranges about 82,000 English nouns into a tree of broader and narrower concepts, and was used because that tree hands the researchers a ready-made ranked list for every query: parent first, grandparent second, and so on.)

### Documents Become Codes, And The Code Is What Ranks

In this architecture a document is not a URL. It is a docID , a short sequence of tokens the model generates one at a time, in the same way it generates words. In the shopping experiment the researchers derived each product’s identifier from the embedding of its title, compressed to three numbers, so the identifier carries meaning and similar products share leading digits. The model ranks by generating the most probable identifier, then the next most probable, through beam search. There is no lookup. The address is produced, not retrieved.

Three things follow for anyone whose job is getting content chosen.

Distinctness becomes the optimization target. If a page is not separable from its neighbors in embedding space, it cannot hold a stable, distinct identifier. Two near-duplicate product pages are no longer competing for adjacent positions. They are competing for the same address, and one of them loses outright. I have a longer piece coming on how a brand’s position in that space drifts over time, so I will leave it at the observation here.

The ranking function is the training set. SToICaL trains on triples: a query, a document identifier, and that document’s true rank in a graded list. Whatever produced the graded lists, whether click logs , rater judgments, engagement signals, or some blend, becomes the algorithm. There is no separate layer of ranking factors to reverse engineer. There is a distribution of learned preferences, fixed at fine-tuning time, that the model reproduces when it decodes.

Freshness becomes a training problem. In a classical index a new page is crawled and inserted. In a parametric generative index it has to be learned, and Google’s own follow-up work, DSI++ , found that continually indexing new documents caused considerable forgetting of documents already indexed. Mitigations exist and that paper describes them, but the shape of the problem changes. For a news publisher , “indexed” and “known to the ranker” stop being the same event. The AutoRegressive Ranking (ARR) experiments sidestep this by keeping candidates in the prompt, which is almost certainly how a real deployment would begin: classical retrieval feeding a generative ranker. That hybrid is the plausible near-term state, and the pure version is the long-term direction.

### The Beam Is The Whole Universe

Here is the claim I would build strategy around. Beam search is how a generative model produces a short list instead of a single answer: at each step of generation it keeps only a fixed number of the most probable partial sequences, say ten, extends those, and discards everything else, so the finished list can never be longer than the number it kept along the way. Autoregressive ranking produces its top-k list through beam search, and the beam width is the complete set of results the system computes. A dual encoder with a nearest-neighbor index gives you the top thousand almost for free, because scoring is cheap and the list is a byproduct. A beam of ten gives you ten. Position eleven is not a bad result. It was never generated.

Page two stops being a design decision and becomes something that does not exist. Rank tracking below the beam measures nothing, because there is nothing below the beam to measure. Visibility turns binary: in the generated set or absent from it. And from the outside there is no way to distinguish “ranked badly” from “never produced,” because both look identical to the person watching. The practitioner’s question shifts from where we rank to whether we are in the generated set, how consistently, and for which shapes of query. That is the question visibility platforms are built to answer.

There is a genuine irony in the paper that I think will define the next few years. Its actual contribution is better ranking below position one. On WordNet, the rank-aware training pushed recall at positions two through five from the fifties into the mid-nineties. Better ordering of the second through fifth results is arriving at exactly the moment the surface shows fewer of them. The improvement lands on the part of the list the consumer is least likely to see.

### What It Does To Clicks And To The Money

Alphabet’s second quarter put Google Search and other revenue at $63.27 billion, up 17%, after 19% growth the quarter before. The ad auction is a separate system, and this paper does not touch it. Where the paper matters to revenue is cost. The two-stage pipeline exists because cross-encoders are too expensive to run against a whole corpus. Autoregressive ranking removes the separate nearest-neighbor index and does not score every document individually, which is a structural cost reduction for generative results. Cost has been the quiet constraint on how far Google pushes AI answers as the default experience. Remove enough of it and the last structural reason to keep 10 blue links , which are where the ad inventory lives, gets weaker. Not because advertising dies. Because the surface that hosts it changes, and the ads move with it.

### I Described This Ad System A Year Ago, Google Shipped The First Piece In May

In August 2025, I published Cohorts, Clusters, and the Coming AI Ad System , where I coined Intent Vector Bidding : an auction in which placement is decided by how closely an advertiser’s content aligns with the meaning of the user’s prompt, and the ad itself is built at the moment of the query from the advertiser’s assets rather than written in advance. I labeled it theory at the time and said I expected the major platforms were already working toward it.

Nine months later, at Google Marketing Live , Google announced ad formats for AI Search that it described as instantly tailored to a person’s unique query, with creative generated from the specific phrasing of the question. You still run campaigns and supply assets, so the endpoint I described is not here. The creative half of it is. I do not get many of these right on that timeline, so I am noting it.

The ARR paper completes the mechanism. Google Research’s token auction paper, which won best paper at the Web Conference in 2024, designed an auction in which advertisers bid to influence ad text as it is generated token by token. Autoregressive ranking generates organic document identifiers token by token. That is the same origin on both sides of the page. A single decoding pass could plausibly produce the answer, the organic sources behind it, and the sponsored inclusion, with the advertiser paying for probability mass rather than for a slot.

On the workflow side, what changes is what you submit. You stop building ads and start feeding the system your business: product data , specifications, credentials, brand constraints, the claims you will not make. The platform assembles and places the creative at the moment of alignment and bills you for inclusion. The paid media role moves upstream, toward data stewardship and governance and away from campaign construction. The earlier article carries the full version of that argument, and I will not repeat it here.

### What The Consumer Gets

Fewer options, better ordered. Faster resolution. An invisible tail. And no signal that distinguishes “nobody else was relevant” from “nobody else was generated,” because the consumer never sees the results that were not produced and has no reason to wonder about them. Of everything in this piece, that is the part I find least comfortable, and the part I think is most likely.

### Where To Put Attention Now

Not on rebuilding a program around a research paper. Three smaller moves are proportionate to where this actually is.

Treat distinctness as a measurable property. Audit for pages that cannot be told apart by meaning, because under any generative index those pages are fighting for one address. Move measurement from position to inclusion , and start building the baseline now, because the day the beam becomes the boundary, you will want history. And read your paid strategy against the ad system I described last August, because the creative side of it has already started shipping.

Google has now proven that one model can rank without a separate index. If that reaches production, the ranked list becomes an internal step, the beam becomes the edge of visibility, and the practitioner’s job shifts from earning a position to earning an address the model chooses to generate. That is speculation, and I have tried to state it as such. It is also the direction every paper in this line has pointed since 2021.

If you see this differently, or you have data on how generative rankers behave at scale, leave a comment or reach out. I would rather be corrected early than confident late. And if you want the fuller version of how content earns its place inside these systems, that is what The Machine Layer is about.

More Resources:

- AI Visibility Rankings Aren’t Stable – New Research Shows It’s Mostly Statistical Noise

- How To Measure PPC Performance When AI Controls The Auction

- AI’s Impact Is Outrunning Measurement: The Trust And Attribution Gap Facing Brands

This post was originally published on Duane Forrester Decodes .

Featured Image: maxim ibragimov/Shutterstock

Category SEO

Read Full Bio

Duane Forrester Founder and CEO at UnboundAnswers.com

Duane Forrester is the Founder and CEO of UnboundAnswers.com, a consultancy helping businesses adapt to the realities of AI-powered search ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-now-has-the-math-to-rank-without-an-index-and-the-results-page-does-not-survive-it/591945/)
