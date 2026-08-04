---
layout: post
title: "WooCommerce Social Login WordPress Plugin Enables Full Site Takeover via @sejournal, @martinibuster"
date: 2026-08-03T23:26:39+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-08-03/WooCommerce Social Login WordPress Plugin Enables Full Site Takeover via @sejournal, @martinibuster.md"
original_url: "https://www.searchenginejournal.com/woocommerce-social-login-wordpress-plugin-enables-full-site-takeover/584601/"
author: "Roger Montti"
categories:
  - "News"
  - "WordPress"
  - "_src_search-engine-journal"
---

# WooCommerce Social Login WordPress Plugin Enables Full Site Takeover via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-03
- URL: https://www.searchenginejournal.com/woocommerce-social-login-wordpress-plugin-enables-full-site-takeover/584601/
- Author: Roger Montti
- Categories: News, WordPress

## RSS 摘要

WooCommerce Social Login vulnerability enables unauthenticated attackers to gain full control of ecommerce sites. The post WooCommerce Social Login WordPress Plugin Enables Full Site Takeover appeared first on Search Engine Journal .

## 原文正文

WooCommerce Social Login WordPress Plugin Enables Full Site Takeover Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- WordPress

## WooCommerce Social Login WordPress Plugin Enables Full Site Takeover

WooCommerce Social Login WordPress plugin enables unauthenticated attackers to gain complete control of ecommerce sites.

A critical vulnerability in the WooCommerce Social Login WordPress plugin enables unauthenticated attackers to log in as any existing user, including an administrator. The authentication bypass vulnerability is rated 9.8 out of 10 and affects all versions up to and including 2.8.7.

### WooCommerce Social Login Plugin

The WooCommerce Social Login plugin enables frictionless one-click login for ecommerce store customers and enables fast checkout using accounts from services such as Facebook, Google, Amazon, PayPal, and Apple.

### Unauthenticated Authentication Bypass

This vulnerability is especially concerning because attackers do not need to acquire any user permission role to exploit it.

The vulnerability affects the plugin’s Apple login handler, which processes the information received when someone signs in with an Apple account.

Apple provides an identity token containing information about the person attempting to log in. The token is protected by a digital signature that should be checked against Apple’s public keys to confirm that it is authentic. This is where the plugin fails, enabling attackers to provide the email address of an existing user and gain access to that account.

According to Wordfence :

“This makes it possible for unauthenticated attackers to log in as any existing WordPress user — including administrators — by supplying a forged id_token whose payload contains the target user’s email address, as that email is used without any role exclusion to resolve a WordPress account and immediately issue an authenticated session for it.”

Because administrator accounts are not excluded from this exploit, a successful attack could provide administrative access to the WooCommerce site that uses this plugin.

The vulnerability was assigned the Common Vulnerabilities and Exposures identifier CVE-2026-8457 and publicly disclosed on August 1, 2026.

Wordfence recommends that users of versions up to and including 2.8.7 should update to version 2.8.8 or higher version.

Featured Image by Shutterstock/file404

Category News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/woocommerce-social-login-wordpress-plugin-enables-full-site-takeover/584601/)
