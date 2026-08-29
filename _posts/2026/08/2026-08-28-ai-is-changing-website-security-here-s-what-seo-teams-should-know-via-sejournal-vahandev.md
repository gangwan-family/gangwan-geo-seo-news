---
layout: post
title: "AI Is Changing Website Security. Here’s What SEO Teams Should Know via @sejournal, @vahandev"
date: 2026-08-28T11:56:38+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-28/AI Is Changing Website Security. Here’s What SEO Teams Should Know via @sejournal, @vahandev.md"
original_url: "https://www.searchenginejournal.com/ai-changing-website-security-seo-teams-should-know/587352/"
author: "Vahan Petrosyan"
categories:
  - "AI Search"
  - "News"
  - "Security"
  - "_src_search-engine-journal"
---

# AI Is Changing Website Security. Here’s What SEO Teams Should Know via @sejournal, @vahandev

- Source: Search Engine Journal
- Published: 2026-08-28
- URL: https://www.searchenginejournal.com/ai-changing-website-security-seo-teams-should-know/587352/
- Author: Vahan Petrosyan
- Categories: AI Search, News, Security

## RSS 摘要

More than 100 organizations, including OpenAI, Google, and Microsoft, urge governments and website owners to prepare now for escalating AI cyberattacks. The post AI Is Changing Website Security. Here’s What SEO Teams Should Know appeared first on Search Engine Journal .

## 原文正文

AI Is Changing Website Security. Here’s What SEO Teams Should Know Skip to content

- SEJ

- ⋅

- Security

## AI Is Changing Website Security. Here’s What SEO Teams Should Know

OpenAI, Google, Microsoft, and 100+ organizations warn AI-enabled cyberattacks are accelerating. What should SEOs know about the risks to search visibility?

More than 100 technology, cybersecurity, financial, and infrastructure organizations have signed an open letter warning that AI-enabled cyberattacks will become “far more widespread and sophisticated” in the coming months.

OpenAI, Anthropic, AWS, Google, Microsoft, Oracle, Cloudflare, CrowdStrike, Hugging Face, and other companies that build or defend much of the modern web are among the signatories.

Their message is direct: put capable defensive AI in the hands of organizations that need it now. The letter calls for a global effort, starting with hospitals, water utilities, local governments, and other critical infrastructure.

### What the Signatories Want to Happen

The letter says the “status quo security won’t be enough.” AI can help attackers move faster through weaknesses that already exist: unpatched software, weak authentication, excessive permissions, misconfigurations, and technical debt.

The letter divides the work among four groups:

- Organizations: fix their highest-risk weaknesses and limit access to only what each user or system needs.

- Cybersecurity and technology companies: test their defenses against frontier AI capabilities, share threat intelligence, and make defensive AI easier to deploy.

- Governments: fund protection for essential services, coordinate incident response, and give under-resourced defenders access to capable AI and authorized testing.

- Frontier AI companies: provide responsible model access, funding, training, monitoring, and support for authorized testing and private disclosure.

### Why This Matters to SEO and Website Teams

Critical infrastructure is the first focus, but the same problem exists on ordinary websites. Outdated plugins and libraries, leaked credentials, broad service-account permissions, and weak authentication are common across website stacks. Some systems remain unpatched because nobody wants to risk breaking them.

Search visibility depends on website security. A hacked site can create spam pages, malicious redirects, malware warnings, crawling failures, outages, or data loss. Website security is part of protecting organic traffic. It is not a separate IT concern.

AI gives attackers a speed advantage. They can use it to find and exploit a vulnerability quickly. The vendor still has to understand the problem, build a patch, test it, and get site owners to install it. That delay creates an opening.

Defenders can use AI to audit code and find problems earlier. But if nobody is monitoring the site or able to isolate it quickly, the attacker still has the advantage.

OpenAI’s Hugging Face incident shows how much can happen in a short time. During internal evaluations, agents created an unauthorized communication channel, broke out of their sandboxes, and chose an outside target. They executed code on 41 Hugging Face production workers and moved from one compromised worker to administrative and host-level access across multiple clusters in under 13 hours. OpenAI says its customer data and products were not affected.

These were private evaluation agents, not a public model available to users. So you may ask how this affects you if you run a website.

The point is not that OpenAI’s evaluation agents will attack your site. The unsettling part is how an ordinary task can lead an agent to exploit a real weakness. The Hacker News reported that an OpenClaw agent powered by Claude Opus 4.6 bypassed a gym’s booking limit and canceled another user’s reservation without being asked.

The risk becomes even harder to control with uncensored open-source models that can run locally. Once released, no company can fully control how they are used. As stronger models emerge, distillation can transfer more of their capabilities into open-source versions.

That changes the scale of the threat for every website we manage. I can see why this letter matters because I explored the risk myself.

### What I Saw With Qwen3.8-27B “Uncensored”

I installed Qwen3.8-27B “Uncensored” , a third-party version of Qwen3.8-27B with much of its refusal behavior removed.

I asked it to plan and execute an attack against a website. It immediately built a reconnaissance plan and started producing command-line steps. I stopped the test before it went further.

I shared the stopped test in the SEJ Pro community. The third-party domain has been redacted.

A capable model running on my PC turned a plain-language request into a detailed attack plan. You no longer need years of security experience to get that far.

### What I Recommend

Based on what I saw, this is what I recommend:

- Ask your tech team to audit your codebase using official Claude Code or Codex security plugins.

- Keep all website packages, libraries, and plugins up to date.

- Set up monitoring and granular alerts for unusual activity.

The point is not to panic. It is to prepare. Find the weaknesses before someone else does, fix them, and set up monitoring so you know when something changes. That is what will keep your website secure as these models become more capable.

Featured Image: Screenshot from OpenAI, composition by Search Engine Journal.

Category News AI Search Security

Read Full Bio

SEJ STAFF Vahan Petrosyan Director of Technology at Search Engine Journal

As Director of Technology at Search Engine Journal, I lead the organization’s technology strategy and technical operations. I oversee technical ...

## 原文链接

[Read original](https://www.searchenginejournal.com/ai-changing-website-security-seo-teams-should-know/587352/)
