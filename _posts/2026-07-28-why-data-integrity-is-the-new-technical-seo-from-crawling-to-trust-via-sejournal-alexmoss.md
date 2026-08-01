---
layout: post
title: "Why Data Integrity Is The New Technical SEO: From Crawling To Trust via @sejournal, @alexmoss"
date: 2026-07-28T14:30:34+00:00
source: "Search Engine Journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-07-28/Why Data Integrity Is The New Technical SEO From Crawling To Trust via @sejournal, @alexmoss.md"
original_url: "https://www.searchenginejournal.com/why-data-integrity-is-the-new-technical-seo-from-crawling-to-trust/582189/"
author: "Alex Moss"
categories:
  - "SEO"
  - "Technical SEO"
---

# Why Data Integrity Is The New Technical SEO: From Crawling To Trust via @sejournal, @alexmoss

- Source: Search Engine Journal
- Published: 2026-07-28
- URL: https://www.searchenginejournal.com/why-data-integrity-is-the-new-technical-seo-from-crawling-to-trust/582189/
- Author: Alex Moss
- Categories: SEO, Technical SEO

## RSS 摘要

Agentic protocols are multiplying with no consensus standard in sight. Own the layers underneath instead of chasing a winner. The post Why Data Integrity Is The New Technical SEO: From Crawling To Trust appeared first on Search Engine Journal .

## 原文正文

Why Data Integrity Is The New Technical SEO: From Crawling To Trust Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- SEO

## Why Data Integrity Is The New Technical SEO: From Crawling To Trust

No consortium is coming to crown a standard like sitemaps or schema.org. Here's a practical order for hedging your bets.

In the past two years, Google has dropped support for nine ItemTypes from its rich result search gallery . This has happened not too long after ChatGPT’s launch and when mass adoption began:

Image from author, July 2026

The question remains whether this decline will continue, but the most recent removal – FAQ/FAQPage – has since caused some debate over the role of schema.org within the future of Search.

### Schema Is Dead, Right?

While some perform tests and experiments to understand whether schema really makes a positive impact on being cited within platform responses, Gianluca Fiorelli notably observed that we may be performing these tests on limited datasets. With that in mind, let’s remind ourselves of the wording of the deprecation message for FAQ rich results:

“…We will be dropping the FAQ search appearance, rich result report, and support in the Rich results test in June 2026.”

Notice here what they did not mention – which is that the use of FAQ schema is no longer required. This is because the deprecation is that of rich results only – a display feature. Schema itself is a comprehension layer – identifying entities and the relationships between them. Is schema dead? In my opinion, it is far from it. While some properties deprecate, others, such as Product, are extended .

That being said, I’m also aware that adding schema isn’t a magic bullet that contributes towards citation growth. However, that growth goes beyond the metrics we’ve been accustomed to rely on such as citations, impressions, etc. Suganthan Mohanadasan wrote a great piece about how schema has three “lives”:

- Google’s index pipeline.

- LLM pretraining (indirect).

- LLM runtime retrieval.

SEOs have been historically focused on No. 1 as something that can positively contribute towards success metrics. But schema goes beyond what we’re used to, or accurately, report on. Schema isn’t dying; one display feature it benefited from is diminishing instead.

### An SEO’s Biggest Threat: Ambiguity

Schema is an ontology that, as a web standard, can contribute towards data integrity. The risk to data integrity is ambiguity. Ambiguity leads to hallucinations. Hallucinations snowball. Eventually the result compounds, which could lead to inaccurate results or even incorrect LLM pre-training which could have longer-lasting effects.

If an agent can misread you, at some point it will. LLMs can then risk traveling into “semantic drift” detracted from the facts and in favor of narrative. This was explored within a piece titled “ Sangue e Grafi: Teaching a Small Model to Read the Bloodline ” by Andrea Volpini and Chiara Carrozza where frontier models tended to fall for narrative over facts, while a small model given knowledge-graph tools drew level with them.

Image from author, July 2026

→ Further reading: Information Retrieval Part 1: Disambiguation

### 5 Layers Of Data Integrity

All this corroborates my belief that an SEO’s role is to maximize data integrity, of which schema plays a role. Below, I illustrate five layers of what data integrity can include:

Image from author, July 2026

- Entities: What exists, and what that thing is. Thing, Organization, and Person, stabilized with @ids and tied out to Wikidata, GS1, ISNI, or ORCID so an agent knows your “Apple” from the fruit.

- Relationships: How those things connect. @id and sameAs, RDF. Yoast SEO’s schema aggregation feature and EntityMap by Dixon Jones.

- Format: How structure is serialized and served. JSON-LD, RDFa, and Microdata. Markdown, too (encompassing LLMs.txt, agents.md, OKF) and endpoints (content negotiation, ARD, MCP).

- Actions: What can be done, declared to agents. Schema.org Actions such as BuyAction, plus the newer WebMCP, ACP, and UCP.

- Perception: Grounding, third-party perception, sentiment, etc.

### Aggregation, Guidance, And Consumption

In a post I wrote in October last year, I said, “SEOs will have to consider both sides of the web and how to serve both.” The emerging protocols (all of which were launched in the past two years) show this to be true, where a new “agentic grounding stack” generally adopts one of three goals:

Protocol

Goal

What It Does

sitemap.xml

Aggregation

Every canonical URL into a single XML index.

