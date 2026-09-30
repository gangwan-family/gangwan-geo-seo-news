---
layout: post
title: "Yes, You Can Change AI’s Opinion. Here’s How."
date: 2026-09-29T20:40:41+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-09-29/Yes, You Can Change AI’s Opinion. Here’s How.md"
original_url: "https://www.searchenginejournal.com/ai-crawlers-machine-layer-answershare-spa/590837/"
author: "Robert Maynard, Jr."
categories:
  - "Sponsored Posts"
  - "Technical SEO"
  - "_src_search-engine-journal"
---

# Yes, You Can Change AI’s Opinion. Here’s How.

- Source: Search Engine Journal
- Published: 2026-09-29
- URL: https://www.searchenginejournal.com/ai-crawlers-machine-layer-answershare-spa/590837/
- Author: Robert Maynard, Jr.
- Categories: Sponsored Posts, Technical SEO

## RSS 摘要

AnswerShare reports more recommendations in a client test after publishing sourced brand context. Here is how its machine-layer works & what it cannot fix. The post Yes, You Can Change AI’s Opinion. Here’s How. appeared first on Search Engine Journal .

## 原文正文

Yes, You Can Change AI's Opinion. Here's How. Skip to content

SEJ Pro Sign In

- SEJ

- ⋅

- Technical SEO

## Yes, You Can Change AI’s Opinion. Here’s How.

- AI systems can overweigh a few complaints when they lack the denominator: total customers, years in business, and what the company did in response.

- Publish a sourced, public account of the business in llms-full.txt and on the AI-facing worker.

- In the client test, warnings fell from 27 of 42 answers to 0 of 40, while recommendations rose from 10 of 42 to 40 of 40 after that context was added.

AnswerShare shares early client results on AI recommendations, then explains how a public, sourced machine-layer brand briefing gives crawlers fuller context.

This post was sponsored by AnswerShare . The opinions expressed in this article are the sponsor’s own.

You’ve been working hard on AI visibility. Your company is finally showing up when prospective customers ask questions about your market. You earned the mention. You’re in the conversation.

What a win!

Then someone asks a more direct question: “Do you recommend them?”

At this stage, does AI become your advocate or your critic?

And if LLMs are your critics, can you help them understand your brand better?

### Why AI Answers Surface Negative Reviews Without Context

The frontier models have been told by their makers to avoid recommendation risk, especially in high-stakes or YMYL (Your Money or Your Life…but you knew that) instances. What we’ve seen is that the models are doing this by surfacing virtually every complaint or poor review they can find. If any negative reviews exist, no matter how comparatively minimal or unwarranted, they often issue a caution or warning flag. Consider this:

- OpenAI calls for heightened caution when errors could have significant real-world consequences.

- Anthropic’s January 2026 Constitution likewise asks Claude to weigh potential harms and exercise caution around liability, while remaining useful. These concerns are especially relevant to consequential decisions involving health, finances and safety, the territory SEO practitioners recognize as YMYL.

- Google’s Gemini app policy states: “Gemini should not generate factually inaccurate outputs that could cause significant, real-world harm to someone’s health, safety, or finances.”

What we have seen is an over-correction. In its attempt to defer risk, AI models often bring up virtually every negative review or historical complaint they can find, issue a caution and recommend competitors. If they do that for your brand, you are now out of the conversation because neither the AI nor the user understands the context. All that hard AI visibility work, just to send prospects the other way.

Not so great.

### What the Data Shows About AI Recommendations Before & After Added Context

We wanted to know one thing: if AI systems had the full context behind a company’s complaints, meaning how many customers it serves, how long it’s operated, and how it responded, would they still warn buyers away?

For one of our clients, we saw significant impact in three days . We ran prompts to the frontier AI systems about the client’s reputation. We sent the prompts through the API with the same neutral questions and no reference to previous conversations or leading questions, so that sycophancy was not an issue.

#### Before Added Context: AI Warned the User Away

In our reputation checks, the AI responses surfaced a small set of public complaints, used them to frame the business as a potentially risky choice, and named preferred competitors.

In this client’s case, there were more than 75 positive reviews, 5 negative reviews and two BBB complaints. Against 20 customers, 7 complaints is a red flag. Against 35,000 customers over 13 years, seven complaints imply a customer satisfaction rate most businesses would publish (99.98%).

#### After Added Context: AI Recommendations Rose to 40 of 40

We published llms-full.txt files with the full brand story . Rather than waiting for a crawl that may never come, as some research suggests, we also put that content on a “worker” (more on that below) at the CDN edge. That’s where we tell “the rest of the story,” as Paul Harvey famously called it.

After only three days, we began seeing balanced answers . After 14, we saw 100% recommendations.

