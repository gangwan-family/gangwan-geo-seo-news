---
title: "Why Part Of Your AI Authority Takes Years, Not Campaigns & Why It Comes From Other People via @sejournal, @DuaneForrester"
source: "Search Engine Journal"
published: 2026-08-06T14:30:36+00:00
fetched_at: 2026-08-07T01:03:13.764774+00:00
url: "https://www.searchenginejournal.com/why-part-of-your-ai-authority-takes-years-not-campaigns-why-it-comes-from-other-people/584467/"
guid: "https://www.searchenginejournal.com/why-part-of-your-ai-authority-takes-years-not-campaigns-why-it-comes-from-other-people/584467/"
author: "Duane Forrester"
categories:
  - "SEO"
---

# Why Part Of Your AI Authority Takes Years, Not Campaigns & Why It Comes From Other People via @sejournal, @DuaneForrester

- Source: Search Engine Journal
- Published: 2026-08-06
- URL: https://www.searchenginejournal.com/why-part-of-your-ai-authority-takes-years-not-campaigns-why-it-comes-from-other-people/584467/
- Author: Duane Forrester
- Categories: SEO

## RSS 摘要

Set expectations before tactics: parametric standing moves on model generations, responds to being described, and sits in functions nobody measured against it. The post Why Part Of Your AI Authority Takes Years, Not Campaigns & Why It Comes From Other People appeared first on Search Engine Journal .

## 原文正文

Why Part Of Your AI Authority Takes Years, Not Campaigns & Why It Comes From Other People Skip to content

🔥[Live 8/12 with Loren Baker] Ecommerce SEO : Own your "brand +promo code" search.

Register Now

- SEJ

- ⋅

- SEO

## Why Part Of Your AI Authority Takes Years, Not Campaigns & Why It Comes From Other People

What models say about your company comes from how other people have described it over time. Today’s work shows up in the next model generation, not this one.

A reader left a comment on the entity mapping article suggesting that the obvious next move was to go win the parametric side. That piece had drawn a line between what a model retrieves at the moment you ask it something and what it already carries in its weights. That comment, I think, accepted the line was there, and then treated one half of it as a work item.

The phrasing is everywhere right now. Influence the parametric side. Build parametric authority. Four words, verb first, sounding like something you assign to someone with a deadline.

I understand why it gets said that way, and the shorthand is doing something useful. The problem is that the work behind those four words was finished years ago in most cases, done for reasons that had nothing to do with language models, and nobody recorded it as a cost at the time because there was no category to record it against.

### We Do This With Every System That Gets Too Complex To Measure Directly

There is a long habit in this industry of taking something nobody controls and giving it shorthand that sounds controllable. Proxy metrics have served practitioners well for exactly that reason, because they give you a usable number for a system you cannot observe directly. That was never the failure. The failure was always in mistaking having a broad understanding for having tight data.

What is different this time is what got compressed. A proxy metric reduces a system nobody can see whole to a single number, and everyone using it understands the number is a stand-in. Influence the parametric side reduces years of work across several departments to a single instruction, and nothing in the phrase admits to standing in for anything. The noun is accurate. The verb is not.

### What This Actually Costs Is Not Time

The years are not the point. What matters is how many separate parties described the company, and how differently each of them said it. Years are simply how long that usually takes to accumulate.

Parametric standing , meaning what a model already says about you before it looks anything up, is the result of that accumulation.

Two terms get used interchangeably here, and they are not the same thing, which matters for what follows. Training data is the text that went in. Parametric standing is what survived compression into the weights. The relationship between them is real and directional. That is why the research below can measure one against the other and get consistent answers. It is also lossy. A great deal goes in and does not come back out in usable form, and that gap is the source of most of the confusion here.

The research here is unusually direct. Kandpal and colleagues found at ICML that a model’s accuracy on a fact tracks the number of relevant documents it saw during pretraining, and they established that relationship causally rather than only correlationally. They also estimated that models would need scaling by many orders of magnitude before answering competitively about subjects with thin support in the data. Waiting for a bigger model does not fix a thin footprint.

Mallen and colleagues reached the same limit from another direction , finding that models handle well-covered entities and struggle badly with the long tail, and that scaling mostly improves recall at the popular end while leaving the tail roughly where it started.

