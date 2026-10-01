---
title: "Using Local (AI) Compute To Reduce Reliance On Frontier Models via @sejournal, @chrisgreenseo"
source: "Search Engine Journal"
published: 2026-09-30T19:00:04+00:00
fetched_at: 2026-10-01T00:39:00.785820+00:00
url: "https://www.searchenginejournal.com/using-local-ai-compute-to-reduce-reliance-on-frontier-models/591047/"
guid: "https://www.searchenginejournal.com/using-local-ai-compute-to-reduce-reliance-on-frontier-models/591047/"
author: "Chris Green"
categories:
  - "AI Search"
  - "SEO"
---

# Using Local (AI) Compute To Reduce Reliance On Frontier Models via @sejournal, @chrisgreenseo

- Source: Search Engine Journal
- Published: 2026-09-30
- URL: https://www.searchenginejournal.com/using-local-ai-compute-to-reduce-reliance-on-frontier-models/591047/
- Author: Chris Green
- Categories: AI Search, SEO

## RSS 摘要

How much SEO work can you move off the cloud and onto the user's machine? A Chrome extension experiment with Gemini Nano has answers. The post Using Local (AI) Compute To Reduce Reliance On Frontier Models appeared first on Search Engine Journal .

## 原文正文

Using Local (AI) Compute To Reduce Reliance On Frontier Models Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- SEO

## Using Local (AI) Compute To Reduce Reliance On Frontier Models

Not every SEO task needs a frontier model. Testing Chrome's built-in Gemini Nano showed what local AI can handle and where it fails.

A lot of the current AI conversation assumes that “useful” AI means getting an agent to do the whole thing for you . There are some tasks where this does make a lot of sense – if done right – but there are many reasons why this isn’t the best option.

If I want to extract & deduplicate a URL list collection from XML sitemaps, you don’t need a frontier model.

What is better is to have an XML parser and deduplication script – for example – something cheap to (vibe)code, run, and ultimately is predictable.

In SEO/GEO/AEO, there are tasks where a degree of interpretation is useful, but sending every request to a large remote model is not needed or even the best option.

When I was experimenting with Exactly Matchy (that helps you understand if your content is retrievable by AI systems) , I wanted something people could run without needing to grapple with APIs, credit cards, or general faffery. I knew that Chrome has a version of Gemini Nano (a tiny model, downloaded when needed), and wanted to leverage this to achieve simple tasks for you.

The aim wasn’t to argue a small local model could replace a much larger model (it really can’t for a lot). It was to explore a more interesting question: How much useful work can we move closer to the user?

### How Does Local Compare To ChatGPT Or Claude?

Running AI locally is where we use our own hardware (phone, computer, laptop) to do the compute work without sending it off somewhere else to be processed.

Using ChatGPT or Claude is simple – and often free to use – but it has drawbacks:

- Resource intensive (data centers, water use, etc.).

- Costly (and will get more expensive).

- Raises data privacy questions.

- Puts in a point of failure you cannot control.

Running most LLMs (models) involves a degree of complexity AND often a powerful machine capable of running the model you select. But what model do you select, and how do you know what the hardware is good for? These are tricky and important questions.

Even after going through all this work, if you’re expecting a Claude-like experience, you’ll likely be frustrated because it still won’t measure up.

What if some small work can be done locally?

#### But A ‘Small Task’ Does Not Necessarily Mean An Easy Task

This journey helped really show the difference between small and simple tasks. Exactly Matchy just selected passages from a page based on a really simple request and removes some friction for the user.

#### Branching Out Into Building Something New And Useful

I set out to see if it could complete small tasks to help someone understand technical SEO/GEO issues and whether they were an actual issue or not. Rather than just a technical checkbox that often leads to the wrong conclusion.

Imagine a Chrome Extension which assists with Technical SEO, but more useful. There are some great Chrome Extensions out there that do relatively simple things, really well. But can AI assist in these small tasks to make you more effective? Would Nano be able to handle this?

For example, comparing raw HTML with the rendered DOM produces a relatively small amount of evidence. With enough planning and deterministic processing, it is possible to then present that information to a model.

An <a> tag (link) might have:

- The same anchor but a different destination.

- The same destination but different anchor text.

- A broken destination in the initial HTML which becomes working after rendering.

- Two different URLs which ultimately resolve to the same final destination .

Any experienced SEOs would find those pieces of data crucial to understanding whether that difference between raw/rendered is actually a problem or not. MOST SEO tools do a pretty bad job at helping people determine this without them doing the hard work!

What if we gave this data to Gemini Nano, could we let it make that decision for us? Sadly not… This kind of decision-making is not an easy reasoning problem; it seems easy, but it isn’t simple.

The model still needs to understand what this evidence means. It has to respect the facts (i.e., not conflict with them), combine multiple signals, and avoid inventing information or rationale that isn’t even present. Then it needs to make an accurate decision based on this.

