---
title: "AI citation outreach: a Semrush & Claude workflow"
source: "Semrush Blog"
published: 2026-09-21T09:49:00+00:00
fetched_at: 2026-09-22T00:11:50.118725+00:00
url: "https://www.semrush.com/blog/ai-citation-outreach/"
guid: "https://www.semrush.com/blog/ai-citation-outreach/"
author: "Carlos Silva"
categories:
  - "AI"
---

# AI citation outreach: a Semrush & Claude workflow

- Source: Semrush Blog
- Published: 2026-09-21
- URL: https://www.semrush.com/blog/ai-citation-outreach/
- Author: Carlos Silva
- Categories: AI

## RSS 摘要

AI answers pull brand facts from the pages they cite. Use Semrush data and Claude Code to get on those pages.

## 原文正文

AI citation outreach: a Semrush & Claude workflow

Find new opportunities across AI search and SEO.

AI search and SEO.

Try free for 7 days

Login Sign up

Outperform your search competitors. Search now spans Google, ChatGPT, and beyond—and Semrush gives you the SEO and AI visibility tools to stay visible everywhere:

See how AI platforms talk about you

Discover valuable topics to cover

Get AI-powered strategy suggestions

Build keyword plans with personalized insights

Identify fixes to improve technical health

Benchmark yourself against competitors

Try for Free

10M marketing professionals have already used Semrush

## AI citation outreach: a Semrush & Claude workflow

Author : Carlos Silva

13 min read

September 21, 2026

Contributor: Faizan Ali

Optimizing for AI search is both an on-page and off-page effort. Your website should be accessible and optimized for AI models. And it also needs to appear on third-party websites that these models cite when answering user prompts.

This guide breaks down the AI citation outreach process step by step.

You’ll learn how to find citation opportunities in Semrush and how to automate the process in Claude Code.

### What is AI citation outreach?

AI citation outreach is the process of finding pages AI answers cite and getting your brand included on those pages.

Securing AI citations isn’t just about collecting backlinks .

When an AI answer cites a specific webpage in an answer to a prompt, it means that AI identified that webpage as authoritative, helpful, and relevant to that prompt.

The brands mentioned on the page also benefit from that authority. Because it boosts their visibility in AI search . And provides important brand context that AI can reference.

### Why third-party sources influence AI visibility

Third-party websites influence AI visibility because large language models (LLMs) retrieve and synthesize information from multiple sources to answer a prompt.

AI also looks at your brand’s website.

But the chances of AI mentioning your brand are higher when you appear in relevant online sources more often.

In fact, our study with Kevin Indig found that 62% of AI citations don’t result in a brand mention, also known as “ghost citations.” So AI might cite your website in a response, but never mention you. The same dynamic shows up in Google AI Overviews , where a brand's visibility often rests on a small number of cited pages.

This is particularly important for evaluation-stage prompts: questions buyers ask when weighing solutions.

For example, if you ask Claude “What are the best AI meeting notetakers?”, it runs a web search and reads multiple sources.

Not all of these websites are AI notetaking companies. For example, Claude used two real user reviews published on Medium. The response also references G2 ratings.

Claude notes in its response that four brands dominate almost every comparison list: Otter, Fathom, Granola, and Fireflies.

So even though the product reviews Claude read mention many other notetakers, it recommends the four with the overall largest presence.

However, the reviews Claude pulled also contain outdated information, which impacts the quality of a brand’s AI visibility.

For example, the response claims that Granola doesn’t separate speakers. But its product documentation says speaker attribution is available through speaker tags on Zoom and Google Meet.

So AI citation outreach isn’t just a strategy to close AI visibility gaps . You should also use it to ensure online sources provide accurate information about your products.

### How to prioritize AI citation opportunities

When prioritizing opportunities for AI citation outreach, take into account the following factors:

Factor

Why it’s important

Citation impact

The pages you prioritize should feature frequently in AI responses across AI platforms. This is proof they are influential.

Prompt relevance

The cited pages should appear in responses to prompts that are highly relevant to your brand. Such as product evaluations or issues your brand helps solve.

Competitor presence

If an AI citation opportunity already features your competitors, prioritize it over pages that don’t mention any of them.

Brand gap size

