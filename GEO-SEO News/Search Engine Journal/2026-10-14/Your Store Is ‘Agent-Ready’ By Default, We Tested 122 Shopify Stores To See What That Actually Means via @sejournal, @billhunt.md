---
title: "Your Store Is ‘Agent-Ready’ By Default, We Tested 122 Shopify Stores To See What That Actually Means via @sejournal, @billhunt"
source: "Search Engine Journal"
published: 2026-10-14T12:00:06+00:00
fetched_at: 2026-10-14T23:59:16.528335+00:00
url: "https://www.searchenginejournal.com/your-store-is-agent-ready-by-default-we-tested-122-shopify-stores/591767/"
guid: "https://www.searchenginejournal.com/your-store-is-agent-ready-by-default-we-tested-122-shopify-stores/591767/"
author: "Bill Hunt"
categories:
  - "AI Search"
  - "SEO"
  - "Search Visibility & Value"
---

# Your Store Is ‘Agent-Ready’ By Default, We Tested 122 Shopify Stores To See What That Actually Means via @sejournal, @billhunt

- Source: Search Engine Journal
- Published: 2026-10-14
- URL: https://www.searchenginejournal.com/your-store-is-agent-ready-by-default-we-tested-122-shopify-stores/591767/
- Author: Bill Hunt
- Categories: AI Search, SEO, Search Visibility & Value

## RSS 摘要

A store can look agent-ready by default and still fail the moment a buyer asks about shipping, pickup, or cancellation. Here's what to verify. The post Your Store Is ‘Agent-Ready’ By Default, We Tested 122 Shopify Stores To See What That Actually Means appeared first on Search Engine Journal .

## 原文正文

Your Store Is "Agent-Ready" By Default, We Tested 122 Shopify Stores Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- AI Search

## Your Store Is ‘Agent-Ready’ By Default, We Tested 122 Shopify Stores To See What That Actually Means

From testing top Shopify stores, Bill Hunt found agents can build a checkout, but can’t answer basic delivery or cancellation questions.

In September 2026, Slobodan Manic argued that the text-only versions of websites now being served to AI “strip out the wrong layer.” A markdown mirror describes the page but drops everything a visitor could press, so it becomes “a brochure … served to the user most eager to act.”

He ends with a brilliant three-part list that every ecommerce team should adopt: expose what can be done, make it callable , and report what happened.

I had been running an audit of the top 122 Shopify storefronts with a related question: not whether AI can find or cite these stores, but whether an agent can actually resolve a purchase decision on them. That means having enough information, context, rules, and the capability to execute to answer the buyer’s questions, commit to the purchase, and deal with what comes after.

His article prompted me to go further. Instead of counting which tools the stores declared, I called them. This article reports what we found, confirms his argument, shows where our results differ, and outlines what both merchants and Shopify can do about it.

### Where Manic Is Right, And What Our Data Confirms

The platform installed the actions, not the merchants. Manic reports that Shopify switched on WebMCP tools for every Liquid storefront on August 5, and that “the merchants did not build it.” Our data shows the same thing at scale:

- 76 of 86 product pages we collected load the same Shopify WebMCP adapter script.

- 89 of 122 stores serve an /agents.md file. 83 of those 89 are near-identical copies of one Shopify-generated template. Only five in the entire sample were written by the merchant.

If you count adoption of agents.md as a sign of merchant readiness, you are really measuring Shopify’s rollout schedule.

GEO does not address the action. Manic writes that GEO “has absolutely nothing to do with the action.” Our data backs this up. Most stores publish the facts an agent needs, and Shopify’s checkout works. What breaks is the step in between: turning a published policy into an answer the agent can use when making its decision. The return window appears as prose on a policy page, but the agent can’t retrieve it when asked. Being cited or ranked doesn’t fix that.

