---
layout: post
title: "Meta Published 2 Documents About Muse And Only One Mentions Attacks via @sejournal, @slobodanmanic"
date: 2026-09-15T14:30:08+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-15/Meta Published 2 Documents About Muse And Only One Mentions Attacks via @sejournal, @slobodanmanic.md"
original_url: "https://www.searchenginejournal.com/meta-published-2-documents-about-muse-and-only-one-mentions-attacks/589071/"
author: "Slobodan Manic"
categories:
  - "AI Search"
  - "SEO"
  - "_src_search-engine-journal"
---

# Meta Published 2 Documents About Muse And Only One Mentions Attacks via @sejournal, @slobodanmanic

- Source: Search Engine Journal
- Published: 2026-09-15
- URL: https://www.searchenginejournal.com/meta-published-2-documents-about-muse-and-only-one-mentions-attacks/589071/
- Author: Slobodan Manic
- Categories: AI Search, SEO

## RSS 摘要

Meta published two Muse documents on the same day. One never mentions risk, attack, or prompt injection. The other uses them 39 times. The post Meta Published 2 Documents About Muse And Only One Mentions Attacks appeared first on Search Engine Journal .

## 原文正文

Meta Published 2 Documents About Muse And Only One Mentions Attacks Skip to content

- SEJ

- ⋅

- SEO

## Meta Published 2 Documents About Muse And Only One Mentions Attacks

Muse browses the web as your activity, and only Meta's engineering post says so. Here is what that means for every website it visits.

Meta launched Muse on September 8. In Meta’s own words, it “can open a browser, fill out forms, and negotiate on their behalf,” and when it comes time to pay, it “can check out with Link built by Stripe.” It runs on Muse Secure VM, “a dedicated, virtual machine (VM) that houses both the agent and a person’s data.” U.S. only, in WhatsApp or the Muse app, and coming to AI glasses.

That is the news. It is also not why I am writing this.

Every AI company is now pushing some version of this, and I do not think anyone has said plainly why.

So, I read what Meta actually published. There are two documents, both dated September 8: a consumer announcement and an engineering post. Across the words risk, attack, attacker, mistake, untrusted, and prompt injection , the announcement uses them zero times, and the engineering post uses them 39. Only the engineering post mentions that Muse will appear as your activity to every website it visits.

### Nobody I Know Has Made One Of These Their Main Way Of Working

I have tried these products, and plenty of other people have. I do not know anyone who has made one of them the dominant way they get things done.

I do not know exactly what it is. My guess is they want to show their AI doing something that looks like it can save you time. More performative than anything.

There is a structural reason for that, and it is not that the models are bad. Web UX is built for human eyes, not for machine-readability and interactivity. Every one of these products picks up a browser and drives it, which is why I argued AI browsers were backward . It is the hardest available version of the job: reading an interface designed for a person, guessing at it, and clicking.

The industry’s answer is that the web being built for eyes is a temporary problem they are going to solve. That is wishful thinking, isn’t it? Let’s see them do it first.

### The Shape Keeps Changing While The Pitch Stays The Same

Agentic browsing has taken three distinct product shapes in under two years.

A browser you install and switch to. OpenAI’s Atlas launched in October 2025 , never left macOS, and stopped working on August 9, 2026. OpenAI did not walk away from the idea; it moved it. The help article covering the shutdown is titled “Evolving Atlas into ChatGPT for browser-based agentic work.”

An AI bolted into the browser you already use. Gemini in Chrome , Claude in Chrome.

And now a browser that lives on their machine, which you talk to. That is Muse, and I think it is the best of the three shapes. You should not need to watch an AI work in a browser. Sitting there while a machine clicks through a checkout on your screen is not automation, it is supervision with extra steps. Putting it in a virtual machine somewhere is the right instinct.

But a browser on Meta’s hardware, logged into your accounts, raises real questions about authentication and identity.

### Meta Published 2 Documents On The Same Day

One is the announcement on Meta’s newsroom , written for people who might use Muse. The other is an engineering post, How We Built Safety Into Muse , from Meta Superintelligence Labs. The announcement links to it, so none of this is hidden.

They are not the same story. I pulled the text of both and counted.

The announcement says Meta “built Muse from the ground up to be a safe, secure, private, and widely available personal AI agent,” with “first-of-its-kind privacy, safety, and security protections engineered into it that no other agent provides.” Nothing reaches the internet “unless the Sentinel approves it.” Muse “has no visibility into people’s passwords or payment methods.” It “checks with the person before sensitive actions.”

