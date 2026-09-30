---
title: "EmDash 1.0 Challenges WordPress Freedom With Cloudflare Lock-In via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-09-29T12:17:17+00:00
fetched_at: 2026-09-30T00:37:08.848595+00:00
url: "https://www.searchenginejournal.com/emdash-1-0-challenges-wordpress-freedom-with-cloudflare-lock-in/591378/"
guid: "https://www.searchenginejournal.com/emdash-1-0-challenges-wordpress-freedom-with-cloudflare-lock-in/591378/"
author: "Roger Montti"
categories:
  - "CMS Software"
  - "News"
  - "WordPress"
---

# EmDash 1.0 Challenges WordPress Freedom With Cloudflare Lock-In via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-09-29
- URL: https://www.searchenginejournal.com/emdash-1-0-challenges-wordpress-freedom-with-cloudflare-lock-in/591378/
- Author: Roger Montti
- Categories: CMS Software, News, WordPress

## RSS 摘要

EmDash 1.0 trades WordPress's freedom of choice for heavy reliance on Cloudflare's infrastructure. The post EmDash 1.0 Challenges WordPress Freedom With Cloudflare Lock-In appeared first on Search Engine Journal .

## 原文正文

EmDash 1.0 Challenges WordPress Freedom With Cloudflare Lock-In Skip to content

SEJ Pro Sign In

Webinar: Where Your Next AI Citations & Clicks Come From

Register Now

- SEJ

- ⋅

- CMS Software

## EmDash 1.0 Challenges WordPress Freedom With Cloudflare Lock-In

EmDash 1.0 is a modern alternative to WordPress, but its features trap users into Cloudflare's infrastructure.

Cloudflare released the production ready version of EmDash, its “spiritual successor” to WordPress. The new CMS comes with EmDash Build, an AI-powered website builder that connects to an external AI model through Cloudflare’s infrastructure. Many of the EmDash features are more secure and flexible than what WordPress offers but they are also are tightly tied to Cloudflare’s infrastructure.

### EmDash 1.0

EmDash was originally announced as a beta (testing) version in April 2026. It is based on the open source Astro web framework that gives developers the ability to create static and high performing web pages that are highly secure.

Cloudflare provocatively named it the spiritual successor to WordPress because it is a modern revision of what a CMS can be, with AI tightly integrated into the builder workflow. Version 1.0 is a significant milestone because it is out of testing mode and is ready to be used on live websites.

### EmDash Build

A new feature of version 1.0 is the AI website builder called EmDash Build, which is powered by an external AI model through Cloudflare’s AI infrastructure. EmDash Build enables users to describe what they need, and the AI agent builds it.

The new builder creates server-rendered Astro pages, a database, media storage, and an admin interface. Its agent creates the content model, populates it through MCP, and can write pages. After the website is generated the website can be edited through EmDash.

There are four useful new features rolling out with EmDash version 1, all of which, like a lot of everything else with EmDash, binds users to Cloudflare’s infrastructure.

These four new and excellent features arose from lessons learned from using EmDash for the Cloudflare blog:

Hyperdrive database adapter

- Gives EmDash a more efficient way to connect to PostgreSQL databases when running on Cloudflare, improving database access for production sites.

Workers cache compatibility

- Enables EmDash to take advantage of Cloudflare’s caching infrastructure to improve response times and handle higher traffic with greater ease.

Per-project sandboxed build environments

- Every EmDash Build project runs in its own isolated Cloudflare Sandbox container. This gives the AI agent a separate workspace where it can build and check its work without affecting other projects.

Git commit tracking in EmDash Build

- Every change made by the AI builder is recorded as a Git commit through Cloudflare Artifacts, A Git-compatible versioned storage service. Commit tracking enables EmDash Build to create a history of what the agent changed, making the work easier to review, trace, and manage.

### Updated Plugin Registry

The official EmDash plugin registry can be reached at its own subdomain (plugins.emdashcms.com) although it’s also built to be decentralized. The registry itself is not new. What is new in 1.0 is its formal launch as part of the stable product.

The plugin registry uses the decentralized AT Protocol publishing model, which enables plugin developers publish plugin information to a shared network that EmDash can index instead of submitting it directly to a central EmDash-controlled database.

Cloudflare presents their plugin ecosystem as decentralized and without a gatekeeper, which is meant to be a contrast to the WordPress repository. Implicitly, it’s also a hard contrast to the abusive activities that can arise in a centrally controlled plugin repository, as recently happened in relation to actions taken by Matt Mullenweg against WP Engine when he locked WP Engine out of the WordPress repository, took over their plugins, and required users to verify they are not affiliated with WP Engine before allowing them to log into the WordPress infrastructure, including the repository.

Cloudflare’s announcement explains:

“A plugin registry that does not own the ecosystem

Traditional plugin registries usually combine three roles: they provide the publisher’s account, hold the authoritative package record, and operate the catalog where users discover it. That is convenient, but it also makes one company the gatekeeper for both identity and distribution. If an account is suspended, a listing is removed, the rules change, or the service shuts down, publishers cannot take the same identity and release history somewhere else.

EmDash separates the plugin from the catalog. Publishers retain control of their packages and release history, while EmDash provides a convenient place for people to find and install them. Other services can index the same publications, build their own catalogs, and apply their own policies without requiring developers to start again.”

Cloudflare represents the plugin repository as decentralized and without a gatekeeper but as with everything else about EmDash, the plugin registry is tightly bound to Cloudflare’s infrastructure. Cloudflare runs the repository on their own subdomain, Cloudflare controls it, and moderates the plugins seen it.

The documentation explains:

“The EmDash catalog applies default content moderation to the names, descriptions, links, and images it displays. Moderation can hide harmful or inappropriate material from this catalog, but it does not rewrite a release, take ownership of the plugin, or erase the underlying publication.”

EmDash’s plugin repository is not as free as Cloudflare represents it. Cloudflare is not an open source company and the repository is still under their control, despite the decentralized aspect of getting listed in it.

### Freedom: WordPress Versus EmDash

Cloudflare positions EmDash as a decentralized, free, and open source Content Management System, but it is tightly bound to Cloudflare’s infrastructure. Many of the features strongly rely on Cloudflare’s infrastructure and make it difficult to host an EmDash site without relying on Cloudflare.

It’s possible to host an EmDash website without Cloudflare by using a server environment that supports Node.js. But many of the Version 1.0 performance, AI-building, deployment, and other features depend on Cloudflare’s infrastructure, making it difficult to create an EmDash website using your own preferred hosting environment.

WordPress, on the other hand, is famous for true freedom of choice. All of the AI features in the EmDash announcement can already be achieved with WordPress. Virtually all of the EmDash 1.0 features rely on Cloudflare-specific infrastructure, whereas WordPress enables users to choose whatever infrastructure is suitable to them, including Cloudflare infrastructure.

EmDash is based on the good idea of building a CMS from scratch that can take advantage of modern technologies without the hindrance of legacy code. But Cloudflare arguably fumbles that mission by making it tightly bound to Cloudflare’s technology ecosystem.

This is very much a page out of Google’s method, where it offers technology for free with one hand while taking control of data and industries with the other, along the way creating a traffic and sustainability crisis in the very web ecosystem it claims to support.

There is a bigger picture here in which Cloudflare is becoming the infrastructure on which the entire Internet functions.

Featured Image by Shutterstock/solar22

Category CMS Software News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/emdash-1-0-challenges-wordpress-freedom-with-cloudflare-lock-in/591378/)
