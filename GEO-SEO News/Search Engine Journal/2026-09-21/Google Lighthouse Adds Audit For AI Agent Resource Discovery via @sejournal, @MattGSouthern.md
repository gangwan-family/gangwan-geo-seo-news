---
title: "Google Lighthouse Adds Audit For AI Agent Resource Discovery via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-21T14:32:33+00:00
fetched_at: 2026-09-22T00:11:50.118725+00:00
url: "https://www.searchenginejournal.com/google-lighthouse-ai-agent-resource-discovery-audit/590274/"
guid: "https://www.searchenginejournal.com/google-lighthouse-ai-agent-resource-discovery-audit/590274/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Tools"
---

# Google Lighthouse Adds Audit For AI Agent Resource Discovery via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-21
- URL: https://www.searchenginejournal.com/google-lighthouse-ai-agent-resource-discovery-audit/590274/
- Author: Matt G. Southern
- Categories: News, Tools

## RSS 摘要

Lighthouse 13.5 adds an audit for AI agent resource discovery, but its checks differ from the latest ARD proposal. The post Google Lighthouse Adds Audit For AI Agent Resource Discovery appeared first on Search Engine Journal .

## 原文正文

Google Lighthouse Adds Audit For AI Agent Resource Discovery Skip to content

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- Tools

## Google Lighthouse Adds Audit For AI Agent Resource Discovery

- Lighthouse 13.5 adds an audit for Agentic Resource Discovery, a proposed agent spec.

- It validates an ARD catalog, falling back to /.well-known/ai-catalog.json when no pointer exists.

- The audit is headed to Chrome DevTools and PageSpeed Insights.

Lighthouse 13.5 adds an audit for Agentic Resource Discovery, a proposed spec for how AI agents find tools. It's due in Chrome DevTools and PageSpeed Insights.

Google’s Lighthouse 13.5 introduces an audit for Agentic Resource Discovery (ARD), which is a proposed spec for how AI agents locate the tools and services offered by an organization. The audit compares a site’s ARD catalog with the schema defined by the ARD project. If the site does not provide a catalog pointer, Lighthouse defaults to /.well-known/ai-catalog.json . The most recent spec, dated Aug. 26, moved this file to ard.json , with the old filename remaining optional for software that reads it.

The Lighthouse team expects this update to roll out in Chrome 156 DevTools, and in PageSpeed Insights within two weeks.

This audit is part of Lighthouse’s experimental Agentic Browsing category, separate from SEO audits, and it is not tied to Google Search anywhere in the release notes . The reports will show an ARD result or Not Applicable if no catalog is found.

### What The Audit Checks

In the 13.5 source code , Lighthouse checks the robots.txt file for an Agentmap line, which is a directive from the ARD specification pointing to a catalog. It then looks for a link tag with the ai-catalog relation and also checks the HTTP Link header for the same relation. If none of the three is available, it requests /.well-known/ai-catalog.json .

If there is no pointer and the well-known path does not serve the file, the audit is marked as Not Applicable . Schema errors cause failure, as does a pointer to an unloadable catalog. The pull request describes ard-schema as a “schema conformance audit.”

The same release groups the new audit with the existing llms.txt audit under a heading called Agent Discoverability. Google’s docs say the Agentic Browsing category doesn’t produce a 0-100 score and shows a pass ratio instead, because “the standards for the agentic web are still emerging.”

### The Spec Has Since Renamed The File

ARD v0.91 now specifies /.well-known/ard.json as the manifest location and mentions ai-catalog.json as the earlier path. When I covered ARD’s launch in June , the spec was a v0.9 draft, with ai-catalog.json as the file for organizations to publish.

In v0.91, software reading these files is required to fetch ard.json and can also check the older path. The spec cautions that a file only available at the old path “may not be found.”

I didn’t find any references to ard.json or the ard link relation in the 13.5 source or in the main branch of the project as of Sept. 21. The spec also mentions discovery through in-page JSON-LD and DNS records, but the 13.5 code doesn’t check either. Lighthouse built its validator based on the ARD project’s own conformance tests .

The specification is still a proposal and credits three authors: Junjie Bu from Google, R.V. Guha from Microsoft , and Shaun Smith from Hugging Face.

### How ARD Differs From llms.txt And WebMCP

ARD is all about discovering resources. It includes MCP tools, A2A agents, skills, and other callable services, so AI systems can find them through search.

An llms.txt file summarizes your site’s content for agents. WebMCP, which I shared about in August , allows a page to offer structured actions that an agent can call once it’s on your site.

### Why This Matters

Based on Lighthouse 13.5 source code, if a website uses /.well-known/ard.json with rel="ard" , doesn’t have an Agentmap line, and doesn’t use the older ai-catalog names, it would be classified as Not Applicable.

This simply means Lighthouse didn’t find a catalog in its current search areas. But it doesn’t necessarily mean the site is missing a current ARD manifest.

As I shared in May , when Lighthouse introduced its llms.txt audit, remember that Google Search’s guidance and Lighthouse’s agent checks are looking at different things.

### Looking Ahead

Lighthouse expects 13.5 to reach PageSpeed Insights within two weeks of the release.

The release also adds a weekly automated check that flags when the ARD project’s schema or conformance test changes upstream. The places Lighthouse looks for a catalog are set separately, in the code that fetches it.

Featured Image: Golden Dayz/Shutterstock

Category News Tools

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-lighthouse-ai-agent-resource-discovery-audit/590274/)
