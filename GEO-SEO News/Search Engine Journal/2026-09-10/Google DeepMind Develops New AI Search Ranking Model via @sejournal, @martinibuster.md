---
title: "Google DeepMind Develops New AI Search Ranking Model via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-09-10T11:24:46+00:00
fetched_at: 2026-09-10T23:17:04.219816+00:00
url: "https://www.searchenginejournal.com/google-deepmind-develops-new-ai-search-ranking-model/589062/"
guid: "https://www.searchenginejournal.com/google-deepmind-develops-new-ai-search-ranking-model/589062/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
  - "SEO"
---

# Google DeepMind Develops New AI Search Ranking Model via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-09-10
- URL: https://www.searchenginejournal.com/google-deepmind-develops-new-ai-search-ranking-model/589062/
- Author: Roger Montti
- Categories: AI Search, News, SEO

## RSS 摘要

Google DeepMind researchers test Autoregressive Ranking (ARR), a unified model that can replace current retrieval and ranking methods. The post Google DeepMind Develops New AI Search Ranking Model appeared first on Search Engine Journal .

## 原文正文

Google DeepMind Develops New AI Search Ranking Model Skip to content

Webinar: AI Cites Your Brand. Now What? Turn AI Visibility Data Into Actions

Register Now

- SEJ

- ⋅

- AI Search

## Google DeepMind Develops New AI Search Ranking Model

Google DeepMind's Autoregressive Ranking is an AI system that can rank documents without the limitations of current systems.

Google recently published a research paper about training an LLM to replace current back-end ranking architectures for search. The researchers propose using Autoregressive Ranking as a replacement for the current two-stage ranking systems.

### Dual Encoders And Cross Encoders

In a very general and plain English sense, traditional search ranking systems typically have a two-stage architecture with a Dual Encoder and a Cross Encoder.

- The Dual Encoder (DE) converts queries and documents into vectors and uses them to quickly retrieve likely documents. Dual Encoders are relatively computationally inexpensive and fast. Those candidate documents are subsequently passed over to the Cross Encoder (CE).

- The Cross Encoder (CE) reviews and ranks the candidate pages the Dual Encoder (DE) had selected.

Dual Encoders are efficient and fast but are limited in how precisely they can rank documents. That’s why ranking systems use Cross Encoders, which are more powerful. But Cross Encoders are too computationally expensive for large-scale retrieval, which is why they’re used in the second stage for ranking the candidate documents.

What the researchers are proposing is replacing the two-stage search retrieval back-end with a new system called Autoregressive Ranking (ARR). The research paper is titled Autoregressive Ranking: Bridging the Gap Between Dual and Cross Encoders . The researchers are from Google DeepMind, University of Massachusetts Amherst, and The University of Texas at Austin.

It’s a fairly radical change to replace the standard two-stage ranking system with a single LLM that produces the ranked list of documents. Should something like this be used, the implications for SEO/AEO would be profound.

### Training A Ranking Model: SToICaL

The first step of creating the ranking model is to train it. The researchers developed a method called SToICaL (Simple Token-Item Calibrated Loss) to teach an LLM how to rank documents.

The training teaches the LLM which documents should rank higher and lower in two ways:

- First, documents that should rank higher are given more weight and those that should rank lower are given less.

- Second, the ranking provided by the training data is used to give more probability to token choices that lead toward higher-ranked documents.

The result is an LLM that learns which documents are relevant and is able to suppress ranking of irrelevant ones.

The researchers explain:

“We then propose SToICaL (Simple Token-Item Calibrated Loss), a generalized rank-aware training loss for LLM finetuning. By using item-level reweighting and prefix-tree marginalization, we distribute probability mass over valid docID tokens based on their ground-truth relevance.”

### Test Results

The researchers tested their new system to evaluate whether it actually improves ranking performance versus ordinary next-token prediction, using two datasets, WordNet and ESCI Shopping Queries. They also compared it to standard Dual Encoders and Cross Encoders in a separate test using WordNet.

The results of the testing showed that Autoregressive Ranking (ARR) performed strongly but not across all metrics.

They shared:

- SToICaL improved ARR’s ranking ability. The researchers wrote that their rank-aware training “significantly improves ranking metrics beyond top-1 retrieval.”

- The SToICaL training method helped ARR successfully rank irrelevant documents below relevant ones. In the WordNet experiments, the researchers say their rank-aware methods “drastically reduce” this kind of ranking error.

- In the WordNet comparison, ARR performed similar to the Cross Encoder (the computationally expensive one) and significantly better than the Dual Encoder.

One area that needs further research is that, in the shopping-search test, one version of the method became worse at ranking the most relevant result first, even though it improved the overall ranking of the results.

### Conclusions

The researchers conclude that Dual Encoders (DEs) become constrained as the number of documents to rank grows because, in order to represent every possible ranking, the vector size has to correspondingly grow. They show that ARR does not have that limitation and in theory it can rank an arbitrary number of documents.

They explain:

“We provide a theoretical foundation for the superior expressive capacity of ARR over DEs. A rigorous analysis of the embedding geometry required for ranking shows that for a DE to achieve any ordering of 𝑘 documents, its embedding dimension must grow linearly with 𝑘.

In contrast, we prove that an ARR model with constant hidden dimension is theoretically sufficient to rank an arbitrary number of documents. This offers a formal explanation for the advantages of ARR.”

However, this is a theoretical result, meaning that it does not necessarily establish that ARR will perform this way in real-world search systems. Yet the researchers also say that their experiments showed the approach improved ranking performance and became better at keeping irrelevant documents below relevant ones.

They write ( PDF ):

“In this paper, we established a theoretical foundation for Autoregressive Ranking, proving that while DEs require embedding dimensions to grow with corpus size, ARR models generating multi-token docIDs can solve complete ranking tasks with a constant hidden dimension, given a mild condition on the rank of the embedding matrix for the docID tokens.

We proposed a generalized rank-aware training loss for (pointwise) autoregressive ranking that relies on item-level reweighting and prefixtree marginalization to distribute probability mass over valid docID tokens based on their ground-truth relevance. Experiments on WordNet and ESCI show this approach successfully suppresses invalid docID generations and improves on key ranking metrics.”

### Takeaways

- Some SEOs tend to say that search has changed because of AI. But this paper makes it clear that, for the ranking part, Dual Encoders and Cross Encoders still play a role.

- Another takeaway is that we have not yet reached the point where “everything has changed” but this research paper shows that Google may be getting closer to a day when search really does change in a profound way.

Featured Image by Shutterstock/Samuel Boivin

Category News SEO AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-deepmind-develops-new-ai-search-ranking-model/589062/)
