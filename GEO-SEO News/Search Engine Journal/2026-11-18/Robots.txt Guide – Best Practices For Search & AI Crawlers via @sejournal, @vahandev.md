---
title: "Robots.txt Guide – Best Practices For Search & AI Crawlers via @sejournal, @vahandev"
source: "Search Engine Journal"
published: 2026-11-18T20:00:31+00:00
fetched_at: 2026-11-19T02:41:06.811446+00:00
url: "https://www.searchenginejournal.com/technical-seo/robots-txt-guide-best-practices-for-search-ai-crawlers/"
guid: "https://www.searchenginejournal.com/technical-seo/robots-txt-guide-best-practices-for-search-ai-crawlers/"
author: "Vahan Petrosyan"
categories:
  - "SEO"
---

# Robots.txt Guide – Best Practices For Search & AI Crawlers via @sejournal, @vahandev

- Source: Search Engine Journal
- Published: 2026-11-18
- URL: https://www.searchenginejournal.com/technical-seo/robots-txt-guide-best-practices-for-search-ai-crawlers/
- Author: Vahan Petrosyan
- Categories: SEO

## RSS 摘要

Learn how to configure robots.txt, avoid crawl and indexing mistakes, and manage AI training, search crawlers, and user-requested visits separately. The post Robots.txt Guide – Best Practices For Search & AI Crawlers appeared first on Search Engine Journal .

## 原文正文

Robots.txt Guide – Best Practices For Search & AI Crawlers Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

## Robots.txt Guide – Best Practices For Search & AI Crawlers

Learn how to use your robots.txt to fix crawl and indexing mistakes, and manage AI training bots, search crawlers, and user-requested website visits.

The robots.txt file has always been an essential tool for managing crawler access to a website. With AI search tools and agents now visiting websites alongside traditional crawlers, you need to know which rules each one follows.

But, blocking the wrong bot can exclude your content from LLMs or SERPs, while leaving unnecessary URLs open can waste crawl budget on large sites. So, you need to know what you are doing.

This guide will help you understand how robots.txt rules work so you can avoid common robots.txt mistakes , keep useful content accessible, but at the same time limit unnecessary crawling.

### What Is Robots.txt?

The robots.txt is a simple text file that sits in the root directory of your site and tells crawlers what should be crawled.

The table below provides a quick reference to the key robots.txt directives .

Directive

Description

User-agent

Specifies which crawler the rules apply to. See user agent tokens . Using * supplies the fallback rules for crawlers without a matching specific group.

Disallow

Asks compliant crawlers not to crawl specified URL paths.

Allow

Allows specific URLs to be crawled, even if a parent directory is disallowed.

Sitemap

Indicates the location of your XML Sitemap by helping search engines to discover it.

This 2024 screenshot shows an example of robots.txt from ikea.com with multiple rules.

Example of robots.txt from ikea.com

Note that robots.txt doesn’t support full regular expressions and only has two wildcards:

- Asterisk (*), which matches zero or more characters.

- Dollar sign ($), which matches the end of a URL.

Also, note that URL path matching is case-sensitive, e.g., “filter=” is not equal to “Filter=.” The directive names and user-agent matching are case-insensitive.

### Order of Precedence in Robots.txt

When setting up a robots.txt file, it’s important to know the order in which search engines decide which rules to apply in case of conflicting rules.

When you write a separate set of rules for a bot, it follows those rules instead of the rules under User-agent: * . For example:

User-agent: * Disallow: /private/ User-agent: Googlebot Allow: /

Here, Googlebot can crawl /private/ because its own rules allow every URL to be crawled. To block that directory for Googlebot, add Disallow: /private/ beneath its Allow: / line.

Within the applicable group, Google follows these two key rules:

#### 1. Most Specific Rule

The rule that matches more characters in the URL will be applied. For example:

User-agent: * Disallow: /downloads/ Allow: /downloads/free/

In this case, the “Allow: /downloads/free/” rule is more specific than “Disallow: /downloads/” because it targets a subdirectory.

Google will allow crawling of subfolder “/downloads/free/” but block everything else under “/downloads/.”

#### 2. Least Restrictive Rule

