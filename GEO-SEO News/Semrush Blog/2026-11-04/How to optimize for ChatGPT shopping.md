---
title: "How to optimize for ChatGPT shopping"
source: "Semrush Blog"
published: 2026-11-04T10:36:00+00:00
fetched_at: 2026-11-05T01:33:38.238538+00:00
url: "https://www.semrush.com/blog/optimize-for-chatgpt-shopping/"
guid: "https://www.semrush.com/blog/optimize-for-chatgpt-shopping/"
author: "Zach Paruch"
categories:
  - "AI"
---

# How to optimize for ChatGPT shopping

- Source: Semrush Blog
- Published: 2026-11-04
- URL: https://www.semrush.com/blog/optimize-for-chatgpt-shopping/
- Author: Zach Paruch
- Categories: AI

## RSS 摘要

How to optimize for ChatGPT shopping: 83% of its carousel products also rank in Google‘s top 40 Shopping results.

## 原文正文

How to optimize for ChatGPT shopping

Find new opportunities across AI search and SEO.

AI search and SEO.

Try free for 7 days

Login Sign up

Outperform your search competitors. Search now spans Google, ChatGPT, and beyond—and Semrush gives you the SEO and AI visibility tools to stay visible everywhere:

See how AI platforms talk about you

Discover valuable topics to cover

Get AI-powered strategy suggestions

Build keyword plans with personalized insights

Identify fixes to improve technical health

Benchmark yourself against competitors

Try for Free

10M marketing professionals have already used Semrush

## How to optimize for ChatGPT shopping

Author : Zach Paruch

11 min read

November 4, 2026

Contributor: Faizan Ali

More than 1 billion people use ChatGPT every week to work, find information, and research products. OpenAI has also been building out how ChatGPT helps them find and buy products.

Ecommerce brands that know how to optimize for ChatGPT shopping can reach these shoppers when they evaluate a product and influence a purchase.

ChatGPT shopping changed in March 2026, when OpenAI stepped back from Instant Checkout, so merchants now use their own checkout and much of the older advice no longer applies. This guide covers how it works today and how to make your products more visible in ChatGPT, as part of your broader ecommerce AI SEO .

### What is ChatGPT shopping?

ChatGPT shopping is a feature that shows product recommendations in chat when a user asks a shopping query, like “Give me recommendations for best cat water fountain.”

The results appear in product cards with images, prices, and short descriptions.

ChatGPT may also add labels like “Budget-friendly” and summarize what reviewers like and dislike about each product.

OpenAI launched it in 2025 , announcing that ChatGPT would retrieve products from across the web and recommend them based on third-party structured metadata like pricing and reviews.

Months later, OpenAI also introduced the Instant Checkout feature. It let users purchase products without leaving ChatGPT. This was possible thanks to OpenAI’s Agentic Commerce Protocol (ACP), which sent the customer’s payment information to the merchant.

However, OpenAI moved away from supporting Instant Checkout in March 2026.

The official announcement cited a lack of flexibility as the reason and said the company would focus more on improving product discovery. As a result, OpenAI expanded the ACP so companies could share their products and promotions.

ChatGPT shopping is currently live only in the U.S., with plans to expand to other regions. Merchants can go further by building their own ChatGPT app, like Walmart did, which takes shoppers from ChatGPT into a Walmart experience with loyalty benefits and payments.

ChatGPT shows ads too, but you can't pay to appear in these results. OpenAI says shopping results aren't ads , and it labels ads and keeps them separate from its answers.

Your products can appear organically in ChatGPT shopping results in two ways.

Approved merchants can submit a product feed directly to OpenAI, which keeps details like pricing up to date in ChatGPT. Shopify and Etsy merchants don’t need to apply, since their product data is already integrated.

But you don’t need a feed to show up. ChatGPT pulls product data from multiple sources, including your website and third-party providers. So as long as OpenAI’s crawlers can access your site, your products can still appear in recommendations.

