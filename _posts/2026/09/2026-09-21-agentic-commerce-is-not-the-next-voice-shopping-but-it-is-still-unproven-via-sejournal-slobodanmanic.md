---
layout: post
title: "Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven via @sejournal, @slobodanmanic"
date: 2026-09-21T14:30:37+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-21/Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven via @sejournal, @slobodanmanic.md"
original_url: "https://www.searchenginejournal.com/agentic-commerce-is-not-the-next-voice-shopping-but-it-is-still-unproven/589439/"
author: "Slobodan Manic"
categories:
  - "AI Search"
  - "Ecommerce"
  - "SEO"
  - "_src_search-engine-journal"
---

# Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven via @sejournal, @slobodanmanic

- Source: Search Engine Journal
- Published: 2026-09-21
- URL: https://www.searchenginejournal.com/agentic-commerce-is-not-the-next-voice-shopping-but-it-is-still-unproven/589439/
- Author: Slobodan Manic
- Categories: AI Search, Ecommerce, SEO

## RSS 摘要

Visa, Mastercard, PayPal, and Stripe name no live merchant. Google names three. Here is what the agentic commerce documentation still refuses to say. The post Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven appeared first on Search Engine Journal .

## 原文正文

Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven Skip to content

- SEJ

- ⋅

- SEO

## Agentic Commerce Is Not The Next Voice Shopping, But It Is Still Unproven

Voice shopping changed the keyboard. Agentic commerce removes the buyer from the room, and your storefront is already in by default.

In March 2018, OC&C Strategy Consultants forecast that voice shopping would reach $40 billion-plus by 2022, up from $2 billion , across the U.S. and UK. Nobody describes voice commerce as a $40 billion market today. Before that, Facebook launched M, an assistant that would book your restaurant and chase your refund. It never left private beta and closed in January 2018, two and a half years in.

The reasonable question is whether agentic commerce is the same story with a new noun. It is not. Your website may already be part of it without you having agreed to anything, and that is one of four things with no precedent.

### Voice Shopping Moved The Input, Agents Move The Decision

Voice shopping was an interface change. You were still there. You decided, you confirmed, you were present for the transaction. Talking instead of typing does not change the shape of commerce; it changes the keyboard.

Agentic commerce claims the purchase happens without you in the room. That is a structural change, and the FIDO Alliance calls it Human Not Present , treating it as its own transaction class, separate from the human-present kind. Comparing that to voice is a category error, and the “we have seen this before” commentary makes it.

### Agentic Commerce Has 4 Things Voice Shopping Never Had

#### 1. The Merchant Does Not Have To Build Anything

Every previous wave needed merchants to build a thing: an Alexa skill, a Messenger bot, a voice-optimized catalogue. OpenAI’s Instant Checkout , the most recent of them, got roughly thirty Shopify merchants in six months before it was retired, and those thirty had built an integration for a surface that no longer exists.

On September 4, Shopify turned on UCP version 2026-08-25 across its storefronts and said the change “doesn’t require any changes to your existing integrations.” Mastercard’s Agent Pay has a compatibility path, DTVC, specifically so a merchant already accepting Mastercard takes agent transactions with no new work. Visa’s Intelligent Commerce says the agent pays through “guest checkout, key entered, web form or through an available merchant API.” It fills in the form a human would use. Between a platform default , a card network’s compatibility path, and an agent typing into a checkout, a merchant does not have to agree to any of it to be reachable.

#### 2. There Is A Way To Pay That Is Built For A Buyer Who Is Not There

Stripe’s Shared Payment Tokens are scoped to one merchant, capped at an amount, and expire. Google’s AP2 uses signed mandates as proof of what the user actually authorized. x402 answers an unpaid request with HTTP 402 and a payment header. Voice commerce had nothing like this. It used your saved card.

#### 3. Standards Bodies Are Involved, And That Is Not Decoration

W3C and GS1 ran a two-day workshop on this in Zurich on September 8 and 9. Google and Mastercard donated AP2 and Verifiable Intent to the FIDO Alliance. Google donated A2A to the Linux Foundation. Voice commerce had no standards process at all, only Amazon’s skills API and Google’s actions, each owned by the company that benefited from it.

#### 4. Merchants Are Organizing Against It On The Record

The Merchant Advisory Group used its Zurich session to set conditions. Without them, it says, merchants are “exposed to risks they did not cause and have limited ability to identify or manage.” Their proposal is a liability waterfall that puts responsibility on whoever controlled the function that failed, and a demand that merchants keep the right to route their own payments. There was no equivalent merchant-side position paper for voice shopping, because merchants were never asked to carry anything.

