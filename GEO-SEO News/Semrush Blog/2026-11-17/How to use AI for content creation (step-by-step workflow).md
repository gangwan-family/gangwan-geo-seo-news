---
title: "How to use AI for content creation (step-by-step workflow)"
source: "Semrush Blog"
published: 2026-11-17T12:38:00+00:00
fetched_at: 2026-11-18T02:58:54.779587+00:00
url: "https://www.semrush.com/blog/how-to-use-ai-for-content-creation/"
guid: "https://www.semrush.com/blog/how-to-use-ai-for-content-creation/"
author: "Carlos Silva"
categories:
  - "AI"
---

# How to use AI for content creation (step-by-step workflow)

- Source: Semrush Blog
- Published: 2026-11-17
- URL: https://www.semrush.com/blog/how-to-use-ai-for-content-creation/
- Author: Carlos Silva
- Categories: AI

## RSS 摘要

How to use AI for content creation, based on the Semrush blog team‘s own process. Includes the research skill we use, ready to copy into Claude.

## 原文正文

How to use AI for content creation (step-by-step workflow)

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

## How to use AI for content creation (step-by-step workflow)

Author : Carlos Silva

17 min read

November 17, 2026

Contributor: Faizan Ali

AI can write a blog post, script, or caption in seconds. The harder part is getting a final draft with a clear point of view, the right evidence, accurate product information, and enough original insight to be worth publishing.

That comes down to what you set up before the first prompt: the data the AI can pull, the standards it follows, and where you step in to review its work. You can run this workflow on its own for a single article or as part of a broader AI content strategy .

We'll use long-form blog articles as the example throughout. The same setup works for social posts, scripts, and email, and the FAQ covers what changes.

### Why most AI content fails

Give AI a prompt like "Write a 2,000-word SEO-optimized blog post on {topic}" and you'll get a draft back.

The sentences flow, the grammar is clean, and the structure usually makes sense. But read past the first few paragraphs and it keeps moving without going anywhere. It covers the expected points but has no point of view and nothing from firsthand experience.

The problem starts with what the model was given. A blank prompt gives it no real search data to work from, so it guesses at what people search for. It also has no standards for how your brand writes, and nobody reviews its decisions along the way.

### Prerequisites for your AI content workflow

Before you use AI for research or drafting, build the same working environment you would use yourself: the right data, clear editorial standards, and defined points for human review.

#### Connect AI to your real data

Model Context Protocol (MCP) lets you plug tools like Semrush straight into Claude or ChatGPT, so the AI pulls live numbers.

Semrush MCP provides access to keyword, SERP, organic ranking, and competitor SEO data. Several Semrush plans include it with 50,000 API units, and every MCP request uses some of them.

If you don’t have MCP access, you can do the same research by hand in Keyword Magic Tool and Keyword Overview .

For content research, we connect a source for each question:

What we need to know

Connected source

What it gives us

What are people searching for?

Semrush MCP

Search volume, keyword difficulty, related keywords, and intent

What does a page or domain already rank for?

Semrush MCP (Organic Rankings data)

Keywords the page or domain ranks for, plus their positions

What ranks for the target query?

Semrush MCP

Top-ranking URLs and SERP features for the query

What do those ranking pages cover?

Firecrawl MCP

Full-page content for comparing structures, arguments, examples, evidence, and gaps

What does our existing page already earn?

Google Search Console (GSC)

Queries, impressions, clicks, and changes over time

Set a clear scope for each MCP request by naming the exact metrics you want back. For example:

Using Semrush data: Analyze the top organic search competitors for {keyword} . Provide the search volume, keyword difficulty, search intent, 10 related keywords, and the top 10 ranking URLs.

If you are unsure what to prompt, the MCP Prompt Library has ready-made workflows for tasks such as discovering keyword gaps and identifying quick-win content updates. Adapt the relevant workflow to your domain, market, and research question rather than building every query from scratch.

Use Firecrawl MCP to retrieve competitor pages and compare their headings, arguments, examples, sources, questions answered, and gaps. You’ll need a Firecrawl account, and each MCP request uses credits from your plan. If a page cannot be retrieved, instruct the model to flag it.

For an existing page, add Google Search Console (GSC). Semrush estimates what a page ranks for, but GSC shows what it actually earns: the queries bringing in impressions and clicks, where performance has changed, and which search demand you could disrupt.

