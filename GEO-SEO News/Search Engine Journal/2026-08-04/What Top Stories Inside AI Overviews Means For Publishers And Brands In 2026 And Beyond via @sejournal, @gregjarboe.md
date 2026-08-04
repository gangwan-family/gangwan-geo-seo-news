---
title: "What Top Stories Inside AI Overviews Means For Publishers And Brands In 2026 And Beyond via @sejournal, @gregjarboe"
source: "Search Engine Journal"
published: 2026-08-04T19:00:12+00:00
fetched_at: 2026-08-04T22:33:41.749245+00:00
url: "https://www.searchenginejournal.com/what-top-stories-inside-ai-overviews-means-for-publishers-and-brands-in-2026-and-beyond/584175/"
guid: "https://www.searchenginejournal.com/what-top-stories-inside-ai-overviews-means-for-publishers-and-brands-in-2026-and-beyond/584175/"
author: "Greg Jarboe"
categories:
  - "Generative AI"
  - "SEO"
---

# What Top Stories Inside AI Overviews Means For Publishers And Brands In 2026 And Beyond via @sejournal, @gregjarboe

- Source: Search Engine Journal
- Published: 2026-08-04
- URL: https://www.searchenginejournal.com/what-top-stories-inside-ai-overviews-means-for-publishers-and-brands-in-2026-and-beyond/584175/
- Author: Greg Jarboe
- Categories: Generative AI, SEO

## RSS 摘要

Most publishers think robots.txt keeps them out of AI Overviews. It doesn't. John Shehata's data shows what the wrong setting actually costs newsrooms. The post What Top Stories Inside AI Overviews Means For Publishers And Brands In 2026 And Beyond appeared first on Search Engine Journal .

## 原文正文

What Top Stories Inside AI Overviews Means For Publishers And Brands In 2026 And Beyond Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- SEO

## What Top Stories Inside AI Overviews Means For Publishers And Brands In 2026 And Beyond

Google now embeds Top Stories inside AI Overviews on 15.5% of U.S. trending news queries, and blocking Google-Extended won't remove publishers from it.

John Shehata, CEO of NewzDash, found something in July that a lot of publishers threatening to block Google’s AI don’t realize is already happening underneath them. Google has started folding entire Top Stories carousels directly inside AI Overviews , and the robots.txt directive most publishers reach for first does nothing to stop it.

Shehata posted on LinkedIn that nearly one in six U.S. trending news queries now place Top Stories inside AI Overviews, and followed it with a full data breakdown on the NewzDash SEO for News blog .

Screenshot from LinkedIn, July 2026

### Google Has Run This Play Before

The topic he is describing is not new in kind, but it is new in mechanism. In 2006, John and I spoke on a panel about “Vertical Creep Into Regular Search Results” at the Search Engine Strategies New York conference. We discussed how Google was quietly pulling what appeared in Google News into its main web results before Universal Search formally arrived. Danny Sullivan called that May 2007 rollout the most radical change Google had ever shipped to its results, blending video, images, books, and news into a single ranked list instead of 10 blue links. Google’s own announcement framed it the same way, describing a shift toward one integrated set of results rather than separate verticals users had to hunt through individually.

Nineteen years later, Google is doing it again. This time the destination isn’t a blended results page. It’s an AI-generated answer.

### What NewzDash’s Data Shows

According to NewzDash’s tracking, among trending news queries where Google displays Top Stories at all, 15.5% in the U.S. and 17.46% in the UK now show that carousel embedded inside the AI Overview rather than as its own standalone module below it. Entertainment queries lead both countries, clearing 35% in the U.S. and 31.5% in the UK. World News hits nearly 32% in the U.S. Health and Science queries barely register. Shehata’s data also shows the two placements are mutually exclusive. When Top Stories lives inside the AI Overview, Google is not also running a separate carousel further down the page for the same query.

That distinction matters more than it sounds like it should, because it reframes the entire opt-out conversation publishers have been having since AI Overviews launched.

### Google-Extended Is Not An AI Overviews Opt-Out

Most publishers who want out point their robots.txt at Google-Extended and consider the matter settled. It isn’t. Google’s own crawler documentation states plainly that Google-Extended governs specified AI training and grounding uses, things like feeding future Gemini models or grounding certain Vertex AI responses, and explicitly does not affect a site’s inclusion in Google Search or function as a ranking signal. Blocking it does not remove a publisher from AI Overviews, AI Mode, standard Top Stories, or Top Stories embedded inside an AI Overview. Shehata is right to keep hammering on this, because the confusion is not a fringe misunderstanding. It’s the default assumption across the industry.

