---
layout: post
title: "Indexed Claude Chats Show Why Disallow Is Not Noindex via @sejournal, @MattGSouthern"
date: 2026-07-28T02:12:20+00:00
source: "Search Engine Journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-07-28/Indexed Claude Chats Show Why Disallow Is Not Noindex via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/"
author: "Matt G. Southern"
categories:
  - "Generative AI"
  - "News"
  - "Technical SEO"
---

# Indexed Claude Chats Show Why Disallow Is Not Noindex via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-07-28
- URL: https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/
- Author: Matt G. Southern
- Categories: Generative AI, News, Technical SEO

## RSS 摘要

Shared Claude chats showed up in Google. We checked the pages and found a noindex header sitting behind a robots.txt block that keeps Google out. The post Indexed Claude Chats Show Why Disallow Is Not Noindex appeared first on Search Engine Journal .

## 原文正文

Indexed Claude Chats Show Why Disallow Is Not Noindex Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- Technical SEO

## Indexed Claude Chats Show Why Disallow Is Not Noindex

- Shared Claude chats showed up in Google.

- The pages tell Google not to list them, but the directive is blocked.

- Unsharing any shared chats fixes the issue.

Shared Claude chats showed up in Google. We checked the pages and found a noindex header sitting behind a robots.txt block that keeps Google out.

Over the weekend, shared Claude chats unexpectedly showed up in Google search results.

On July 27, I checked out the crawl rules on the Claude share pages and found a noindex directive that was hidden behind a block, preventing Google from accessing it

The share path is blocked by robots.txt on claude.ai. These pages also send back an X-Robots-Tag header set to none, which Google’s robots meta tag guidelines treat as the same as noindex and nofollow.

Because of this, the rules conflict with each other. According to Google’s guidance , a noindex tag only works if the crawler is allowed to access and read the page. If a page is blocked by robots.txt, it can still be indexed if other pages link to it, since Googlebot notes the URL without actually opening it.

The pairing is not unique to AI companies. If Google discovers a blocked URL elsewhere, it can list the URL without crawling the noindex.

### What Happened

404 Media reported on Monday that Claude share pages were showing up through the site: operator. TechCrunch reported being able to find medical material, internal company documents, and files carrying the names and phone numbers of primary school-aged children. Artifacts, the documents and mini apps built inside Claude, showed up through a second path.

Much of the coverage, including The Decoder , reported that the share pages lacked a noindex tag. As of July 27, a noindex header is being served and sits behind a robots.txt block. It’s unclear whether that header was in place before the weekend, as I couldn’t confirm this.

### What The Crawl Rules Return

Findings from my July 27 checks against claude.ai:

- The robots.txt file at claude.ai disallows /share/* under the User-agent: * group, with no separate Googlebot group, so that is the group Google goes by.

- A live share URL responds with the header x-robots-tag: none on a GET request.

- The same header appears when the request claims to be Googlebot, and the response includes Vary: User-Agent.

- The /public/artifacts/ path is not listed in robots.txt.

I didn’t verify whether artifact URLs return a page-level noindex, so these two paths can’t be compared based on their controls.

Independent IT consultant Daniel J. Glover reported the same conflict on July 26. My check shows the setup still in place on July 27, after it was reported that the chats were no longer displayed in search results, but I couldn’t establish what was served to Google when those URLs were first discovered.

### Why Blocking A Page Doesn’t Remove It

Robots.txt helps guide how search engines crawl your website, but it doesn’t decide what gets indexed. Google has been clarifying this for years.

For example, John Mueller explains that even pages blocked by robots.txt can appear in search results if other pages link to them. If you want to keep a page out of search results, using the “noindex” tag is the right choice. Martin Splitt also recommends avoiding placing both rules on the same page. Google recently emphasized this distinction again, as seen in their update last week.

Blocking URLs with robots.txt doesn’t remove already indexed pages. For a more permanent removal, Google’s guidance is to use a “noindex” tag that its crawler can read.

### Anthropic’s Response

Anthropic told TechCrunch that share links will appear in search results only if people post them in accessible locations for crawlers, and that links sent through private messages won’t be indexed.

Spokeswoman Amie Rotherham added that these links “are not guessable or discoverable unless people choose to share them themselves.” This addresses one way a public share URL can be discovered, but it doesn’t address the conflicting rules I found on July 27.

Google spokesperson Ned Adriance stated that search engines do not determine which pages are made public, and that Google provides site owners with control over crawling and indexing and follows those controls.

### Why This Matters

Any chats or artifacts you haven’t unshared are still accessible to anyone with the link. In Claude, go to Settings > Privacy > Shared Chats to see a complete list.

Unsharing a chat disables the direct link, but removing the URL from Google is a different thing. As a Claude user, you can’t control what it serves to Googlebot or submit a removal request, as these are managed by Anthropic.

Artifacts are published through their own process, which makes unsharing a chat and unpublishing an artifact from that chat two separate actions.

Beyond settings changes, consider establishing a rule around sharing AI chats and artifacts. If a chat contains something you wouldn’t post publicly, don’t share it through a link that might get indexed later.

### Looking Ahead

The pattern isn’t unique to Anthropic. OpenAI pulled shared ChatGPT chats from search in August 2025, and Google blocked Bard transcripts from indexing in 2023. Each case involved a public share URL that traveled further than its owner may have expected.

Three companies have now had customer chats turn up in search. That’s reason enough to treat a public share link as a public webpage from the moment it exists.

Featured Image: Cast of Thousands/Shutterstock

Category News Generative AI Technical SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/)
