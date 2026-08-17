---
title: "Google: Subject/Object Entity Order Affects AI Answers via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-17T11:11:31+00:00
fetched_at: 2026-08-17T21:47:12.415274+00:00
url: "https://www.searchenginejournal.com/google-subject-object-entity-order-affects-ai-answers/586089/"
guid: "https://www.searchenginejournal.com/google-subject-object-entity-order-affects-ai-answers/586089/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
  - "SEO"
---

# Google: Subject/Object Entity Order Affects AI Answers via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-17
- URL: https://www.searchenginejournal.com/google-subject-object-entity-order-affects-ai-answers/586089/
- Author: Roger Montti
- Categories: AI Search, News, SEO

## RSS 摘要

Google's research shows that LLMs struggle to recall facts when questions reverse the usual subject/object entity order. The post Google: Subject/Object Entity Order Affects AI Answers appeared first on Search Engine Journal .

## 原文正文

Google: Subject/Object Entity Order Affects AI Answers Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- AI Search

## Google: Subject/Object Entity Order Affects AI Answers

Google's research shows that LLMs experience difficulty recalling facts when questions reverse the usual subject/object entity order.

Google published a new research paper that found that frontier LLMs encode 95–98% of the tested facts but are unable to directly recall 26–34% in answers to queries. Part of the problem is that recall becomes more difficult when questions reverse the subject/object entity order in which a fact was encountered in training.

### Parametric Information

Parametric information is, essentially, the information that LLMs have encoded during training. That information comes from the web pages, song lyrics, books, instructions, code, and everything else that the LLM was trained on.

The question the researchers were seeking to answer was: Why do LLMs fail to recall some of the information they were trained on? It was previously thought that maybe LLMs weren’t trained on enough information, but the researchers found that isn’t always the case for frontier LLMs.

The researchers explain that encoding is saturated, meaning that the information needed to answer questions is generally already in the LLMs.

They write:

“Encoding is saturated; recall is not. For frontier LLMs such as Gemini-3-Pro and GPT-5, factual encoding is near saturation, with 95-98% of facts encoded. Yet these models fail to directly recall 26–34% of the facts, or 11–12% even with thinking.

Accordingly, recall failures account for more than 70% of GPT-5.2’s errors and a larger share in stronger models, suggesting recall is indeed a bottleneck.”

What that means is that the bottleneck isn’t that frontier LLMs don’t have enough facts and information. The bottleneck is in accessing that information.

### Subject And Object Entities

A curious discovery of the research is that one of the reasons why LLMs failed to recall specific facts is that the subject entity and object entity relating to a fact were learned in a specific order. When a query containing the reversed order is put to the LLM, the LLM has more difficulty recalling the fact because it was learned in a different order.

The research paper explains what the subject and object entities are:

“The roles of subject and object are determined by the source text from which the fact was extracted (e.g., a Wikipedia document): the subject is the entity that appears first in the text, and the object appears subsequently.”

Then it explains what it means by reversing the subject and object:

“A question whose answer is the object is termed a direct question, while a question whose answer is the subject is termed a reverse question.”

Google’s explainer uses the following example to illustrate the subject/object entity pair:

“Oasis played their first gig at the Boardwalk club.”

In the above example, “Oasis” is the subject entity and “the Boardwalk club” is the object entity.

So, in the example of “Oasis” and “the Boardwalk club”, when those pairs consistently turn up with Oasis first, the LLM experiences an inability to recall the fact when the query has the subject/object reversed.

Now here’s another curious discovery. The LLM is able to recognize the fact when the reversed subject and object entities are presented among alternatives in a multiple-choice question.

The researchers don’t explain why the LLM is able to recognize the answer when it’s part of a multiple-choice question. They use it as evidence that the answer is encoded in the LLM and recognizable.

### Phrasing Of The Question Had Insignificant Impact On Recall

The researchers tested whether rephrasing the questions made a difference in the ability of frontier LLMs to recall facts. They found that it didn’t significantly affect a model’s ability to recall a fact. What did matter was reversing the subject/object order.

### Long-Tail Facts Are Hard To Recall

Another interesting finding is that frontier LLMs experienced difficulties with long-tail facts, what the researchers called rare facts. The gap between encoding popular facts and rare facts was small, but larger for recall. The inability to recall rare facts was often not due to the LLMs not learning the information. They were just bottlenecked at the recall stage.

### Tested Solution: More Thinking

The researchers tested thinking for recalling facts and discovered that LLMs were able to recall 40–65% of the encoded facts that couldn’t previously be recalled directly. The downside of more thinking is that it is computationally expensive. The researchers also note that there is the additional problem of knowing when to trigger more thinking.

### Scaling LLM Training Is Not A Solution

Lastly, the researchers noted that scaling frontier LLMs is not a solution to the recall problem.

### SEO And Subject/Object Entity Pairs

The intuition regarding the order of subject and object entity pairs is that it may be beneficial to order them according to the most common way that queries order them. That’s not a finding in the research paper. Nor is it something that’s proven. But intuitively, it may be reasonable to order subject entities and object entities according to their most common order pairing.

While the research paper did not say that common ordering of these entities will help an LLM pick a particular web page, it’s a reasonable hypothesis from the point of view of SEO.

The research paper is called Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality ( PDF )

Google’s explainer is titled, Why does recall fail?

Featured Image by Shutterstock/Runrun2

Category News SEO AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-subject-object-entity-order-affects-ai-answers/586089/)
