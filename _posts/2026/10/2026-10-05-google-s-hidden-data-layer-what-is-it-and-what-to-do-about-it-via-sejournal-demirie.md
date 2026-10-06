---
layout: post
title: "Google’s Hidden Data Layer: What Is It And What To Do About It via @sejournal, @demirie"
date: 2026-10-05T14:30:56+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-10-05/Google’s Hidden Data Layer What Is It And What To Do About It via @sejournal, @demirie.md"
original_url: "https://www.searchenginejournal.com/googles-hidden-data-layer-what-is-it-and-what-to-do-about-it/590234/"
author: "Emina Demiri-Watson"
categories:
  - "Digital Marketing"
  - "Ecommerce"
  - "SEO"
  - "_src_search-engine-journal"
---

# Google’s Hidden Data Layer: What Is It And What To Do About It via @sejournal, @demirie

- Source: Search Engine Journal
- Published: 2026-10-05
- URL: https://www.searchenginejournal.com/googles-hidden-data-layer-what-is-it-and-what-to-do-about-it/590234/
- Author: Emina Demiri-Watson
- Categories: Digital Marketing, Ecommerce, SEO

## RSS 摘要

Trace misleading sale badges and outdated product images to Google's hidden data layer, with checks that go beyond your current feed. The post Google’s Hidden Data Layer: What Is It And What To Do About It appeared first on Search Engine Journal .

## 原文正文

Google's Hidden Data Layer: What Is It And What To Do About It Skip to content

SEJ Pro Sign In

Ebook: State Of Search 2027

Download The Report

- SEJ

- ⋅

- Ecommerce

## Google’s Hidden Data Layer: What Is It And What To Do About It

Trace misleading sale badges and outdated product images to Google's hidden data layer with checks of price history, indexed images, and feed mismatches.

At some point, most of us working in ecommerce have had that email. A client, a colleague, someone senior, asking why a product looks like it’s on sale when it isn’t. Or why an old product image is showing up in Shopping. Or why a campaign that looks fine on Google is getting rejected somewhere else entirely.

You check what you always check. The feed. The schema. The website. But you can’t figure out what’s causing the issue.

That’s usually the first sign you’re dealing with Google’s hidden data layer.

Google isn’t only working with what you’re currently telling it. It builds a persistent memory of your products. Prices, images, and other product data are gathered over time and sometimes stitched together across sources.

Like an elephant, it never forgets what it’s previously seen on your own site, long after you’ve moved on. And like a truffle pig, it sometimes goes foraging well beyond your domain entirely, into marketplace listings and third-party pages you may not have thought about in years.

Meanwhile, nobody on the SEO or PPC team is usually watching what it finds and remembers. Different teams own different layers , and audits don’t cross over.

And, you only find out something is wrong when the email lands.

This piece covers what that hidden layer actually contains, how it manifests in ways that hurt performance, and what to look for when you’re already stuck.

### What The ‘Hidden’ Layer Actually Is

The hidden layer is Google’s internally generated data about your products – gathered over time and sometimes stitched together across sources.

When you submit a product feed , you’re telling Google: this product costs £169.99, it’s in stock, here’s the image. This is your truth, right now.

In comes the elephant.

Google also crawls your pages and revisits your feed over time, building its own running history. And that history keeps going long after you’ve changed the underlying reality on your side.

Then there is the truffle pig.

Google looks at your wider digital footprint on sites you don’t own, like an old product image still live on a marketplace listing. It may also extend to something even less visible: data that platforms exchange directly with each other behind the scenes.

All this is crunched, verified, and can be taken into consideration alongside whatever you’re currently submitting.

This is not some kind of clandestine agenda by Google. Ultimately, Google is just trying to keep an accurate, ongoing picture of your products, and the gap opens up when either side stops updating: You forget to tell Google something has changed, or Google’s own record hasn’t caught up yet. It’s not an easy task, on either end.

How Google finds and understands your data over time and sources is complex. There are so many layers to it.

Here we will discuss three components of the hidden layer I encountered during my work and in conversations with other practitioners in the field:

- Price Tracking: Google crawls your product pages, schema, and feed over time and builds a running price history of its own. If your schema labels, HTML copy, or historical feed prices imply a sale, even one that never existed as an explicit sale_price submission, Google’s price memory can corroborate those signals and surface an annotation nobody actually wanted.

- Image Indexing: Google indexes your product images, runs its own classifiers on them and applies flags or restrictions based on what it finds. Without a clean signal that an old image is gone, Google can keep using an old product image in your ads and free listings long after you’ve ‘swapped’ it on the website or even in the feed.

- Cross-Platform Data Exchange: While not publicly confirmed, we suspect major marketplaces share product feed data with each other (possibly via paid API access). A mistake in your Merchant Center (MC) feed can cause rejection in Google Ads and Amazon marketplace simultaneously.

See also: Why Product Feeds Shouldn’t Be The Most Ignored SEO System In Ecommerce

### Price Tracking

Many of us working in ecommerce have had an email come in asking why it looks like we are running a sale when we are not.

It’s easy for someone not involved in the day-to-day management of ads or SEO to be confused. Google has, so far, three distinct price-related features and it’s very easy to conflate them. They all look similar and they can all be bundled under this “sale” umbrella.

In reality, these are very different with completely different mechanisms behind them.

First we have Sale price annotations (or sales badges) .

These are the straightforward ones. You submit sale_price and sale_price_effective_date in your feed. Google validates the discount is between 5% and 90%, and that the original base price has been submitted for a qualifying period. In the UK, at least 30 days within the past 200 days. If you meet those conditions, the badge shows. It shows because you told it to and because the price history on record supports it.

The interesting element of sale price annotations is that Google doesn’t just read your current submission. It validates your base price against its own record of what you’ve submitted historically. Which is the first hint that Google’s price memory is doing more work than many of us realize.

Then we have Price drop annotations .

These are a very different beast than your run-of-the-mill sale price annotations. You can’t control price drop annotations. They are a result of Google crawling your page. Google compares your current submitted price against the average price it recorded for your product over the past 60 days and, if the drop is significant enough against a stable baseline, it automatically generates a “Price drop” badge with a “Was” reference price. You never actually submit the “Was” figure.

Lastly, there are the Price drop rich snippets . These are the organic search equivalent. To be eligible your Offer schema needs to have a specific price and not the AggregateOffer price with lowPrice and highPrice. But again, what Google actually displays doesn’t just come from your markup. As Brodie Clark, who first documented this feature in depth, noted: “It isn’t the site owner that is specifying this in the Structured Data. It is actually Google stepping in and adding what their historical records about the page have been for the price.”

Google’s own documentation treats these as separate features across separate help pages which is part of the confusion. But the practical consequences across all are the same: Google is holding a price history and surfacing them in ways that aren’t always visible inside the tools you use to manage your data.

Now let’s look at a use case.

You’ve probably seen annotations like the ones below in the wild. They make it look like the retailer is running a deliberate sale. On the face of it this looks like a Sale Price badge. It has a percentage decrease from the original price and not just a Price Drop label, commonly seen in price drop annotations.

Price drop & sale badges shopping results (Image from author, September 2026)

Google was displaying “Was £474, now £355” in Shopping and a sale price drop badge.

Yet, the client was adamant that no sale was running.

So, where did the “Was £474” come from?

First, we checked the current primary feed . The feed carried £355 – the ex-VAT price, with no sale_price attribute submitted. Not ideal since Google needs to infer VAT, but that’s a separate conversation.

While we were in MC, we checked the latest crawl data. The last page crawl returned £426, which is £355 inc-VAT.

Merchant Center “Information found on your site” panel output (Image from author, September 2026)

Then we looked at the live website and found the word “Now” in the price display!

Website HTML with Now included in the code (Image from author, September 2026)

When we checked the schema markup, we also saw the site used AggregateOffer with a priceSpecification array and two tiers – one tier labeled “List price” at £395, one labeled “Sale price” at £355.

AggregateOffer schema markup with priceSpecification array and Sale in the name (Image from author, September 2026)

That “List price” of £395 is where we found the mysterious “£474” price. £395 ex-VAT is £474 inc-VAT.