GSC doesn’t have the same one-click connection as Semrush MCP. The quickest option is to export the relevant Performance data, such as queries, impressions, clicks, and changes over time, and upload it to your AI tool. For repeatable access, set up an API connection instead. Our Claude Code SEO guide covers both approaches in detail.

#### Give it your standards as files for context

Give AI two layers of context: persistent standards that apply across articles and article-specific context that changes with each piece .

Persistent standards can include:

- Brand and style guidelines: voice, formatting, spelling conventions, terminology, and constructions you avoid

- Brief template: the structure every content brief needs to follow

- Sitemap: the current URLs available for internal linking

- Product rules: what your products do, their limitations, and current UI labels

- Deprecated tools list: tools or features you no longer recommend and their replacements

Store these as files in a project or skill (we cover projects and skills below) so that your AI tool can reference them throughout the workflow. You write the rule once instead of re-explaining your terminology, comma policy, product conventions, or formatting rules every time you start a new chat.

For instance, if you add your product list and deprecated tools as files and tell AI to check every product mention against them, it can flag outdated names before the draft reaches editing.

In our workflow, this check caught a draft that called Semrush's social scheduling tool "Semrush Poster" and changed it to the current name, Social Poster.

Article-specific context changes with every piece and can include:

- target keywords and search intent

- SERP and competitor findings

- content gaps

- internal and external evidence

- subject matter expert input

- requirements unique to the brief

For product-led content, add the documentation for the features you plan to cover: current Knowledge Base articles, supported workflows, and limitations. Screenshots or your own notes from the current UI help it describe workflows correctly.

#### Decide where humans stop the process

Fully automated publishing doesn’t hold up because research errors compound. If the research reads the search intent wrong, the outline builds the article around that mistake, and the draft repeats it in every section.

Build in at least two places where you stop to approve the work:

- After research : Review the evidence, conclusions, and gaps before they shape the article

- After you edit the outline :Review the argument, scope, order, and product or tool choices before drafting begins

In our workflow, those two gates take 40-50 minutes combined. A structural problem that takes a minute to fix in the outline can take hours to untangle once the article has been drafted around it.

With both stops in place, the workflow looks like this:

Research → [Gate 1: approve research] → Outline → Edit outline → [Gate 2: approve outline] → Draft → Review and revise → Verify → Ship

### The workflow, step by step

Run the article through seven tasks: research, outline, edit, draft, review, verify, and ship. Each one produces the input the next stage needs.

#### Step 1: Research

Start with a seed keyword for a new article or an existing URL for an update .

If you have Semrush MCP connected, run a prompt to identify 3-5 keywords for the topic and their metrics, analyze the SERP for the primary keyword, and surface the subtopics the article needs to cover.

For our "website marketing" article, the research pass picked "website marketing" (5,400 searches a month) as the primary keyword, with four secondaries. It left out agency-hire queries like "website marketing company" on purpose. Some had more volume than the secondaries it kept, but they belong on a service page. It also flagged a mismatch. When we ran it, Semrush tagged the keyword as commercial, but the live SERP was mostly informational guides, so we planned an informational article. Semrush has since updated the tag to informational, which is what the Keyword Magic Tool screenshot below shows.

If you’re running the workflow manually, enter the seed keyword in Keyword Magic Tool to find related terms and question queries, then review their volume, difficulty, intent, and topic groupings.

Use Keyword Overview for the primary query. Its SERP Analysis shows the ranking URLs and SERP features currently appearing for that keyword.

Use Firecrawl MCP to pull the top-ranking pages and compare their formats, arguments, and data points. Drop any that don't match your intent, like the help page and the glossary in our results.

Then add your own evidence and audience language. Paste or upload material from sales calls, support tickets, reviews, or forums.

This is your first stop. Review the findings, then save the approved sources, gaps, and observations in a research file. That file becomes the input for the outline.

#### Step 2: Turn the research into an outline

Give AI the approved research file, your brief template, and the point you want the article to make.

Ask it to build an outline that:

- builds every section toward that point

- matches the search intent from the research

- names the stat, study, or example from the research file that backs up each section

- incorporates product or tool workflows where they solve the reader’s problem