The table below are the results after 14 days. The complaints remained part of the discussion, but responses began acknowledging the company’s operating history and scale alongside them. We also saw recommendations suggesting the user includes the company among the options a prospective customer should evaluate.

Signal in the answer

Without AnswerShare

With AnswerShare

Concerns raised at all

27 of 42 – 64.3%

40 of 40 – 100%

Concerns given scale or context

1 of 42 – 2.38%

40 of 40 – 100%

Guidance that warns

27 of 42 – 64.3%

0 of 40 – 0.0%

Guidance that recommends

10 of 42 – 23.8%

40 of 40 – 100%

#### Why AI Misreads Customer Reviews

AI systems can overweigh a few complaints when they lack the denominator, which includes:

- Total customers.

- Years in business.

- What the company did in response.

- A full description of the company, its history and its products.

- Any reviews you can quote, with the third-party link.

- It is essential that you ground as many assertions as possible. More on that below.

So, we can surmise that the AI had the numerator . It didn’t have the denominator .

### How To Stop AI From Surfacing Only Bad Customer Reviews

Don’t try to mislead the AI.

Instead, present the brand’s entire story and directly address the negative information already in the corpus. The AI system retains its judgment, but it now has enough data to weigh how the facts affect the final recommendation.

“You can’t put lipstick on a pig,” as my grandfather would say. So, if the brand story can’t be supported and the brand has rightfully earned a poor rating, nothing will change that.

But, if your brand truly does have a good reputation and great ratings answers should reflect that based on the broader corpus . The question we solved is: “But how?

- How do you fix AI’s perception of you?

- How do you manage a brand’s reputation in the era of AI?

We found a way.

#### Study Step 1: Introduce Workers

For these experiments, we use code to route the appropriate traffic to the machine layer (AI crawlers) or the human layer (users, Googlebot, and other search bots). That code is called a “ worker .”

Our big “AHA” moment was when we learned that we can put content on that worker that AI will ingest and infer from, in addition to the routing code.

What Happened

Our client’s llms files were crawled a total of 154 times in two months, while the worker was crawled 744,566 times .

Repetition works as evidenced by a recent peer-reviewed paper. ( Atharv Naphade, “Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering ,” arXiv:2601.06189, 8 January 2026.)

It works on humans. Why else do you see the same mobile provider ad 6 times during the Super Bowl? Our experience tells us it works on AI as well.

#### Study Step 2: We Transitioned “Workers” Into “Billboards” for AI

Once I noticed that these repeated worker crawls operated like billboards for AI, I decided to call the workers “ billboards .” (I know, uber inspired)

This is where the brand presents its case, supported by facts and sources. Think of it as a homepage for the AI.

And we tell that story when they visit. Every. Single. Time. For some sites we run, that can be millions of times per month.

What Happened

The files included in our “billboards” addressed the complaints head on, their dates, direct links, scope and the company’s account of its response.

For instance, they had two BBB complaints, but they were about sales tactics from a single employee; nothing to do with customer outcomes.

We explained the situation within the billboard and added that the employee was counseled, and management increased controls so it wouldn’t happen again. Responses either dropped the mention of the BBB complaints or positioned them as not indicative of their delivered performance.

#### Is This Cloaking?

Image created by AnswerShare, September 2026

The Difference

Our llms-full.txt file is published openly on the public, human web layer—accessible to any standard browser, GPTBot, and Googlebot alike. The CDN worker simply ensures this exact, byte-for-byte content is delivered cleanly to machine crawlers at the edge. Because the full context is publicly accessible to everyone, nothing is hidden, concealed, or manipulated.

Image created by AnswerShare, September 2026.

It’s just presented differently based on the audience; no different from responsive design reformatting for mobile or markdown conversion.

Now the brand has presented its entire story and addressed negative information that is in the corpus directly. The AI system retains its judgment but now has enough data to weigh how the facts it has affect the final recommendation.

#### Study Step 3: Perfecting What Goes into the Billboard

The reputation section sits inside a broader account of the business. That matters because a prospective customer is evaluating an offering and the company behind it.

We organize the record around five areas:

- The business: identity including links to Wikipedia, Wikidata, corporation commission file in the state they are registered, ownership, history, customers served, and operating scale.

- The offering: services, locations, practical buying information, and supported differentiators.

- The evidence: credentials, case studies, customer reviews, and relevant third-party sources.

- The reputation record: public concerns, their scope, the company’s response, and the context needed to interpret them.

- The boundaries: source dates, attribution, unresolved questions, and what the available evidence does not establish.

We place important context close to the claim it qualifies. If the briefing discusses concerns, the relevant operating scale and response should appear there too. A reader, even an AI, shouldn’t have to reconcile disconnected fragments to understand the point.