Since we had an older feed export on file, we checked what the feed price had been three months earlier to confirm. On April 15, the price field even carried £474.

Main MC feed export April 15 (Image from author, September 2026)

But, a sale_price attribute had never been submitted in the feed – in the current feed or the historical one.

The product had been repriced at some point. No one submitted a sale price in the feeds. Yet, Google assembled the sale narrative from three independent signals: a schema label it read as a sale indicator, page HTML it read as a current-price marker, and a price history it built from feed submissions over time. None of those signals individually said, “Run a sale badge.” Together, they did.

People forget. Systems don’t.

### Image Indexing

How website managers handle old product images varies company to company. It’s often one of those boring processes that slips between the cracks and yet can cause issues if not done properly.

Some retailers delete the image file from the server when retiring a product, which forces a 404 on the old URL and gives Google a clean signal to drop it from the index. Others do a periodic cleanup of orphaned images at scale. While there are also those who leave the image file live on the CDN indefinitely. The latter is the biggest issue, but a periodic cleanup is also problematic.

Without a 404, the image file is still publicly accessible at its original URL, which means Google can continue to surface it. Indefinitely or during the gap between cleanups.

Platforms handle this differently too. Shopify CDN URLs are permanent by design, and deleting a product doesn’t remove its images from the CDN. Magento stores images in a flat media directory, and unless someone manually purges the file, it stays live. WooCommerce uploads sit in the standard WordPress media library and are rarely cleaned up when products are retired.

The problem compounds when teams use image renaming conventions. A product gets a new lifestyle shot, the old filename stays on the server, and the new image is uploaded under a different name. Google has now indexed two image URLs for the same product and has to decide which one to associate, and it doesn’t always choose the current one.

Google maintains its own image index for your product images independently of what you’ve submitted in your feed’s g:image_link field or in any schema markup. When Google crawls a page, it finds the images on that page, stores them against that URL, and runs its own classification on them. That classification happens server-side. The results don’t appear anywhere in your feed or schema audits.

The elephant never forgets.

You find out about it only when a client comes to you and asks: Why do we have an old product picture appearing on this ad?

This is exactly what happened with our client.

We could clearly see the offending image in MC.

Merchant Center product attributes panel with image link (Image from author, September 2026)

So, we ran the usual checks. Looked at the images in assets, checked the feeds (primary and any supplemental), checked the rules, visited the website, checked the HTML and the schema.

And found nothing.

Only when we started thinking about indexing did we actually come close to figuring out what was going on.

Google had indexed the old image URLs from previous crawls. Updating the feed and the page HTML removed the submission-side signal, but Google’s independent image index still held the old association.

Without the 404, there was no way for Google to update the index, and for some reason it decided that this image was the best one to show as primary, regardless of the feed saying something different.

We discovered that the client had a purge cycle as their strategy to deal with old images. Obviously, this needed a process tweak since Google was catching old images between the cycle and using them in ads as the primary image for the ads and the free listing.

Things get even more complex when we pile on the truffle pig nature of Google. Its foraging can go well beyond your website and into places like other marketplaces and third-party websites.

A great example of this was shared with me by International Structured Data and Semantic SEO consultant Jarno van Driel during a recent catch-up (hope we will have many more of those since it was brilliant!).

One of his clients had spent months building out their feed, website, and schema correctly. Yet some of their best-selling products were consistently showing the wrong product image in search results, and nobody could work out why.

Until a simple filename search revealed the image on an Amazon product detail page that an employee had manually created two years earlier. The image was never updated and long since forgotten about.

Amazon is a huge brand with a lot of authority behind it. So in a way it makes sense why Google would think this image was important to surface.

But most ecommerce managers and SEOs won’t think to look there.

Which brings us to the last and possibly most interesting dimension of the hidden layer.

I haven’t encountered this directly in client work, but it’s consistent with everything else we know about how Google builds its product data picture.

### Cross-Platform Data Exchange

Everything we’ve covered so far has been about Google’s independently built data layer for your own products on your own site or Google selecting data it finds publicly available that you have at some point provided and maybe forgotten about.