Every one of those is true, and the engineering post backs each of them with real mechanism.

Here is what the announcement never says. Not once, in roughly six thousand characters.

Risk. Attack. Attacker. Mistake. Untrusted. Prompt injection.

The engineering post uses those thirty-nine times between them. It opens by saying “any agent like this will still make mistakes, and it will sometimes be attacked via the data it reads,” and that Meta “designed the system to assume the agent may be under attack and limit the potential damage.” It says plainly: “Muse can and will still make mistakes.” It offers up to $300,000 for security reports, “including up to $130,000 for successful prompt injection attempts that affect one user.”

That is a company being unusually straight with engineers. Assume it is compromised, contain the damage, here is money if you can break it.

But the two describe the same product as two different things. One is a capability story where safety is a finished property. The other is a containment story where the agent is assumed to be under attack . If you only read the one written for you, you would not know the second exists in that form.

### Only The Engineering Post Says Muse Will Appear As Your Activity

One sentence decides what every website Muse visits sees, and it is absent from the announcement.

“When Muse browses the internet, it will appear as your activity, so if you ask Muse to buy a shirt from a clothing designer’s website, that designer might use your visit to show you an ad on Instagram.”

Meta is describing the design, not conceding a flaw. Muse drives “a real up-to-date Chromium-based browser.” So the designer sees a person. Their analytics records a visit . Their retargeting fires. And the ad chases a human who was doing something else entirely while a virtual machine did the browsing.

That sentence sits in the post written for engineers. It is absent from the one written for the people it happens to.

### There Are 2 Tiers, And Most Websites Are In The Second One

Meta’s engineering post uses the word connector eleven times, and the announcement never uses it once.

For services Meta has a relationship with, there is no browser at all. “For each connector, we worked closely with the service provider to integrate their API.” A negotiated interface, scoped credentials, an allowlist per worker, and a service that knows exactly what it is talking to.

For everyone else, Muse opens Chromium and behaves like you.

So the question a website owner should ask is not whether agents are coming. It is which tier they are in. If you are big enough for Meta to build a connector, you get an interface and a conversation. If you are not, you get a machine wearing your visitor’s face.

### Your Bot Rules, Your Paywall And Your Analytics All Check The Same Thing

Bot rules name crawlers . A paywall for machines checks the name in one line of the request. Analytics counts a visit as human when a browser runs the JavaScript . All of it keys on a machine identifying itself, or on a machine failing to look like a browser.

Muse does neither, and Meta has written that down. Muse is doing something you asked for, with your credentials, under an approval you gave, and Meta disclosed the behavior in a document anyone can read.

### The Alternative Is Being Built By The Same Industry, In Parallel

There is a whole set of agentic protocols now where the machine talks to the website as a machine. MCP, and its browser-side sibling WebMCP , let a website hand an agent a set of named tools instead of making it guess at buttons. UCP and AP2 do it for commerce , so a checkout is a call with terms rather than a form filled in by something imitating fingers. A2A does it between agents. There is an IETF working group on Web Bot Auth, the piece that would let an agent prove which agent it is. That split, between agents that can prove who they are and agents that can only do things, is the fault line the whole agentic web is forming along .

None of those require anyone to pretend. Maybe the better way to do this is through those protocols, and not having AI pretend it is human as it browses.

That is the fork. One path has a machine driving a human interface while nobody on the receiving end is told. The other has machines and websites talking to each other on purpose. Right now the money and the launch events are going into the first, and the second is where the actual engineering is happening.

I am not going to tell you to do anything today, because there is nothing useful to do yet. But keep a very close eye on it, and there are three specific things to watch.

Whether any of these agents ever carry an identity a website can verify , which is what the Web Bot Auth work at the IETF would give them. Whether the connector list grows, because that is the list of websites that get an interface instead of a browser. And whether the next one of these launches with one document or two.

More Resources:

- The Agentic Web Is Splitting Into Two Bets: Identity And Capability

- Google Gemini Can Now Control Your Computer. Hackers Are Already Targeting AI Agents

- Google Tells Developers To Build For AI Agents, Not Just Humans

This post was originally published on No Hacks .

Featured Image: Viktoriia_M/Shutterstock

Category SEO AI Search

Read Full Bio

Slobodan Manic Founder of No Hacks and machine-first website optimisation consultant at No Hacks

Slobodan “Sani” Manić is a website optimisation consultant with over 15 years of experience helping businesses make their websites faster, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/meta-published-2-documents-about-muse-and-only-one-mentions-attacks/589071/)