Does the cited page contain outdated or incorrect information about your brand? If yes, it’s a priority since it could also influence LLMs to misrepresent you.

Publisher authority

Publications with industry authority carry more weight in AI responses. And your audience is more likely to trust them, too.

Outreach feasibility

Some websites, like those belonging to competitors or governments, are less receptive to outreach.

Your final list of top opportunities should be feasible to implement and include frequently cited domains .

### How to find, win, and track AI citation outreach opportunities

To find AI citation outreach opportunities, extract the pages AI cites for your priority prompts, analyze them, then plan your outreach.

If you’re only analyzing a handful of prompts, you can do this manually in your AI visibility tracking tool.

But to do it at scale, you can use Claude Code. We’ll show you how to do it step by step below.

#### Step 1: Pull citation data

The first step is to export citation data from the AI visibility tracking tool you use to monitor prompts.

If you aren’t monitoring prompts yet, you can do it in Semrush’s Prompt Tracking tool. Enter your domain and click “ Set up tracking .”

Select the AI model to track prompts in. You can choose from ChatGPT, Gemini, and Google AI Mode. Add your location, then click “ Continue To Prompts .”

Then, upload prompts to your campaign.

After you paste the prompts, click “ Add prompts to campaign ” > “ Start tracking .” Wait up to 24 hours for the data to populate.

In the Prompt Tracking report, go to “Sources.” Here, you’ll find the pages AI cites in responses to your tracked prompts. And whether your brand is mentioned.

Download the list by clicking “ Export .” Name it “sources.”

You’ll use this CSV file to run the rest of the analysis in Claude Code.

#### Step 2: Set up your Claude Code workflow

Claude Code is a version of Claude that works with files on your computer.

Although it’s a developer tool, you don't need to have coding knowledge to use it. You write your instructions in plain English, save them in a file, and Claude follows them.

Our AI citation outreach workflow in Claude Code allows you to analyze hundreds of webpages at a time. And find the best opportunities to get more AI visibility.

The workflow automatically checks whether your brand appears on specific pages and in what context, saving you hours of manual work.

Here’s how to set it up.

##### Install the Claude desktop app

Download the desktop app from claude.com/download and install it. Then launch it, sign in, and look for the “ Code” tab.

You'll need a paid Claude plan (Pro, Max, Team, or Enterprise). Claude Code isn't available on the free tier.

##### Create your project folder

Make a new folder on your computer and name it “ai-citation-outreach.” Move your prompt tracking CSV export into it.

Then, create three plain text files in the “ai-citation-outreach” folder that tell Claude Code how to execute the workflow.

You can create these files manually using any text editor or generate them with Claude’s help.

File

What it does

CLAUDE.md

Explains the AI citation outreach project. Claude reads it automatically at the start of every session.

brand-facts.md

Your approved brand information. When analyzing outreach opportunities, Claude will check pages against this document to flag issues.

analyze-sources.md

Your instructions for the citation outreach analysis. Claude will save it as a command in the “.claude/commands/” subfolder.

We’ll cover how to create these files and what they need to include in the next section.

##### Create the project files

The “CLAUDE.md” file is a project context document. It needs to explain the CSV data so Claude reads it correctly. And understands what to do.

Here’s an example using the Prompt Tracking CSV export.

Then, prepare the “brand-facts.md” file. It should include information about your:

- Product positioning

- Pricing

- Available products and services

- Direct competitors

- Any incorrect information or claims that third-party pages often publish

And other key information that you want third-party websites to include or get right. Keep the document succinct, as overloading Claude with too much context can create confusion and slow down the process.

The file "analyze-sources.md" contains detailed analysis instructions.

Before you write it, first decide which pages Claude should skip. For example, exclude:

- Your domain

- Social media

- Knowledge bases that don't take pitches

- Directories and marketplaces

- Vendor help centers, like help.openai.com

Handle review platforms separately. Instead of skipping them, ask Claude to write them to a second file.

And don't exclude competitor domains. A competitor's blog or comparison page might still be worth pitching.

Then, tell Claude how to categorize the pages. You can use this type of framework:

- Not mentioned: The page covers your category and lists comparable brands, but you're absent.

- Underrepresented: You appear, but with less depth or prominence than comparable brands on the same page.

- Outdated or inaccurate: Your brand is represented, but the page contradicts your brand facts.