The semantic floor is broken, including on product pages. He cites WebAIM’s 2026 finding that unlabelled form inputs appear on 51% of home pages, empty links on 46.3%, and empty buttons on 30.6%. We ran the same checks on the product page, where the purchase action actually lives, for the 68 stores we could retrieve:

Check on the product page

Stores

At least one unlabelled input

47%

At least one empty link

46%

At least one empty button

37%

Size or option dropdown with no label

65% of stores that use dropdowns

No add-to-cart control in the server HTML at all

19 of 68

Passes the full floor (native, named buy button; labeled controls; a live region to announce results)

31 of 68

The buy button itself is usually fine. When it is present, it is a native, named <button> 92% of the time. The problem is around it. If two-thirds of size selectors have no label, an agent cannot reliably tell which dropdown sets the size and which sets the color.

This is where UX, accessibility, and agent readiness must work together because they depend on the same markup. A labeled size selector, a named buy button, and an announced “added to cart” message serve a screen-reader user, a keyboard user, and a browser agent at once. The conflicts stem from a visual-only design: swatches with no names and confirmations that only appear on screen. Fix the markup once and all three benefit.

### Credit Where It Is Due: What Shopify Built

Huge props to Shopify as nobody else has deployed an agent-callable commerce surface at this scale, and that deserves recognition before any criticism.

Across our sample, 89 of 122 stores answered a standard MCP tool listing. Shopify says its catalog now spans “billions of products across millions of merchants,” and that orders from AI-powered searches grew nearly 13 times year over year in Q1 2026 . Merchants on the platform received catalog search, cart, checkout, and policy lookup tools without writing a line of code.

The quality is also better than I expected. We ran a live, non-completing checkout on every store that exposed the Universal Commerce Protocol (UCP) endpoint: create a checkout for one in-stock item going to a Boston address, read it back, cancel it, then cancel it again. We never completed a purchase or sent payment details.

Behavior

Result across 74 live checkouts

Checkout created when given a current, in-stock item

74 of 74

Typed status returned on every step

74 of 74

Coded error messages with a severity level

74 of 74

Checkout readable after creation

74 of 74

Cancel confirmed as canceled

74 of 74

Repeat cancel refused with a coded error

74 of 74

A handoff URL returned so the agent can pass to a human

74 of 74

This bears directly on the third item on Manic’s list. He describes an agent that re-submitted a form because the only confirmation was “rendered for eyes.” On Shopify’s tool layer, that failure is handled: the second cancel is refused with a machine-readable error instead of being silently repeated. On that test, Shopify’s tools already report back to the agent properly.

### Where Our Results Differ

These are differences of timing and scope, not disagreements.

1. We Tested A Different Door, And Shopify Has Since Finished His

Shopify offers agents two routes into checkout. The first is a server endpoint that an agent calls directly, with no browser (UCP over MCP). The second is WebMCP: tools that register inside the shopper’s own browser tab . Manic tested the browser route on August 6 and found that “the buying path died on an internal error.” At that point, the browser tools covered the storefront and cart, and the checkout step mostly moved the tab to the checkout page.

Our updated September test used the server route. Checkout creation succeeded on every store we gave a real, in-stock item, with a median response time of about 1.1 seconds. The only failures came from our own stale data. We had collected item IDs a few weeks earlier. By test day, five of those items had sold out, and two IDs no longer existed. The stores rejected them with clean out_of_stock or invalid codes (“The merchandise with id … does not exist”). So our result does not show that his defect was fixed. We were testing a different route.

That small failure is still a lesson for merchants, because agents work the same way we did. An assistant may hold an item ID from a product feed, an earlier conversation, or a shared cart, and try to buy it days later. A sold-out item is normal commerce, as long as every surface an agent reads reports availability promptly. A vanished ID is avoidable. It usually happens when a product is deleted and re-created, or re-imported, instead of edited, and the agent then has to start its search over. Keep variant IDs stable, and keep inventory current across your feeds and catalog .