### Google’s Agentic Checkout Asks Permission First

Google’s agentic checkout is live. It is running now on Search and in AI Mode with named merchants: Wayfair, Chewy, Quince and select Shopify merchants. It watches a price, and when it drops it buys on the merchant’s website using Google Pay.

Google says:

We’ll always ask for your permission first, and only buy after you’ve confirmed the purchase and shipping details.

The user confirms the purchase. The user confirms the shipping details. Google’s agentic checkout is human-present , which by the distinction above makes it an interface change.

Asking first is the correct design, and I would rather they did. FIDO’s Human Not Present class is a target for harmonisation by the end of 2026, not something running today. The trillion-dollar projections are priced on the structural change. The structural change is not what you can buy today.

### The Agentic Commerce Forecasts Are The Same Class Of Number As Voice Shopping’s

McKinsey projects $1 trillion in U.S. retail revenue orchestrated by agents by 2030. Gartner predicts 90% of B2B purchases handled by agents by 2028, intermediating $15 trillion.

Those are the same class of number, from the same class of firm, about the same class of behaviour change, as OC&C’s $40 billion. I am not saying they are wrong. I am saying that the last time this exact shape of prediction was made about machines buying things on our behalf, it was out by an order of magnitude, and the people quoting it had moved on by the time that became obvious.

### What The Payment Companies Would Publish If Agentic Commerce Were Working

Removing the merchant’s obligation to build also removed the merchant’s decision to join. Shopify says it runs these protocols across millions of merchants, which means a very large number of storefronts now speak a protocol their owners never evaluated, under liability terms nobody has settled. It is a much larger trust requirement than the Alexa-skill era, because building something was friction, and friction is also consent. You knew what you had joined. Now you are in by default, trusting a platform’s judgment in place of your own.

Which means the burden of proof belongs to the people selling this, not to the merchants absorbing it.

Name one live merchant. Their documentation, read on 14 September 2026: Visa’s Trusted Agent Protocol names none. Visa Intelligent Commerce names none. Mastercard Agent Pay names none. PayPal names none. Stripe names none. Google names Wayfair, Chewy, and Quince.

Publish a version anyone can pin. Visa’s two products carry no version number and no date. Mastercard’s carries none. PayPal’s carries none. Stripe publishes 2026-04-22.preview , and is the only payments company here that does.

Publish a status anyone can plan around. Visa’s page says the product “is in the process of development and deployment” and that depictions “are representations of potential features.” Stripe says preview , twice, and lists 34 countries by name. The rest say nothing.

Say who pays when it goes wrong. Nobody does. It is the Merchant Advisory Group’s central demand, and no protocol on the table answers it.

Three of those four cost nothing. A version number is a string. A status is a word. Naming a live merchant takes one merchant’s permission, and Google got three. Only the fourth is genuinely difficult, and it is the one merchants have been asking for out loud since Zurich. Mastercard’s Agent Pay page calls this “a paradigm shift” offering “unparalleled convenience and efficiency,” and names the challenges as “trust, security and interoperability.” That page names no merchant, carries no version, and states no status.

An unfinished technology is not a scandal. Refusing to say it is unfinished, while merchants’ storefronts are already answering agents, is a choice. Five companies have made that choice, and the merchants carry the risk of it. The premise of this entire category is that a machine can check a claim instead of taking it on trust: signed mandates, tokens scoped to one merchant and one amount, a payment header a server can verify. None of it is documented in a way anyone can check.

So for the love of every single divine entity humans ever invented, publish the version. Publish the status. Name a merchant. Say who pays. Until somebody does, nobody outside these five companies can tell the difference between a payments rail and a press release.

More Resources:

- What Google’s UCP Tells Us About Agent-Ready Websites

- Agentic Commerce And The New Rules Of Google Ads

- Agentic Commerce Optimization: A Technical Guide To Prepare For Google’s UCP

This post was originally published on No Hacks .

Featured Image: tete_escape/Shutterstock

Category SEO AI Search Ecommerce

Read Full Bio

Slobodan Manic Founder of No Hacks and machine-first website optimisation consultant at No Hacks

Slobodan “Sani” Manić is a website optimisation consultant with over 15 years of experience helping businesses make their websites faster, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/agentic-commerce-is-not-the-next-voice-shopping-but-it-is-still-unproven/589439/)