Then there is the finding this whole argument rests on. Allen-Zhu and Li showed that knowledge only becomes reliably extractable when it turns up in sufficiently varied phrasing during pretraining. Without that variation, a fact can sit inside the model and still return zero percent accuracy under questioning, present but unusable. Their work runs on a controlled dataset and the recommendation is aimed at engineers building pretraining pipelines, so I would not stretch it into a claim about brands. As a mechanism, though, it explains a great deal: repetition from a single source does not produce what variety from many sources produces.

Parametric standing is not earned by publishing more. It is earned when enough independent parties describe a company, in enough different ways, that the description survives compression into the model’s weights. Volume of self-published content does not substitute for variety of independent description, because the mechanism rewards distinct phrasing from separate sources rather than repetition from one.

Still, somebody can point at a company founded in 2023 that current models describe accurately, and that deserves a clear answer. It did not beat the mechanism. Enough separate sources described it at once that the accumulation happened fast. The exception runs on the same rule. The concept of “viral” applies here, too, just like in social media.

The bottom line here is this: more content alone doesn’t work here. You still need to influence people to speak about your company in the way you want, to have the desired impact. And that takes a long time to accumulate. More content answering questions directly is useful, but still takes time to influence the process.

### Nobody Holds An Account With The Corpus

The second reason this cannot be tasked is that there is nothing to task it against.

Elazar and colleagues, in a project called What’s In My Big Data , examined 10 corpora used to train popular models. One of them is C4, the Colossal Clean Crawled Corpus, a public training dataset built by filtering a single snapshot of Common Crawl. They found C4 drawing from such a diverse set of domains that even the single most common one accounts for less than five hundredths of one percent of documents. Your own property, however much you publish on it, is a vanishingly small share of that.

Common Crawl’s own published statistics add something anyone who has watched crawl behavior will recognize. They note that their domain rankings only partly reflect the importance of those domains, because the crawler respects robots.txt and works hard not to overload servers, with the result that highly ranked domains tend to be underrepresented, and the crawler favors plain HTML over other document types.

A separate paper documenting C4 , led by Jesse Dodge, found the same divergence, noting that the sites inside the corpus do not represent the most used sites on the internet.

Set that against where people actually discuss companies online and the problem compounds. Several of the places where a business accumulates the most description are large, heavily trafficked platforms of exactly the kind a polite crawler treats gently, and much of what sits on them is rendered rather than served as static HTML.

### Most Of It Was Created Before The Question Existed

This is the part I keep coming back to, but I want to be careful not to overstate it.

Language models entered general use about four years ago. The text they were built from is considerably older, in two ways that are documented rather than assumed. The most thoroughly examined corpus available is C4, whose source snapshot was taken in April 2019. The Dodge team sampled a million of its URLs and used the earliest Internet Archive index date as a proxy for when each page was written, estimating that 92% were written between 2011 and 2019. They also noted the date distribution is long-tailed, with a non-trivial amount of material written ten to twenty years before collection. C4 is not what current production models run on, so take it as the best-documented corpus rather than a current one. The pattern still tells you something.

More pointed is the work by Cheng and colleagues at Johns Hopkins on effective cutoffs . They found that the date a model reports and the date its knowledge actually concentrates around often differ substantially, for two traceable reasons: New Common Crawl dumps carry some amounts of older material, and deduplication can struggle with semantic and near-duplicate content. The practical consequence is that a model’s picture of a company is probably older than its published cutoff suggests.

The description a model carries of a company was deposited years before anyone thought to optimize for it. Mainstream language models have existed for around four years; the corpora underneath them skew substantially older, and research on effective cutoffs indicates that a model’s knowledge concentrates earlier than its published cutoff date implies. Whatever standing a company holds today came from work done when the category did not exist. So that means your structured data, your content, your PR work, your review management from then, had to be best of breed to serve you well today.

### The Functions Were Yours, But The Sentences Were Not

Here is where it gets awkward for anyone who has run a marketing organization.

Almost every function that built this reports to marketing. Public relations, analyst relations, community management, trade and event presence, local press work, crisis communications, review operations. None of it sits outside the remit. It is the ordinary work of the department, year after year. (Depending on your company, IT or Systems teams also have a portion of impact.)

What none of those functions ever owned was the output, and this is critical.

Public relations earns coverage a journalist writes. Analyst relations earns assessments an analyst forms. Community participation earns descriptions from people with no relationship to the company at all. Crisis response produces press written by parties who are, at that moment, adversarial in some cases. Wikipedia presence depends on editors deciding a company is notable, which is an editorial judgment that has never been for sale.

