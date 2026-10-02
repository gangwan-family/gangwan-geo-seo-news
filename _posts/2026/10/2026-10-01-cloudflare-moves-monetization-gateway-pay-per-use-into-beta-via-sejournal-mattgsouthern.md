---
layout: post
title: "Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta via @sejournal, @MattGSouthern"
date: 2026-10-01T08:30:55+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-01/Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/cloudflare-moves-monetization-gateway-pay-per-use-into-beta/591719/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-01
- URL: https://www.searchenginejournal.com/cloudflare-moves-monetization-gateway-pay-per-use-into-beta/591719/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Cloudflare's Monetization Gateway charges AI agents per request in a closed beta, and Pay Per Use pays publishers for the AI uses that buyers report. The post Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta appeared first on Search Engine Journal .

## 原文正文

Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta Skip to content

SEJ Pro Sign In

CallRail’s six-step checklist shows how to track calls from ChatGPT, Claude, and Perplexity instead of losing them in ‘direct/other.’

Download the Checklist

- SEJ

- ⋅

- AI Search

## Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta

- Cloudflare moved its Monetization Gateway and Pay Per Use into beta.

- The Gateway's U.S. closed beta lets sellers charge AI agents per request.

- Pay Per Use pays publishers who accept an AI company's offer for reported uses.

Cloudflare's Monetization Gateway charges AI agents per request in a closed beta, and Pay Per Use pays publishers for the AI uses that buyers report.

Cloudflare put two AI payment products into beta on Sept. 30. The Monetization Gateway enables sellers to charge AI agents for each request to an API, MCP tool, dataset, or site. It’s currently in closed beta for U.S.-based sellers and buyers. Pay Per Use , a separate product also in beta, compensates publishers when an AI company reports using their content after retrieval.

Cloudflare announced the Gateway on July 1 and opened a waitlist. In my comparison on Sept. 18 of AI content payment models , I mentioned that Cloudflare’s July Pay Per Use announcement called it an experiment.

With the Gateway, sellers have the control to decide which requests are billed and at what price. Meanwhile, with Pay Per Use, the AI company defines the use and sets the price, and publishers can decide whether to accept or decline.

### Monetization Gateway Charges Per Request

The Monetization Gateway charges an AI agent per request, with prices set by the seller. As mentioned in the company’s post, it is designed for resources that involve usage with each request, such as APIs, tools, and data.

The Gateway uses the x402 protocol and the HTTP 402 Payment Required status code. When an agent attempts to access a protected resource, it first receives the payment terms and signs a payment authorization before retrying the request. Payment is processed within this request and verified before the seller’s server responds, according to the documentation .

Each rule specifies the domain, URL, price, and target audience, with more details on the monetization rules page . The audience can be everyone or only verified bots identified by Cloudflare’s BotBase.

Fixed pricing ensures that requests with fixed inputs all cost the same, while variable pricing authorizes a maximum limit. For variable pricing, the seller’s origin reports the actual paid amount, with settlements from $0.001 and prices up to $100.

Payments are processed using the USDC stablecoin on the Base blockchain via Coinbase’s x402 Facilitator. The company has announced plans to add support for more payment methods.

### Who Can Use The Gateway Now

The Gateway is currently in closed beta, and the eligibility page states that both buyers and sellers need to be based in the United States. Sellers need, among other things, a credit card on file, a verified email address, and an account that’s more than 60 days old. The zone must also be proxied through Cloudflare, be more than 30 days old, and pass zone security checks. Sellers can request access through the dashboard.

### Four Uses Cloudflare Says Are Live

Cloudflare lists four live implementations, including its own AI Gateway.

Ceramic.ai provides a web search API for agents, with fixed pay-per-search pricing and no need for an API key. In July, Cloudflare described Ceramic as a Pay Per Use partner, paying content sites whenever their content appears in its search results. In the Gateway, Ceramic serves as the seller.

AI Gateway accepts payment per inference request across four open models for U.S. users, as explained in its documentation . Stocktwits charges for each market signal request via a dedicated route for agents.

API2PDF is a PDF-generation API with variable pricing based on each request’s compute and bandwidth. Cloudflare’s post notes that, for API2PDF, asking customers for a credit card after the first month caused a drop of over 50% in conversion.

### Pay Per Use Pays After Retrieval

Cloudflare’s Pay Per Use post clarifies that Pay Per Crawl “charges for access,” whereas Pay Per Use “pays for what happens next,” such as providing a cited answer in AI search.

The post splits the roles this way:

“Each AI company defines the use it will pay for and sets a price. Publishers decide which offers to accept, and then can see how often their content is used and what it has earned. Cloudflare handles enrollment, usage records, billing, and payment.”

Each program’s terms cover what the AI company may do with the content, including any restrictions on training.

The buyer keeps track of every use by reporting a timestamp, the source URL, and the event ID. The post explains that usage is self-reported, while the program rules require complete reporting. It adds that Cloudflare checks that each reported use matches an enrolled publisher. The company then bills the buyer and pays the publishers each month.

During the beta, the company says it’s working directly with each buyer and with publishers who opt in, without naming the buyers.

### Where This Leaves The Sept. 18 Comparison

On Sept. 18, I compared the Pay Per Crawl and Pay Per Use options with Google’s AI contribution pilot and Microsoft’s Publisher Content Marketplace. With the Gateway now included, Cloudflare’s side has expanded to include three different payment events.

Pay Per Crawl charges a crawler for each successful paid retrieval, based on the rate set by the site owner. The Gateway charges per request at a rate determined by the seller. Pay Per Use pays out for each reported use, at the price offered by the AI company.

### Why This Matters

For a publisher on Cloudflare, Pay Per Use means the AI company defines the use and the price. You determine if an offer is acceptable, and the usage data that affects your earnings is provided by the buyer’s reports.

A U.S.-based company selling an API, MCP tool, or dataset controls its per-request pricing once admitted to the Gateway’s closed beta.

Neither Cloudflare’s Gateway post nor its Pay Per Use post reports transaction counts or payouts.

### Looking Ahead

Cloudflare says the Pay Per Use beta will help it work out how to let publishers counter a buyer’s price and charge differently by use.

Watch whether Cloudflare names the AI companies buying through Pay Per Use. For the Gateway, the company says support for new geographies is “on the way.”

Featured Image: Samuel Boivin/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/cloudflare-moves-monetization-gateway-pay-per-use-into-beta/591719/)
