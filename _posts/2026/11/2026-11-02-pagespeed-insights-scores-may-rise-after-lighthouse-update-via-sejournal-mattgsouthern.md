---
layout: post
title: "PageSpeed Insights Scores May Rise After Lighthouse Update via @sejournal, @MattGSouthern"
date: 2026-11-02T21:52:57+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-02/PageSpeed Insights Scores May Rise After Lighthouse Update via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/pagespeed-insights-scores-lighthouse-update/595698/"
author: "Matt G. Southern"
categories:
  - "News"
  - "Technical SEO"
  - "_src_search-engine-journal"
---

# PageSpeed Insights Scores May Rise After Lighthouse Update via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-02
- URL: https://www.searchenginejournal.com/pagespeed-insights-scores-lighthouse-update/595698/
- Author: Matt G. Southern
- Categories: News, Technical SEO

## RSS 摘要

A Google Lighthouse update changes how PageSpeed Insights simulates page loads, which can raise lab scores on pages that haven't changed. The post PageSpeed Insights Scores May Rise After Lighthouse Update appeared first on Search Engine Journal .

## 原文正文

PageSpeed Insights Scores May Rise After Lighthouse Update Skip to content

AI Search Tracking Checklist: How to Attribute Calls From ChatGPT, Claude, and Perplexity

Download the Checklist

- SEJ

- ⋅

- Technical SEO

## PageSpeed Insights Scores May Rise After Lighthouse Update

- PageSpeed Insights now runs a Lighthouse version that simulates page loading differently.

- Google's Barry Pollard says scores usually come out better, with JavaScript-heavy sites more likely affected.

- Check the Lighthouse version and field data before crediting a higher score to site work.

A Google Lighthouse update changes how PageSpeed Insights simulates page loads, which can raise lab scores on pages that haven't changed.

PageSpeed Insights is now using Lighthouse 13.6.0 , which was released Oct. 27. This version of Lighthouse changes how it simulates how long a page takes to load.

Chrome’s Web Performance Developer Advocate, Barry Pollard, has stated on Bluesky that the updated version of PageSpeed Insights with Lighthouse 13.6.0 is now available. He said this improves the simulated FCP (First Contentful Paint) and the simulated LCP (Largest Contentful Paint), both of which Pollard says will be more accurate than before and generally result in higher scores.

A page may receive a different PageSpeed Insights score without anything on it changing, due to the change in the test. Pollard also said that websites heavily dependent on JavaScript would be more likely to see an impact from the updated test.

### Pollard Points To JavaScript-Heavy Sites

Pollard quoted a developer who had posted about how single-page apps (SPAs) had seen a big improvement in their results since the Lighthouse update, citing react.dev. He opened his post stating, “True!”, then added:

“Note this is not SPA-specific (and unrelated to other SPA things we’ve been working on), but more likely to impact JS-heavy sites.”

The experimental soft navigation metrics in Chrome that I wrote about back in October are a separate way of measuring user experience. The data comes from real Chrome users through the Chrome User Experience Report (CrUX) and Lighthouse uses a simulated test.

### What Changed In The Simulation

By default, Lighthouse will load a page at full speed and then estimate how it would load on a slower connection. The throttling docs say that this simulated throttling matches PageSpeed Insights’ setup.

The release notes for version 13.6.0 of Lighthouse list several changes to Lantern, which is the simulation behind those estimates, aimed at improving its accuracy.

Lighthouse 13.5 used each request’s fetch priority to decide whether or not it blocked rendering. In 13.6, Lantern uses Chrome’s own render-blocking label for each request (and falls back to using priority only when that label is missing).

A second change applies when the LCP element is text that appears in the same frame as the page’s first content. Lantern now estimates that LCP from the same requests and page tasks it uses for FCP instead of from a set that can include every request made before LCP.

Ivan Akulov showed in a GitHub issue how the old simulation handled a test page created with Framer whose only content above the fold was text, so one element counted as both FCP and LCP. Lighthouse reported much later LCP than FCP for that text. Even though preloading the page’s JavaScript modules improved interactive time for the real page, they caused simulated LCP to be worse.

Pollard thanked Akulov in a reply , saying he “kicked off some of these improvements.” The Lighthouse team closed the issue as completed in the Lantern upgrade listed in the 13.6 release notes.

### The ARD Audit Now Checks For ard.json

Lighthouse 13.6 has also updated the Agentic Resource Discovery (ARD) audit from Lighthouse 13.5, which I covered in September . When Lighthouse 13.5 was released, it looked for an ARD manifest under the old ai-catalog names even though the spec had changed to ard.json . So if your website only used the new name but you didn’t include a line in your robots.txt file called Agentmap, it would show as Not Applicable.

With this update, Lighthouse 13.6 will look for an Agentmap line, a rel="ard" link tag or Link header and /.well-known/ard.json prior to looking for the ai-catalog names. And if Lighthouse 13.6 finds the manifest only at an ai-catalog location, it will note that ARD consumers are not required to check there.

### Lab Scores And Field Data

The performance score listed for your page in PageSpeed Insights is based on data generated by Lighthouse. According to Google’s PageSpeed Insights documentation , lab data are results of a simulated load using a single device running on a fixed set of network conditions. They note that “having good lab data does not necessarily mean real-user experiences will also be good.”

Field data (also shown in the same report) represents real visits to your website within the last 28 days, as reported by CrUX. Each PageSpeed Insights report includes the version of Lighthouse used to generate results, next to the emulated device.

### Why This Matters

PageSpeed Insights scores from before and after the Lighthouse 13.6 update weren’t measured with the same simulation. Part of a higher lab score on a page you just optimized may come from the new version, and charts that track lab scores over time may show a jump at the switch to 13.6.

Before reporting an improvement, check that both reports name the same Lighthouse version, and compare the field data.

### Looking Ahead

Lighthouse’s release notes say its team expects 13.6 to ship in the DevTools of Chrome 159, which is now in Chrome’s desktop Dev channel and in Canary. As of Nov. 2, Chrome’s release schedule lists Chrome 159 for stable release on Dec. 8.

An open issue on Lighthouse’s GitHub is also looking into cases where Lantern’s simulated LCP runs far above measured LCP, using large JavaScript and SPA sites as examples.

Featured Image: Remo_Designer/Shutterstock

Category News Technical SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/pagespeed-insights-scores-lighthouse-update/595698/)