Then, on September 28, Shopify announced support for WebMCP in checkout . Browser agents can now “read and update Shopify checkouts,” covering “the full shopping journey… through checkout and order confirmation,” with no merchant configuration. On September 30, we ran a new test and opened live checkouts at a sample of sites in a browser, with WebMCP exposed to the page. Both registered the four announced tools: get_checkout, update_checkout, complete_checkout, and navigate_to_storefront. A read-only get_checkout call returned the full checkout: line items, totals with tax, fulfillment method, and coded messages showing which fields were still missing. We did not submit an order, but the browser route that failed for Manic now reaches and reads the checkout properly.

The tool descriptions also answer his point about agents repeating actions. They tell the agent to “use get_checkout to verify the outcome” and “do not resubmit while status is complete_in_progress or completed.” That’s the “report what happened” requirement, written directly into the tools.

#### 2. ‘Callable’ Is Not The Same As ‘Completable’

Every one of the 74 checkouts came back with the status requires_escalation and a message flagged requires_buyer_input. This matches the rule in Shopify’s default agents.md that checkout requires human approval. That is a reasonable safety choice, and it changes what “agent-ready” means. The new browser tools keep the same rule: complete_checkout is to be used “only after the buyer authorizes the purchase,” and control goes back to the buyer for steps such as 3D Secure . On Shopify today, the agent builds a priced cart, and a person commits the money.

#### 3. His List Stops At The Action; The Buying Decision Also Needs Rules And A Way Back

An agent can act on a decision only after making one. Manic’s framework covers the doing. Our audit asked whether the agent has what it needs to make a decision and whether it can undo the result. On both, the answer was mostly no, and the September 28 release doesn’t change that. In the browser checkout, the refund terms still reach the agent only as a link to the refund policy page, not as values. get_checkout reads “post-completion order details,” but no tool cancels or changes the order. At one site, the checkout also contained a line item the shopper hadn’t chosen, “Free Returns Coverage” for $2.98, added by the store. The agent can see it, but nothing in the checkout data marks it as optional or explains how to remove it. That’s a rule the buyer needs before committing, and it’s exactly the kind of thing the tools don’t explain.

### The ‘Ready By Default’ Trap

This is the part I most want ecommerce leaders to take away. It is easy to look at a Shopify store today and conclude it is agent-ready : the agents.md file exists, the UCP profile exists, the MCP tools answer, and many readiness checkers will score the store well.

What the defaults don’t give you: declared is not the same as done.

The agent can’t find the answers to buyers’ questions. Every store with Shopify’s policy tool was asked six questions that a real buyer would ask. We then ran a control test with broad, policy-style questions.

Questions asked of the store’s own policy tool

Returned anything

Gave a usable answer

“What is your shipping policy?” (control)

32 of 32

not scored

“What is your cancellation policy?” (control)

32 of 32

not scored

“What is the return window for this item?”

88 of 88

70 of 88

“What does shipping cost to Boston, and when will it arrive?”

1 of 88

0 of 88

“Can I cancel an order after placing it, and by when?”

8 of 88

2 of 88

“Can used or open-box items be returned?”

88 of 88

5 of 88

Return windows are the one clear success. For everything else, the content is there, and the tool can reach it when the question sounds like a policy page. It cannot reach it when the question sounds like a buyer. One store’s FAQ says “free standard ground shipping on U.S. orders over $75,” and that answer never comes back for a question about what shipping costs.

Worse, when asked about cancellation, two stores instead returned their shipping FAQ. A wrong answer that looks confident is more dangerous than no answer, because an agent has no reliable way to tell it doesn’t address the question.

Delivery date is missing everywhere. A live checkout priced shipping to Boston for 36 of 74 stores, so for half the sample you can get the cost, but only by starting a purchase. None of the 74 returned an arrival estimate or a carrier, even though the protocol has fields for both. “When will it arrive?” could not be answered through any agent path on any store we tested.