### The Control That Reaches AI Overviews Is A Different One Entirely

Google began testing a generative AI exclusion inside Search Console in June, currently limited to a subset of UK site owners. It lets an eligible publisher exclude their links and content from AI Overviews, AI Mode, and generative Discover features specifically, without touching their eligibility for traditional Search. Google’s support documentation says an excluded site’s content won’t appear in those features and won’t even be used as an input for generating a response. Choose that setting and, by Shehata’s reading, you almost certainly lose your spot in the embedded Top Stories carousel too, since it’s just a collection of publisher links riding inside one of the covered surfaces.

Google has not confirmed what happens next at the layout level. Would the AI Overview keep showing an embedded carousel built from the publishers who remained opted in? Would Google fall back to a standalone Top Stories module instead? Nobody outside Mountain View knows yet, and Shehata is careful to label this a high-confidence interpretation rather than a documented outcome. That kind of restraint is rarer than it should be in AI SEO commentary right now, and it’s a large part of why I trust his data over the louder takes circulating on the same topic.

### The Bigger Story Is Trust

I think the bigger story here is not the mechanics of Google-Extended versus the Search Console control, even though publishers genuinely need to understand that difference before they touch a setting. The bigger story is that AI Overviews’ central problem has always been trust , not visibility. Users don’t yet have a reliable way to know whether an AI-generated answer is drawing on something a credible newsroom actually reported or synthesizing something thinner. Pulling Top Stories, with its named publishers, real bylines, and direct links, into the body of the AI Overview instead of stacking it below a wall of generated text is a genuine, if incomplete, answer to that problem. I’ve watched Google reshuffle where news lives in its results since the “vertical creep” days of 2006. This is the first move in the AI Overview era that looks aimed at rebuilding trust rather than just reducing clicks to the open web.

Although this is my considered opinion, it comes with a caveat. A step in the right direction is not the same as a finished solution, and Google’s refusal to document what happens to publishers who opt out is exactly the kind of ambiguity that erodes the trust this move is supposed to build.

### 3 Things To Do This Week

For SEO practitioners managing news clients or in-house newsroom sites, three things are worth doing this week rather than waiting for Google to clarify the layout question.

First, separate your controls before you touch either one. Audit whether your site currently blocks Google-Extended, uses the new Search Console generative AI exclusion, or neither, and document which surfaces each one actually governs. Treating them as interchangeable is how a site accidentally forfeits AI Overview visibility while believing it only opted out of training data.

Second, if you have access to the Search Console exclusion , test it on a URL-prefix property or a single section before applying it sitewide. Google’s control supports inheritance between parent and child properties, which means a news publisher can trial the exclusion on, say, an opinion vertical and watch what happens to that section’s Top Stories eligibility before deciding whether the tradeoff is worth it domain-wide.

Third, start pulling Google’s generative AI performance reports in Search Console now , and pair them with a tool like NewzDash that tracks how often your URLs surface inside Top Stories carousels versus embedded AI Overview placements. You cannot make an informed opt-out decision without a baseline for how much visibility is actually at stake, and that baseline needs to exist before you flip the setting, not after.

Twenty years ago, “vertical creep” meant publishers had to figure out how a blended results page would treat their headlines. Today, it means figuring out how a generated answer treats them instead. The mechanism changed, but the need for publishers to understand exactly what they’re opting into, and out of, did not. John Shehata is doing the unglamorous work of documenting that shift in real time, and until Google says otherwise, his data is the closest thing the industry has to ground truth.

More Resources:

- Google Gives Sites AI Search Opt-Out, But Not The Data To Use It

- Preferred Sources & AI Mode Are Creating Filter Bubbles – A New Discovery Problem

- Google Shows How To Get More Traffic From Top Stories Feature

Featured Image: PeopleImages/Shutterstock

Category SEO Generative AI

Read Full Bio

VIP CONTRIBUTOR Greg Jarboe President and co-founder at SEO-PR

Before Greg Jarboe retired, he was the president of SEO-PR, which he co-founded with Jamie O’Donnell, from 2003 to 2025. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/what-top-stories-inside-ai-overviews-means-for-publishers-and-brands-in-2026-and-beyond/584175/)