### How to list your products in ChatGPT

Before you optimize for better visibility in ChatGPT shopping, you need to have these foundations in place.

The technical requirements apply to every store. Applying for a merchant feed is optional, but it gives you more control over the way your products appear.

#### Meet the technical prerequisites

If OpenAI’s crawlers can’t access or read your product pages, ChatGPT can’t recommend your products. This is particularly important if you aren’t an approved merchant yet, since your website is a key source for ChatGPT to understand your products.

To meet the technical requirements, do the following:

- Implement server-side rendering: A 2024 Vercel test found that OpenAI’s crawlers don’t read JavaScript, and a 2026 experiment found that ChatGPT summarized only the raw HTML of a page when a user shared its URL. Check that price, stock, and key specs are in the HTML your server sends, not added by client-side scripts.

- Add product schema markup : ChatGPT uses structured metadata from first and third-party sources when deciding which products to recommend. At minimum, include the properties Google requires : the name, image URL, and the product offer. If you also submit a product feed to OpenAI, make sure your schema matches it.

- Check your robots.txt file : Make sure it doesn’t block the OAI-SearchBot that searches the web and surfaces webpages in responses. You can still block GPTBot to keep your content out of ChatGPT training.

- Check your Content Delivery Network (CDN) configurations: Some CDNs, like Cloudflare, allow users to block AI crawlers from accessing their website. Check that your firewall and bot rules allow OAI-SearchBot.

Check these prerequisites before you apply to OpenAI as a merchant. Issues with any of the above hurt your overall AI visibility , not just in ChatGPT shopping.

#### Apply to become a ChatGPT merchant

To connect your product feed with ChatGPT, first apply on OpenAI’s website .

You will need to provide your personal and company information, as well as your:

- Primary product categories, like pet care or beauty

- Product feed size, or the number of stock keeping units (SKUs)

The application also asks for confirmation that your product feed meets OpenAI’s specifications . We’ll cover this below.

After applying, you’ll be on an onboarding waitlist.

#### Submit a product feed to OpenAI

Once approved, share your product feed via the ACP with OpenAI.

You don’t need to build a custom integration. OpenAI accepts feeds over Secure File Transfer Protocol (SFTP) and through third-party providers like Salesforce and Stripe. So you can use the systems you already have.

It’s also possible to connect via file uploads or an API.

OpenAI recommends submitting your entire product feed once a day using file upload and using the API to share updates during the day.

If you have a smaller product feed, the API can support both daily uploads and updates. Any promotions data must be submitted via the API.

OpenAI’s product feed specifications require you to submit nine fields:

Field

Example

item_id

CAT-WATER-FOUNTAIN-STAINLESS-60

title

Stainless steel cat water fountain 60oz

description

Stainless steel water fountain for cats with 60oz capacity.

url

https://example.com/products/cat-water-fountain

brand

Pet Supply

seller_name

Pet Supply Webstore

image_url

https://example.com/images/cat-water-fountain.jpg

availability

in_stock , out_of_stock , pre_order , backorder , or unknown

price

49.99 USD

When submitting product titles and descriptions, keep the length to 150 and 5,000 characters, respectively.

Make sure your feed matches your product page. For example, OpenAI asks you to use the brand name as it appears on the page and, when possible, a URL that opens the specific product variant.

In addition to the required fields, there are optional fields you can also fill out for richer product context. We’ll cover this in the optimization section further down.

### How to optimize for ChatGPT shopping

After ensuring ChatGPT can get your product information, here’s how you can appear more often in its product recommendations:

#### Rank higher in Google Shopping

The products ChatGPT recommends often overlap with top Google Shopping results.

A Semrush experiment found that the top product ChatGPT recommended was featured in the top three Google Shopping results 75% of the time.

A March 2026 study from Peec AI also found that about 83% of products in ChatGPT carousel positions also appeared in the Google top 40 products. The study excluded paid ads, so this overlap comes from organic rankings only.

