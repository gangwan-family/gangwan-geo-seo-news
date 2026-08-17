---
title: "The AI Conversations Leaking Into Your Search Console via @sejournal, @suganthan"
source: "Search Engine Journal"
published: 2026-08-17T19:00:05+00:00
fetched_at: 2026-08-17T21:47:12.415274+00:00
url: "https://www.searchenginejournal.com/the-ai-conversations-leaking-into-your-search-console/585663/"
guid: "https://www.searchenginejournal.com/the-ai-conversations-leaking-into-your-search-console/585663/"
author: "Suganthan Mohanadasan"
categories:
  - "AI Search"
  - "SEO"
---

# The AI Conversations Leaking Into Your Search Console via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-08-17
- URL: https://www.searchenginejournal.com/the-ai-conversations-leaking-into-your-search-console/585663/
- Author: Suganthan Mohanadasan
- Categories: AI Search, SEO

## RSS 摘要

Search Console records what people say to AI Mode. Here's how to pull those fragments out and sort them into seven buckets. The post The AI Conversations Leaking Into Your Search Console appeared first on Search Engine Journal .

## 原文正文

The AI Conversations Leaking Into Your Search Console Skip to content

AMA with Reddit Experts: What's Working Now & How To Get Into The Threads AI Cites

Register Now

- SEJ

- ⋅

- AI Search

## The AI Conversations Leaking Into Your Search Console

A classifier for the AI conversations leaking into Search Console. Seven kinds, from human replies and comparison questions to tracker bots and agent prompts.

In early August, an SEO called Anastasia Kourou noticed queries in her Search Console report that didn’t look like searches: “Yes.” “Yes go on.” “Yes, pricing.”

She posted a screenshot and asked John Mueller whether Search Console was tracking what people say to AI.

Image Credit: Suganthan Mohanadasan

His reply confirmed it.

Search Console includes AI Overviews and AI Mode data in the general performance report, and Google’s documentation explains the mechanism. A follow-up question inside AI Mode counts as a brand new query , and everything in the response gets attributed to it. When someone tells the AI “yes go on” and your page appears in what comes back, Search Console records an impression for your page against the query “yes go on.”

Search Engine Roundtable covered the thread on August 6, and Ross Tavendale asked the question everyone was circling. If Search Console is recording people’s responses to AI Mode, how do we reverse engineer it?

Image Credit: Suganthan Mohanadasan

Nobody answered him.

This post is my answer.

I pulled every one of these fragments out of 16 months of my own Search Console data, worked out that they come in seven recognizable kinds, and built the classifier into my free Search Console MCP so you can run it on your site with one prompt. Sorting them is what makes the leak usable.

The whole thing comes down to four ideas.

- Google’s new AI report hides queries, but the queries leak into the report you already use.

- The leaked fragments come in seven recognisable kinds, and a classifier can sort every one.

- What you can see is a floor. Most of the conversation is in impressions Google anonymises.

- Joined with the new Generative AI report’s export, the fragments turn into a page-level picture.

I found 1,127 queries and 20,300 impressions across 16 months on my site, against millions of ordinary impressions. Small, and every row of it is something a real session said or ran.

### The Report Everyone Asked For Is Missing Its Queries

Google launched Generative AI performance reports in June and, as of August 11 , they’re live for everyone. The report shows how often your pages appear inside AI Overviews and AI Mode. It has five data views . Impressions, pages, countries, devices, dates.

Queries and clicks are the two things it leaves out , and there’s no API support either. I checked that last part on my own property just to be sure. The Search Analytics API’s type parameter still ends at googleNews, the searchAppearance dimension returns nothing AI-related, and the BigQuery bulk export schema doesn’t have an AI column. The export button in the UI is the only way this data leaves Google.

So, the report tells you how much AI visibility you have and refuses to say for what. (I think we all know why lol) Meanwhile the ordinary performance report, the one you’ve been reading for years, has been picking up AI conversation fragments the whole time. Nobody filters them out because officially they’re just queries.

### Idea 1: Your Query Report Is Part Conversation Log