But the hidden layer doesn’t necessarily stop at this.

During our call, Jarno van Driel mentioned a mechanism that most ecommerce practitioners have never considered.

Major marketplaces, Google, Amazon, and others, might be sharing feed data with each other – possibly via some kind of paid API access. At least for now.

“Big major marketplaces pay each other for API access to their product feeds,” he told me. “So what ends up happening is that when you’ve got a mistake in your Merchant Center feed, that follows through all the way. Then you can get ad campaigns in Amazon rejected, and ad campaigns in Merchant Center rejected. There’s so much cross-matching between all those different data sets.”

He encountered this directly. The investigation eventually led to a discrepancy between the Merchant Center feed and the Amazon feed.

These are two totally different data sources that, on the surface, had nothing to do with each other. And yet they were influencing each other with real impacts on the ad side.

Jarno is clear that there is no public documentation for the specific mechanism he describes. It comes from conversations with engineers rather than published policy. He also notes these are edge cases and don’t happen to many companies. But they do happen, and knowing about them makes a real difference in hours spent trying to figure this out.

I tried to find any public record of this arrangement and came up with nothing to confirm this.

I did find a publicly documented data-sharing agreement on a platform level in general between Google and Amazon. The Amazon MCF integration, announced by Google in 2024, means that Amazon can now provide fulfillment and shipping data directly to the Merchant Center to power delivery speed estimates in Shopping.

Obviously, that’s hardly the same thing, but it shows the infrastructure and commercial relationship between the two platforms exists.

Whether product feed data flows between them, we can’t know for sure, but it is not implausible and fits the wider pattern of this article and what we know about other platforms sharing APIs.

### When You’re Stuck

We shared three examples of when the hidden layer surfaced unexpectedly. Here’s how to investigate when it happens to you.

#### Price Layer Checks

The easiest place to start is in MC: Go to Products > All products , click into any individual product, and scroll to the bottom of the Product details tab.

The “Information found on your site” section shows you the price and availability Google last crawled from your page HTML, along with the date it checked. This is Google’s independent crawl record and not what you submitted via the feed. Check the price there.

If the crawled price differs from your feed price by exactly 20%, you almost certainly have a VAT mismatch: your feed submits ex-VAT, your page renders inc-VAT, and Google’s consistency check doesn’t know the difference.

If it differs by more, or matches a price you haven’t submitted in months, you might have a price history exposure that may be generating annotations you might not want.

You can often see all the products that have the different badges from the MC.

In your Products panel, just filter the below.

Merchant Center filtering by badge type (Image from author, September 2026)

It’s definitely a useful filter, although we found that sometimes the products don’t appear there. We didn’t see this client’s product there when we checked, even though it was displaying a price annotation in Shopping results.

Do a quick MC check, but whether you find the product or not, the main point is to check your data. Check your schema and the website (frontend AND code). If your schema mentions sale anywhere in the markup or your HTML has Sale/Now/Was mentioned, and you are not actually running a sale, change the label. It sounds trivial, but it’s contributing to how Google assembles its picture of your pricing.

Check your current feed, but also consider using a more permanent solution to keep a comparable history on file. For me, that’s likely going to be testing out a private repo on Git. We had the old feed on file this time by luck. Next time we’ll have it by design.

#### Image Layer Checks

When a client reports a wrong image appearing in Shopping or search results, check the campaign assets, the feed, and the live site, but then go further.

Dig deeper into the MC and find all the images Google actually has on file for that product. Take that URL, check the status code, and all the possible places it could be.

Search the filename in Google Images. If it appears on a third-party site, an old marketplace listing, or a page you’ve forgotten about that should actually be a 404, that’s likely the source. Google can pull image associations from anywhere it has crawled – your own domain or third-party sources.

This is why it’s important to not just find the image in question but to think about what this means for your operational processes. Think about how you currently manage your product images:

- What happens when an image is removed from the website front end?

- How are you currently auditing for orphaned images on a site level?

- What system are you using, and how does this impact how you should be managing this?

- How are you managing images across sources? Do you remove it just from your website, or do you check other third-party websites?