To optimize for Google Shopping, you need to submit high-quality product data to the Google Merchant Center feed. This includes both required and optional data to provide extra context, like material or color.

In addition, Google recommends merchants to:

- Check that free listings are on: They’re on by default for most stores, but confirm the status

- Write accurate titles: Describe the product clearly and match the title on your product page

- Add unique product identifiers: This includes Global Trade Item Numbers (GTIN) and Manufacturer Part Numbers (MPN)

- Upload more images: Use additional images to show the product from multiple angles or in use

- Fix feed errors: Check Diagnostics in the Merchant Center regularly

- Collect product reviews: Star ratings can appear on your free listings and drive more shopper interest

Google also suggests updating your product feed and website at the same time, so there are no data discrepancies.

#### Structure your product pages for extraction

Make it easy for OpenAI’s crawlers to extract information from your product pages.

The standard on-page SEO best practices and ecommerce SEO basics still apply. Use a clear heading hierarchy. The H1 should contain the main product name, like “Self-tanning lotion.” And use H2s for the “Product Description” or “User Reviews.”

In addition, display price and stock status as text on the page, and use HTML tables for product specifications rather than images.

AI crawlers primarily read text and code. So, don’t provide user reviews as just images or videos. Create a dedicated section where the reviews are in text format.

For example, Beauty By Earth’s self-tanner product page includes a video carousel with customer reviews.

Underneath the carousel, the page also provides written user reviews that OpenAI crawlers can read.

#### Deepen your product schema

On your website, add more structured data to your product pages. Google and OpenAI's crawlers read it when browsing your site, and it gives them labeled details like price, availability, and shipping to work with.

We suggest adding Google’s recommended properties , as this can help with your visibility in Google Shopping, which overlaps with ChatGPT’s product picks.

The recommended properties include:

- Reviews

- Material

- Color

- Description

- Shipping details

- Item condition

- Product return policy

- Product identifiers like GTIN

If you sell multiple versions of the same product, use the ProductGroup schema in addition to Product. It helps Google identify which products are unique versus a variant, and it saves you from repeating shared details, like the brand and description, on every variant.

#### Optimize your product data feed beyond the minimum

OpenAI requires merchants to provide nine fields containing basic product data. Go beyond the minimum and submit information like:

- condition: Whether the item is new, refurbished, or used.

- material: What the product is made from.

- dimensions: The product’s length, width, and height, plus the unit of measurement.

- age_group: Who the product is for: newborn, infant, toddler, kids, or adults.

- additional_image_urls: Extra photos of the product, like different angles.

- review_count and star_rating: The product’s total number of reviews and its average rating.

- accepts_returns and return_policy: Whether you accept returns, plus a link to your return policy.

Although OpenAI hasn’t confirmed that these optional fields result in more visibility, the extra context allows ChatGPT to suggest your products to the right user queries.

For example, it will more easily surface your products to a user looking for “new toddler shoes made from rubber” if that data is already in your product feed.

#### Write content that supports query fan-out

Query fan-out is a method ChatGPT uses to retrieve information.

It breaks a single user prompt into multiple sub-queries, then combines the information to provide the response.

OpenAI documentation only asks for “factual” descriptions in your product feed. On your website, however, provide rich product descriptions that align with fan-out queries.

For example, when we asked ChatGPT “what’s the best cat water fountain?”, one of the fan-out queries it generated was “best cat water fountain stainless steel,” even though our prompt didn’t mention the material.

Material is a common way to compare fountains, so it's worth answering on the page.

So in your product description, write something like: “Made from stainless steel, this cat water fountain doesn’t hold onto odors like plastic and comes apart easily for cleaning.” The conversational copy also better matches the way users write prompts.

Then answer the questions shoppers ask ChatGPT, such as:

- Use case : Does it suit a home with several cats, or a cat that doesn't drink much?

- Budget : What do you get at this price?

- Comparison : How does it differ from the fountains shoppers weigh it against?

Avoid vague marketing copy like “elegant water fountain all cats will love” because it gives ChatGPT little helpful information to take back to the user.

#### Build off-site trust signals

ChatGPT searches the internet to answer user queries, so your off-site presence is as important as on-site optimization. You need to be featured on review sites and authoritative industry publications.

Here’s an example.

If you sell cat water fountains, ChatGPT will use your product feed when suggesting your product. But what happens when the user asks: “Compare this water fountain to the Petlibro fountain”?

In this case, ChatGPT will likely visit websites that reviewed these products to get more information.

Below, it cited both Petlibro’s website and the FountainPaws review article.

If your brand isn’t present on these types of pages, or if the pages contain outdated information, it impacts the quality of information ChatGPT provides. This could ultimately sway users to purchase a competitor’s product.

Here are some ways to build trust signals:

- Encourage customers to leave detailed product reviews on Google, Trustpilot, Amazon, etc.

- Monitor journalist requests on platforms like Featured and respond to relevant opportunities, like product roundup posts

- Pitch publications that haven’t covered your product yet, or have covered it poorly

You can also start building off-site trust signals by finding your AI visibility gaps and focusing on getting featured on third-party pages cited in AI responses. Our guide to finding AI visibility gaps breaks this process down step-by-step.

### How to monitor your ChatGPT shopping performance

To monitor your ChatGPT shopping performance, set up the following:

- A fixed set of shopping prompts that you track on a schedule. Find them with Prompt Research in Semrush's AI Visibility Toolkit, then track them in Prompt Tracking with the platform set to ChatGPT Search.

- A filter in your website analytics platform to track referral visits from ChatGPT to your product pages

Referral traffic from ChatGPT might be tagged with “utm_source=chatgpt.com” or include an HTTP referrer.

But referrer data can be stripped depending on the user’s browser and recorded as direct traffic.

Also monitor direct traffic to product pages for any unusual growth patterns as they could indicate AI referrals.

Consider asking users who just completed a purchase how they discovered your product and offer ChatGPT as one of the options.

### How to keep up with ChatGPT shopping changes

ChatGPT shopping has already changed less than a year after launch, with OpenAI stepping back from Instant Checkout and shifting focus to product discovery.

It’s likely that more changes are on the horizon, especially as the feature expands outside the U.S. Google co-developed its own agentic commerce standard, the Universal Commerce Protocol, too. OpenAI also says it's building a merchant platform for self-serve data integration later in 2026.

Feed specs, portals, and checkout options will keep changing. What lasts is crawler access, accurate product data that matches your site, and trust signals from other sites.

To stay on top of future changes, check OpenAI's commerce documentation regularly, keep your feeds in sync with your website, and track your key prompts so you notice when your visibility drops.

Zach Paruch

Zach Paruch is a data-driven SEO strategist with 10+ years of experience driving organic growth through scalable search strategies. He specializes in on-page and technical SEO, content strategy, AI search optimization, and AI-driven processes.

Tells Google to show you more from Semrush in AI, Search, and Discover.

### Most popular pages

#### What Is Keyword Search Volume? (& How to Check It)

Keyword search volume is the average number of monthly searches for a search term in a particular location.

Keyword Research

Rachel Handley 3 min read January 10, 2025

#### How to Use Google Keyword Planner

Google Keyword Planner is a free tool that lets you research the queries people type into Google.

Keyword Research

Rachel Handley 7 min read July 23, 2024

#### How to Get Backlinks: 10 Realistic Methods

Learn how to get backlinks by responding to media requests, creating link bait, finding broken links, & more.

Link Building

Rachel Handley 10 min read October 17, 2024

## 原文链接

[Read original](https://www.semrush.com/blog/optimize-for-chatgpt-shopping/)
