---
layout: post
title: "Google Ad Tags In Server-Side GTM To Get Full IP Addresses via @sejournal, @MattGSouthern"
date: 2026-11-03T19:30:00+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-11-03/Google Ad Tags In Server-Side GTM To Get Full IP Addresses via @sejournal, @MattGSouthern.md"
original_url: "https://www.searchenginejournal.com/google-ad-tags-in-server-side-gtm-to-get-full-ip-addresses/595807/"
author: "Matt G. Southern"
categories:
  - "News"
  - "PPC"
  - "_src_search-engine-journal"
---

# Google Ad Tags In Server-Side GTM To Get Full IP Addresses via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-03
- URL: https://www.searchenginejournal.com/google-ad-tags-in-server-side-gtm-to-get-full-ip-addresses/595807/
- Author: Matt G. Southern
- Categories: News, PPC

## RSS 摘要

Google says ad tags in server-side Tag Manager will accept full IP addresses while Analytics tags stay redacted. Here's what changes and how to redact. The post Google Ad Tags In Server-Side GTM To Get Full IP Addresses appeared first on Search Engine Journal .

## 原文正文

Google Ad Tags In Server-Side GTM To Get Full IP Addresses Skip to content

AI Search Tracking Checklist: How to Attribute Calls From ChatGPT, Claude, and Perplexity

Download the Checklist

- SEJ

- ⋅

- PPC

## Google Ad Tags In Server-Side GTM To Get Full IP Addresses

- Google says its ad tags in server-side GTM will accept full IP addresses.

- Google Analytics tags will keep applying IP redaction, according to the notice.

- Google's Help Center describes a Transformation that sends ad tags a partially redacted IP.

Google says ad tags in server-side Tag Manager will accept full IP addresses while Analytics tags stay redacted. Here's what changes and how to redact.

Server-side Google Tag Manager will let tags for Google’s ad products accept full IP addresses starting Jan. 11, 2027, according to a Google notice to advertisers .

The change covers tags that send data to Google Ads, Display & Video 360, Search Ads 360 and Campaign Manager 360 from a server container. Google Analytics tags will keep redacting IP addresses, the notice says.

Google Ads specialist Adriaan Dekker shared the notice on LinkedIn on Nov. 2. It carries no issue date, and Google’s Tag Manager release notes don’t mention the change as of Nov. 3.

Advertisers with Google ad tags in a server container have until Jan. 11 to decide whether those tags should get full or partially redacted IP addresses.

### What The Notice Changes

The notice, titled “Updates to network signal processing in server-side tagging,” explains that server containers “will transition from container-wide IP address redaction to individual tag-level processing.” It then outlines four effects:

Tags sending data to Google Ads, Display & Video 360, Search Ads 360 and Campaign Manager 360 will now accept the full IP address.

Google Analytics tags will continue to apply IP redaction.

Third-party tags will maintain independent control over the signals that they accept.

Transformations can redact these signals before any tag accesses the data.

The notice addresses server containers only. It says nothing about the Google tag or web containers running in the browser.

Google’s release notes show server-side Tag Manager could redact or anonymize IPs through Analytics server tags as of March 2021. Transformations, which edit or exclude event data before tags read it, followed in June 2023.

The notice doesn’t explain how container-wide redaction is currently set up. Google’s server-side setup page for the Google Ads conversion tag says the tag sends “all the available conversion data to Google” unless transformations change it, and, as of Nov. 3, doesn’t mention IP addresses.

### How To Keep IP Addresses Redacted

The notice directs users to “our Help Centre article for detailed opt-out instructions” and does not reveal where the link is pointing to based upon the screenshot provided. A Tag Manager Help Center page, IP address redaction for server-side tagging , shows an example of how to use transformations.

The page outlines the main steps to set up this functionality using transformations:

- Create a new Custom Template Variable that calls Google’s getAnonymizedIpAddress function.

- Create a new Augment event transformation that overwrites the ip_override field with the anonymized IP address from step one.

This will affect the tags you choose (such as Google Ads or Floodlight). After completing these steps the page also states to check the results in Preview prior to deploying the changes to production. Additionally, the page explains that Analytics server tags “already apply partial IP redaction by default.”

Google’s API reference says the function zeroes the last octet of an IPv4 address and the last 80 bits of an IPv6 address. The Help page calls the result a “partially redacted IP.”

Google added the function to its API reference after Oct. 12. The Internet Archive’s Oct. 12 capture of the page doesn’t list it. The live page does, and shows an Oct. 30 update date.

Some third-party tags may need a Transformation of their own. The Help page notes that these tags can read IP addresses from custom headers or event parameters rather than from ip_override, so you’ll need to set the Transformation to target the field each tag uses.

### Consent Requirements

Per the notice, advertisers utilizing Google’s advertising products “must ensure that proper end-user notices and legally required consents are in place before data collection begins.” In addition, all advertisers using Google’s advertising products in the EEA “must strictly adhere” to Google’s EU User Consent Policy , and the policy extends to those customers whose end users reside in the United Kingdom and/or Switzerland. All customers in other areas where privacy regulations apply must follow those regional requirements and platform terms.

Google says the update “integrates privacy-enhancing technologies (PETs),” filters spam and invalid traffic, and will improve campaign performance.

The announcement does not provide information about how changes will interact with consent mode as well as the non-consenting requests that were stated in the Release Notes (Floodlight tags in server containers are said to have begun sending in July 2025) nor was there any mention of where or how long full IP addresses would be stored.

The announced server-side change is distinct from Google’s planned Analytics data control updates ; these will encrypt IP addresses collected by the Google tag and SDK and pass them to linked Google Ads accounts, on dates Google plans to share later this year.

### Why This Matters

You can use server-side tagging to decide how much information goes with each tag as it leaves your servers, and Google’s notice determines whether its ad tags will accept full IP addresses in this configuration.

Prior to Jan. 11, review all Google Ads, Floodlight and third-party tags inside your server containers and identify which IP field each tag is reading. The method outlined by Google in the help section on how to build a Transformation using preview testing is currently the documented solution for keeping an ad tag’s IP partially masked. Your consent process should include any IP data used by these tags.

### Looking Ahead

Tag-level IP processing for Google server containers is scheduled to begin January 11, 2027. There are no references to IP addresses in either of Google’s server-side pages on Transformations or consent mode as of Nov. 3.

The Tag Manager release notes may provide an official announcement when tag-level IP handling for server containers is available and the developer pages may have the detailed information. The Redaction help page should be reviewed prior to creating your Transformation because that is how you do this now.

Featured Image: Stockinq/Shutterstock

Category News PPC

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-ad-tags-in-server-side-gtm-to-get-full-ip-addresses/595807/)