AI Mode looks like a chatbot. Underneath, every message is processed as a Google search, including the follow-ups, and Google folds all of it into the web search type alongside the classic 10 blue links. Your query report now holds two different things. Searches people typed, and fragments of conversations people had with a model that happened to show your page.

The position data proves it’s the second thing. My site shows average position 4.5 for the query “yes.” On the open web, that ranking is impossible; “yes” belongs to songs and grammar sites. Inside an AI response, it makes sense, because Google’s documentation says links in an AI Overview inherit the position of the whole block , and AI Mode citations get counted under the same rules once they scroll into view. Position 4.5 on a reply word means my link sat inside the answer block, not on a results page.

That’s the leak. The question is whether the fragments can be told apart from normal queries at scale.

### Idea 2: The Fragments Come In 7 Kinds

I pulled 16 months of queries from my property and classified everything that couldn’t be a typed search. Seven kinds came out, and each one has a different origin.

Note: I haven’t included all of my queries for obvious reasons, just a sample. When you run this on your own GSC account, you’ll get all of your data.

#### Reply Artifacts

Bare replies: “yes,” “sure,” “really?,” “show me.” A person answered the AI mid-conversation; the reply was processed as a search, and your page appeared in the response. Positions here come from the answer block, not a results page.

Image Credit: Suganthan Mohanadasan

#### Pivot Follow-Ups

Mid-conversation comparisons: “what about resend?,” “what about gemini,” “how about in chinese?” The person has an answer in front of them and asks the AI to test an alternative, and the alternative they name is the one they care about.

Image Credit: Suganthan Mohanadasan

#### Conversational Questions

Questions addressed to someone rather than typed at a search box: “can you jailbreak meta raybans,” “how do i sell it,” “is it free.” The giveaway is grammar that only works with a listener, which gets its own section below.

Image Credit: Suganthan Mohanadasan

#### Tracker Probes

Synthetic prompts from AI visibility tools, run on a schedule. Two signatures in my data. Prompts ending “. my location is usa.” and prompts in the form “evaluate the [company] on [facet].” Nobody searches the same sentence every day for two months, so these are software.

Image Credit: Suganthan Mohanadasan

#### Agent Harnesses

A machine’s complete instructions, logged whole: “search the web for… return the 3 most relevant results you actually found … do not invent results or urls.” Somewhere an engineer wrote a prompt template, and Google filed it as a query.

Image Credit: Suganthan Mohanadasan

#### Pasted Strings

Error messages and spreadsheet headers searched as-is, by people or pipelines. My data includes a rank tracker’s full CSV column header as a single query.

Image Credit: Suganthan Mohanadasan

#### Long Uncategorized

Ten or more words with no other marker. Some are quoted sentences, some are agents, some are people. The classifier files them for review instead of guessing, which is the right amount of confidence for this bucket.

Image Credit: Suganthan Mohanadasan

The classifier is a ladder of checks, applied in order, and a query stops at the first one it matches.

Take “what about resend?” It isn’t on the reply list, so it passes the first rung. It matches the second, a pivot, “what about” followed by a short noun. Classification done, and the row tells me the rest.

One impression on my newsletter cost post , position 10, one click. Somewhere, someone was asking an AI about newsletter tools, asked “what about resend?” got my self-hosted setup in the response, and clicked through. That’s a person mid-decision, and the query names the alternative they cared about.

There’s no machine learning in any of this. The patterns are a curated list anyone can read and disagree with, which is the point. Every classification is explainable.

#### How Is This Different From A Long-Tail Query?

The obvious objection to all of this is that long queries existed before AI. [how to get not provided keywords in google analytics] is nine words, and nobody said it to a chatbot. The split comes down to who the query is addressed to.

When I first showed this to my co-founder Andy, that was his question.

A long-tail query is a detailed request addressed to nobody. It has its own subject and names its own tools.

A conversational query is addressed to someone, and four signals give it away.

Signal

Example from my data

Why it can’t be long tail

Instructing an assistant

“give me step by step”

Nobody instructs a search box

First person context

“i am using lmstudio”

You don’t brief Google about your setup

Dangling pronouns

“is it free”, “does it work”

“It” has no referent in the query. The referent lives in a conversation