- Negative: You appear in a critical or unfavorable framing.

- No clear opportunity: The page is off-topic, doesn't cover brands like yours, or already covers you well.

- Manual review: Pages Claude couldn't open or assess.

Write the file manually or with Claude’s help. Here's an example .

Now have Claude save the file to your project folder.

Open Claude Code > “ Select folder ” > “ ai citation outreach .”

Paste this prompt, with your own instructions in place of the placeholder:

Create a folder called .claude/commands/ in this project, and save the following as analyze-sources.md inside it. Use the text exactly as written:

[paste your instructions here]

Claude will confirm once it creates the command:

To check the command saved correctly, type "/" in the prompt box. If "analyze-sources" shows up in the list, Claude found it and you're ready to run the workflow.

The file should also appear in your project folder.

This is what the completed folder looks like:

Now, you’re ready to test the AI citation outreach analysis workflow.

#### Step 3: Run the AI citation outreach analysis

To run the AI citation outreach analysis, open Claude Code, select your project folder and type “/” in the prompt box.

Select “ /analyze-sources .” Use a more advanced model like Opus for the analysis.

Hit enter.

Claude Code will run the workflow and update you on its progress:

The amount of time and tokens Claude spends on the workflow depends on how many URLs are in the Sources file. (Tokens are data units that AI processes. The more data that Claude analyzes, the more tokens it uses.)

If the analysis is taking too long, you can always tell Claude to stop the workflow and resume it later at your command.

When Claude finishes, or when you stop it early, you'll get a summary of what it produced:

