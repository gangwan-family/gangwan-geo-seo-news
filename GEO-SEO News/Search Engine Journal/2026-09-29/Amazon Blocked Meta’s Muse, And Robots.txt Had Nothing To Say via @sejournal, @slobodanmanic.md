---
title: "Amazon Blocked Meta’s Muse, And Robots.txt Had Nothing To Say via @sejournal, @slobodanmanic"
source: "Search Engine Journal"
published: 2026-09-29T14:30:54+00:00
fetched_at: 2026-09-30T00:37:08.848595+00:00
url: "https://www.searchenginejournal.com/amazon-blocked-metas-muse-and-robots-txt-had-nothing-to-say/590494/"
guid: "https://www.searchenginejournal.com/amazon-blocked-metas-muse-and-robots-txt-had-nothing-to-say/590494/"
author: "Slobodan Manic"
categories:
  - "AI Search"
  - "SEO"
---

# Amazon Blocked Meta’s Muse, And Robots.txt Had Nothing To Say via @sejournal, @slobodanmanic

- Source: Search Engine Journal
- Published: 2026-09-29
- URL: https://www.searchenginejournal.com/amazon-blocked-metas-muse-and-robots-txt-had-nothing-to-say/590494/
- Author: Slobodan Manic
- Categories: AI Search, SEO

## RSS 摘要

Any website can write Amazon's block-page sentence into its own terms. Spotting an agent that looks like a shopper is the hard part. The post Amazon Blocked Meta’s Muse, And Robots.txt Had Nothing To Say appeared first on Search Engine Journal .

## 原文正文

Amazon Blocked Meta's Muse, And Robots.txt Had Nothing To Say Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- SEO

## Amazon Blocked Meta’s Muse, And Robots.txt Had Nothing To Say

Amazon blocked Meta's Muse with its Conditions of Use because robots.txt had no user agent to name and the CFAA was gone.

On the night of Sept. 20, 2026, shoppers who sent Meta’s shopping agent Muse to amazon.com got a page that said: “Continued access by an unauthorized AI agent violates Amazon’s Conditions of Use, to which our customers have agreed.” Todd Bishop reported it for GeekWire that night, with Amazon confirming the block.

A website owner who has spotted an automated visitor and wants it gone has a few controls, and Amazon reached for terms of service, the agreement with whoever is logged in.

The second control, robots.txt, had nothing to work with. A rule in that file names a user agent string , the label a piece of software sends when it asks a website for a page, and then states what that software may fetch. Meta’s crawler documentation gives none for Muse. Also, robots.txt can’t enforce the rule .

The Computer Fraud and Abuse Act (CFAA), the 1986 anti-hacking statute, had got much weaker for Amazon on Aug. 4, 2026. That was the day the Ninth Circuit, a U.S. federal appeals court, threw out a court order Amazon had won against Perplexity and ruled that the shopper, not the agent’s vendor, is the one accessing the website.

### Amazon’s Conditions Of Use Is An Agreement With The Human Shopper, Not With Meta

Conditions of Use is the agreement a shopper accepts when they open an Amazon account, and Meta has nothing to do with it. Amazon gave GeekWire three reasons: Meta never told Amazon that Muse would access its store, the agent “doesn’t identify itself when it browses”, and it “appears to capture and store customer credentials,” which Amazon says could create privacy and security risks. An Amazon spokesperson told GeekWire that third-party applications making purchases on a customer’s behalf “should operate openly and respect service provider decisions about whether or not to participate.”

All three reasons are complaints about Meta, and the document Amazon is enforcing binds the shopper. Amazon has separately asked Meta to remove Amazon from the Muse experience.

### Muse Has No User Agent String, So Amazon’s Robots.txt Cannot Refuse It

Meta’s crawler documentation lists five agents and Muse is not among them, so Amazon has no name to put in the rule.

Amazon’s robots.txt, fetched from amazon.com/robots.txt on 22 September 2026, declares 101 user agent blocks, 100 of which carry Disallow: / , the line that refuses an agent the entire website. ClaudeBot is listed twice, so those hundred blocks name 99 distinct agents. GPTBot, CCBot, PerplexityBot, ClaudeBot, Google-Extended, GoogleAgent-Mariner and GoogleAgent-Shopping are refused everything.

Meta appears three times in Amazon’s robots.txt. meta-externalagent crawls for model training and indexing, meta-externalfetcher fetches individual links at a user’s request, and meta-webindexer improves Meta AI search results. All three get Disallow: / , meaning Amazon tells them not to read any pages.

Two of Meta’s five documented crawlers are absent from the named blocks, so they fall under the general User-agent: * rules like any crawler Amazon has not named , and those rules instruct crawlers to stay out of the cart, sign-in, and account paths while leaving product pages open. FacebookExternalHit is how a shared Amazon link gets its preview inside Meta’s apps, and Meta-ExternalAds supports Meta’s advertising business.

### Meta Said That Muse Would Appear As Your Own Activity

Meta’s wording, published on Sept. 8, 2026 in the engineering account of the design that went out the day Muse launched, is that when Muse browses the internet it “will appear as your activity.” Meta puts that in a section on data policy, disclosing that how a person uses Muse can influence the ads they see. The agent drives “a real up-to-date Chromium based browser,” so the website on the other end records an ordinary customer session . I went through the post at the time . Muse is U.S. only and free with paid tiers, and neither Meta’s launch post nor GeekWire gives a number for how many people shop through it. I expect Meta to either proudly share a number soon, or not share one at all.