Politeness

“please clarify”

Nobody says please to an input field

Any of those four, at any length, and the query is conversational.

Length alone is the weak signal, so it gets quarantined.

Ten or more words with question syntax gets classified as conversational, because typed queries average two to four words and almost nobody types 11.

Ten or more words with no other marker goes to the review pile instead of into a claim. And anything at nine words or fewer with none of the signals is treated as an ordinary search, which is why the not provided query above never enters the dataset.

One tell validates the boundary, and I’m not using it yet. Repetition. That not provided string has 1,853 impressions on my site because thousands of people type the same long-tail query.

Conversational strings almost never repeat; most of mine sit at one to three impressions, because no two people phrase a follow-up identically. Impressions per string as a typed versus spoken signal is the obvious second version of this classifier.

### What 16 Months Of My Data Shows

Start with the timeline. Reply artifacts on my site, by month. Zero impressions from April to November 2025. A first flicker in December. Then March 2026 switches the class on, and it’s run at 20 to 30 impressions a month since.

Image Credit: Suganthan Mohanadasan

ProTip: Go to Search console → Search results → Add filter → Query → Select custom.

Add this regex → ^(yes|yeah|ok|okay|sure)[?!.,]*$

You can see all of the artifacts.

A query class that didn’t exist for eight months and then becomes persistent is a behavior change with a date on it. “ Y es ” alone has 110 impressions, six clicks, and an average position 4.5 across the window. Six people replied to Google’s AI and then clicked through to my site off the back of their own “ yes. ”

The pivots line up with my posts one for one. [ what about claude ] hit my WebMCP guide .

[ what about xcode? ] hit the Xcode post . [ what about wayback machine ] hit the Wayback guide .

Each one is a reader asking the AI to compare something against the thing my page covers.

The conversational bucket is the biggest, and it has a signature. 559 queries, 8,834 impressions, 13 clicks.

That ratio is what being read inside answers looks like.

My biggest single row is [ do ai crawlers like gptbot support content negotiation for markdown ] at 2,998 impressions, and my favorite is [ what ai search monitoring tools let me combine ga4 session data, gsc click data, and ai citation rates in a single analysis so i can understand the full search picture? ].

Sixty-five impressions of someone asking an AI for the product category I was building while they asked.

Then there are the machines.

124 of my queries are tracker probes with 2,902 impressions, and the facet matrix aimed at my Roam review ran daily for 59 consecutive days.

The agent harnesses total 2,181 impressions, and one of them ran roughly 2,160 times across five days in July, the Dubai weather prompt from the list above.

Every run surfaced my ChatGPT teardown in its results, presumably because the post is about searching the web for sources. I still don’t know whose hallucination checker that was. If it was yours, the weather in Dubai is hot. (41 degrees today, ugh)

Three rows for the road. Someone pasted a full rank tracker CSV header, 17 columns of it, and it earned 146 impressions as a query.

Someone else pasted X Support’s entire rejection email, the one that says the username is available, and Google filed it against my handle post at position 1.3. And a single impression exists for [ you didnt give me the link ], a user complaining at the AI, recorded by Google, filed against my Wayback post.

Google recorded a person losing an argument with a robot haha. Classic!

### Idea 3: What You Can See Is The Tip

Before you run this on your site, the main limitation. Google anonymizes rare queries, and conversations are almost by definition rare strings. Nobody phrases a follow-up the way you do. So the fragments that survive into the report are the repeated ones, and the bulk of the conversation pool is hidden.

My BigQuery export shows that over the last 59 days, 57.7% of my web impressions carry no query string at all. 454,720 anonymized against 333,651 visible. The 1,127 classified queries are the visible tip of that pool. Read every number in this post as a floor.

#### 3 Quick Caveats Before You Run This

The classifier judges how a query looks, not what the person meant. [is it agent ready] looks like a dangling pronoun aimed at an assistant, and it probably is, but somebody may have typed it at my agent readiness guide deliberately. Single rows are evidence, not statistics.

AI Overviews and AI Mode can’t be separated at the query level. Google reports both under web search, so a fragment tells you a conversation happened, not which surface hosted it.