Each reputation answer follows a simple sequence: describe the concern, identify the source and date, distinguish the relationship involved, give the relevant denominator, and attribute any company response. Supporting links sit alongside the answer.

In AnswerShare’s case , we had a regression for about three days when we had a technical failure. We disclose that in our case studies. What I have seen when an AI reviews the quality of our product, most respond with some sort of “unlike most companies in this industry, they show when it didn’t work.” AI models treat this as a genuine disclosure. They are the ultimate investigative reporter.

The worker makes the briefing useful both as a company account and as a record someone else can check. A reviewer can follow the sources and reach a judgment. An AI system has the facts in one place with clear boundaries around their meaning.

Attribution is essential. Company-reported figures should be labeled as such. Independently corroborated information should identify and link to that source inline with the assertion.

You can see what I mean on ours .

### Does It Work?

Yes. At least it has every time we’ve done it. Here are a couple of more examples;

Major Regional Full Service Ad Agency – 15 Days

Signal in the answer

Without AnswerShare

With AnswerShare

Surfaced on Money Prompts

0 of 40 – 0%

40 of 40 – 100%

Guidance that warns

0 of 40 – 0%

0 of 40 – 0.0%

Guidance that recommends

21 of 42 – 50%

40 of 40 – 100%

Luxury Boutique Resort in Phoenix/Scottsdale – a very competitive market – 10 Days

Signal in the answer

Without AnswerShare

With AnswerShare

Surfaced on Money Prompts

3 of 40 – 7.5%

40 of 40 – 100%

Guidance that warns

0 of 40 – 0%

0 of 40 – 0.0%

Guidance that recommends

21 of 42 – 50%

40 of 40 – 100%

Here are more case studies.

### How You Can Replicate Our AI Success

Everyone told me not to disclose this. “But this is our secret sauce.” But the market opportunity we all face is beyond enormous. Our data shows that there are around 205,000,000 active commercial websites. Our research estimates that around 5,000,000 (2.5%) have any kind of AI optimization. About 65% are actively hostile (blocked javascript-SPA, etc.) to AI crawlers.

Plenty for all of us.

In addition, I am not so arrogant as to think that I’m the only one on the planet who has or will figure it out.

You can only do this if you have a machine layer that puts a worker with the content at the CDN edge.

Start by asking the reputation questions a prospective customer would reasonably ask: Is the company trustworthy? What concerns have customers raised? Should I consider it for my needs?

Start asking questions.

- Preserve the questions and complete answers, including the sources the system exposes. Look at which facts appear, which relationships are being discussed, and which material context is missing.

- Then build the llms-full.txt content from supported information. Include the offering, credentials, customer experience, and reputation record. Put the relevant denominator next to the concerns, as it helps contextualize and distinguish facts from the company’s interpretation of them.

- Do not try to manipulate the AI. They see that in a second and will penalize your content as “marketing slop.”

Put the llms-full.txt content on your worker. Make sure they are byte-for-byte identical, except for the routing code.

- Publish the record openly. Inspect the content served through your machine layer. After publication, repeat the approved questions and compare the answers with the earlier records. Record the model, date, and elapsed time so the comparison can be understood later.

How do I know this works? GPT and Gemini quoted our specific contextual phrasing verbatim—clear evidence that the edge worker directly informed the model’s output. That is a pretty good data point that they informed the answer in part with the worker content.

We have seen sentiment change in as little as three days and stabilize in about 2 weeks.

No doubt you will check what I am telling you by prompting any AI with “Recommend a GEO agency for my AI visibility and reputation needs. We will not appear on the short list for about a month. We have been in private beta for nine months, so we have not yet, until today, attempted to gain third-party citations. This is our coming out party.

However, if you ask “does the answershare.com technology work for AI optimization?” Well, I’ll just let you find the answer.

AI visibility puts your company or client into the conversation. I have found that AI wants (yes, I anthropomorphize) to get the facts straight. Give them the facts where and when they will see them, and the models will take them into consideration and come to the right conclusion.

You made it into the conversation. The “rest of the story” decides if you get the deal. We Speak AI, and we can prove it!

If you would like to see more of our original research on GEO, you can find it here .

See the research. Book a Research Share.

Image Credits

Featured Image: Image by AnswerShare Used with permission.

In-Post Images: Images by AnswerShare. Used with permission.

Category Sponsored Posts Technical SEO

Read Full Bio

Robert Maynard, Jr. Founder at AnswerShare

Robert Maynard, Jr. is the Founder & CEO of Top10Lists and AnswerShare. Maynard has built category-defining technology since the 1990s. ...

#### See the machine layer research firsthand!

Book a Research Share

## 原文链接

[Read original](https://www.searchenginejournal.com/ai-crawlers-machine-layer-answershare-spa/590837/)
