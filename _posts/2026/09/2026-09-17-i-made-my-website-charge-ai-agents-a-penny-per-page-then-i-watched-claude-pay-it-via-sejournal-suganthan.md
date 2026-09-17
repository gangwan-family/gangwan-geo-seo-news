---
layout: post
title: "I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It via @sejournal, @suganthan"
date: 2026-09-17T19:00:29+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-17/I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It via @sejournal, @suganthan.md"
original_url: "https://www.searchenginejournal.com/i-made-my-website-charge-ai-agents-a-penny-per-page-then-i-watched-claude-pay-it/589447/"
author: "Suganthan Mohanadasan"
categories:
  - "AI Search"
  - "SEO"
  - "_src_search-engine-journal"
---

# I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-09-17
- URL: https://www.searchenginejournal.com/i-made-my-website-charge-ai-agents-a-penny-per-page-then-i-watched-claude-pay-it/589447/
- Author: Suganthan Mohanadasan
- Categories: AI Search, SEO

## RSS 摘要

GPTBot, ClaudeBot, and Googlebot won't pay your price yet. Charge now and you lose citations. Here's what to decide before the dashboard toggle arrives. The post I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It appeared first on Search Engine Journal .

## 原文正文

I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It Skip to content

- SEJ

- ⋅

- SEO

## I Made My Website Charge AI Agents A Penny Per Page, Then I Watched Claude Pay It

Google's AI contribution pilot pays publishers a monthly figure with no calculation behind it. I built the alternative: my page charges agents before they read.

Google is paying some publishers when their content helps generate its AI answers.

Barry Schwartz covered it at Search Engine Roundtable on September 14 , following Digiday’s report that morning. Google confirmed the program to Digiday. It’s called the AI contribution pilot .

Publishers who accept the terms get an earnings figure in Search Console each month. What they don’t get is a breakdown of how Google calculated it.

Google pays when it decides a page contributed significantly to an answer while it was being generated in AI Overviews, AI Mode, or the Gemini app. If the page only gets linked after the answer has been written, it doesn’t qualify.

I’m not in the pilot. According to Digiday, Google has approached at least dozens of publishers, with smaller publishers showing more interest than the larger ones. One executive familiar with it described it as a black box. Barry had actually found the help page back in April , but it wasn’t clear then what the feature did.

The sign-up screen publishers in the pilot see in Search Console. Image published by Search Engine Land on 14 September 2026.

I’ve been testing a different approach on my own site since August.

My page sets a price before an agent reads it. If the agent wants access, it pays.

On the morning of September 15, five payments went through. Each one settled on a blockchain and has a public transaction hash. One came from Claude Code, running on my machine and using a wallet I’d set up for it.

To be clear, all the payments so far have come from my own agents. No search crawler is turning up and paying me. The payments also use testnet USDC , which means the tokens have no real monetary value.

But the payment process works. An agent requests a page, checks the price, pays and receives the content. Cloudflare is building products around that same idea, and I wanted to understand how it works before it becomes another setting in a dashboard.

Image Credit: Suganthan Mohanadasan

### What That Cloudflare Wallet Handle Is For

Screenshot from X , September 2026

On August 4, during Agents Week, Cloudflare announced Wallets and opened handle reservations.

Claiming a handle is free. I suspect plenty of people grabbed theirs the way we grab usernames : quickly, before someone else gets there, with a vague intention of reading the details later.

If you did that, this is the kind of thing those wallets are being built for.

Cloudflare’s design has two parts :

- Account Wallets belong to people. You add funds, set spending limits, and allocate money to your agents.

- Virtual Wallets are for the agents. They spend within the permissions and limits you’ve set.

Your handle gives that account a recognizable identity.

As of September 15, though, reserving a handle gets you a page displaying the name and a notification when Wallets becomes available. Cloudflare’s documentation explicitly says a reserved handle can’t yet send, receive, or hold funds.

The other part is the Monetization Gateway , which will let sites charge agents for access to resources. Cloudflare announced it on July 1 , and access is still through the waitlist linked from that announcement.

So the products are announced, but you can’t yet use a reserved wallet handle to run this whole process.

My demo shows what that process looks like today using x402. The site charges one cent per page; my agent pays, and spending limits control what it can buy. It’s the same general arrangement Cloudflare describes for Virtual Wallets.

