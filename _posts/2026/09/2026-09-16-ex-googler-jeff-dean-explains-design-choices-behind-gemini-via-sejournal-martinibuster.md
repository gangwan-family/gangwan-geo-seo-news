---
layout: post
title: "Ex-Googler Jeff Dean Explains Design Choices Behind Gemini via @sejournal, @martinibuster"
date: 2026-09-16T10:31:08+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-16/Ex-Googler Jeff Dean Explains Design Choices Behind Gemini via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/ex-googler-jeff-dean-explains-what-users-should-understand-about-gemini/589593/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "News"
  - "SEO"
  - "_src_search-engine-journal"
---

# Ex-Googler Jeff Dean Explains Design Choices Behind Gemini via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-09-16
- URL: https://www.searchenginejournal.com/ex-googler-jeff-dean-explains-what-users-should-understand-about-gemini/589593/
- Author: Roger Montti
- Categories: AI Search, News, SEO

## RSS 摘要

Ex-Googler Jeff Dean shares insights from Gemini's development and the approach he uses to discover promising new ideas. The post Ex-Googler Jeff Dean Explains Design Choices Behind Gemini appeared first on Search Engine Journal .

## 原文正文

Ex-Googler Jeff Dean Explains Design Choices Behind Gemini Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- AI Search

## Ex-Googler Jeff Dean Explains Design Choices Behind Gemini

Ex-Googler Jeff Dean explains what Google learned while building Gemini and shares the thinking behind some of his biggest innovations.

Jeff Dean recently explained the origins of Gemini, including the design philosophy behind it. Surprisingly, Gemini was lagging a bit until its coding abilities were improved, which subsequently improved the model’s reasoning ability.

### The Origin Of Gemini

Dean explains that the origin of Gemini was when he realized that there were multiple teams working separately toward the same goal. From the outside looking in, that seems like a silly approach, and that’s exactly the insight Dean had.

The interviewer, Dawn Song, asked:

“So now looking back on the development of Gemini, what surprised you the most and what lessons from building Gemini do you think that you can share and can help shape the next generation of AI systems?”

Dean answered:

“I think Gemini is really the culmination of a few earlier research projects, both within Legacy DeepMind and Google Brain and other parts of Google Research.

And at that time, we sort of realized that we were all converging to very similar kinds of directions, like training, trying to scale up the size of models we trained. We had some efforts, independent parallel efforts, on how do you make language models also be multimodal so they can understand images and so on.

And I wrote a one-page memo. I’m like, this is just silly. We should just all work together. Let’s combine our people and ideas and compute resources and train one model that is multimodal from the start that brings our best people together from across multiple research organizations within Google.

And I think that was really good.

…And so we sort of saw a way to bring ourselves back in closer collaboration. And I think that’s been a really successful thing.”

#### Screenshot of Jeff Dean

### Why Gemini is Multimodal

We know that Gemini is multimodal, but what is less known is that this was a design effort from the very beginning. Dean explained that the goal for Gemini was to create a model that could understand audio, images, language, text, and other forms of information. But interestingly, it was when they trained it for coding that Gemini experienced a breakthrough improvement in reasoning.

Jeff Dean explained:

“I think the focus on making the model multimodal from the beginning has been really, really good. You want the model that you’re gonna use for everything to understand text and language and code and images and videos and audio and other modalities besides.

So like we put a little bit of, say, LiDAR data in the training data so it at least knows that LiDAR data is a thing because that’s an important use case for, you know, further training of Gemini models. So that is important.

And that’s been, I think, a success of a decision we made at the very beginning to bring that through all the current Gemini models as well. …We wanted to make the model good at lots of things.

And so I think maybe our focus on making it amazing at coding was lagging a little bit and we realized that in our work to catch up on that.

And I think we have good efforts underway. But I think by focusing on that, you end up with a system that is able to really do a good job of reasoning and doing other kinds of tasks that needs to sort of work its way through breaking a complicated problem down into multiple sub-pieces and so on.

And so that’s a good– if you improve coding, you also tend to improve that capability in non-coding things.”

### Insight About Learning

That’s actually super interesting because it shows how making the LLM expert in one thing leads to benefits in other areas. This is actually kind of similar to how humans become expert in things. Many centuries ago, a samurai sword master named Miyamoto Musashi encouraged learning arts and professions that are outside of the martial arts. He used carpentry as an example of how a master carpenter understands tools, planning, how to manage workers, and understands the structure of buildings and then maps those skills and insights back into the martial art of sword fighting.

Jeff Dean’s explanation about the origin of Gemini is useful because it gives users a better understanding of what Gemini is, creating an awareness of what is possible with Gemini when it’s considered as a multimodal model, not just a generative text model.

### Jeff Dean’s Secret For Innovation And Success

Dawn Song asked:

“So essentially, this is one thing that stands out about your career is that so many of these ideas, from MapReduce to MOE and so on, they actually took years before the broader community realized how important they would become.

But you had the Midas touch, and you had the special, really foresight to actually build and develop these ideas and systems and so on.

So I think many people in the audience would love to learn how do you do it?

How do you distinguish between technologies that are genuinely foundational and those are simply fashionable?

And what engineering principle that has remained surprisingly timeless throughout your career?

And also as AI shifts from models to increasingly autonomous agents, what new abstractions do you think we’ll need over the next few years and decades for our future?”

Jeff Dean responded:

“I think I’ve been very lucky, maybe, as part of it. But I also think one of the things I try to do is keep track of a lot of different trends or research topics that the community is exploring.

I often tell students it’s better to skim 10 papers than to read one in detail, because you kind of then get 10 points in your cloud of what might be possible, or even skim 100 abstracts.

Because what you want to be able to do is connect important ideas that have not yet been connected.

And sometimes when you think about a hard problem, if you have some of these things that are now kind of vaguely starting to be possible in mind, that can help you kind of shape a full solution to a problem where instead of it seeming like seven unsolvable problems, you can squint at it and say, okay, well, these five things, I know there’s sort of vague work going on that seems important and might be able to address some of the things.

Then there’s two sort of additional things that I have no idea how to do. But if I work hard on them, I can imagine solving those.

And sometimes that’s super important to do the things that are incremental improvements to what we’re doing now, but you want to look for the things that are you know, maybe very different ways of doing things that might be possible or might be possible soon.

…I’ve done a bunch of things that have not worked out well too, so that’s also a good tip. Try lots of things that might not work. Some of them will.”

### Watch Interview Of Jeff Dean

Featured image/Screenshot of interview

Category News SEO AI Search

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/ex-googler-jeff-dean-explains-what-users-should-understand-about-gemini/589593/)
