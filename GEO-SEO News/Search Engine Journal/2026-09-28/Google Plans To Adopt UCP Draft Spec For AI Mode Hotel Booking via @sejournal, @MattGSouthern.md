---
title: "Google Plans To Adopt UCP Draft Spec For AI Mode Hotel Booking via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-28T13:44:16+00:00
fetched_at: 2026-09-29T01:05:54.844618+00:00
url: "https://www.searchenginejournal.com/google-plans-to-adopt-ucp-draft-spec-for-ai-mode-hotel-booking/591235/"
guid: "https://www.searchenginejournal.com/google-plans-to-adopt-ucp-draft-spec-for-ai-mode-hotel-booking/591235/"
author: "Matt G. Southern"
categories:
  - "AI Search"
  - "News"
---

# Google Plans To Adopt UCP Draft Spec For AI Mode Hotel Booking via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-28
- URL: https://www.searchenginejournal.com/google-plans-to-adopt-ucp-draft-spec-for-ai-mode-hotel-booking/591235/
- Author: Matt G. Southern
- Categories: AI Search, News

## RSS 摘要

UCP has published a draft hotel booking specification, Google says it will adopt the open standard for AI Mode hotel booking over the coming months. The post Google Plans To Adopt UCP Draft Spec For AI Mode Hotel Booking appeared first on Search Engine Journal .

## 原文正文

Google Plans To Adopt UCP Draft Spec For AI Mode Hotel Booking Skip to content

SEJ Pro Sign In

Webinar: A New Place To Look: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- AI Search

## Google Plans To Adopt UCP Draft Spec For AI Mode Hotel Booking

- UCP released a first draft of its Lodging Booking capability for public feedback.

- Google says it will adopt it for AI Mode hotel booking over the coming months.

- Google's docs say the business stays merchant of record and ranking isn't affected.

UCP has published a draft hotel booking specification, Google says it will adopt the open standard for AI Mode hotel booking over the coming months.

On Sept. 25, the Universal Commerce Protocol (UCP) project announced that a draft of its Lodging Booking feature has been added to the protocol’s GitHub repository. According to Google’s developer documentation , the company plans to adopt this standard for its hotel booking feature in AI Mode over the coming months.

Google began rolling out hotel booking in AI Mode for U.S. English users on August 27, working with 10 hotel chains and online travel platforms. The draft released on September 25 is the standard Google plans to adopt for this feature. It gives hotels and booking sites their first published glimpse at the new standard, and Google’s FAQ explains details about ranking, attribution, and who keeps the customer relationship.

### What The Lodging Spec Covers

The dev.ucp.lodging.booking specification describes how a platform manages booking sessions via REST or MCP, covering creation, updates, completion, or cancellation. The announcement lists features such as real-time pricing, availability checks, guest details, occupancy, check-in/check-out dates, and special requirements.

The draft ties into payment extensions like deposits, deferred balances, and split payments from the August 25 release , along with a new extension for cancellation policies . It also includes shared UCP components such as identity linking and payment handlers.

The spec says PCI DSS compliance isn’t necessary for card payments. Bookings have to be finalized by a person through a trusted interface, except when using UCP’s AP2 Mandates extension for agent-led payments.

Data models and bindings may evolve, with breaking changes possible, the draft banner warns. The Lodging Technical Council, comprising Amadeus, Booking.com, Expedia, Google, Hilton, Marriott, and Trip.com , is acknowledged in the announcement.

### How Google Plans To Use It

Google’s FAQ , updated Sept. 24, calls the first milestone booking and says:

“Over the coming months, Google will adopt this standard to power its hotel booking feature on AI Mode.”

The FAQ states that this milestone covers one room, with multiple rooms “potentially as a future extension.” The open spec’s data model allows a reservation to include one or more stay units.

The FAQ clarifies that choosing the booking integration “does not influence how we rank your properties or rates in listings.” However, entries with UCP integration get the direct booking option. The business acts as the merchant of record, keeping its own customer information and booking details, and its own terms and conditions govern the reservation.

Google highlights that lifecycle events shared via the API let a business see which traffic and payments came through Google’s AI surfaces rather than its own website or app. Also, before the final “Book” button appears, Google checks real-time price and availability via the partner’s API.

While businesses don’t need the Google Pay API on their site, their payment provider must support processing Google’s tokens. The FAQ mentions that AP2 can act as a payment layer within UCP for future agent-led transactions, though it stops short of calling it required. For now, Google’s UCP for Lodging page directs interested businesses to join a waitlist, with detailed onboarding instructions and specifications “coming soon.”

### How We Got Here

The Lodging Technical Council was set up on August 11 . UCP’s release on August 25 introduced the structure needed to expand beyond retail. In my update on August 31 , I shared that the lodging specifications were still in development, with no release timeline at that point.

Back in May at Google Marketing Live, Google connected hotel booking to UCP , but its August 27th launch post didn’t specify whether all integrated partners use the protocol.

### Why This Matters

UCP now offers a public booking contract for lodging, expanding from a council and structure a month ago. The draft explains how a platform and a hotel share information to make reservations, including details like rate plans, occupancy, payment schedules, and cancellation policies.

Google’s documents settle a few commercial questions for hotel and travel marketers. Joining the integration doesn’t change property ranking, and the business continues to act as the merchant of record. Plus, UCP reservations can be distinguished from direct bookings. The current documentation doesn’t yet offer options beyond the waitlist.

### Looking Ahead

The draft is open for feedback on GitHub . Neither Google’s FAQ nor its lodging page gives a date for the AI Mode switch or says which of the existing AI Mode booking partners will move to the standard.

Watch for a stable lodging release, Google opening onboarding, and additions to the booking spec, starting with the multi-room extension the FAQ calls a possibility.

Featured Image: MAYA LAB/Shutterstock

Category News AI Search

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-plans-to-adopt-ucp-draft-spec-for-ai-mode-hotel-booking/591235/)