llms.txt

Aggregation

Summary of a site’s content with important information and links to further reading.

Yoast Schema Aggregation

Aggregation

Page-level JSON-LD into one connected site-wide graph.

EntityMap

Aggregation

A site’s entity declarations into one explicit map.

Knowledge Catalog

Aggregation

Structured, unstructured, and SaaS data into a governed context engine.

OKF

Aggregation

Site knowledge into a markdown bundle at /okf/.

ARD · ai-catalog.json

Aggregation

A domain’s tools and agents into a catalog; registries federate above it.

OpenKB

Aggregation

Source documents compiled into a markdown wiki.

Schema.org

Guidance

The shared vocabulary that tells machines what things mean.

agents.md

Guidance

How agents should represent and interact with you.

Markdown for Agents

Consumption

Same URL served as clean markdown via content negotiation.

Markdown alternate output

Consumption

A separate .md version linked with rel=alternate.

/crawl endpoint

Consumption

Renders a page, or entire site, as clean markdown on demand.

WebMCP

Consumption

Exposes a site’s actions as tools an agent can invoke.

NLWeb

Consumption

Ingests schema, feeds , and sitemaps to answer natural-language queries.

ACP

Consumption

Agent checkout inside ChatGPT against merchant product data.

UCP

Consumption

A common language for agent commerce actions across surfaces.

These three goals help reduce the number of requests while increasing token efficiency. Some of the above protocols have been covered in more detail within Search Engine Journal, including my own on ACP and UCP and Emina Demiri-Watson’s thorough article on OKF, ARD, and others earlier this month.

But there’s something none of these protocols have…

### There Is No Consensus Or Agreed Standard

Schema.org was born out of consensus between Google, Microsoft/Bing, and Yahoo! (Yandex joining later) who launched it under joint governance. The same happened five years earlier with the XML sitemap . When the search engines needed a standard, they simply sat down and created one – together.

Nothing like this is happening now, and it comes at the detriment of SEOs who genuinely want clarity on what to implement and what not to implement for sites they work on. Even basic facts about consumption are contested, where the debate over markdown is a great example of this.

While these debates continue, there’s no room where platforms are convening and agreeing to one universal standard. The ecosystem has changed so dramatically that these companies are not in the business of Search and the good of the web, but must now navigate how their businesses affect jobs, economies, livelihoods, and the future of humanity as a whole. As such, I just don’t believe questions posed by SEOs are at the top of their priorities.

### What Can You Do About It Now?

Looking back at the five layers of data integrity, the four you have control over can be illustrated below when looking at what an agentic grounding stack can look like:

Image from author, July 2026

There’s a lot to consider, and all have different goals and technical debt. Decide which are most applicable to you, as well as adopting anything that should not require too much technical debt.

If I had to pick an order, it would be this.

- Stabilize your @ids and add sameAs links out to Wikidata and the other authorities first, because everything else stands on it.

- Then test how you’re actually interpreted, with NLWeb , rather than assuming the graph reads the way you intended.

- If you’re in ecommerce, audit the product feed before touching anything shiny, and look at BuyAction while you’re there: only ReadAction and SearchAction are deployed at any real scale today, so the field is genuinely open. Look into the recent news about what has been added to the Product schema .

- Attempt to implement WebMCP . It can be done on any website, and doesn’t need to be ecommerce.

- Markdown serving and content negotiation can wait until you have engineering capacity to spare (unless you can use Cloudflare’s Markdown for Agents ).

- Look into OKF and ARD. When Google launches new protocols, I always take notice – especially when it comes to how an agent or LLM understands a site as a whole.

None of this is a bet on a specific protocol. Implementing any of these reduces the risk that an LLM has to go “the long way round” to form the answer it wants to respond with. By hedging bets to welcome any agent from any platform, this will also help you think more about exactly how your site may be interpreted by them, and how this improves when these protocols are adopted.

Even if you want to make small experiments away from larger sites, it’s worth exploring not only to see if there are positive results from it, but also to understand how they all work in practice. This is exactly what I have done recently, where I have rebuilt my personal website, which has several “agentic ready” protocols running, including content negotiation, markdown alternate, llms.txt and WebMCP.

### Don’t Chase The Protocol, Own The Layers Underneath

Right now, it seems there is no single “winner” that will progress from a proposal or protocol to a web standard. There’s no consortium to repeat what was done with the XML sitemap and Schema.

The stack is now big, but there’s one thing they all share. Whether it aggregates, guides, or consumes, each one is fed by the same substrate: Accurate entities, explicit relationships, and content a machine can read without guessing or researching further.

Rankings were the success metrics of the old web. Trust, integrity, accuracy, and validity. Earning this is still the role of an SEO.

More Resources:

- What Is The Agentic Web?

- AI Agent Standards: What Do We Need To Know?

- The Fully Non-Human Web: No One Builds The Page, No One Visits It

Featured Image: hmorena/Shutterstock

Category SEO Technical SEO

Read Full Bio

Alex Moss Principal SEO at Yoast & Co-Founder at FireCask at Alex Moss

Alex is an online marketer and expert-level SEO consultant, specialising in technical and structural SEO as well as WordPress and ...

## 原文链接

[Read original](https://www.searchenginejournal.com/why-data-integrity-is-the-new-technical-seo-from-crawling-to-trust/582189/)
