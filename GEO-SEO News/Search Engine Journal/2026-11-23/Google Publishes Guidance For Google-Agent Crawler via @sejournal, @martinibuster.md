---
title: "Google Publishes Guidance For Google-Agent Crawler via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-11-23T13:12:32+00:00
fetched_at: 2026-11-24T05:23:13.943601+00:00
url: "https://www.searchenginejournal.com/google-publishes-guidance-for-google-agent-crawler/598526/"
guid: "https://www.searchenginejournal.com/google-publishes-guidance-for-google-agent-crawler/598526/"
author: "Roger Montti"
categories:
  - "News"
  - "SEO"
---

# Google Publishes Guidance For Google-Agent Crawler via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-11-23
- URL: https://www.searchenginejournal.com/google-publishes-guidance-for-google-agent-crawler/598526/
- Author: Roger Montti
- Categories: News, SEO

## RSS 摘要

Google explains how website owners and SEOs can identify legitimate Google-Agent requests and prevent security systems from blocking them. The post Google Publishes Guidance For Google-Agent Crawler appeared first on Search Engine Journal .

## 原文正文

Google Publishes Guidance For Google-Agent Crawler Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

- SEJ

- ⋅

- SEO

## Google Publishes Guidance For Google-Agent Crawler

Google published new guidance for recognizing Google-Agent and allowing its agents to interact with websites securely.

Google published new guidance on how to keep from blocking its user-triggered AI agents that identify themselves as Google-Agent. The new documentation shows how to verify legitimate Google-Agent requests and configure firewalls to allow them on websites.

### Google-Agent

Google-Agent is the name used by AI agents hosted on Google’s infrastructure that navigate websites and perform actions on behalf of users. Google’s guidance and also Google’s User-Triggered Fetcher documentation do not identify which Google products or services use Google-Agent. Neither documentation mentions Google Search, AI Mode, Gemini, or any other Google product.

It describes Google-Agent as agents that are hosted on Google’s infrastructure, interact with and navigate websites, and complete tasks on behalf of a user.

The document says or implies that the Google-Agent does the following:

- Navigate websites.

- Search within websites.

- Filter search results.

- Click through to detail pages.

- Add products to shopping carts.

- Make bookings.

- Trigger requests to website APIs, including XHR, GraphQL, and api.* endpoints.

### How To Identify Google-Agent

The new guidance explains there are three ways that website owners can verify that a request comes from Google-Agent.

1. The request’s User-Agent header contains “Google-Agent.”

2. The request originates from an IP address listed in Google’s published file of user-triggered agent ranges.

3. Only where it’s present, when the request carries a cryptographic signature under Google’s experimental Web Bot Auth protocol, which can be checked against Google’s published public keys.

The first two checks are the baseline, and the signature check adds stronger verification when it’s available. A Google-Agent bot can then be allowed through whatever bot defenses are in use once it passes those checks. Google also notes that some CDNs and bot-detection services handle this verification automatically.

### Troubleshooting

Lastly, Google offers guidance on troubleshooting when the Google-Agent is unintentionally blocked.

Google recommends checking:

#### 1. Rule priority configuration

Google recommends ensuring that rules allowing Google-Agent requests have higher priority and are evaluated before broader blocking rules, including:

- Rules blocking traffic from cloud providers or data centers.

- Managed bot protection rules.

- Rules that block categories of AI agents.

#### 2. Scope of coverage

If bot detection, firewall (WAF), or CDN rules only covers the initial page request, the agent will be able to land on the website but it will be unable to finish whatever task it’s there to accomplish.

Google recommends checking that CAPTCHA challenges are disabled for verified Google-Agent requests, reviewing rate limits, IP address updates, and proxy configurations.

Google’s documentation states:

“Proxy headers: Confirm that load balancers and intermediate proxies preserve the original client IP, the User-Agent header, and (for signed requests) the Signature, Signature-Input, and Signature-Agent headers.”

#### 3. Traffic and network handling

Google’s new guidance addresses three issues to check if Google-Agent is being inadvertently blocked:

- Rate limiting

- IP address updates

- Proxy headers

Google’s guidance explains:

“Shared-IP rate limits: Confirm that per-IP rate-limiting rules account for or exempt verified Google-Agent IP ranges, as concurrent requests from multiple users share the same egress pool.

IP range updates: Confirm that IP-based rules stay synced with the latest ranges in user-triggered-agents.json.

Proxy headers: Confirm that load balancers and intermediate proxies preserve the original client IP, the User-Agent header, and (for signed requests) the Signature, Signature-Input, and Signature-Agent headers.”

### Takeaways

Google’s new Google-Agent guidance offers tips for website owners who want to allow Google-Agent interactions, stressing that they need to make sure that legitimate Google-Agent requests can pass through security defenses without compromising protections against unwanted bots.

#### Read more:

Complete Crawler List For AI User-Agents

Featured Image by Shutterstock/Ao Zaa Studio

Category News SEO

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-publishes-guidance-for-google-agent-crawler/598526/)
