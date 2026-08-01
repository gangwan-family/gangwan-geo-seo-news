---
layout: post
title: "Google’s Open Knowledge Format Adds Five Trust Signals via @sejournal, @martinibuster"
date: 2026-07-29T11:00:20+00:00
source: "Search Engine Journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-07-29/Google’s Open Knowledge Format Adds Five Trust Signals via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/googles-open-knowledge-format-adds-five-trust-signals/584120/"
author: "Roger Montti"
categories:
  - "Generative AI"
  - "News"
  - "SEO"
---

# Google’s Open Knowledge Format Adds Five Trust Signals via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-07-29
- URL: https://www.searchenginejournal.com/googles-open-knowledge-format-adds-five-trust-signals/584120/
- Author: Roger Montti
- Categories: Generative AI, News, SEO

## RSS 摘要

Google announced version 0.2 of the Open Knowledge Format, introducing five new trust signals. The post Google’s Open Knowledge Format Adds Five Trust Signals appeared first on Search Engine Journal .

## 原文正文

Google's Open Knowledge Format Adds Five Trust Signals Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- SEO

## Google’s Open Knowledge Format Adds Five Trust Signals

Google announced an update to the Open Knowledge Format that adds five trust signals, available now in version 0.2.

Google has announced an update to the Open Knowledge Format (OKF), version 0.2. The new version adds five trust related features that a “consumer” of the OKF can use to verify five aspects about the OKF bundles.

The five trust signals and their related OKF fields and concept type are:

- Provenance (field: sources)

- Trust (fields: generated, verified)

- Freshness (field: stale_after)

- Lifecyle: (field: status)

- Attestation (new concept type: Attested Computation)

The announcement positions these five signals as answering five questions about the OKF bundle in order to establish trust.

The five questions:

- “What was this created from? (provenance)

- How much should I trust it? (trust)

- Is it still true? (freshness)

- Is it the current version? (lifecycle)

- Was this number produced the way we said it must be? (attestation)”

### Provenance

Google introduces a new “sources” field that records where the information in a concept came from. This enables consumers to identify the original sources used to create it. This provides source information that consumers can use to evaluate a concept’s trustworthiness, answering t he question, “What was this created from?”.

This is Google’s example of the sources field:

sources: - id: warehouse-schema resource: https://wiki.acme.internal/data/warehouse/schemas/sales title: Acme Retail warehouse schema — sales dataset author: team:data-platform usage_count: 1240 last_modified: 2026-06-15 - id: revenue-policy resource: policies/revenue-recognition.md title: Revenue Recognition Policy (FY2026) author: human:jsmith@acme last_modified: 2026-06-15

Google explains what it all means:

“The new sources field records the materials a concept derives from: an external doc, a bundle-relative path, or even a scope descriptor like “all queries in project X.” At the same time, an entry can carry objective credibility signals: author, usage_count, last_modified.

The deliberate choice here is what we didn’t add. OKF records the signals, not a credibility score. A score is subjective, doesn’t port across consumers, and goes stale the moment it’s written.

Instead, credibility is inferred from the signals by whoever is consuming (and can be dynamically scored by the consumer, if desired), the same way you’d trust a heavily used, recently updated, authoritatively authored source more than an anonymous one. And when the body cites a specific source, it does so with an ordinary markdown footnote keyed to the source id ([^export-schema]), so attribution is per-claim instead of a dangling list at the bottom.”

### Trust: Generated And Verified Fields

The next part of the trust signals are the Generated and Verified fields.

The “generated” field records who created a concept, while the “verified” field records who independently confirmed it. A consumer (such as an AI agent, an LLM, or an application) can use the verification information to filter concepts based on whether they are unverified, machine-confirmed, or human-reviewed.

This is the example of the Generated and Verified fields in use:

type: Metric title: Revenue generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z } verified: - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z }

### Freshness and Lifecycle: status and stale_after Fields

The status field communicates what part of the lifecycle a concept is in so that a consumer can identify whether it’s in draft, current, or it’s outdated (deprecated). It signals whether a concept is a draft, stable, or is deprecated.

The stale_after field specifies the date after which the concept should be re-verified before being used. Consumers can use these fields to identify concepts that need to be re-verified or to exclude outdated concepts from new work while preserving them for historical reference.

Here’s the example of this in use:

type: Metric title: Gross Margin (legacy, pre-FY2026) status: deprecated

### Attested Computation: For Verifying Calculations

Attested Computation is not a field, it’s a new Type. Attested Computation defines the approved way to calculate a value and provides a way to verify that the calculation was performed the way it was supposed to be calculated.

The official description explains:

“Provenance answers where a claim came from. Attestation answers a harder question that matters the moment an agent reports a dollar figure: was this number produced the way we said it must be, or did the agent improvise its own SQL?

OKF v0.2 introduces a new concept type, Attested Computation. It carries not just what a value means but a sanctioned way to compute it, and the means to check that the sanctioned thing actually ran.”

Here’s the example:

--- type: Attested Computation title: Revenue for a fiscal year runtime: bigquery parameters: - { name: year, type: integer, required: true } executor: resource: skills/run-on-bq.md receipt: [job_id, executed_sql, result] attester: resource: attesters/sql_equality.py generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z } verified: - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z } status: stable stale_after: 2026-12-31 sources: - id: revenue-policy resource: policies/revenue-recognition.md title: Revenue Recognition Policy (FY2026) author: human:jsmith@acme last_modified: 2026-06-15 --- # Computation SELECT SUM( CASE WHEN o.currency = 'USD' THEN o.net_amount ELSE o.net_amount * fx.rate_to_usd END ) AS revenue_usd FROM `acme.sales.orders` AS o LEFT JOIN `acme.finance.fx_daily_rates` AS fx ON fx.currency = o.currency AND fx.rate_date = DATE(o.order_ts) WHERE o.order_status = 'delivered' AND DATE_DIFF(CURRENT_DATE(), DATE(o.order_ts), DAY) >= 30 AND EXTRACT(YEAR FROM o.order_ts) = @year"

### Updated Open Knowledge Format Documentation

Google has updated the GitHub Repository to reflect this update and has published an announcement that serves as an explainer.

Featured Image by Shutterstock/Cranium_Soul

Category News SEO Generative AI

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/googles-open-knowledge-format-adds-five-trust-signals/584120/)