Watch for headings that sound good but don’t tell the reader anything, and sections that claim more than the research shows.

#### Step 3: Edit the outline yourself

Spend about half an hour here. It’s the cheapest point in the workflow to fix the structure.

Check for:

- Order : Move sections so each one builds on the one before it

- Scope : Give each section one job. Split a section that's doing two, and fold thin sections into the one they support

- Priority : Give your strongest ideas their own sections instead of burying them as subheadings

- Research support : Remove sections the research does not support, or add the missing evidence before drafting

- Product choice : Make sure each product or feature you mention is the right one for that section

For our “website marketing” article, the initial outline placed the UX section at point 12 and Digital PR as a subheading under Guest Blogging. During review, we moved UX earlier so the first four tactics stayed focused on optimizing the website itself before shifting into social and third-party channels. We also made Digital PR a standalone section because it covers a broader set of authority-building activities than guest blogging alone.

When you’re happy with the outline, approve it. That’s your second stop. Drafting starts from the approved version.

#### Step 4: Draft using the approved outline

Give AI the approved outline, research file, brand and style guidelines, and any article-specific context, such as a subject matter expert’s input or product documentation.

AI handles structured material well, especially definitions, step-by-step explanations, comparisons, and tables built from the information you’ve already gathered. You still have to supply the parts that take judgment or experience: the point of view, firsthand examples, and the call on which product or feature fits the use case. Write those yourself, or give AI your notes to work from.

Ask AI to draft one section at a time so it can work from that section’s question and evidence in the outline.

#### Step 5: Review and revise

Review the completed draft in two passes. First, read it as a whole to make sure it makes the point.

Google updated its helpful content guidance in October 2026, and it now names four qualities its search quality raters look for: effort, originality, talent or skill, and accuracy. Use them as a quality check.

Check whether the draft includes original analysis, firsthand testing, or insights from subject matter experts that demonstrate real experience and expertise. Strengthen or remove sections that simply rephrase what's already published.

Our Google E-E-A-T explainer video covers why experience and expertise matter:

Then move to sentence-level edits. When something is off, identify the exact issue and give AI the context needed to correct that section.

For example, if a section blurs two terms your brand defines differently, highlight the passage, provide the relevant definitions, explain the distinction, and ask AI to revise that section.

Use the same approach for other problems:

- provide the relevant product documentation when a feature is described incorrectly

- supply supporting evidence when an argument lacks support

- restate the applicable style rule when the writing drifts from your standards

- clarify the section’s purpose when the argument moves in the wrong direction

Apply the correction, check that it solves the original problem, and then continue through the draft.

#### Step 6: Verify claims and links

Use AI to build a verification list from the draft, flagging claims, statistics, links, and product details that need checking. The model that wrote a claim is a bad judge of whether that claim is correct, so verify each item yourself against the relevant source.

Google's guidance on generative AI content , also updated in October 2026, says the same: a person should fact-check AI-generated content before it's published.

Check:

- Claims and statistics : Open the original source and confirm that the data, context, and findings support exactly what the draft says

- Internal links: Verify every link against your current sitemap

- Product details and workflows : Check claims against current product documentation and, where possible, the product itself. Confirm that the feature works as described and fits the stated use case

- AI-generated metadata : Check title tags, meta descriptions, structured data, and image alt text for accuracy and relevance

While we were editing this article, AI flagged our Claude skills plan details as wrong. It said skills needed a paid plan and couldn’t be shared directly with colleagues. Anthropic’s help center showed our draft was right: skills were available on the Free plan, and Team and Enterprise users could share them directly. If we’d taken the flag at face value, we’d have published the wrong plan details.

#### Step 7: Ship it

Read the article yourself one last time for formatting, image placement, links, CTA, heading hierarchy, and anything affected by the final revisions.

For a deeper walkthrough of researching, outlining, drafting, optimizing, and editing AI-assisted content, see our AI-generated content guide .

### Updates work differently from new URLs

The workflow follows the same basic sequence for new URLs and existing pages, but the starting point changes what each stage needs to do.

Stage

New URL

Update

Starting point

Seed keyword

Existing URL + performance data

Research job

Decide what the article should cover

Diagnose what broke and what is missing

Structure

Build the structure from scratch

Keep the existing headings and add or correct what is needed

