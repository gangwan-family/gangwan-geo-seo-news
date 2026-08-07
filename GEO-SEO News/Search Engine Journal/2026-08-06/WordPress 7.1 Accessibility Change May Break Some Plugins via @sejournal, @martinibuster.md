---
title: "WordPress 7.1 Accessibility Change May Break Some Plugins via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-06T13:10:41+00:00
fetched_at: 2026-08-07T01:03:13.764774+00:00
url: "https://www.searchenginejournal.com/wordpress-7-1-accessibility-change-may-break-some-plugins/584820/"
guid: "https://www.searchenginejournal.com/wordpress-7-1-accessibility-change-may-break-some-plugins/584820/"
author: "Roger Montti"
categories:
  - "News"
  - "WordPress"
---

# WordPress 7.1 Accessibility Change May Break Some Plugins via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-06
- URL: https://www.searchenginejournal.com/wordpress-7-1-accessibility-change-may-break-some-plugins/584820/
- Author: Roger Montti
- Categories: News, WordPress

## RSS 摘要

A WordPress 7.1 accessibility improvement could impact some plugins that make changes in the admin screens. The post WordPress 7.1 Accessibility Change May Break Some Plugins appeared first on Search Engine Journal .

## 原文正文

WordPress 7.1 Accessibility Change May Break Some Plugins Skip to content

🔥[Live 8/12 with Loren Baker] Ecommerce SEO : Own your "brand +promo code" search.

Register Now

- SEJ

- ⋅

- News

## WordPress 7.1 Accessibility Change May Break Some Plugins

WordPress 7.1, scheduled for release on August 19, is scheduled to ship with a change that improves accessibility but will cause a breaking change to the admin page for a small number of users. While it’s not likely to impact most users, plugin and theme developers may want to take notice of the change.

### What Is Changing?

WordPress 7.1 will ship with changes to the HTML structure of post list tables in the WordPress admin. The change affects the part of the admin screen that lists posts, pages, and custom post types.

These are the changes:

- The checkbox column changes from a row header <th> to a regular table cell <td>.

- The post-title column changes from a <td> to the row header <th scope=”row”>.

- The post-title row header receives an aria-label containing the post title.

- Collapsed table cells in the responsive view are being updated to use flex layout.

These changes will have no effect on themes that only contain public-facing markup. But there is a chance of breaking plugins or admin customizations that modify post list tables because of CSS and JavaScript that target specific <th> and <td> elements in WordPress admin post list tables.

### Why Is WordPress Making The Change?

This issue that’s being fixed has been an open bug for eleven years but WordPress core contributors finally closed it nine days ago

The problem it solves is that the row header should have a semantic label. Screen readers read each row using the checkbox text instead of the post title. Locked posts made this worse. When a post is locked, the lock icon has no label a screen reader can announce. So instead of hearing the post title, users heard the column header, “Select All,” a phrase that says nothing about the post in front of them.

One of the edge cases that the core trac ticket described mentioned how a “Select All” label creates a problem for WordPress users with screen readers because it does not describe what that column header is about.

WordPress core trac ticket #32892 describes one of the edge cases:

“One more good reason to address this issue is that, when a post is locked and the lock icon appears, the icon has no label or text that can be announced so screen readers will read out the column header “Select All”;”

WordPress core trac ticket #32892 describes the accessibility issue:

“In all the List Tables in the admin, the “Select %s” (where %s is the name of the Post, Attachment, Plugin, User, etc,) is used as row header:

<th scope=”row” class=”check-column”> This is not correct from a semantics and accessibility point of view for all the reasons mentioned in #31654. The row header should be the cell with the main object the table refers to: the Post title, the Plugin name, etc.”

### What Should Plugin Users Do?

Plugins that use CSS or JavaScript to target specific <th> or <td> elements in WordPress admin post list tables are the ones at risk.

You may be affected if you use a plugin that adds information or controls to WordPress admin post lists and relies on the existing <th> and <td> structure.

Review that plugin’s changelog once WordPress 7.1 rolls out. To do that, just Google the name of the plugin plus the keyword “changelog” in order to find the log of changes made to the plugin as well as information about compatibility. Most plugins test for compatibility. If the plugin is marked as compatible, update it before installing WordPress 7.1. If compatibility has not been confirmed, use a staging site to test whether the plugin breaks the WordPress 7.1 admin post list.

The three most popular SEO plugins, Yoast SEO, Rank Math, and All in One SEO, have functionality related to the admin post list, but they are unlikely to break. A review of their publicly available code found no selectors that appear to rely on the <th> and <td> structure changed in WordPress 7.1. That’s not a guarantee, though, so it’s prudent to check their website blogs and changelogs to make sure.

Even if a plugin breaks with WordPress 7.1, the change is unlikely to be an issue on the public-facing side of the website.

### What Should Plugin Developers Do?

WordPress software developers should already know to audit their software for changes. But there are many people nowadays who are vibe coding their own plugins so it’s important for non-developers who rely on AI to code their plugins to also audit any CSS or JavaScript selectors that specifically target <th> or <td> elements in WordPress admin post list tables, because those selectors may stop working when the element type changes in WordPress 7.1.

The official WordPress announcement offered the following before and after examples of how the code will change:

#### Code Before Change

<tr> <th scope="row" class="check-column"> <input type="checkbox" name="post[]" value="123"> </th> <td class="title column-title column-primary page-title"> <a class="row-title" href="...">Hello world!</a> </td> <td class="author column-author">admin</td> </tr>

The th is in the first column, followed by a td with the column title.

#### Code After Change

<tr> <td class="check-column"> <input type="checkbox" name="post[]" value="123"> </td> <th scope="row" class="title column-title column-primary page-title" aria-label="Hello world!"> <a class="row-title" href="...">Hello world!</a> </th> <td class="author column-author">admin</td> </tr>

The checkbox cell is changing from a <th> to a <td>, while the post title cell is changing from a <td> to a <th>. Because plugins may need to support both the old and new markup, developers should update their CSS and JavaScript to work with both versions of the code.

Featured Image by Shutterstock/Konstantin Kolosov

Category News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/wordpress-7-1-accessibility-change-may-break-some-plugins/584820/)