Gemini Nano is an intentionally small, fast model and then quantized so it fits in Chrome without slowing things down. It is intentionally the way it is, which isn’t ideal for what I was trying to achieve.

In testing, Nano was useful at some tasks but unreliable at making the final judgment you could really trust. A stronger API (ChatGPT or Gemini) model handled the same evidence considerably better. When I gave it the deterministic details (i.e., those link attributes above), it did a really strong job at reasoning for you.

Is this a failure of local AI? Maybe – I was a little disappointed, if not entirely surprised – but this was highly useful as a lesson in architecture for these kinds of problems.

### Key Lesson: Put The Right Work In The Right Place

Throughout this process, the new extension has gradually settled into three layers:

#### 1. Code Handles Things That Should Be Exact

Fetching URLs, comparing HTML, checking HTTP responses, matching elements, identifying canonical relationships , and detecting whether a destination changed do not need probabilistic reasoning. If anything, asking an LLM to answer these questions is risky!

#### 2. A Small Local Model Handles Light Interpretation And Communication

Once the facts have already been established, Nano can turn a fairly ugly bundle of evidence into something a human can use quickly. If anything I’ve learned building teams, SEO/Serch programs, or training is that friction kills progress more than almost anything else.

Presenting an easily readable passage rather than blocks of JSON or spreadsheets is highly valuable.

I’d consider it a strength that Nano doesn’t have to make the decision – it’s actually easier in the long run.

#### 3. A Larger Model Is Available When Actual Judgment Is Needed

If there are technically complex, ambiguous details or we need some significant semantic or technical reasoning, a larger model does show its worth. We can provide the same structured evidence to Gemini, OpenAI, or another capable model.

This is when you need to prioritize speed or supplement some knowledge gaps in a pretty reliable way. The important part is that the pipeline does not need to change. Only the model does, which impacts what exactly you get back.

### Local Models Don’t Need To Win Every Benchmark

This all started as a test. I wanted to probe what Nano could do, so I benchmarked Nano’s reasoning ability against Gemini Flash and ChatGPT Luna.

In each test, I pitched them against each other, treating the models equally in the test. This, I think, is where thinking about different AI models goes wrong.

They do not need to replace frontier models to be useful! You certainly don’t need a frontier model for everything either! But how many people are going to know/understand this – and, to be honest, why should they?

In the context I am testing here, the local model (Nano in this instance) needs to be good enough to take a meaningful amount of work off the user.

There are several reasons this still makes local inference (via Nano) attractive:

- No API call is required for every minor task.

- Data can remain on-device, which helps with security, costs, and compute resources.

- Speed can be good enough if the model/session startup is handled well.

- Tools (that you build) can continue working without depending on an external AI service.

- Large models can be reserved for tasks where they are needed – but not an integral part of the process.

Another positive side effect was that forcing yourself to support a small model encourages you to improve the rest of the system. Your own poor decision-making or skimping on something that code can achieve can be hidden by a large AI model. But to be brutally honest, I don’t think compute costs as they are today are sustainable, so maybe we shouldn’t overly rely on it.

In this project, the limitations of Nano pushed me to spend more time looking into the deterministic code. This meant the evidence became better and Nano’s responsibilities became much more focused. All the technical assumptions had to be more explicit, for the better.

A great by-product of this was that these improvements also made the stronger models perform better when you chose to use them.

### Reasons For Optimism For Smaller, Local Models

The local model available in Chrome today will not be the last local model Chrome ships. This likely applies more broadly across browsers, operating systems, laptops and phones.

The models will improve & the methods of quantization will improve. Hardware will also improve – even if the costs increase – alongside managing context, “memory,” tool calling, etc.

So if an application you’re building is already designed around a replaceable local model, those improvements can arrive without redesigning everything. We can – I hope – rely on local models even more.

What’s more interesting – for me – was that I intentionally limited myself to Nano. It’s something that ships with all Chrome. If you wanted to run slightly larger models – or you have the hardware to be more adventurous – you can of course do more, now, today!

The opportunity isn’t to recreate ChatGPT or Claude locally. It is to build software where:

Exact computation happens in code, lightweight intelligence happens locally, and expensive intelligence is called only when it is truly needed.

For me, this is a MUCH more sensible direction for AI tooling, rather than treating every problem as an excuse to spin up the largest model available.

More Resources:

- How To Use AI To Streamline Time (And Money) Consuming SEO Tasks

- Google’s Mueller On Why AI-Built Websites Miss SEO Basics

- The Next AI Protocol Won’t Save Your SEO Strategy

This post was originally published on Chris Green SEO .

Featured Image: Roman Samborskyi/Shutterstock

Category SEO AI Search

Read Full Bio

Chris Green Technical Director & Senior Consultant at Torque Partnership

## 原文链接

[Read original](https://www.searchenginejournal.com/using-local-ai-compute-to-reduce-reliance-on-frontier-models/591047/)
