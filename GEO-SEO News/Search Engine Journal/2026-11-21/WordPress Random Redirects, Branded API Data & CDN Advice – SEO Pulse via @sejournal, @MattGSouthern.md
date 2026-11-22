---
title: "WordPress Random Redirects, Branded API Data & CDN Advice – SEO Pulse via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-11-21T13:00:00+00:00
fetched_at: 2026-11-22T01:27:45.625038+00:00
url: "https://www.searchenginejournal.com/seo-pulse-wordpress-random-redirects-branded-api-data-cdn-advice/598173/"
guid: "https://www.searchenginejournal.com/seo-pulse-wordpress-random-redirects-branded-api-data-cdn-advice/598173/"
author: "Matt G. Southern"
categories:
  - "SEO"
  - "SEO Pulse"
---

# WordPress Random Redirects, Branded API Data & CDN Advice – SEO Pulse via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-11-21
- URL: https://www.searchenginejournal.com/seo-pulse-wordpress-random-redirects-branded-api-data-cdn-advice/598173/
- Author: Matt G. Southern
- Categories: SEO, SEO Pulse

## RSS 摘要

This week's SEO Pulse covers WordPress's random redirect, branded data in Search Console API, Google's CDN guidance, and who controls access for bots and agents. The post WordPress Random Redirects, Branded API Data & CDN Advice – SEO Pulse appeared first on Search Engine Journal .

## 原文正文

WordPress Random Redirects, Branded API Data & CDN Advice – SEO Pulse Skip to content

Webinar: State Of Agentic AEO For 2027: What’s Scaling & What’s Stalling

Register Now

- SEJ

- ⋅

- SEO

## WordPress Random Redirects, Branded API Data & CDN Advice – SEO Pulse

This week's SEO Pulse covers WordPress's random redirect, branded data in Search Console API, Google's CDN guidance, and who controls access for bots and agents.

Welcome to the week’s Pulse: updates include a WordPress default that you will need to decide on, new data from Search Console via the API, and the question of which party determines whether Googlebot, AI agents or Google’s own calls will be allowed through.

WordPress 7.2 will introduce a /random/ redirect (turned on by default), and Google has added branded data to the Search Console API. Google also published the referrer values its traffic sends and shared ways in which a CDN move could lead to blocking Googlebot. Ask Maps began contacting local businesses, and United Airlines included its AI agent rules within its terms.

Here’s what matters for you and your work.

### WordPress 7.2 Plans A /Random/ Redirect That’s On By Default

WordPress version 7.2, which is scheduled for Dec. 8 , contains a new feature called /random/, turned on by default, to send a visitor to a randomly selected published post. There is no option in the dashboard settings for this to be turned off.

Key facts: According to the developer note , /random/ randomly selects posts and also custom post types as long as they are publicly queryable and have archives (unless the developer has registered them using 'randomable' => false ) and excludes pages and attachments. The development code uses a 302 status code along with an X-Robots-Tag: noindex, follow HTTP header when it redirects the visitor but does not send that header on the post that the visitor arrives at. To turn the feature off, developers need the wp_enable_random_content_redirect filter, and the different spelling given in WordPress’s November developer news roundup isn’t found anywhere in the code.

#### Why This Matters

Testimonials for clients (and other custom post type entries) may never be accessed via navigation. When their post type is eligible, they can be reached through /random/, even if they have been set to noindex by an SEO plugin. Before you update, check which post types would meet WordPress’s eligibility criteria, and ask a developer to exclude those that should not show up.

Read our full coverage: WordPress 7.2 Arrives Dec. 8 – Last-Minute Changes Still Being Made

### Branded Query Data Comes To The Search Console API

Teams using the Search Console API can now segment the data they pull into branded and non-branded searches without having to maintain a list of their brands as regular expressions (regex).

Key facts: Three Performance report features were added to the Search Analytics API by Google on Nov. 16. The brandedClassification dimension works only with eligible properties, and according to the API reference , the data provided for this dimension starts on Feb. 21, 2026. Setting type to webMultimodal returns results from Google Lens, Circle to Search on Android and image uploads, and a new filterLists field allows you to filter by multiple countries or devices in a single request.

#### Why This Matters

For reports covering dates before Feb. 21, 2026, you’ll still need your own brand regex. Google’s announcement of the branded queries filter says “some queries may occasionally be misidentified,” so comparing the API split with the regex you already use can help you spot where they differ.

Read our full coverage: Branded Query Data Is Now In The Google Search Console API

### Search, Discover And Google Images Share Referrer Values

A google.com referrer lets you know in your analytics when Google sends a visitor, but it doesn’t show which source (Search, Discover or Google Images) was behind it, says a new Search Central page .

Key facts: The page was listed Nov. 12 in Google’s documentation updates log . It says Google Search utilizes an origin referrer policy for its Search results; thus, the header will contain only the scheme and host, and not the search query. Referrers from Discover carry the values of the surface where Discover was viewed. Same-origin services such as Google Images send the same values as Search and Discover.

#### Why This Matters

To distinguish Discover clicks from Search clicks, use Search Console’s Discover report rather than referrer data. If Google traffic appears as referral or direct in your analytics, Google’s page recommends checking whether custom channel rules, referral exclusions, or filters are reclassifying it.

