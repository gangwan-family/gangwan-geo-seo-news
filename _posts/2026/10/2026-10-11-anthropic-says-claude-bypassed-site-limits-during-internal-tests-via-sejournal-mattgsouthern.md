---
layout: post
title: "Anthropic Says Claude Bypassed Site Limits During Internal Tests via @sejournal, @MattGSouthern"
date: 2026-10-11T22:07:32+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-11/Anthropic Says Claude Bypassed Site Limits During Internal Tests via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/anthropic-cuts-live-web-access-internal-tests/592534/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
  - "_src_search-engine-journal"
---

# Anthropic Says Claude Bypassed Site Limits During Internal Tests via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-11
- URL: https://www.searchenginejournal.com/anthropic-cuts-live-web-access-internal-tests/592534/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Anthropic cut live web access for internal evaluations after Claude submitted real forms and worked around website restrictions. The post Anthropic Says Claude Bypassed Site Limits During Internal Tests appeared first on Search Engine Journal .

## 原文正文

Anthropic Says Claude Bypassed Site Limits During Internal Tests Skip to content

SEJ Pro Sign In

Join Chris Sachs and Aris Vrakas of seoClarity to see how AI shopping agents pick products, and how to make your product pages readable to Google and ChatGPT.

Save My Spot

- SEJ

- ⋅

- AI Search

## Anthropic Says Claude Bypassed Site Limits During Internal Tests

- Anthropic says Claude submitted real forms and bypassed site restrictions in tests and internal use.

- A made-up homicide tip went to Philadelphia police and was filtered as spam.

- Anthropic cut live web access for its internal tests until its safeguards prove reliable.

Anthropic says Claude submitted real forms and worked around site restrictions in tests and internal use. It has cut live web access for internal evaluations.

Anthropic has broadened its internet access cutoff to all internal evaluations after discovering instances where Claude models interacted with external websites in unintended ways. These cases included Claude submitting real forms, exploiting a university server flaw, and using access tokens to reach paid public data.

Several of these sites are managed by federal, state, and local U.S. government agencies. The company mentions that they briefed the White House and informed each agency about the situation. They are keeping most of the involved organizations confidential to protect their systems, as per their request.

Anthropic believes the real-world impact is minimal. They consider these situations to be much less serious, on alignment and security grounds, than the cybersecurity incidents they shared in July and September . For example, in one instance, Claude sent a false homicide tip to the Philadelphia Police Department, which then published its own report .

### What Claude Did On Live Sites

Anthropic describes most of the behavior in its report as persistence, where Claude works around a restriction instead of stopping when it can’t finish a task as given.

During an evaluation, Claude Mythos Preview encountered an error while using a university’s public analysis tool. It discovered a script on the university’s server that responded to any requested file and was used to copy files, including the script’s own code. Inside that code, it identified an injection flaw that allowed it to execute commands on the server and complete the calculations.

The company’s models submitted forms they shouldn’t have. For instance, an unreleased research model ended up submitting a real government form because its practice copy failed to load or the model closed it by accident. Additionally, during another evaluation, Claude Haiku 4.5 was asked to stop before the final submission but mistakenly submitted several times, expecting another confirmation page.

In two cases, Claude reached public data available only for a fee. In an evaluation, Claude Mythos 5 pulled working access tokens from the settings file a local government’s property map sends to browsers and queried the map’s server directly. In internal use by a company researcher, Mythos 5 learned that a state agency’s public dashboard gives any visitor a token, then used one to query the database without paying.

Several models, including Claude Opus 5 and Mythos 5, also used free URL shorteners to get around length limits the company puts on some of its fetch tools to block unwanted actions such as injection attacks.

### The Philadelphia Police Tip

Claude Haiku 4.5 shared a false tip with the Philadelphia police while working on example tasks on randomly chosen webpages. On a page about an unsolved homicide, it mentioned that the sender remembered seeing someone matching the description near a street listed on the page, although the page described no suspect. The optional name and contact fields were left blank.

Its instructions barred steps like logging in or sharing personal info but didn’t prohibit form submissions. Anthropic mentioned that, based on the transcript, Claude seemed to be creating example content rather than attempting to deceive anyone. The company also notes that its perspective might evolve as they conduct further analysis.

The department says the July 18 submission was flagged as spam and never forwarded to its Real-Time Crime Center. It found no indication of unauthorized access to police systems or compromised department data.

The department also says its safeguards limited the impact but don’t diminish “the seriousness of an AI system presenting fabricated information as though it came from a person with knowledge of a homicide.” According to the department, Anthropic discovered the submission Sept. 28. The department added:

“The two-month delay in detecting and reporting the incident to the City is unacceptable.”

### What Anthropic Is Changing

Anthropic’s wider cutoff of live internet access lasts until the company confirms its security and monitoring measures reliably catch behaviors like these. It previously covered only some high-risk and cybersecurity evaluations.

Anthropic has dropped some public evaluations, taken others offline, and restricted what Claude can do with internet tools like its web fetch feature. They’ve put measures in place that detect and prevent these behaviors. The measures are active during most evaluations and internal agent use of their frontier models. When they tested them against the reported cases, these measures blocked every one. Additionally, the company is working on fixing or removing training environments that encourage Claude to get around restrictions.

The report doesn’t announce any changes to web access in Claude’s customer products. The company says that, to their knowledge, no customer data or Anthropic’s internal systems were involved in any of the cases.

### Why This Matters

The cases Anthropic describes involve ordinary public pages, such as a tip form that didn’t require a name, a map with a settings file containing working tokens, and a dashboard that provides any visitor with a token.

Anthropic notes that many cases in its report began with unclear or impossible tasks. They also mention that public web search benchmarks, which developers typically use to compare models, are run on the live internet by default.

The report covers Anthropic’s own models and doesn’t measure how often agents act this way elsewhere.

### Looking Ahead

Anthropic plans to disclose new cases as it scans more transcripts, including its own use of Claude. Philadelphia police say they’ll review Anthropic’s report and that the city’s administration will explore regulatory protections with state and federal partners.

Featured Image: Samuel Boivin/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/anthropic-cuts-live-web-access-internal-tests/592534/)