Pickup is invisible. All 93 stores with a UCP fulfillment declaration list shipping as the only method; none declares pickup. That includes retailers that clearly offer it. A store that documents Pickup in Store, yet its agent endpoint answers “No pickup locations available.” Another offers Click & Collect and declares shipping only. Here, the agent gets a clear, machine-readable answer that is wrong, and it will send the customer to delivery when same-day collection was available.

Most policy information isn’t machine-readable . 70% of the stores whose policy text we could read state a return window in prose. Only 7% of product pages expose it as structured merchantReturnDays.

Nothing can be undone. Not one of the 122 stores exposes a tool to cancel, change, or return an order after it is placed. This is not the merchants’ fault. The UCP order specification defines two operations, reading an order and an order-event webhook, and no operation to cancel or amend one ( UCP ). It even defines a permission scope for “cancellation, returns, and other modifications” without defining how to perform any of them.

#### Cross-Layer Coverage Of 5 Purchase Decision Requirements

Across all nine checks we used to decide whether an agent could complete a purchase decision, zero of 122 stores passed. The best were three stores that reached seven of nine. All three failed the same two: no stated cancellation window, and no way to cancel.

### Why This Is Not A GEO Problem

When we sorted the failures by the team that owns the missing information, a pattern appeared:

What’s missing

Who owns it

Pickup availability and cutoff

Fulfillment / Stores

Delivery estimate

Fulfilment

Cancellation window and ability

Order management

Used and open-box exceptions

Legal / Customer service

Return window as data

Legal

None of these teams owns the website. The checks nearly every store passes are the ones the platform generates automatically: catalog, variants, price, checkout. The ones nearly every store fails to meet need someone outside the web team to write a commercial rule and a system to enforce it. That is an organizational problem, and the search team cannot fix it alone .

### What Shopify Could Change

Because Shopify is deployed at this scale, it can also fix much of this at scale. Several of the gaps involve data Shopify already holds in structured form.

- Put the merchant’s own rules in the agent surfaces. Shopify’s return and cancellation rules already store a return window (14, 30, or 90 days, unlimited, or custom), per-product overrides, final-sale designations, return shipping fees, restocking fees, and a cancellation window for unfulfilled items (“No cancellations,” “Until item is fulfilled,” 15 minutes, 1 hour, or 24 hours) ( Shopify Help Center ). Where a merchant has set these, they are exactly the values missing from the default agents.md, the policy tool, and product-page structured data. Generating those surfaces from these settings would close the biggest gap in one release.

- Pass delivery dates through to the protocol. Shopify already supports manual and automated delivery dates at checkout ( Shopify Help Center ). The UCP fulfillment option has earliest and latest fulfillment time fields, and they came back empty on all 74 checkouts. From outside,e we can’t tell whether merchants have delivery dates switched off or whether they aren’t being passed through. Shopify can tell and close the gap for everyone who has them switched on.

- Declare pickup when the merchant offers it. Shopify checkout supports pickup at retail locations ( Shopify Help Center ). If a store has pickup enabled, its UCP profile should say so, not default to shipping only.

- Make the policy tool answer buyer questions, and say clearly when it doesn’t know. An empty result and a wrong-topic result both mislead an agent. An explicit “no information on cancellation” is honest and lets the agent hand off.

- Flag leftover robots.txt templates. 51 of the 122 stores block /policies/ in robots.txt . That isn’t Shopify’s current default. Shopify’s own documentation says the rule persists only on themes with an old robots.txt.liquid template, and that deleting the template restores the default ( Shopify Help Center ). A simple admin warning would fix it for large stores that never noticed.

- Distinguish “already canceled” from “never existed.” A repeat cancel currently returns checkout_not_found. A separate already_canceled code would give an agent certainty rather than just an error.

- Lead on the protocol’s missing piece. Shopify describes UCP as covering “cart creation, checkout, payment, and post-purchase” ( Shopify ). The specification does not yet define post-purchase operations. As co-developer, Shopify is best placed to define the cancel, change, and return operations it already supports for customers in their own accounts.

