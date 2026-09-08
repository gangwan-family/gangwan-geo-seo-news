---
title: "Some Sites Use llms.txt Like robots.txt, Common Crawl Finds via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-08T14:09:20+00:00
fetched_at: 2026-09-08T23:29:12.190870+00:00
url: "https://www.searchenginejournal.com/common-crawl-llms-txt-robots-txt/588786/"
guid: "https://www.searchenginejournal.com/common-crawl-llms-txt-robots-txt/588786/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Some Sites Use llms.txt Like robots.txt, Common Crawl Finds via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-08
- URL: https://www.searchenginejournal.com/common-crawl-llms-txt-robots-txt/588786/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

Common Crawl analyzed 584,107 llms.txt files and found most came from templates, many had no links, and some carried crawler rules the format can't enforce. The post Some Sites Use llms.txt Like robots.txt, Common Crawl Finds appeared first on Search Engine Journal .

## 原文正文

Some Sites Use llms.txt Like robots.txt, Common Crawl Finds Skip to content

Webinar: AI Cites Your Brand. Now What? Turn AI Visibility Data Into Actions

Register Now

- SEJ

- ⋅

- AI Search

## Some Sites Use llms.txt Like robots.txt, Common Crawl Finds

- Most llms.txt files came from templates, and many contain no links.

- Some sites write crawler restrictions into llms.txt.

- A block written only in llms.txt does nothing.

Common Crawl analyzed 584,107 llms.txt files and found most came from templates, many had no links, and some carried crawler rules the format can't enforce.

Common Crawl looked at over 500,000 llms.txt files and discovered that 68% originated from a plugin or template, while 22% had no links at all.

The analysis , shared by senior research engineer Malte Ostendorff, showed that 6% of the files included guidelines on AI site usage, such as rate limits and copyright notices, which the llms.txt standard doesn’t cover. Additionally, some files named specific crawlers and whether they were allowed access, something llms.txt can’t regulate. Of the 32 files that appeared to deny Common Crawl’s own crawler, the team could assess 31 sites, and none blocked it outright in robots.txt.

In June, I covered Ahrefs data showing that 97% of llms.txt files in its dataset received no requests. That analysis focused on whether anyone accessed the files. The Common Crawl article examines the contents of those files.

### Most Files Come From Templates

Wix makes up 41% of the files looked at. Some generators include a line naming the tool, and the analysis grouped unsigned files by shared boilerplate.

Just under half (49%) have the full structure the analysis tested for: an H1 title, a summary blockquote, and sections of link bullets. 32% add a short note describing each link, and 22.56% have no links. The spec requires only the H1 and treats the link notes as optional.

Across 73,000 files, All in One SEO never writes a summary but has a median of 138 links. The article says it treats llms.txt as a sitemap. GoDaddy’s parked-domain files successfully pass all structural checks even without links, serving as a sales pitch.

### Some Sites Are Using llms.txt Like robots.txt

The llms.txt format is a proposal for giving AI systems a curated list of a site’s pages. The report explains that the file “grants nothing and blocks nothing, and no crawler is obliged to read it.” Crawlers refer to robots.txt to learn the access rules.

Some websites may be mixing up llms.txt with robots.txt. Beyond the llms.txt files analyzed, Common Crawl found 136,578 robots.txt files at the llms.txt path, which is about 10% of the 1,287,207 responses that returned HTTP 200.

Out of the analyzed files, 1,570 cited a specific crawler, while 32 appeared to deny CCBot. Robots.txt files were retrieved for all 32 sites, and none of the 31 sites it could assess blocked CCBot outright. Five sites explicitly allowed it, 11 limited access to certain paths but permitted others, and 15 had no restrictions. One site returned an HTTP 429 error and could not be tested.

The article points out a site where the llms.txt file states that CCBot is blocked “as of June 2026,” but interestingly, its robots.txt actually permits the crawler under a wildcard rule. The post describes llms.txt as a policy description rather than a policy itself, and says it has drifted out of sync with the robots.txt it describes.

Common Crawl operates CCBot , and it says robots.txt is the file it honors.

### Prompt Injection Exists, But It Was Rare

Ten files matched Common Crawl’s strictest test for instructions aimed at the model itself. The team found four genuine cases, including one file whose summary tells the model to ignore prior instructions and fetch a second file. The other six were false positives, mostly documentation that quoted control tokens in order to explain them.

The authors clarify that the finding isn’t that llms.txt is filled with prompt injections. In all the actual cases identified, individuals intentionally inserted it to make a point. Additionally, 3,793 files showed milder guidance, like saying “focus on these pages.”

### What The Analysis Can And Can’t Show

The sample came from sites CCBot had recently fetched without problems. The crawl requested /llms.txt from a large, random group of those sites, sampled /llms-full.txt more specifically, and included sites already known to serve either file from two previous crawls.

This means the sample is random only within sites accessible to the crawler, not the entire web. The post mentions that its 11% adoption rate for /llms.txt isn’t directly comparable to figures from Ahrefs or the Web Almanac because the populations differ.

This analysis is based on a single crawl, so it can’t determine whether templated files, policy language, or prompt injections are increasing. It also can’t confirm if any AI system reads these files. The counts for policies and injections are based on keyword matches, which the post admits are likely undercounts.

### Why This Matters

A crawler restriction written into llms.txt doesn’t do anything by itself. Common Crawl mentions that CCBot respects robots.txt, so for that crawler, the rule needs to be included there. Also, any llms.txt line about it should match those rules.

### Looking Ahead

The llms.txt v2 update I reported on in August introduced link relations to make it easier to find Markdown versions of pages. However, it didn’t alter what the file can enforce. Since plugins and site builders now create about two-thirds of the files Common Crawl finds, how the format is used in practice depends more on what those tools produce than on manual writing.

Featured Image: Cast Of Thousands/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/common-crawl-llms-txt-robots-txt/588786/)