The workflow produces opportunities.csv (assessed pages), manual-review.csv (pages Claude couldn't open or finish), and routed-reviews.csv (review-platform pages from your exclusion rules). Open each CSV file to start the review process.

#### Step 4: Review and validate Claude's output

Review the output in the “opportunities.csv” file.

Human review is non-negotiable because Claude Code can still make mistakes.

Claude is also non-deterministic. So if you run the analysis of the same file twice, you might get slightly different classifications on borderline pages.

Using our H&M example, one of the top opportunities is this roundup of the most affordable office clothes for women .

The page links to H&M twice, but Claude labeled it as “Underrepresented” and provided this explanation:

“H&M appears once (a ~$50 blazer) among ~50 brands. Expand its workwear presence, tailored trousers, blazers, and knitwear, with current price points so it reads as a fuller affordable-workwear option next to Uniqlo, Mango and Zara.”

A manual review of the page confirms Claude’s opportunity categorization. There are additional categories where the webpage could mention H&M products, but doesn’t.

Claude also missed that the article features H&M twice, in the blazer and tops sections, not once.

This is exactly why a human needs to review every opportunity. If a publisher finds an error in your pitch, they might ignore your email.

The first time you run the workflow, you might find similar errors or areas for improvement. Ask Claude to diagnose the issues in the current workflow and update the project files so future runs don't repeat the same errors.

#### Step 5: Prepare the outreach handoff

Create a separate spreadsheet with a list of your human-reviewed priority opportunities. It should include:

- The page URL

- Associated prompts

- Number of citations

- Claude’s classification

- Claude’s recommendation alongside any of your additions

- Outreach owner

- Date of outreach

- Outcome

In the “Recommendation” column, provide enough context to the outreach owner so they write a tailored pitch .

- Insufficient context: “Add H&M to this listicle.”

- Sufficient context: “H&M appears as a $50 blazer among 50 brands. Suggest adding pants and tops with current prices.”

When drafting the pitch, suggest a low-lift change instead of a long list of additions to the article.

Sean Markey, who does outreach for Semrush, found that opening with a single correction and then asking permission to send more gets a better response than leading with the full request.

Here’s an example of his pitch:

Hi Andi,

My name is Sean and I'm working with Semrush.

I'm writing about your post on how to check your Google ranking. We're in there as "SEMrush" (thanks for the mention!), but I'm hoping we can fix that to just "Semrush," plus a few other small things.

Is it cool if I send over a quick write-up from the content team you can use to update it?

Thanks, Sean

Of his last 14 responses, 8 agreed to receive the changes without asking for anything in return.

You can adapt the same structure to any opportunity type. Here’s an example using H&M:

Hi Kat,

My name is [Name] and I work with H&M.

I'm writing about your roundup of the most affordable office clothes for women. We're in there with a $50 blazer (thanks for including us!). Our prices and stock move around a fair bit, so I'd be happy to send you the current details for that piece.

We also have a few other workwear items that would fit the post well. Is it cool if I put together a short write-up with current prices you can use to update it?

Thanks, [Name]

Send a follow-up email if you don’t get a response in 3-4 days.

Some publishers might come back with a value exchange request. Before starting the outreach, align on a negotiation approach so your outreach team has a clear process to follow.

For example, you might offer:

- A backlink, as long as your website contains pages where you can include links organically, like a blog

- Free or discounted product access

- A social media shoutout

- A one-time payment. Give the outreach owner a clear budget, so they have room to negotiate

Log every ask in your outreach spreadsheet next to the opportunity.

#### Step 6: Track results

Track your AI citation outreach results in the same spreadsheet you built in step 5.

Note publisher responses, implemented changes, and when they went live. Then watch what happens in your prompt tracking.

Re-export the Sources report every month and compare it to your previous export. Monitor the following:

- Is the page still cited?

- Does your brand now appear in the prompt responses where AI cites these pages?

- Are new webpages appearing as citations? Do they mention your brand?

The North Star metric to track is your overall AI visibility and sentiment. Within a quarter, you should see growth in your AI response presence.

If this doesn’t happen, evaluate other aspects of your AI brand visibility strategy . Perhaps your product positioning and messaging is inconsistent. Or you might not have any organic content on your website that talks about what you do.

### AI citation outreach vs. traditional link building

The main differences between link building and AI citation outreach are:

Difference

Link building

AI citation outreach

Goal

Focuses on acquiring links from high-authority websites to drive referral traffic and improve off-page SEO . Links from authoritative websites also help search engines see your website as authoritative, which can improve your rankings.

Focuses on ensuring your brand appears on pages AI cites in relevant prompts. May include links but also incorporates important information about your brand.

Target selection

Targets high-authority websites in your industry that are also relevant to your audience.

Targets websites whose pages AI cites in relevant prompt responses, and where your brand doesn’t appear. Or it appears, but the information is outdated, incomplete, or negative.

Success metrics

Referral and organic traffic growth, increased domain authority, improved search rankings over time.

Looks at improved AI visibility in tracked prompt sets. AI referral traffic growth.

Outreach prioritization

Link building outreach prioritizes opportunities based on the domain’s industry relevance and domain authority.

Prioritizes outreach based on citation volume of a specific page and your visibility gap in the prompt set where the page is cited.

Even though there are differences between link building and AI citation outreach, our study with Kevin Indig and Growth Memo found that high-quality backlinks do influence AI visibility.

So investing in both is beneficial for your search and AI presence.

### Make AI citation outreach an ongoing part of your strategy

AI visibility is dynamic and requires ongoing monitoring. Now that you have a Claude Code workflow set up, it’ll be easier to perform AI citation outreach on a monthly basis.

Semrush Prompt Tracking shows you the pages AI cites for your prompts. And whether your brand appears in the answers.

Claude Code reads those pages and drafts the recommendations against your rules, which saves you hours of manual review.

But human involvement is still an essential step, especially when drafting the pitch, choosing opportunities, and building relationships with publishers .

Carlos Silva

Carlos Silva leads the editorial pipeline for the English blog and builds AI workflows that boost content quality and AI visibility. 10+ years writing and editing across in-house and agency roles.

Tells Google to show you more from Semrush in AI, Search, and Discover.

### Most popular pages

#### What Is Keyword Search Volume? (& How to Check It)

Keyword search volume is the average number of monthly searches for a search term in a particular location.

Keyword Research

Rachel Handley 3 min read January 10, 2025

#### How to Use Google Keyword Planner

Google Keyword Planner is a free tool that lets you research the queries people type into Google.

Keyword Research

Rachel Handley 7 min read July 23, 2024

#### How to Get Backlinks: 10 Realistic Methods

Learn how to get backlinks by responding to media requests, creating link bait, finding broken links, & more.

Link Building

Rachel Handley 10 min read October 17, 2024

## 原文链接

[Read original](https://www.semrush.com/blog/ai-citation-outreach/)