Reviews are the clearest case and the most humbling. A company controls the response. It does not control the review. Influence over what a customer writes depends on marketing, product, service, pricing, and staffing all landing correctly on the same day, and even then the customer writes whatever they want. That record accumulates across thousands of separate nodes, over years, in language nobody at the company chose, attached to a business the executive team is accountable for.

None of that text entered a model as itself. What it did was change how outside parties described the business, and independent description is the only channel into the weights that exists. The support agent (human) writing careful replies in 2018 was not depositing text into a corpus. That work made the business something a local writer would describe warmly, and the writer’s sentence is what the model absorbed.

Which means marketing’s oldest tradition turns out to be the relevant one. Earned media has always been the practice of paying for outcomes you cannot author. That constraint did not arrive with language models. It has been the defining condition of the discipline the entire time, and it is the only mechanism that reaches parametric standing. (Earned = paid here refers to the fact that you employ people to do the work. Those are hard costs, often significant. Or you pay a third party for your content. It might “earn”, but it’s definitely “paid for”.)

There is an inheritance problem here, too. The output that got encoded was produced under previous strategies, on budgets that closed years ago, frequently by people who have since moved on. Whoever holds the role now owns the function and inherited the result.

### Why None Of This Comes Apart Easily

Look at what happens when the people who own the weights try to change one thing on purpose. Cohen and colleagues, writing in Transactions of the Association for Computational Linguistics , tested prominent knowledge editing methods and found they fail to introduce consistent changes, because editing a single fact sets off a ripple of related facts that also need updating and largely do not get updated. That is, researchers with direct parameter access, no adversary, and full knowledge of the target, still unable to make a clean change to a single fact. Remember when Bing and Google told us all they couldn’t simply “reach in and make a change”? Yeah, that was real, and still is.

Against that, the idea that an outside party installs a description by publishing harder or more just does not survive.

But the same property runs the other direction as well, and that is where it turns useful. Standing built from thousands of separate descriptions does not come apart because of one bad quarter, one unflattering article, or one competitor’s campaign. Distribution produces the difficulty and the durability together. They are the same fact seen from opposite sides.

It also means a model can carry a description of a company that stopped being true a while back, which is a real problem and a subject for another day.

### What You Can Reasonably Expect

If there is a practitioner takeaway, it lives in expectations rather than tactics.

Parametric standing moves on the timescale of model generations , not campaigns. It responds to being described, not to publishing. The only work that reaches it is work that makes a company something outsiders want to describe, and most of that sits in functions never measured against this outcome, which probably should not start being measured against it exclusively.

The measurement question and the authorship question get conflated constantly, and they are not the same. What a model says about a company right now is observable. You can measure it , watch it shift across releases, and compare it against what the company believes about itself, which is roughly what I built myself. What is not available is a way to compose the input.

Parametric standing is observable but not authorable. What a model says about a company today can be measured and tracked across model releases. What the next model says is determined by how independent parties describe that company between now and then, which no marketing team can write directly. But CAN influence broadly.

The retrieval layer is a different matter, and it is where most of the actual work sits right now.

So when the next person suggests going and winning the parametric side, the honest answer is that you were already paying for it, across years of other people’s sentences, by work nobody was counting as an investment in machine memory, because at the time there was nothing to count it against. Now, that work has value in an entirely new way. Today’s work impacts tomorrow’s review, public statement, or description of your business, which influences the next training dataset.

I go deeper on how these systems build their picture of a company in The Machine Layer , available here .

More Resources:

- How AI Chooses Which Brands To Recommend: From Relational Knowledge To Topical Presence

- Most Major News Publishers Block AI Training & Retrieval Bots

- The Web Is Eating Itself And Your Metrics Look Fine

This post was originally published on Duane Forrester Decodes .

Featured Image: ORION PRODUCTION/Shutterstock; Paulo Bobita/Search Engine Journal

Category SEO

Read Full Bio

Duane Forrester Founder and CEO at UnboundAnswers.com

Duane Forrester is the Founder and CEO of UnboundAnswers.com, a consultancy helping businesses adapt to the realities of AI-powered search ...

## 原文链接

[Read original](https://www.searchenginejournal.com/why-part-of-your-ai-authority-takes-years-not-campaigns-why-it-comes-from-other-people/584467/)