Drafting

Draft the full article

Draft only the new or corrected sections

Main risk

Repeating the same generic coverage that already ranks

Disrupting a page that is already performing

Before you touch an existing page, use GSC to see where clicks and impressions have changed, then check Organic Rankings for the keywords and positions it still holds. Leave the headings that support those rankings alone, and change only the sections the diagnosis calls for.

To see Claude audit a site’s existing content, watch our walkthrough:

### How to use Claude AI for content creation with a reusable workflow

Once the workflow works by hand, save each step as a Claude skill so you don’t have to re-explain it for every article.

#### Turn recurring tasks into skills

A skill lets you save instructions for a recurring task so Claude can apply the same process again. When a request matches a skill’s description, Claude can load that skill automatically and follow its instructions.

As of November 2026, skills are available on Free, Pro, Max, Team, and Enterprise plans, with code execution enabled. On Team and Enterprise plans, skills can also be shared with colleagues when skill sharing is enabled, or provisioned across the organization by an owner.

You can build a skill by describing the task, when it should run, and the instructions it should follow. Anthropic's guide to creating skills walks through each part.

Claude also has ready-made skills . Go to Customize > Skills and open the Discover tab to browse them, or use the Add button to create or upload your own. Skills need code execution turned on: check Settings > Capabilities, or ask your org owner on Team and Enterprise plans.

Skills can also include supporting files, scripts, or other resources the workflow needs.

To turn one stage of your content workflow into a skill:

- Choose one recurring task : Start with something bounded, such as research, briefing, drafting, or verification

- Describe when to use it : Claude reads the description to decide when to load the skill, so say what it does and when it applies

- Define what it receives : Specify the inputs the skill needs before it starts, such as a seed keyword, research file, approved outline, or completed draft

- Write the instructions : Document the steps it should follow, the tools or files it should use, and the rules it should apply

- Define the output : Tell it exactly what to return so the next stage can use it

- Add supporting context : Attach the templates, product documentation, brand standards, or other resources the task needs

Start with research, since everything after it builds on what it finds.

---

name: research-new-article

description: Research a new article from a seed keyword using Semrush MCP, Firecrawl, and supplied audience evidence. Use before outlining a new article.

---

Research a new article from a seed keyword and produce a research file for human review.

## Input

A seed keyword.

Use any supplied brief, audience research, customer language, SME input, or internal evidence as additional context.

## Process

1. Use Semrush MCP to retrieve relevant keyword metrics, related queries, SERP data, and ranking URLs.

2. Identify the ranking pages that compete with the article. Exclude pages with mismatched intent or page type.

3. Use Firecrawl MCP to analyze those pages for:

- Topics and subtopics

- Arguments and angles

- Examples and workflows

- Evidence and sources

- Questions answered

- Content gaps

4. Incorporate relevant audience language and internal evidence supplied with the task.

5. Keep retrieved data separate from your interpretation of it.

6. Flag anything you cannot retrieve or verify.

## Output

Create a research file containing:

- Keyword and SERP findings

- Relevant competitor findings

- Recurring questions

- Useful evidence and sources

- Content gaps

- Audience insights

- Open questions for human review

Stop after producing the research file. Wait for explicit human approval before creating the outline or draft.

If you build it in Claude’s “Create a skill” form, like the one below, the name and description go in their own fields and everything below the second “---” goes in the instructions box.

Skills in ChatGPT can support the same workflow. As of November 2026, they’re available to eligible Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability. Use the same inputs, instructions, output, and approval gates so the workflow stays consistent across AI tools.

#### The five skills

Package the workflow into five skills with clear handoffs:

Skill

Input

What it does

Output

Research skill

Seed keyword

Pulls keyword, SERP, and competitor data with Semrush MCP and Firecrawl, and adds the audience evidence you supply

Research file

Brief skill

Approved research file + brief template

Turns the research into an outline using your template

Draft brief and outline

Draft skill

Approved outline + research file + style guidelines

Writes the article section by section using the approved structure and relevant context

Draft

Verify skill

Completed draft + source and context files

Flags statistics, links, claims, and product references for manual verification without rewriting the draft

Flagged verification list

Update skill

Existing URL + performance data

Diagnoses what broke and what is missing, keeps the existing heading structure, and identifies the sections that need to be added, corrected, or refreshed