### What Merchants Should Do: Verify, Don’t Assume

You do not need a full audit to find out where your store stands. Most of this takes an afternoon.

Ask your own policy tool the questions buyers ask. This one call shows you what an agent gets back:

curl -s https://YOURSTORE.com/api/mcp \ -H 'Content-Type: application/json' \ -d '{"jsonrpc": "2.0" ,"id":1, "method": "tools/call", "params":{"name":"search_shop_policies_and_faqs", "arguments":{"query": "Can I cancel an order after placing it, and by when?"}}}'

Repeat it for the return window, shipping cost, arrival time at a real address, pickup today, and used or open-box returns. If you get an empty list, a link, or the wrong topic, that’s what the agent gets too.

Then work through this list:

- Set your return and cancellation rules in Shopify admin , and write the same values plainly, as numbers, in your refund and shipping policy pages and FAQ.

- Turn on delivery dates if you can meet them.

- Check /.well-known/ucp.json. If you offer pickup and it says [[“shipping”]] only, raise it with Shopify.

- Check robots.txt for Disallow: /policies/, and remove the old robots.txt.liquid rule if it’s there.

- Replace or extend the default agents.md with your actual return window, cancellation rule, shipping threshold, and pickup options. Five of the top 122 stores have done this.

- Add MerchantReturnPolicy and OfferShippingDetails to product structured data , including itemCondition if you sell used or refurbished stock.

- Run WAVE on your product page , as Manic recommends, and label every size and option selector.

### The Brochure And The Checkout

Manic’s closing line is that a text-only version of a site is a brochure. Our data adds a second half. Shopify has given its merchants a working checkout that an agent can operate. What it hasn’t yet given them, and what most haven’t provided themselves, is the rulebook an agent needs to use it responsibly: how much, how soon, can I collect it, and can I change my mind?

Having the information isn’t enough. An agent needs information, context, rules, and operational capabilities to resolve a customer’s decision. For now, most stores that look ready by default are only ready until the buyer asks a real question.

One thing our test did not measure, and that surprised me most in hindsight: we told each store exactly which item to buy. A real buyer rarely arrives with a variant ID. They need help choosing between sizes, models, and related products, and that decision logic is merchant knowledge no platform can install by default. Shopify can carry it; only the merchant can write it. That’s the next test, and the subject of a future column.

Methodology: 122 leading Shopify storefronts, selected from published rankings of top Shopify merchants, probed between August and September 2026. The layers tested were: agents.md, llms.txt, UCP profiles and MCP tool listings; product-page structured data; the visible text of policy pages; the buyer questions and control questions put to each store’s own policy tool; a non-completing checkout lifecycle test (never calling complete_checkout or sending payment); a static-HTML accessibility check of each product page; and, on September 30, a browser check of the new WebMCP checkout tools at two stores, reading the checkout without submitting it. Requests were rate-limited, and responses that were throttled or blocked were recorded as unknown rather than absent. Coverage varies by test: policy text for 56 stores, policy tool for 88, live checkout for 74, product-page accessibility for 68. Shipping was tested to one Boston address. The accessibility check reads server HTML only, so it understates what JavaScript may add.

More Resources:

- Getting Your Product Into ChatGPT Isn’t The Hard Part, Getting It Through Checkout Is

- The Web Is Growing A Second Layer – Almost A Third Head

- Does My Product Page Copy Still Matter If Agents Read Feeds And Schema? – Ask An SEO

Featured Image: Woonsen16/Shutterstock

Category Search Visibility & Value SEO AI Search

Read Full Bio

Bill Hunt President at Bisan Digital

Bill is a Global Strategist with Bisan Digital, which focuses on helping companies implement and scale Global Digital Marketing Strategies. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/your-store-is-agent-ready-by-default-we-tested-122-shopify-stores/591767/)
