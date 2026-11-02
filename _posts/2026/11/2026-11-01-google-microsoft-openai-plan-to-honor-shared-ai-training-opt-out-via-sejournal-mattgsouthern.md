---
layout: post
title: "Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out via @sejournal, @MattGSouthern"
date: 2026-11-01T08:00:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-01/Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/google-microsoft-openai-shared-ai-training-opt-out/595387/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-01
- URL: https://www.searchenginejournal.com/google-microsoft-openai-shared-ai-training-opt-out/595387/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

A shared robots.txt line could let sites opt out of AI training with several providers at once, but companies involved are handling it differently. The post Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out appeared first on Search Engine Journal .

## 原文正文

Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out Skip to content

SEJ Pro Sign In

Ebook: State Of Search 2027

Download The Report

- SEJ

- ⋅

- AI Search

## Google, Microsoft & OpenAI Plan To Honor Shared AI Training Opt-Out

- Google, Microsoft, and OpenAI plan to honor one shared AI training line in robots.txt.

- Google plans to read that opt-out as a Google-Extended block unless the site specifies Google-Extended.

- Microsoft is replacing NoArchive and NoCache with separate training and grounding preferences.

A shared robots.txt line could let sites opt out of AI training with several providers at once, but companies involved are handling it differently.

Google , Microsoft , and OpenAI announced plans on Friday to honor a shared robots.txt line for AI training preferences. A site could use it to state one training preference to every provider that takes part, instead of writing rules for each company’s crawler.

The line is from an Internet Draft that Anthropic’s Kevin Kelley submitted to the AI Preferences working group at the IETF (same date). This is listed in the IETF’s document tracker as an individual draft, which does not represent official IETF standardization activity. In a post to the working group’s email list , Kelley indicated that Anthropic has started development to provide this feature.

Based on their provided timelines, none of the three companies currently supports the line. Google and Microsoft described how each would handle it differently. According to Google, if a site sets up a shared opt-out line, Google plans to treat it like a Google-Extended block when a website doesn’t specify Google-Extended, and this control also applies to grounding within Gemini Apps. Microsoft wants sites that use its NoArchive and NoCache tags to switch to new preferences by March 1, 2027.

### How The Shared Line Works

Kelley’s draft adds no new directive to robots.txt. An ordinary rule group, that a site might write under what the draft calls a policy token, __usage_ai-training, would be written like it always has been, using Allow and Disallow. The draft provides an example of how one might opt out of AI training on the entire site, except for the /press-kit/ folder.

User-Agent: __usage_ai-training Disallow: / Allow: /press-kit/

The token itself has its meaning based upon the working group’s vocabulary draft , specifically defining AI Training as using content to modify a generative AI model’s learned parameters. Those models that do nothing but non-generative tasks like classification or ranking are exempted from this definition.

Rules that have already been put into robots.txt files will not be considered as part of any shared training preference. In the draft, a wildcard group (User-Agent: *) can never match the token, and a file without a __usage_ai-training group indicates no preference, which Kelley states is true of every robots.txt file currently published. The token doesn’t control crawling either.

On Oct. 22, I covered a different working group draft, co-written by Google’s Gary Illyes, that would add a Content-Usage rule to robots.txt. Kelley wrote that the group set that draft aside to make progress on the vocabulary.

### Google Ties It To Google-Extended

Google’s post, by John Mueller, says that when a site opts out of training with the shared line and doesn’t specify Google-Extended, Google plans to interpret that “as if the publisher had disallowed Google-Extended.” Google aims to support the control in 2027, according to the post, and its crawler documentation says early 2027.

The documentation says Google-Extended controls whether content can be used to train future Gemini models and whether it can be used for grounding in Gemini Apps and on Vertex AI. Grounding, in Google’s description, means supplying content from the search index to the model when it answers. The post adds that sites that specifically allow Google-Extended are eligible to appear in Gemini Apps responses through grounding.

The documentation also says Google-Extended doesn’t affect a site’s inclusion in Google Search. AI Overviews and AI Mode have a separate opt-out, the Search generative AI control in Search Console, which I covered when it rolled out worldwide in August.

### Microsoft Splits Training From Grounding

Microsoft’s post, by Bing principal product manager Krishna Madhavan, adopts the shared line for training and adds a separate AI Grounding preference. That one is set only at the page level and governs whether content can help inform AI-generated answers. Microsoft also lets a meta tag or HTTP header set the training preference for a single page, overriding robots.txt for that page.

A default of Allow is what happens with grounding, and keeping a page out is how Disallow works. The new option called DisallowExtended allows grounding in Microsoft created tools like Copilot and Bing’s AI Mode but does not allow grounding through Microsoft provided grounding services that are used by other businesses (Web IQ). Microsoft said either restriction will limit visibility of your brand in answers using Artificial Intelligence (AI) and will have no effect on your ability to be listed in search results from Bing.

Microsoft is replacing NoArchive and NoCache for training and grounding with these two new options. They will begin honoring the new options on February 1, 2027, as they crawl, and they will stop recognizing the older tags as training or grounding options after March 1, 2027.

Sites that use the old tags and want to stay out of grounding also need to record a temporary preference in Bing Webmaster Tools. The setting opens Dec. 15 and is available only to sites still using those tags on that date. Microsoft’s FAQ says pages without one by March 1 default to allowing grounding until Microsoft recrawls them. Microsoft also says that once it detects either new preference on a site, it will disregard any NoArchive or NoCache tags still on that site.

### OpenAI And Anthropic

OpenAI aims to honor the signal in the next few months, though its current robots.txt policy will still be in effect.

Neither OpenAI’s blog post nor its crawler documentation (checked Oct. 30) states what would happen when a website has both a shared line rule and GPTBot rule that conflict with each other.

As of Oct. 30, there was no posting in Anthropic’s newsroom regarding the signal. According to Kelley’s mailing list message, implementing support for this feature across all of Anthropic’s services will take some time.

According to Anthropic’s crawler-help webpage (checked Oct. 30), they have only three crawl control options available, which are ClaudeBot, Claude-User, and Claude-SearchBot.

### Why This Matters

One robots.txt group could replace a stack of per-company training rules once each company reads it; however, an opt-out through the shared line won’t reach the same uses at Google and Microsoft. For example, at Microsoft, training and grounding are separate settings. In contrast, both sit under Google-Extended at Google, and there is no way described in the crawler documentation to keep content out of Gemini training while still letting Gemini Apps use it for grounding.

Microsoft’s is the only announcement that replaces controls sites already use. According to Google, OpenAI, and Anthropic’s Kelley, existing controls will continue to work, so sites that use NoArchive or NoCache to limit how Copilot uses their content have things they need to do first.

### Looking Ahead

OpenAI’s post encourages other AI providers to honor the signal, and Kelley wrote that he hopes others will join. Google and OpenAI say they’ll share more details as their support arrives. Kelley’s draft expires May 3, 2027, unless a new version replaces it, and he plans to propose his design as a change to the Content-Usage draft.

Featured Image: Teodora ART/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-microsoft-openai-shared-ai-training-opt-out/595387/)