And the pattern library is English. A conversational query in Tamil or German only gets caught if it trips the length rung or a tool signature. The one Spanish probe in my data was caught by its “. my location is spain.” suffix, not its words. The multilingual model at the end of this post is built to close that gap. It isn’t out yet.

### Run It On Your Site

The classifier is genai_conversation_queries , a free tool inside my Search Console MCP , released today as v2.4.0.

If you don’t have the MCP yet, one command sets it up.

npx -y suganthan-gsc-mcp setup

The wizard signs you into Google, verifies the connection with a live call, lets you pick your property from a list, and writes the Claude config for you. The full setup guide covers Claude Desktop, Claude Code, and the manual routes with screenshots. It’s free and open source, and the server runs on your machine, so your data moves between you and Google and passes through nobody else’s servers.

If you already use it, the default config starts the server through npx, which picks up the latest published version.

Restart Claude, and you’re on v2.4.0. If you installed the one-click desktop bundle instead, download the new one from the releases page .

Either way, the next step is one sentence.

Run genai_conversation_queries on my site

One call pulls 16 months of your queries through Google’s regex filter, classifies every match down the ladder, attaches the landing pages, and returns the seven buckets with the monthly artifact timeline. BigQuery isn’t required; there are no new permissions beyond the Search Console access you already granted, and your data goes to Google and back like every other tool in the server.

If you run the BigQuery version of the MCP , v4.1.0 adds gsc_genai_conversation_queries , the same classifier over your bulk export. That twin has no API row limits, which matters on large sites, and it reports the anonymised split, so you get your own iceberg percentage next to your fragments.

https://cdn.searchenginejournal.com/wp-content/uploads/2026/08/screendrop-2026-08-12-19-53-25-3dfcfc-1-a7kt5.mp4

### John Mueller’s Tip (New)

I woke up to this nice comment from John Mueller on my LinkedIn post about it. He suggested setting up the BigQuery data export, because it might surface more of these queries.

Image Credit: Suganthan Mohanadasan

He’s right for large sites, and the reason is how much data each route out of Search Console hands over. The UI export stops at 1,000 rows per table. The API goes far deeper but tops out around 50,000 rows a day per search type. The bulk export has no row cap at all. On a big property, the tail the API drops is where these fragments live, since conversational strings are rare and almost never repeat.

On a site my size, the routes agree. I checked on August 14. My busiest day in the last four weeks held 988 distinct visible queries, about 2% of the daily API ceiling. The classifier found 625 conversation queries via the API versus 621 through the export, with the export lagging only because its data stops two days earlier. Small properties get identical answers from either route. If yours is big, run the BigQuery twin , which is the point John was making.

The pool from Idea 3 stays out of reach either way. Anonymized impressions sit in the export as rows with no query string, so BigQuery tells you how big the hidden pool is and keeps the strings to itself.

If you have already connected your Search Console property with BigQuery, then you can use my MCP to pull all of the queries with the same prompt.

You can access my BigQuery MCP here .

### Idea 4: Add The Generative AI Report Export

The tool you just ran shows what people ask. The Generative AI report shows how much of your visibility sits inside AI answers, page by page. Joining them gives you both numbers for every page.

The join needs one manual step from you, and here’s why. Google still doesn’t provide this data via the API, which I verified earlier in this post, so the tool has no way to fetch it. The export button in the UI is the only way.

Five steps, about two minutes.

Image Credit: Suganthan Mohanadasan

- In Search Console, open Performance, then Generative AI.

- Set the date range to the full 16 months.

- Press Export, top right, and choose Download CSV. It downloads as a zip.

- Unzip it. The file the join needs is Pages.csv, your AI impressions per page.

- Attach Pages.csv to the Claude chat where you ran the tool, and ask.

Map this export against my genai_conversation_queries results. For each page, show its AI impressions next to the fragments Google recorded on it.

Now every page has two numbers. How much of its visibility is inside AI features, and which actual conversation fragments Google recorded against it.

Image Credit: Suganthan Mohanadasan

The overlap gives you a directional hint I haven’t seen anywhere else. (We all know all the SEO tools are going to magically come up with this idea soon LOL.)

