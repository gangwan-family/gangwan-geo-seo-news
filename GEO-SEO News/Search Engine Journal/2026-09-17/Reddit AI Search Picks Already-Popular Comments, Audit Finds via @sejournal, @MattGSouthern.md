---
title: "Reddit AI Search Picks Already-Popular Comments, Audit Finds via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-17T15:44:51+00:00
fetched_at: 2026-09-17T23:35:21.610221+00:00
url: "https://www.searchenginejournal.com/reddit-ai-search-picks-already-popular-comments-audit-finds/589771/"
guid: "https://www.searchenginejournal.com/reddit-ai-search-picks-already-popular-comments-audit-finds/589771/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Reddit"
---

# Reddit AI Search Picks Already-Popular Comments, Audit Finds via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-17
- URL: https://www.searchenginejournal.com/reddit-ai-search-picks-already-popular-comments-audit-finds/589771/
- Author: Matt G. Southern
- Categories: News, Reddit

## RSS 摘要

An audit of Reddit AI search found formal, highly upvoted comments were selected more often, while experiential language appeared less often. The post Reddit AI Search Picks Already-Popular Comments, Audit Finds appeared first on Search Engine Journal .

## 原文正文

Reddit AI Search Picks Already-Popular Comments, Audit Finds Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- Reddit

## Reddit AI Search Picks Already-Popular Comments, Audit Finds

- Researchers audited Reddit's AI search answers across advice and support subreddits.

- Formal, highly upvoted comments had higher selection odds, and experiential language had lower odds.

- The written answers dropped nearly all first-person language from the comments they quoted.

An audit of Reddit AI search found formal, highly upvoted comments were selected more often, while experiential language appeared less often.

Reddit’s AI search was more likely to pull formal, already-upvoted comments into its answers than comments with more markers of personal experience, according to a new preprint from researchers at the University of Illinois Urbana-Champaign.

The team processed 10,000 questions through the feature three times and analyzed 30,000 answers by tracing them back through 14.68 million comments. These questions originated from 20 advice and support subreddits, so the findings cover that segment of Reddit, though the paper has not undergone peer review.

Additionally, the answers carried almost none of the first-person language in the comments they quoted, a change the authors say transforms personal testimony into more general advice.

### Formal Language Was Tied To Higher Selection Odds

The researchers looked at comments that an answer quoted or listed as a source and compared them to other comments in the same discussion that the answer passed over.

They found that the level of formality was the strongest language predictor of which comments were chosen. Specifically, when a comment was one standard deviation more formal, it had 49% higher odds of being selected (odds ratio 1.488), with formality scored by a text classifier. Additionally, comments that used words like “should” and “must” also had higher odds of being picked (1.070).

Comments with more markers of personal experience had lower odds of selection (0.789), and so did supportive language (0.924). The paper calls the first measure experiential voice and scores it from features such as first-person pronouns and past tense.

Formality was also associated with higher community voting, while experiential voice was associated with lower voting. After the researchers accounted for a comment’s score, position, and age, the associations shrank to 1.213 for formality and 0.860 for experiential voice.

The paper doesn’t show that writing formally gets a comment selected. The authors write, “Our study is observational and should not be interpreted causally.”

### Comments That Were Already Visible Had An Edge

A comment’s vote ranking within its thread showed the largest association in the selection model, with a one-standard-deviation increase multiplying the odds of being chosen by 2.88.

The median selected comment was at the 91st percentile for score in its thread, compared to the 45th percentile for comments not chosen. Of the selected comments, 92% were direct replies to the original post, which also accounted for 53% of all comments. Additionally, selected comments appeared a median of 1.2 hours after the post, whereas non-selected comments appeared after a median of 5.9 hours.

A one-standard-deviation increase in comment length had an odds ratio of 1.79. Comments containing an external link had an odds ratio of 2.25.

Comments with a score of zero or below made up 0.53% of selected comments and 5.1% of all comments collected.

### The Written Answer Dropped Most First-Person Language

In an analysis of 1,000 of the queries, researchers compared Reddit’s quoted comments with the responses crafted around them. Usage of words like “I” and “my” decreased from 3.3% in the quoted comments to 0.06% in the answers.

The same queries were processed through GPT-4o-mini and GPT-5 via OpenAI’s API with web search enabled. Both models used less first-person language than Reddit comments, with Reddit’s responses showing the largest reduction.

Overall, out of 4,932 citations, 18 referenced Reddit across both models and search configurations. This data is based on API calls for advice queries, which differs from the setup used in the ChatGPT app.

### How The Audit Worked

The researchers used an LLM to rewrite real posts from the 20 subreddits into short search queries. Ten are large communities such as r/personalfinance and r/AskDocs, and ten are smaller ones such as r/UKJobs and r/AusLegal.

The three runs were spaced about five hours apart so that differences would reflect the system and not changes on Reddit. When two runs pulled from the same source posts, the responses were almost identical. This shows that most of the differences came from which posts the system chose to retrieve.

A typical answer used about seven different subreddits. The subreddit where the question was first asked contributed 17.7% of the retrieved posts in the large-community set and 15.7% in the small-community set. The authors mention they don’t see a higher share as better.

The paper refers to this feature as Reddit Answers, which was its name when I first reported on its launch in December 2024. Reddit’s announcement page now shows an update from May 26, 2026, stating, “Reddit Answers is now merged into Reddit search for one unified search experience.”

The questions were created from posts dated through July 2026, so these runs happened after that change, although the paper doesn’t specify the collection dates. Reddit’s Help page now describes the feature as AI search, accessible through an Ask button in the search bar.

### Why This Matters

Reddit’s value for audience research is people describing their own experience with a product or a problem. In these 20 communities, comments with more markers of that experience were less likely to reach the AI answer, and most of the first-person wording was gone when they did.

Reddit CEO Steve Huffman told investors in February that Reddit is particularly good at questions where “the answer actually is multiple perspectives from lots of people.” This audit measured which of those perspectives reached the AI answer.

You’ll see the source threads listed beneath each answer. Make sure to read them first before including the summary in your report.

### Looking Ahead

The authors say these selection patterns may not carry over to other kinds of communities or to other AI search systems. I’ll update this story if a revised or peer-reviewed version changes the findings.

Featured Image: Accogliente Design/Shutterstock

Category News Reddit

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/reddit-ai-search-picks-already-popular-comments-audit-finds/589771/)
