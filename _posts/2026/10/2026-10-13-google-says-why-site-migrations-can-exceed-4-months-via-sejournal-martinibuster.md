---
layout: post
title: "Google Says Why Site Migrations Can Exceed 4 Months via @sejournal, @martinibuster"
date: 2026-10-13T11:23:58+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-13/Google Says Why Site Migrations Can Exceed 4 Months via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/google-says-why-site-migrations-can-exceed-4-months/592757/"
author: "Roger Montti"
categories:
  - "News"
  - "SEO"
  - "_src_search-engine-journal"
---

# Google Says Why Site Migrations Can Exceed 4 Months via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-10-13
- URL: https://www.searchenginejournal.com/google-says-why-site-migrations-can-exceed-4-months/592757/
- Author: Roger Montti
- Categories: News, SEO

## RSS 摘要

Google may process a site migration for months, then blow it and rank the old URLs anyway. Mueller says what to focus on. The post Google Says Why Site Migrations Can Exceed 4 Months appeared first on Search Engine Journal .

## 原文正文

Google Says Why Site Migrations Can Exceed 4 Months Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- SEO

## Google Says Why Site Migrations Can Exceed 4 Months

Google can keep a site migration in limbo for months. Mueller identifies an overlooked setting that may help end the uncertainty.

Google’s John Mueller suggested that a change of address for a domain and website can take longer than four months to process. He also provided insight on how to prevent that from happening in order to have a better outcome.

### Curious Domain Migration Experience

A site owner reported on Reddit that they had a successful domain migration at the beginning of 2026 and everything progressed relatively smoothly with traffic fully recovered by April.

Four months later Google restored the old domain’s search visibility, essentially deindexing the new domain and resurrecting the old version in the search results. Site visitors clicking to the old domain were still being redirected to the new version, which search console began reporting as crawled but not indexed.

They explained :

“So I have a website that was doing very well, especially on Google. At the start of 2026, I changed the name and domain so that one additional topic could be covered. Did all the redirects, Change of Address, and internal name changes right away so traffic recovered quickly around the start of April.

Everything was indexed on the new site and the new domain was getting around 5,000 impressions per day. Four months later, Google suddenly reverted everything back to the old domain.

More than 5,000 pages of the new domain were changed to Crawled, Not Currently Index and the new domain now gets 20 impressions per week.

But if I open GSC on the old domain, everything is there. The entire old domain was suddenly indexed all over again and all the impressions and clicks are showing there.

So one post shows up on Google under the old domain and when you click it, it redirects to the same post under the new domain and counts as a regular view for the new domain.

Why would Google suddenly revert this four months after everything was fixed? How do I fix this? Do I actually have to fix this since the impressions and clicks are still there, just being redirected?”

### Many Details Missing

The person sharing their experience doesn’t say if they crawled their new domain to see if there are any internal links that are hardcoded with absolute URLs using the old domain name instead of using a relative URL.

Here’s the difference:

- Absolute URL: www.example.com/some-page.html

- Relative URL: /some-page.html

Sometimes absolute URLs can sneak into the site navigation, footer navigation, or within the content itself as contextual links. The best way to catch those is to give the old domain a full crawl with Screaming Frog prior to the domain name migration in order to identify those stray absolute internal links.

Another critical detail missing is how they redirected the old domain to the new domain. Was it a domain registrar-level redirect that preserves URL paths or was it a URL to URL redirect? The registrar-level redirect might not preserve file paths. HTTPS forwarding may fail if the old domain doesn’t have an SSL certificate.

Another issue that can potentially complicate a migration are chained redirects.

And here’s a big one: Redirects can sometimes fail when or if the navigational structure on the new site changes.

Lastly, the person asking the question on Reddit did not indicate if they updated their XML sitemap. This matters because XML sitemaps communicate preferred canonical URLs to Google. If the sitemap still lists the old domain, it could send conflicting canonicalization signals during the migration.

Google explicitly mentions the usefulness of sitemaps as part of a URL migration:

“Submitting a sitemap can help make the discovery process quicker, and it’s fine to move your site in sections.”

That advice presumes that the sitemap is for the correct domain name, right?

Google’s John Mueller offers his inside knowledge of other things to avoid.

### John Mueller’s Advice For A Successful Domain Migration

Mueller responded that sometimes the domain name migration can take an extra long time. He also recommended doing a search console change of address for both WWW and non-WWW versions of the domain name.

He responded:

“Happy to take a look if you want to DM me the domains. Sometimes things just take a particularly long time to be fully processed.

One thing which we noticed (and adjusted in the documentation a while back) that can help is to make sure that you have change of address set up in search console for both www and non-www , so that it can fully migrate the domain.”

### Canonicalization And Site Migration

The WWW and non-WWW domain versions of URLs for a change of address is a good catch. There could be links from outside of the site that are linking to one or the other that could be contributing to Google choosing the old domain as the canonical.

For diagnosing a site migration gone wrong, it’s not unreasonable to approach it as a canonicalization issue. Canonicalization is when Google chooses one domain or URL over all others as the one to index and rank.

Featured Image by Shutterstock/Mulad Images

Category News SEO

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-says-why-site-migrations-can-exceed-4-months/592757/)