Reply artifacts and pivots come from AI Mode specifically, because that’s where follow-up conversations happen, while the export counts AI Overviews and AI Mode together. So a page with high AI visibility and rich fragments skews towards AI Mode conversations, and a page with high AI visibility and no fragments skews towards one-shot AI Overview citations. It’s an inference, not a measurement, but it’s the only wedge anyone has into a split Google won’t provide.

When Google adds an API for this report, I will update the MCP to fully automate this process.

### What To Do With What You Find

Each bucket wants a different response, and two of them want you to do nothing at all.

Pivot follow-ups are content instructions. [what about resend?] on my newsletter post means the comparison readers want isn’t in the post. Writing the Resend section answers a question people are already asking an AI about my page.

Conversational questions with impressions and no clicks show which pages get read inside answers. For those, title tweaks do very little, because the person never sees a title. What travels into an AI response is the passage that answers the question, the first paragraph under a heading, the table, the named fact. That’s the part to work on, and it’s the same conclusion I keep reaching from the ChatGPT side of this research.

Reply artifacts are corroboration, and a warning. They prove pages live inside multi-turn conversations, and they’ll wreck a naive analysis if left in. A keyword tool that doesn’t know about this class will eventually recommend optimizing for the query “yes.” Exclude the machine buckets, the probes and harnesses, from any opportunity analysis, and treat artifacts as a signal rather than demand.

And the probes deserve a minute of your attention on their own. If you run an AI visibility tracker , some of those daily prompts are yours, independently logged by Google, which makes your Search Console a free audit of what your tracker actually runs. If you don’t run one, third parties are sweeping topics you rank for, every day, and you can watch them do it.

Which is the general point about all seven buckets. These are prompts from real sessions where Google’s AI reached for your pages. Every query fan-out tool , mine included, generates synthetic questions and hopes they resemble reality. This is reality, small sample, floors and all. Use it as a guide to how people phrase things at your content, not as a volume dataset.

### The Answer To The Question

Ross asked how we reverse-engineer Search Console recording people’s responses to AI Mode.

The answer turned out to be a pattern library, a strict order of checks, and the discovery that the recording includes more than people.

It includes the AI industry’s own machinery too, tracker probes and agent harnesses showing up in everyone’s query reports.

Run the tool, read your fragments, and go look at what your site says in the passages the AI keeps choosing. The conversations are already happening. Google’s been taking minutes.

### Why Google Isn’t Showing Query Or Click Data

I know this is a small dataset with leaked fragments. Even so, there are barely any clicks , despite having decent impressions and very good average positions.

Which answers why Google isn’t including this in Generative AI reports.

I doubt they’ll ever add it, but only time will tell.

Image Credit: Suganthan Mohanadasan

### The Multilingual Model

The pattern list has edges. It only works in English, and on the border between a conversational query and an ordinary long one, it makes rule-based guesses. Both problems want machine learning rather than more regex, so I’ve already trained a model.

It understands languages the patterns can’t, including [kannst du mir das bitte zeigen], and it handles the border cases the rules guess at. (Don’t ask what it is because I picture a German politely asking me if I want some coffee.)

Image Credit: Suganthan Mohanadasan

I’m not releasing it yet. It’s currently trained on some real and synthetic data.

For example, on a recipe site, [can you freeze cooked chicken] is a regular search that looks like a conversation. So I’m testing it against other niches and making it better first.

The plan is a free tool where you drop your export in and get your buckets back, with the classification running in your browser so your queries never leave your machine. (As usual, respecting your privacy.)

It’s coming when I’m happy with the output.

More Resources:

- Google Now Reports AI Search Impressions. Here’s How To Read Them

- Google’s ‘Generative AI’ Search Console Data Is A Trap For Marketers

- How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers)

This post was originally published on Suganthan .

Featured Image: Ball SivaPhoto/Shutterstock

Category SEO AI Search

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

I’m the Co-founder of Snippet Digital, A Search Journey Optimization agency helping brands win across every stage of modern discovery. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/the-ai-conversations-leaking-into-your-search-console/585663/)