### Why Charge Crawlers At All?

The arrangement between search engines and websites used to be fairly straightforward. Search engines crawled your content, showed it in their results, and sent visitors back.

Publishers got traffic. Search engines got something useful to show their users.

AI answers have changed that arrangement. An agent can read your page, use the information in its response, and answer the user without sending them to your site .

I’ve spent months looking at what these systems actually fetch . There’s plenty of crawling. The traffic coming back often doesn’t reflect it.

Publishers have responded in different ways, partly depending on how much negotiating power they have.

Smaller sites often block AI crawlers . I understand why. If someone is taking your content and you’re getting little in return, blocking them is a reasonable response. But it comes with a trade-off: restricting access can also reduce your visibility in training datasets and AI answers .

Large publishers can negotiate licensing deals . News Corp, the Financial Times and Reddit all have agreements with AI companies. According to Press Gazette’s reporting on 4 September , People Inc.’s chief executive told investors that blocking crawlers through Cloudflare had helped bring AI companies to the negotiating table.

Google’s pilot offers another approach: paying publishers according to the value their content contributes to AI answers.

In that same Press Gazette piece, Cloudflare said it was moving its own default approach from pay per crawl towards pay per use, with pilots involving Ceramic.ai and You.com. Its reasoning was that fetching a page doesn’t prove the content was actually used.

I think that distinction matters.

Using a page to answer a question is a stronger indication of value than simply downloading it. But it’s also something the website owner can’t independently observe. Once my page has left my server, I can’t see whether it influenced an answer.

With pay per use, I’m relying on the platform to tell me what happened and what it was worth. With pay per crawl, I can check the request and the payment myself.

Google’s eligibility rules make this particularly clear. As Barry Schwartz explains , contributing during answer generation can earn a payment. Being linked afterwards doesn’t. The publisher sees the total, without the calculation behind it.

Each approach leaves something unresolved.

Blocking earns nothing directly. Individual licensing agreements don’t scale to millions of small websites. Revenue-sharing arrangements leave the platform deciding how much to pay.

Putting a price into the request gives a site a standard way to sell access. An agent can accept that price and receive the content, with a receipt for the transaction. There’s no need to negotiate a separate commercial agreement with every buyer.

That’s the pay-per-crawl model I wanted to test.

Cloudflare already has a product called Pay Per Crawl , but it’s still in closed beta. On the paying side, bot operators need verification through Web Bot Auth , Stripe onboarding, and program approval.

My personal agent can’t simply join that program.

So I built a version using the open x402 protocol , which Cloudflare is also using for its upcoming Monetization Gateway. My demo makes actual x402 payments independently of Cloudflare’s closed Pay Per Crawl programme.

### How x402 Works

HTTP has included a status code called 402 Payment Required since 1997. The specification reserved it for future use.

Twenty-nine years later, x402 gives it a practical purpose.

In my setup, the exchange has four steps:

- The agent requests a page. The server responds with 402 Payment Required , including a PAYMENT-REQUIRED header that describes the price and payment requirements.

- The agent signs an authorisation to transfer the exact amount in USDC. It then retries the request with a PAYMENT-SIGNATURE header.

- A payment facilitator verifies the signature and settles the transaction on the blockchain. My demo uses Coinbase’s facilitator at x402.org .

- The server returns the content, along with a PAYMENT-RESPONSE header containing the settlement receipt.

Here’s the offer from my site, decoded from a live 402 response this morning:

{ "x402Version": 2, "accepts": [{ "scheme": "exact", "network": "eip155:84532", "amount": "10000", "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e", "payTo": "0xEdF2444D0259BBB8aC5094216D0148938F8308ff", "maxTimeoutSeconds": 300, "extra": { "name": "USDC", "version": "2" } }] }

That offer asks for one cent in testnet USDC on Base Sepolia , paid to the burner wallet I’m using for the demo.

USDC uses six decimal places, so 10000 represents 0.01 USDC .

A compatible client can read those payment requirements and pay without creating an account with my site or asking me for an API key.

That’s a useful difference from robots.txt . A rule in robots.txt depends on a crawler choosing to respect it . Here, the server can withhold the protected content until payment succeeds.

