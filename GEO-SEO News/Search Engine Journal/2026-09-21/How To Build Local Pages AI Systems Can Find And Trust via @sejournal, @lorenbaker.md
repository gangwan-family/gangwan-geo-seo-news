---
title: "How To Build Local Pages AI Systems Can Find And Trust via @sejournal, @lorenbaker"
source: "Search Engine Journal"
published: 2026-09-21T12:00:25+00:00
fetched_at: 2026-09-22T00:11:50.118725+00:00
url: "https://www.searchenginejournal.com/how-to-build-local-pages-ai-systems-can-find-and-trust/588097/"
guid: "https://www.searchenginejournal.com/how-to-build-local-pages-ai-systems-can-find-and-trust/588097/"
author: "Loren Baker"
categories:
  - "AI Search"
  - "Local Search"
  - "SEO Strategy"
---

# How To Build Local Pages AI Systems Can Find And Trust via @sejournal, @lorenbaker

- Source: Search Engine Journal
- Published: 2026-09-21
- URL: https://www.searchenginejournal.com/how-to-build-local-pages-ai-systems-can-find-and-trust/588097/
- Author: Loren Baker
- Categories: AI Search, Local Search, SEO Strategy

## RSS 摘要

AI ranks passages, reads alt text, and cites whatever numbers you publish. Practical rules for local service pages from SEJ Live. The post How To Build Local Pages AI Systems Can Find And Trust appeared first on Search Engine Journal .

## 原文正文

How To Build Local Pages AI Systems Can Find And Trust Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- Local Search

## How To Build Local Pages AI Systems Can Find And Trust

Whitespark's Darren Shaw and Duda's Russ Jeffery on why local AI visibility starts with crawler access, accurate data, and pages an LLM can read.

A local page cannot earn visibility from an AI system that cannot access, render, or trust its information.

As Whitespark founder Darren Shaw said: “You cannot be surfaced in AI responses if the AI can’t even access your website.”

Before adding new FAQs or rewriting service copy, marketers need to confirm two things: crawlers can reach the page and the business details they find there are accurate.

I recently hosted this SEJ Live session with Darren Shaw and Russ Jeffery, Duda Director of Platform and Product Strategy, to walk through the technical and content foundations of local AI visibility:

- What blocks crawlers.

- Where stale data leaks into AI answers.

- How to research what an AI needs from a service page.

- How to structure the page so the right passage gets pulled.

You can read the summary below and watch the free on-demand recording .

https://cdn.searchenginejournal.com/wp-content/uploads/2026/09/clip_01_Cloudflare_Is_Silently_Blocking_AI_Crawlers_short.mp4

### Start With Whether Crawlers Can Reach The Page At All

Jeffery recommended starting with the basic controls that determine whether a page can be discovered: the robots.txt file, noindex directives, security settings, sitemaps, and the way content is rendered. Although, he admitted he has launched a site with a noindex tag left in place by accident. His verdict: Fixing the error later “takes heck of a lot longer than just doing it right the first time.”

Shaw flagged Cloudflare as another potential blocker, which may be enabled without the marketing team realizing it. “Cloudflare often blocks AI crawlers by default,” he said, and many business owners do not know their web developer or host turned it on. He described a Shopify site that was blocking AI crawlers and the culprit was Cloudflare. His fix is to check for Cloudflare and then review the settings.

Both Shaw and Jeffrey consider the default to block all crawlers is as a policy built for publishers and applied to everyone. For publishers like Time or The New York Times, they may want crawlers to pay for their content and to block them. “But every small business in the world, they do not want to block crawlers.” Jeffery called it “a bad default by them.”

One caution to note on robots.txt, Jeffery described as “a guidance policy” for compliant crawlers, and “a little bit of a weak link in the chain” as it’s a soft set of intructions. Truly private content should be restricted at the server or application level.

The principle underneath all of this, in Shaw’s words, is that optimization work cannot help an AI response if the system cannot access the source.

### Server-Side Rendering Matters Again

Jeffery said JavaScript rendering has “gone backwards in the past few years.” Google executes JavaScript and “is still doing a good job at this,” the newer AI systems largely do not. “ChatGPT doesn’t have their own index, they don’t take the time to actually index and save pages within their infrastructure,” he said. His advice is to deliver important content in the HTML response through server-side rendering and verify it, rather than assuming the framework handled it.

Many established website platforms and frameworks do this out-of-the-box or offer it as an option. Jeffrey named WordPress and Next.js. The greater risk may come from a newly generated site that relies heavily on client-side JavaScript without confirming what a non-rendering crawler can see.