Update plan

#### Set up the workflow context

Put preferences that apply to every chat, like tone or formatting, in your account-wide instructions in Claude’s settings or ChatGPT’s custom instructions.

For a specific content workflow, create a project and add the relevant files and instructions it needs. Project instructions apply only within that project.

For an SEO blog project, add the persistent standards files from earlier in this guide, plus any instructions specific to that workflow. A case study or whitepaper project would get its own files and instructions.

Create and enable the research, brief, draft, verify, and update skills in your Claude account, and connect Semrush MCP and Firecrawl. Skills are available across your account and don't need to be added to individual projects.

Build the approval gates into the skill instructions. The research skill stops after producing the research file and waits for human approval. The brief skill does the same after producing the outline. Start the next stage only after you approve the previous output. The last line of the SKILL.md above is what makes it stop.

For a new article, the sequence looks like this:

- Run the research skill : Enter the seed keyword and save the findings in a research file

Gate 1: Approve research (10-20 minutes) : Correct wrong conclusions, remove weak sources, and resolve open questions before proceeding

- Run the brief skill: Build an outline from the approved research using your brief template

- Edit the outline (about 30 minutes): Fix the order, scope, unsupported sections, and product choices

Gate 2 : Approve outline: Sign off on the edited version before drafting

- Run the draft skill: Draft the article from the approved outline, research, and supporting context

- Review and revise: Check the argument, logical flow, originality, and writing quality. Revise the draft before verification

- Run the verify skill: Generate a flagged list of claims, links, statistics, and product mentions. Check each item against its source

- Ship: Resolve remaining issues, complete the final formatting, and publish the article

For an existing page, the update skill becomes the entry point. Give it the URL and performance data so it can diagnose what needs to change and produce an update plan. Review and approve that plan, then draft and verify only the sections it covers.

### What AI still can't do

Four things stay with you: original opinion, firsthand experience, deciding what matters, and knowing when the SERP data is wrong.

An opinion is a position you'd defend to a colleague, and the model has none. Firsthand experience is what you saw happen on a real project, and the model wasn't there. Deciding what matters is choosing which of twelve valid sections are the three worth writing, which is a judgment about your reader. And knowing when the data is wrong, such as a volume inflated by a news spike or a SERP temporarily distorted by a breaking event, comes from having watched it before.

### Common ways this goes wrong

Here's where it usually breaks:

- Skipping the setup : AI describes a product feature using an outdated name or workflow because you never gave it the current product documentation or deprecation rules.

- Trusting an unverified statistic : The draft cites a statistic correctly but makes a broader claim than the original data supports.

- Removing the approval gates after a few good runs : The research skill pulls the wrong competitor pages, and the outline is built around the wrong search intent before anyone reviews it.

- Treating an update like a rewrite : AI rewrites the whole page, replacing headings that still rank and missing the sections that lost traffic.

Start with one content type and run it by hand a few times before you turn the steps into skills.

### Frequently asked questions

#### Can you use this workflow for social posts, video scripts, or email?

Yes. The setup and the two reviews carry over. The skill instructions change with the format.

For social posts, define the platform, length, hook, and CTA. For video scripts, add runtime and spoken structure. For email, specify the audience, offer, CTA, and any compliance requirements.

#### Does Google penalize AI content?

Google does not penalize AI content based on how it was produced. It evaluates the quality and purpose of the content instead. AI-assisted content can rank when it’s accurate, useful, and adds something beyond what already exists.

The bigger risk is scaled content abuse: publishing large volumes of low-value or unoriginal pages primarily to manipulate rankings, whether they were created by AI, humans, or both.

For more, see our guides on whether Google penalizes AI content and whether AI content is good for SEO .

#### Which AI tool should you use for content creation?

We run ours in Claude. ChatGPT can run much of the same setup with projects, the Semrush MCP connector, and skills on Business, Enterprise, Healthcare, and Edu workspaces.

If you’re choosing a tool, check whether it can hold your standards files, connect to live data, and save reusable instructions, since this workflow depends on all three. Then give each one the same real task and compare how much editing the output needs. Our AI writing tools guide covers more options.

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

[Read original](https://www.semrush.com/blog/how-to-use-ai-for-content-creation/)