The buyer wallet also held zero ETH , yet every settlement went through. The facilitator submitted the transactions and covered the blockchain transaction fees, usually called gas. I checked the balances twice.

For this setup, the agent only needed the testnet USDC it was spending.

There’s broader industry support behind the protocol too. The x402 Foundation became operational under the Linux Foundation on 14 July , with 40 members, including Visa, Mastercard, Google, AWS, Stripe and Cloudflare.

That’s useful context, but the actual exchange is still those four steps.

### What’s Running On My Site

The demo is at paid.suganthan.com .

It runs on a Cloudflare Worker, using roughly 300 lines of Hono code and the x402 middleware. It’s been running since August 8, and the public earnings page records every paid crawl since then.

There are three routes:

- The landing page is free and explains the demo.

- /research/agentic-seo/ charges $0.01 per crawl.

- /earnings/ shows the running total, timestamps, payer addresses, and transaction hashes.

Request the article with curl, and you’ll get this:

$ curl -i https://paid.suganthan.com/research/agentic-seo/ HTTP/2 402 payment-required: eyJ4NDAyVmVyc2lvbiI6MiwiZXJyb3Ii...

Image Credit: Suganthan Mohanadasan

Open the same URL in a browser, and you get a page explaining the charge. It still returns HTTP status 402 , but a human visitor gets something readable.

There’s also a preview button. That opens the article for free with a banner, so you can inspect the content as well as the payment screen.

Image Credit: Suganthan Mohanadasan

I built another mode that isn’t enabled in the demo. Changing one variable makes the Worker charge only requests that identify themselves as known AI crawlers, including GPTBot, ClaudeBot, and PerplexityBot. Human visitors can browse for free.

I tested that mode using spoofed user-agent strings, and it behaved as expected.

Of course, those strings can be faked. Checking a user agent is enough to demonstrate the behaviour, but it doesn’t prove who made the request. Cloudflare’s approach uses cryptographic verification of crawler identity to address that problem.

### Giving The Agent A Budget

The buyer is a small Node script. Before it pays, it checks whether the request fits its budget.

I gave it two limits:

- A maximum of $0.05 per call .

- A $0.25 daily allowance , recorded in a spending ledger on disk.

The script decodes the payment offer and checks both limits before authorizing anything.

If the request is within budget, it pays, retries the request, prints the settlement details, and records the spend. If it exceeds either limit, it refuses.

Here’s a refusal with the per-call cap set below the page’s price:

[step 3] Spending guardrails [refused] Price $0.0100 exceeds the per call cap of $0.0010. This agent does not negotiate. Raise MAX_PER_CALL to override.

That refusal is one of the most useful parts of the demo.

If an agent pays every price a server gives it, you haven’t really delegated a budget. You’ve given it a way to empty a wallet.

The spending checks happen before signing. When the request fails those checks, the script exits with code 3 without creating a payment signature.

This follows the same general design Cloudflare describes for its wallets: a person provides the funds and sets the limits, and an agent spends within them. My buyer script demonstrates that behaviour without being an actual Cloudflare Virtual Wallet.

Image Credit: Suganthan Mohandasan

The successful run in the screenshot settled at 07:21 UTC . Two earlier payments went through at 06:10 and 06:11 , with the second still within the daily allowance.

All three appeared on the public earnings page within seconds of confirmation.

The seller’s balance increased, the buyer’s balance decreased, and the amounts matched. The August transactions are still listed underneath them. I haven’t touched the payment code since those earlier payments.

Image Credit: Suganthan Mohanadasan

### Watching Claude Pay During A Task

This was the part I was most interested in.

Claude Code supports hooks: scripts that can run around tool calls. Cloudflare documents a pattern that watches WebFetch , and I connected that pattern to my wallet.

The process works like this:

- Claude tries to fetch a page and encounters a 402 .

- The hook requests the payment offer itself.

- It checks the price against the per-call spending cap.

- If the price is allowed, it pays and retrieves the content.

- It passes the content and receipt back to Claude as additional context.

Claude can then continue with its task. I don’t have to stop what I’m doing and manually pay for the page.

That’s what happened in the session shown near the top of this article. The hook returned this receipt:

Paid $0.0100 for "https://paid.suganthan.com/research/agentic-seo/" via x402. Settlement tx: 0x51b5eba4fb34ddff27052d89cb79ae3d748b379800a723a6f4f020c11e2871c9

You can inspect the transaction on BaseScan .

Claude encountered a payment requirement during a task, and the hook handled it within the budget I’d set. It paid one testnet cent, returned the article, and let Claude carry on.

If the price exceeds the cap, the hook refuses and tells Claude to show the price to the human instead.

I quite like that boundary. Claude can buy a page when it needs one, but it can’t decide on its own that my five-cent limit no longer applies.

### Should You Start Charging For Your Pages?

I wouldn’t do it this month expecting search crawlers to pay you.

The software for paying agents is developing quickly. The crawlers that most site owners care about haven’t caught up.

AWS made AgentCore payments generally available on August 18 . An agent using it can encounter a 402 during a task and pay through x402, much like my Claude hook. Cloudflare’s Agents SDK also has a client that can make payments.

But that doesn’t mean GPTBot, ClaudeBot, PerplexityBot, or Googlebot will arrive at your site with a wallet and pay your asking price.

Until those crawlers support the process, requiring payment prevents them from retrieving the protected content. You could lose access to the systems that surface and cite your work without earning anything in return.

I’d also be careful with the transaction numbers being used to describe this market.

Decrypt reported on September 13 that TRM Labs had examined 198.9 million x402 settlements . Its analysis suggested that most of the payment volume wasn’t coming from AI agents.

Scheduled scripts, load tests, and payments between accounts controlled by the same party can all produce similar blockchain records. TRM’s methods also can’t conclusively distinguish an agent from a script, so the estimates have limits.

A large number of transactions tells us that the payment infrastructure is being used. It doesn’t, by itself, tell us that autonomous agents are buying useful things from independent websites.

My own demo makes that distinction fairly obvious. The payments work, but I’m on both sides of them.

What I would think about now is which parts of your site you might eventually charge for .

I don’t think the answer is every page.

Being cited in an AI answer still has value. General explainers may be worth keeping freely accessible because they help people discover your work.

Original datasets, research, and useful tools are more obvious candidates for paid access. An agent may need something specific from those resources to finish a task. Charging for that individual request makes more sense than trying to fit a machine into an advertising or subscription model designed around human readers.

Google’s pilot approaches that value question from the platform’s side. It pays when content contributes to the answer, rather than simply appearing as a link underneath it.

For a site owner, the practical questions become: What is the agent getting, what should that access cost, and who decides?

My expectation is that adoption will become easier when products such as Cloudflare’s Monetization Gateway move beyond their waitlists. Charging for a resource could become a routine configuration choice for a large number of websites.

I’d rather have thought through what to charge for before that option appears in the dashboard.

And if Google offers you a monthly payment in the meantime, ask how it was calculated. Digiday’s reporting describes limited transparency, and one publishing executive argued that accepting early terms could weaken publishers’ position in future negotiations. Those terms deserve as much attention as the payment itself.

### Moving From Test Tokens To Real Money

Everything in this demo has used testnet tokens. The payments haven’t cost me real money.

The code also supports the real Base network. In my setup, the NETWORK setting switches from base-sepolia to base , moving the payment flow to real USDC.

My next step is to run exactly one real transaction.

When an agent pays my site its first real cent, I’ll put the transaction hash in the next post.

And when those reserved Cloudflare handles become working wallets, this is the kind of process they’ll support: an agent finds something it needs, checks the price against its budget, pays, and carries on.

The demo is staying online in the meantime. Try the curl request, inspect the payment offer, and have a look at the public earnings page .

More Resources:

- Should I Block AI Crawlers Or Measure Their Value First? – Ask An SEO

- Cloudflare’s AI Crawler Rules Can Block Googlebot

- Google Claims AI Training Is Fair Use In New Governance Paper

This post was originally published on Suganthan .

Featured Image: SvetaZi/Shutterstock

Category SEO AI Search

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

Suganthan Mohanadasan is the co-founder of Snippet Digital, an AI SEO agency, and Keyword Insights, an AI content intelligence platform. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/i-made-my-website-charge-ai-agents-a-penny-per-page-then-i-watched-claude-pay-it/589447/)