Shaw noted that most small businesses use Claude Code or a similar tool to generate a React-heavy site. “If you’re just vibe coding a website, they’re usually pretty bad, and I would just pay attention to that,” he said.

Shaw’s reassurance for everyone else: “For the vast majority of business owners, they don’t need to worry about this.” Sites on Duda, WordPress, or Wix already serve rendered HTML. The work is confirming what crawlers receive and hunting down the cases where important copy only appears after JavaScript runs, such as review carousels loaded by a widget.

Jeffery also discussed delivering markdown versions of pages, which Cloudflare is now pushing as an option. “I wouldn’t say it’s required right now,” he said. He has yet to find an AI search engine that relies on the markdown version of a page. Accessible, server-rendered HTML stays the priority.

Watch the full SEJ Live session .

### Old Pages Can Feed AI Systems The Wrong Information

Crawl access is only useful when the information is correct. I raised a problem I sometimes find when fact-checking AI Overviews: orphaned or duplicated URLs with labels such as “-old,” “-new,” “/home,” or “v2,” left behind when developers cloned pages during a redesign and never de-indexed the originals. Those pages may still carry an outdated phone number or address.

Customers rarely reach those pages through navigation. Crawlers do. As Shaw put it, “the AIs would grab it.” A technical audit that only looks for broken pages will miss them; it also has to look for stale versions.

My recommendation is a basic crawl audit, whatever the platform: Run the crawl, filter for URLs carrying those suffixes, and make sure none of them are indexable.

### Schema Is A Validation Layer That Has To Be Maintained

Schema was the one topic where the panel split, and the split is the useful part.

I’m a big fan of schema. I mirror every Google Business Profile data point in the site’s schema, and the sites I do this for seem to get more visibility within the local pack and also traditional organic results. But I don’t see it as a ranking factor per se; I see it as a validation tool.

Shaw is the skeptic. “I’ve never seen any noteworthy study that said, if you do schema, your traditional rankings will go up or your AI visibility will go up.” He pointed to detailed testing by Jake Hundley where “he found nothing.” Where Shaw does see value is disambiguation. Product data in a table, for example, becomes unambiguous once it is expressed as structured data, and that is easier for a crawler to parse than the page layout.

Jeffery landed in the middle. “You totally should do it,” with one condition. Schema is a third source of business data, alongside the website and Google Business Profile, and the worst case is that it goes stale.

The risk is maintenance.

Shaw described a site built in 2017 where the developer added schema; in 2025, the owner refreshed the site and never touched the schema because it lived in a RankMath setting they did not know existed. Jeffery said Duda sees the same pattern when a client updates a phone number on the page without configuring the sync to Google Business Profile, leaving the old number live in the markup. In his words, that is “more of a process problem” than an optimization problem.

Shaw agreed with my validation framing and was taken with one idea from it: Take every data point in the Google Business Profile and map it to schema. He said he wanted to build a tool that does exactly that. Jeffery said Duda already has one.

The practical rule is to treat schema as another business-data source that belongs in the update process. If the team changes an address, phone number, service, or area served, it should verify every place where that fact appears.

An audience question from Todd Vaughn asked whether FAQ or Q&A schema still matters now that Google has dropped the rich result. Shaw said, “I wouldn’t call it important. I would say it’s helpful for sure” when the answer is injected by JavaScript. Otherwise, an LLM strips the page down to what he described as “a big markdown file of text,” so an FAQ marked up in schema and printed on the page simply appears twice: “Here it is once and then further down that text document, here it is again.”

### What An AI-Ready Local Service Page Includes

Shaw’s research process starts with a question to the machine itself: “What does AI care about?” His working example was a plumber’s hot water tank repair page, already optimized for SEO and now getting a second pass for AI visibility. He asks Google’s Ask Maps (Gemini grounded in Maps data), or Gemini or Claude directly, what should be on that page. The answers are predictable: “They’re always going to tell you pricing,” plus trust symbols, reviews, and case studies. Jeffery extended the list to credentials and service area.

Step two is query fan-out, using Mark Williams-Cook’s queryfan.com. Shaw’s illustration: A user tells a chatbot their hot water tank died last night, they need it repaired quickly, and their budget is tight. To answer, the AI runs a set of its own searches. “It takes your one prompt and turns it into 10 other prompts.” Those 10 searches are the page’s FAQ list: “Those are your frequently asked questions.” The more of them a page is relevant for, the higher the odds it is cited in the response to the original prompt. Jeffery added the low-tech source: Ask the business owner what customers ask all the time. “Whether it’s yes or no, you still need to have an answer.”