Read our full coverage: Google Explains How To Find Search Traffic In Analytics & Logs

### A CDN Move Can Speed Up Googlebot Before The Cache Is Ready

A CDN can let Googlebot crawl your site faster before the CDN’s cache has filled, according to Google , and those requests then go to your origin server.

Key facts: On Nov. 11, Search Central posted Google’s explanation that a fast and reliable CDN may slowly increase a site’s crawl capacity limit, while a brand new CDN begins with an empty cache. The first visit to each URL is a cache miss, so the page has to come from your origin server, and crawlers visit far more of your site’s URLs than visitors do, with most visitors sticking to a small set of popular pages. When admins block all bots from their site using blanket bot protection, they can cause Googlebot to fail CAPTCHA challenges. If this stays in place, then the pages of the site begin to drop out of search results.

#### Why This Matters

Google’s advice for the move is to allow verified bots in the CDN and firewall settings, then pre-warm caches by fetching your most popular and frequently crawled URLs before switching traffic. Before enabling bot protection during the migration, be sure the verified-bot setting is turned on.

Read our full coverage: Google Explains How To Avoid CDN Migration SEO Problems

### Ask Maps Starts Calling Local Businesses To Find Open Appointments

Google’s Ask Maps has started calling some U.S. beauty, pet care, auto and home-repair businesses to identify available appointment times for customers.

Key facts: On Nov. 16 a post from Google said that customers can use Ask Maps to find these appointments online and have it call local businesses, then see available time slots so the customer can decide where to book. The feature started rolling out on Android and iOS, with the ability to find appointments launching in the U.S. first. Google already makes automated calls to businesses for customers using Google Search and Maps, including booking appointments and confirming availability, and this process is covered in Google’s Business Profile help page .

In Google’s demo, Ask Maps shows four times for a gel manicure that it confirmed were available online.

Some sequences in the demo were shortened and simulated. Source: Google .

#### Why This Matters

The setting Google documents for those automated calls is the “Bookings and inquiries from customers” option in Advanced settings in your verified Business Profile. However, Google’s Ask Maps post does not indicate if calls received via Ask Maps are subject to this setting. Check what you have set, and make sure whoever answers the phone knows these calls come from Google on behalf of a customer.

Read our full coverage: Google Adds Appointment Finding & Business Calls To Ask Maps

### United Makes AI Agents Ask First But Keeps Search Indexing Open

United Airlines’ website terms , updated Nov. 11, let search engines index its public pages but require written permission for any AI agent that searches, books or buys on its site or app.

Key facts: The terms also bar using data from United’s site or app, such as fares and schedules, to “train, fine-tune, ground, evaluate, or otherwise develop” an AI model. As of Nov. 14, United’s robots.txt named no AI crawlers or agents. Separately, HUMAN Security’s October report found that Meta’s and OpenAI’s agents made about 90% of the agent requests on sites and apps it protects.

In HUMAN Security’s October data, Muse accounted for 59% of agent requests. Three OpenAI agents accounted for about 30% combined.

Source: HUMAN Security, October 2026 agentic traffic report .

#### Why This Matters

Meta’s Muse publishes no user agent for a robots.txt rule to name, as Slobodan Manic wrote in October , so whether it gets in comes down to your terms and bot protection. Muse sent the most requests in HUMAN’s data, and bot rules can check the signatures some of its requests carry, whose key directory DataDome reported had moved to muse.ai by Nov. 9.

Read our full coverage: United Lets Search Engines Index Its Site, Makes AI Agents Ask First and Meta & OpenAI Agents Made Nearly 90% Of Agent Requests In Bot Data

### Theme Of The Week: Decisions That Sit With Other Teams

Much of this week’s SEO work sits with teams outside of SEO. The next steps for this week include identifying who is responsible for the off switch for the /random/ redirect, as well as reporting on the branded split and the analytics rules for referrers. Google’s CDN advice should be reviewed by whoever runs the CDN and firewall, and the automated calls toggle is managed through the Business Profile. United’s rules related to agents are contained within a legal agreement. Before the next change, the first step is to determine who has responsibility for each of these in your own organization.

Top Stories Of The Week:

- WordPress 7.2 Arrives Dec. 8 – Last-Minute Changes Still Being Made

- Branded Query Data Is Now In The Google Search Console API

- Google Explains How To Find Search Traffic In Analytics & Logs

- Google Explains How To Avoid CDN Migration SEO Problems

- Google Adds Appointment Finding & Business Calls To Ask Maps

- United Lets Search Engines Index Its Site, Makes AI Agents Ask First

- Meta & OpenAI Agents Made Nearly 90% Of Agent Requests In Bot Data

More Resources:

- Amazon Blocked Meta’s Muse, And Robots.txt Had Nothing To Say

- Google Search Console Adds Multimodal Filter For Image-Based Searches

- Google Explains How Redirects Affect Ranking Signals

Featured Image: Ground Picture/Shutterstock

Category SEO SEO Pulse

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/seo-pulse-wordpress-random-redirects-branded-api-data-cdn-advice/598173/)