- How can this be improved, and who owns it?

#### Cross-Platform Checks

If you’re running on both Google and Amazon and experiencing disapprovals or performance anomalies that you can’t trace back to anything in your own feed or schema, it’s a good idea to pull both feed exports and put them next to each other.

Compare price, availability, title, and image URL for the affected products. You’re looking for any mismatch between what your MC feed says and what your Amazon says. These are two data sources that most ecommerce managers and SEOs treat as entirely separate. But they may not be after all.

Also, check the timestamps to see when your MC feed was last processed compared to your Amazon feed. If those dates differ, the two platforms may be working from different versions of the same product data even if you believe they’re in sync. Date-stamping your feed exports when you audit is such a small habit, and it can save you a ton of time and stress going down rabbit holes.

### Lastly, Actually Firstly: Deal With The Bigger Gap

Most ecommerce teams are already operating with a fragmented picture of their own product data. That’s before Google adds its independent layer on top.

The hidden layer doesn’t create this problem. It lands inside one that already exists.

SEOs aren’t logging into MC. The feed is treated as a PPC asset. Schema is treated as an SEO asset. The PPC manager optimizing the feed has often never looked at the structured data on the product page. The SEO auditing the schema has often never pulled a feed export. Development owns the page but answers to neither. Ecommerce operations manages the product catalog and the images but sits outside both channel conversations entirely.

I’ve written before about the general organization problem we have. There simply isn’t enough co-ownership between PPC and SEO teams . It still surprises me how many SEOs have never even logged into the MC!

Each team audits what they submitted. And because they’re auditing separately, nobody has a shared view of what Google is actually working with across all three layers – feed, schema, page. What I fondly call the unholy trinity of ecommerce.

Google itself is trying to reconcile all the layers it uses to manage ‘the truth’ about the products. For one, they’ve been wanting to unify schema.org markup and Merchant Center feed data into one consistent product data model.

Then there is the question of all the different knowledge graphs Google runs as the verification layer for both traditional and AI search. Two of which are key to ecommerce companies: Knowledge Graph and Shopping Graph.

The Shopping Graph alone now contains over 50 billion product listings, with more than 2 billion of those refreshed every hour. The data is pulled from a wide set of sources, including Merchant Center and Manufacturer Center feeds, but also YouTube videos, manufacturer websites, product detail pages, product testing data, and reviews.

This data is then cross-referenced against what Google understands about products, brands, and entities more broadly via the Knowledge Graph.

How conflicting signals are weighted and reconciled when they contradict each other across those layers is not publicly documented.

Meanwhile, new AI-led standards are ballooning and adding further complexity. Agentic commerce is no longer a future scenario. Google has already launched agentic checkout , where a shopper can set a target price, receive a price drop notification, and have Google autonomously complete the purchase on their behalf via Google Pay.

For that to work accurately at scale, Google needs a single authoritative truth about your product (the right price, image, availability…) pulled in real-time from everything it knows.

Right now that picture is assembled from multiple conflicting sources across teams that aren’t talking to each other. And, as autonomous buying becomes the norm, the cost of that fragmentation goes up significantly.

All of us working in this space – SEOs, PPC managers, developers, ecommerce operations – are ultimately working toward the same thing: a single, accurate, consistent picture of our products that every system can trust. Google is trying to build that from its end. The hidden layer is what happens in the gap while we catch up from ours.

More Resources:

- The Web Is Growing A Second Layer – Almost A Third Head

- The Technical Signals AI Search Uses That Most SEOs Still Aren’t Optimizing

- Stop Treating AI Visibility As One Problem. It’s Actually Three, On Three Different Layers

Featured Image: Roman Samborskyi/Shutterstock

Category Digital Marketing SEO Ecommerce

Read Full Bio

Emina Demiri-Watson Head of Digital Marketing at Vixen Digital

Emina Demiri-Watson is a digital marketing leader, strategist and speaker based in Brighton, UK. She currently serves as the Head ...

## 原文链接

[Read original](https://www.searchenginejournal.com/googles-hidden-data-layer-what-is-it-and-what-to-do-about-it/590234/)