Consumers, he said, “are searching for more and vastly different, and they’re searching for longer queries and following up more frequently.” Customers may ask whether a technician is certified, whether a provider serves a particular area, or whether the business can handle an urgent job. His print-shop example: Can I print A1 size on 297 gsm stock? If that answer lives nowhere on the site, there is nothing for the AI to pick up and answer with.

### Competitors’ Negative Reviews Are Page Research

Review research can reveal the pain points customers experience across a local market.

Shaw’s favorite research prompt runs in Ask Maps because it is grounded in Google Business Profile data: “For plumbers in my city, please analyze their reviews and tell me the most common pain points that people are complaining about in negative reviews.”

A business can address those concerns directly on its service page with accurate commitments it can support. This helps conversion because it answers a fear before the customer asks, and it gives AI systems explicit evidence about the experience the business promises.

Shaw’s examples: we will always be on time; we will treat your home like our own; “we wear special booties on our shoes so we don’t mess up your house”; we clean up after ourselves. He is certain about the conversion effect and thinks, “100% they’re going to be valuable for conversions,” and hedged on the AI effect that “they might give you a slight edge in the AI responses.”

Shaw then demonstrated how literally AI reads a page: “You can basically say any BS numbers you want on your webpage, and AI will cite it.” Write that you have 10,000 five-star reviews when you have 220, and the AI repeats 10,000. “The takeaway is not to fudge your numbers. The takeaway is to put those words on your page.” A review carousel loaded by a widget is invisible to the model; in his words, “I can’t read it because it’s JavaScript.” So write the sentence: this many reviews, this rating, this award. “You want to hype your business.”

### Drop The “We”: Name The Business In Its Own Copy

Answering an audience question from Cody Anderson on semantic triples, Shaw called them “a hard yes.” The problem he sees on nearly every small business site: the copy says “we” and never names the entity. “We are experts at hot water tank repair” gives a crawler nothing to attach the claim to. “Johnson Plumbing Denver are experts at hot water tank repair” does. The same applies to pricing, say, “Johnson Plumbing Brothers Denver’s pricing for this service is…” His reasoning: “robots are kind of stupid,” so the page has to state the subject explicitly.

Jeffery pushed back on readability by asking, “How do you make it not awkward? Because at that point you are writing for robots.” Shaw agreed it cannot open every paragraph. “It’s a sprinkling.” He reserves the brand name for the passages he most wants the AI to connect to the entity: the core service, pricing, differentiators, and ratings, and uses “we” everywhere else.

### What Local Teams Should Audit First

- Crawl controls. Check robots.txt, noindex directives, security headers, and Cloudflare’s AI crawler settings.

- Rendered HTML. Confirm that important content appears without requiring client-side JavaScript.

- Stale URLs. Find duplicate, orphaned, and archived pages that expose outdated business facts.

- Structured data. Compare schema with the visible page and Google Business Profile.

- Customer evidence. Add accurate answers, proof, FAQs, and trust information based on real questions and review themes.

Local AI visibility begins with access and accuracy. Once crawlers can retrieve reliable content, the work shifts to detail: specific answers, maintained structured data, customer proof stated in text, and the kind of exhaustive service information a human would never read and an AI will.

### Key Takeaways

- Audit access before funding optimization. A Cloudflare default or a forgotten noindex tag can zero out every dollar spent on content. Run a bot access check first.

- Stale data is a liability with no owner. Old URLs and outdated schema feed AI answers nobody on the team ever sees. Assign one person to every place a phone number, address, or service list lives.

- Schema is a maintenance commitment, with no proven ranking return. Do it for consistency and budget for upkeep; unmaintained markup was the one scenario the panel called detrimental.

- Research with the tools your customers use. Ask Maps and query fan-out reveal the questions an AI asks before it recommends a provider. Those questions are the content plan.

- Proof has to be written, in numbers, with the brand name attached. Widgets and badges are invisible. “Johnson Plumbing is rated 5.0 across 500 reviews” is not.

- Passages compete; pages do not. Cut every paragraph that fails “does this even deserve to be on the page?” Gains show up in traditional search too.

- Build the knowledge base nobody reads. Every unanswered detail is an invitation for the AI to source it from someone else’s account of your business, or a competitor’s site.

Watch this full session for free .

Featured Image: Koupei Studio/Shutterstock

Category AI Search Local Search SEO Strategy

Read Full Bio

SEJ STAFF Loren Baker Founder at Foundation Digital

Loren Baker is the Founder of SEJ, an Advisor at Alpha Brand Media and runs Foundation Digital, a digital marketing ...

## 原文链接

[Read original](https://www.searchenginejournal.com/how-to-build-local-pages-ai-systems-can-find-and-trust/588097/)