Twelve days later, on September 20, Amazon says the agent “doesn’t identify itself when it browses.” Amazon was able to tell Muse sessions apart from ordinary shoppers, and then served them a different page. Neither Amazon nor GeekWire says how Amazon did this.

### Amazon Published No Evidence For Its Credential Claim

Amazon says Muse “appears to capture and store customer credentials.” Meta had published on launch day where Muse stores them. The credentials are held by a background service called authd, inside the virtual machine Meta gives each Muse user, a computer that runs as software on hardware somewhere else. Meta’s wording is “stored in your VM, not in centralized Meta infrastructure.” The agent itself works only from surrogate tokens, stand-ins for the real credential. Meta’s wording is that a component called Sentinel “will replace any surrogate tokens with the real credential, obtained from authd, at the network boundary.” On Meta’s description the model never sees the credentials, and I have found no independent check of that in the coverage of the block as of September 22.

So Amazon raised as a concern something Meta had published, and the part Amazon added, that this could create privacy and security risks, came with no captured request, no named endpoint and no disclosure timeline.

Of course Amazon has a shopping agent of its own and an advertising business built on people looking at its pages. Alexa for Shopping launched in May 2026, as GeekWire notes. Amazon made more than 68 billion dollars in ad revenue in 2025, by GeekWire’s figure, from a business that “depends on people browsing its pages and seeing sponsored products.” And GeekWire records Amazon’s point that its other agent, Buy for Me, identifies itself and lets brands opt out, which is the behavior Amazon is asking of Meta.

Meta had not answered by the time GeekWire published, and I have found no response in the coverage since, as of September 22. Nothing a shopper can run from outside Meta’s VM settles the credential claim. Two things would settle it: Meta opening the VM to an independent audit, or Amazon producing whatever their “appears to” rests on.

### Amazon Already Lost This Argument Against Perplexity, And The Court Left Muse’s Case Open

Amazon had already tried the courts against Perplexity, and lost. It sued over Comet, a browser that logs into a shopper’s Amazon account and buys on their behalf, and in March 2026 it won a court order keeping Perplexity’s agent out of the password-protected parts of the store while the case ran. The Ninth Circuit put that order on hold, heard the appeal on June 11, and threw the order out on August 4.

Comet runs on the shopper’s own computer, so Perplexity’s machines never talk to Amazon’s. That is where the court started. It ruled that the shopper is the one visiting Amazon, not the company that wrote the software, and quoted a brief from the Electronic Frontier Foundation and four other outside groups: “Perplexity’s servers never directly access Amazon’s servers.” The case is written up in full here .

Amazon asked for the case to be reheard by a larger group of judges, which lawyers call going en banc. In this circuit, that is 11: the Chief Judge and 10 drawn by lot, rather than every judge on the bench. On September 10, the court refused , and not one judge asked for a vote on it.

So in this circuit the anti-hacking law is mostly gone as a tool against an agent, a person sent , and what the court left Amazon was its own terms of service. Twelve days after Muse launched and ten days after that refusal, Amazon put a Conditions of Use notice in front of its own shoppers.

There is one question the Ninth Circuit did not answer, and it wrote the reservation into the opinion : “We do not address whether, on a different record or new facts, Perplexity may exercise control over the Assistant in such a way as to gain entry to Amazon’s servers.” That is the case where the software company, not the shopper, is the one running the agent.

Muse does not run on the shopper’s machine. Meta’s own description is that “you and your Muse share your own dedicated computer in the cloud,” an “isolated Linux box” reachable from WhatsApp, the Muse apps and muse.ai . Meta names no hosting provider. GeekWire notes that Meta signed a multibillion-dollar deal in April 2026 to run agentic AI workloads on Graviton, the server processors Amazon designs for its own cloud, and neither company has said whether Muse is among those workloads. If Muse is among them, Amazon is blocking an agent that runs on hardware Amazon rents out .

### Conditions Of Use Was The Only Reason Amazon Could Put On The Page Without A Name Or A Lawsuit

Amazon’s Conditions of Use reached Muse because the shopper running Muse had already accepted those terms, and neither robots.txt nor the Computer Fraud and Abuse Act had that hold. Terms of service bind your customer, so enforcing them means telling the person who was trying to buy something that the way they chose to shop is not allowed. That is the sentence on Amazon’s block page. It’s more honest than yelling CFAA, anyway.

Anyone can write that sentence in their own terms. What Amazon has not explained is how it spotted Muse in the first place, and until it does, this is something Amazon did rather than something any website can do.

More Resources:

- OpenAI Says Robots.txt May Not Apply To ChatGPT’s Fetch Bot

- Google Lost Its Scraping Case – Now You Have To Pick A Side On The Open Web

- Google-Agent: The Web’s New Visitor Just Got An Identity

This post was originally published on No Hacks .

Featured Image: Roman Samborskyi/Shutterstock

Category SEO AI Search

Read Full Bio

Slobodan Manic Founder of No Hacks and machine-first website optimisation consultant at No Hacks

Slobodan “Sani” Manić is a website optimisation consultant with over 15 years of experience helping businesses make their websites faster, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/amazon-blocked-metas-muse-and-robots-txt-had-nothing-to-say/590494/)