When multiple rules are equally specific, for example:

User-agent: * Disallow: /downloads/ Allow: /downloads/

Google will choose the least restrictive one. This means Google will allow access to /downloads/.

### Why Is Robots.txt Important in SEO?

Blocking pages that don’t need SERP visibility (e.g. privacy policy) with robots.txt reduces wasted crawling and can help Googlebot focus its crawl budget on useful URLs (e.g. core product/service pages). Google cautions that this does not automatically transfer crawl budget to other pages unless the site is already reaching its crawl capacity limit . It also helps search engines save computing power, contributing to better sustainability .

Google’s 2024 reminder about action URLs focused on add-to-cart and wishlist links that waste crawler and server resources.

Imagine you have an online store with hundreds of thousands of pages. There are sections of websites like filtered pages that may have an infinite number of versions. Those pages don’t have unique value, essentially contain duplicate content, and may create infinite crawl space, thus wasting your server and Googlebot’s resources. That is where robots.txt comes in, preventing search engine bots from crawling those pages.

If you don’t do that, Google may try to crawl an infinite number of URLs with different (even non-existent) search parameter values, causing spikes and a waste of crawl budget .

### When to Use Robots.txt

As a general rule, you should always ask why certain pages exist, and whether they have any value for search engines to crawl and index.

Depending on your site and indexing goals, candidates for crawl restrictions include:

URLs that contain query parameters such as:

- Internal search.

- Faceted navigation URLs created by filtering or sorting options if they are not part of URL structure and SEO strategy.

- Action URLs like add to wishlist or add to cart.

- Account areas that do not need search visibility. Protect private information with authentication, regardless of robots.txt rules.

- JavaScript files not relevant to website content or rendering, such as tracking scripts.

- AI training crawlers or other bots whose documented use you want to restrict, while considering search and user-requested access separately.

Let’s dive into examples of how you can use robots.txt for each case.

#### 1. Block Internal Search Pages

Internal search results are a common source of unnecessary crawling by Google and other search engines . If those results are not intended to appear in search, consider restricting their crawl space.

On WordPress websites, it is usually an “s” parameter, and the URL looks like this:

https://www.example.com/?s=google

Gary Illyes from Google has repeatedly warned to block “action” URLs as they can cause Googlebot to crawl them indefinitely even non-existent URLs with different combinations.

Here is the rule you can use in your robots.txt to block such URLs from being crawled:

User-agent: * Disallow: /*?s= Disallow: /*?*&s=

- User-agent: * supplies fallback rules for crawlers without a matching specific group.

- Disallow: /*?s= matches s as the first query parameter. Disallow: /*?*&s= matches it after another parameter. Both paths begin with / and avoid matching a different parameter name that merely ends in s .

- The parameter name remains case-sensitive, so these rules do not match /?S= . Test the parameter order and spelling your site actually uses.

This crawl-stats screenshot, included in the original 2024 guide, illustrates reduced crawling of non-existent internal search URLs after they were blocked via robots.txt.

Screenshot from crawl stats report

Note that Google may index blocked pages based on links to their URLs. Robots.txt does not guarantee their removal from search. If removal is your goal, use noindex and allow Google to crawl the page so it can read that instruction.

#### 2. Block Faceted Navigation URLs

Faceted navigation is an integral part of every ecommerce website. There can be cases where faceted navigation is part of an SEO strategy and aimed at ranking for general product searches.

Zalando’s color-based landing pages, such as those targeting “gray t-shirt” illustrate this approach. The principle is to keep useful search landing pages crawlable while restricting unwanted filter combinations.

However, in most cases, this is not the case, and filter parameters are used merely for filtering products, creating dozens of pages with duplicate content.

There may be multiple filter parameters in one URL. Identify which ones generate unwanted crawl space; do not block facets that form part of your search strategy. Google’s faceted-navigation guidance distinguishes these two cases.

For example, if you have filters with the following parameters “sortby,” “color,” and “price,” you may use this set of rules:

User-agent: * Disallow: /*?sortby= Disallow: /*?*&sortby= Disallow: /*?color= Disallow: /*?*&color= Disallow: /*?price= Disallow: /*?*&price=

These pairs match each parameter in the first position or after another parameter. Add only the parameters you intend to restrict, and test both wanted and unwanted URLs.

##### What About UTM Parameters?

UTM parameters are used for tracking purposes.

In the Reddit exchange shown below, John Mueller addressed tracking parameters on external links. Keep that context separate from internally generated filter or search URLs.

John Mueller on UTM parameters. Screenshot by Author, November 2026.

Keep internal links pointed at the URLs you want crawled. Decide whether to block a parameter by what it does on your site; the presence of a query string alone is not a reason to disallow a page.

#### 3. Block PDF URLs

Let’s say you have a lot of PDF documents, such as product guides, brochures, or downloadable papers, and you don’t want them crawled.

Here is a simple robots.txt rule that will block search engine bots from accessing those documents:

User-agent: * Disallow: /*.pdf$

The “Disallow: /*.pdf$” line tells crawlers not to crawl any URLs that end with .pdf.

By using /*, the rule matches any path on the website. As a result, any URL ending with .pdf will be blocked from crawling. It will not match /guide.pdf?download=1 or an uppercase .PDF extension; test any such variants separately. If you want a PDF excluded from search, use an X-Robots-Tag: noindex HTTP header and keep it crawlable so Google can read the header.

If you have a WordPress website and want to disallow PDFs from the uploads directory where you upload them via the CMS, you can use the following rule:

User-agent: * Disallow: /wp-content/uploads/*.pdf$ Allow: /wp-content/uploads/2024/09/allowed-document.pdf$

You can see that we have conflicting rules here.

In case of conflicting rules, the more specific one takes priority, which means the last line ensures that only the specific file located in folder “wp-content/uploads/2024/09/allowed-document.pdf” is allowed to be crawled.

#### 4. Block a Directory

Let’s say you have an API endpoint where you submit your data from the form. It is likely your form has an action attribute like action=”/form/submissions/.”

If a crawler discovers the URL /form/submissions/, you may want to prevent crawling of that path. You can request that with this rule:

User-agent: * Disallow: /form/

By specifying a directory in the Disallow rule, you are telling the crawlers to avoid crawling all pages under that directory, and you don’t need to use the (*) wildcard anymore, like “/form/*.”

Note that you must always specify relative paths and never absolute URLs, like “https://www.example.com/form/” for Disallow and Allow directives.

Be cautious to avoid malformed rules. For example, using /form without a trailing slash will also match a page /form-design-examples/, which may be a page on your blog that you want to index.

Read: 8 Common Robots.txt Issues And How To Fix Them

#### 5. Block User Account URLs

If you have an ecommerce website, you likely have directories that start with “/myaccount/,” such as “/myaccount/orders/” or “/myaccount/profile/.”

With the top page “/myaccount/” being a sign-in page that you want to be indexed and found by users in search, you may want to disallow the subpages from being crawled by Googlebot.

You can use the Disallow rule in combination with the Allow rule to block everything under the “/myaccount/” directory (except the /myaccount/ page).

User-agent: * Disallow: /myaccount/ Allow: /myaccount/$

And again, since Google uses the most specific rule, it will disallow everything under the /myaccount/ directory but allow only the /myaccount/ page to be crawled.

Here’s another use case of combining the Disallow and Allow rules: in case you have your search under the /search/ directory and want it to be found and indexed but block actual search URLs:

User-agent: * Disallow: /search/ Allow: /search/$

#### 6. Block Non-Render Related JavaScript Files

Every website uses JavaScript, and many of these scripts are not related to the rendering of content, such as tracking scripts or those used for loading AdSense.

Only block a script after confirming it is unnecessary for rendering the content and links you want indexed. Use URL Inspection to check the rendered page; blocking a shared bundle or a script with rendering dependencies can prevent Google from seeing important content. A robots.txt file on your host also cannot control a script fetched from a different host.

Below is a sample line that is disallowing sample JavaScript, which contains tracking pixels.

User-agent: * Disallow: /assets/js/pixels.js

#### 7. Control AI Bots and Scrapers

You can block training bots while allowing AI tools to find your pages and retrieve them for users. The key is to give training, search, and user-requested AI crawlers separate rules.

Publishers may block training to limit the use of their reporting without attribution, while ecommerce brands may welcome it if product mentions lead people to search and buy. Because the benefits differ by business, developers should set these rules with stakeholders.

Disallowing training bots cannot guarantee that your content stays out of training datasets, because crawlers that ignore robots.txt can still collect it. It also does not force AI tools to visit or cite your site, as they may find the information elsewhere.

A BuzzStream study covered by SEJ in January 2026, found that 79% of the US and UK news sites examined disallowed at least one training bot, while 71% disallowed at least one retrieval or live-search bot. Because retrieval helps AI tools find and cite your pages, blocking those bots is a separate decision from opting out of training.

##### Block Training Bots and Allow Search and User Bots

OpenAI uses OAI-SearchBot to surface websites in ChatGPT search answers, while ChatGPT-User handles user-requested visits. Because search and training permissions are separate, you can allow OAI-SearchBot and ChatGPT-User while blocking GPTBot .

This example blocks OpenAI’s and Anthropic’s training crawlers while allowing their search and user-requested bots, along with Perplexity’s:

# Block model-training crawlers User-agent: GPTBot User-agent: ClaudeBot Disallow: / # Allow search and user-requested visits User-agent: OAI-SearchBot User-agent: ChatGPT-User User-agent: Claude-SearchBot User-agent: Claude-User User-agent: PerplexityBot User-agent: Perplexity-User Disallow: /private/

In the example above, /private/ is an excluded directory. Replace it with any paths you want to keep those bots from crawling.

Most major AI crawlers follow robots.txt, including OpenAI’s GPTBot and Anthropic’s ClaudeBot .

User-requested visits work differently because some providers allow their bots to bypass robots.txt or generally ignore it when acting on a user’s request. OpenAI says robots.txt may not apply to ChatGPT-User , and Perplexity says Perplexity-User generally ignores it. Anthropic says its bots, including Claude-User , honor robots.txt. Because robots.txt only tells bots which URLs they may crawl, you need authentication to protect private content.

User-Requested Bots

Follows robots.txt?

ChatGPT-User

Perplexity-User

Claude-User

Yes

Google-Agent

Google-GeminiNotebook

MistralAI-User

Yes

meta-externalfetcher

Amzn-User

The bot tokens and robots.txt policies for Copilot’s browser visits , Grok , DeepSeek , and Meta Muse remain unknown because I could not verify them in the providers’ public documentation.

##### Restrict Google and Apple Training Uses

Google and Apple provide separate robots.txt tokens for controlling how crawled content is used:

User-agent: Google-Extended User-agent: Applebot-Extended Disallow: /

Google-Extended covers Gemini training and specified grounding uses, where source content helps generate an answer. Blocking it does not block Googlebot or affect ordinary Google Search inclusion. Applebot-Extended controls foundation-model training without blocking Applebot’s search crawl. Neither token is a separate crawler, so these rules do not reduce crawling requests by themselves.

After changing the file, check your server log files and confirm that your firewall allows the bots you want. Use server or CDN controls when you need to enforce access restrictions.

For background, see SEJ’s earlier coverage of AI content use and AI chatbot traffic .

#### 8. Specify Sitemap URLs

Including your sitemap URL in the robots.txt file helps search engines easily discover all the important pages on your website. This is done by adding a specific line that points to your sitemap location, and you can specify multiple sitemaps, each on its own line.

Sitemap: https://www.example.com/sitemap/articles.xml Sitemap: https://www.example.com/sitemap/news.xml Sitemap: https://www.example.com/sitemap/video.xml

Unlike Allow or Disallow rules, which allow only a relative path, the Sitemap directive requires a full, absolute URL to indicate the location of the sitemap.

Ensure the sitemaps’ URLs are accessible to search engines and have proper syntax to avoid errors.

Sitemap fetch error in search console. Screenshot by Author, September 2024.

#### 9. When to Use Crawl-Delay

The crawl-delay directive in robots.txt specifies the number of seconds a bot should wait before crawling the next page. While Googlebot does not recognize the crawl-delay directive, other bots may respect it.

It helps prevent server overload by controlling how frequently bots crawl your site.

For example, if you want ClaudeBot to crawl your content for AI training but want to avoid server overload, you can set a crawl delay to manage the interval between requests.

User-agent: ClaudeBot Crawl-delay: 60

This requests a 60-second delay from ClaudeBot, which Anthropic documents as supporting the non-standard Crawl-delay extension. Use this when you intend to allow that crawl. Adding a delay does not override a Disallow: / rule for the same bot; review the complete group rather than copying both policies.

Of course, there may be AI bots that don’t respect crawl delay directives. In that case, you may need to use a web firewall to rate limit them.

### Troubleshooting Robots.txt

Once you’ve composed your robots.txt, you can use these tools to troubleshoot if the syntax is correct or if you didn’t accidentally block an important URL.

#### 1. Google Search Console Robots.txt Report

Once you’ve updated your robots.txt, you must check whether it contains any error or accidentally blocks URLs you want to be crawled, such as resources, images, or website sections.

Navigate to Settings > robots.txt to open the robots.txt report . It shows the files Google fetched and any parsing warnings or errors. You can request a recrawl after a critical change. To test whether an individual page is blocked, use URL Inspection.

The video below illustrates the report workflow; interface details may differ from the current version.

https://cdn.searchenginejournal.com/wp-content/uploads/2024/09/google-search-console-how-validate-robots.txt-guide.mp4

#### 2. Google Robots.txt Parser

Google’s robots.txt parser is an open-source parser and matcher based on the implementation used in Google’s crawler.

It requires advanced skills to install and run on your local computer. But it is highly recommended to take time and do it as instructed on that page because you can validate your changes in the robots.txt file before uploading to your server in line with the official Google parser.

### Centralized Robots.txt Management

Robots.txt rules apply to the host, protocol, and port where the file is requested. If you need crawl restrictions on a subdomain, its robots.txt URL must serve the rules or redirect to a file that does; the parent domain’s file is not inherited.

It creates challenges when you have a website with a dozen subdomains, as it means you should maintain a bunch of robots.txt files separately.

However, it is possible to host a robots.txt file on a subdomain , such as https://cdn.example.com/robots.txt, and set up a redirect from https://www.example.com/robots.txt to it.

You can do vice versa and host it only under the root domain and redirect from subdomains to the root.

Google applies the retrieved rules to the host that originally requested robots.txt, not automatically to the host storing the shared file. Configure a redirect from each host you want to manage, and check that the shared paths make sense for all of them.

It helps make updates and maintenance more efficient. Otherwise, you would need to use a separate robots.txt file for each subdomain.

### Robots.txt Is One Part Of Crawl Management

A properly optimized robots.txt file is crucial for managing a website’s crawl budget . It ensures that search engines like Googlebot spend their time on valuable pages rather than wasting resources on unnecessary ones.

Blocking compliant crawlers can reduce unwanted requests. For AI systems, distinguish crawl restrictions from training-use controls, and verify the effect in your logs. Google-Extended and Applebot-Extended do not stop a separate crawler.

Make sure you always validate your changes to avoid unexpected crawlability issues.

However, remember that crawl demand and serving capacity both matter. Useful content, efficient page loading, and a healthy server remain important alongside robots.txt rules.

Happy crawling!

More resources:

- 500 Response on Robots.txt Fetch Can Impact Rich Results

- Crawler Traps: Causes, Solutions & Prevention – A Developer’s Deep Dive

- 8 Common Robots.txt Issues And How To Fix Them

- 9 Tips to Optimize Crawl Budget for SEO

- 7 SEO Crawling Tool Warnings & Errors You Can Safely Ignore

Featured Image: BestForBest/Shutterstock

Category SEO

Read Full Bio

SEJ STAFF Vahan Petrosyan Director of Technology at Search Engine Journal

As Director of Technology at Search Engine Journal, I lead the organization’s technology strategy and technical operations. I oversee technical ...

## 原文链接

[Read original](https://www.searchenginejournal.com/technical-seo/robots-txt-guide-best-practices-for-search-ai-crawlers/)
