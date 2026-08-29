---
title: "How To Add Google’s Preferred Sources Button To Your Website via @sejournal, @vahandev"
source: "Search Engine Journal"
published: 2026-08-28T19:00:53+00:00
fetched_at: 2026-08-29T03:12:57.517440+00:00
url: "https://www.searchenginejournal.com/add-google-preferred-sources-button-website/586908/"
guid: "https://www.searchenginejournal.com/add-google-preferred-sources-button-website/586908/"
author: "Vahan Petrosyan"
categories:
  - "SEO"
  - "Technical SEO"
  - "WordPress"
---

# How To Add Google’s Preferred Sources Button To Your Website via @sejournal, @vahandev

- Source: Search Engine Journal
- Published: 2026-08-28
- URL: https://www.searchenginejournal.com/add-google-preferred-sources-button-website/586908/
- Author: Vahan Petrosyan
- Categories: SEO, Technical SEO, WordPress

## RSS 摘要

Add Google's Preferred Sources button with the standard embed, a configurable WordPress widget, or a deeplink. The post How To Add Google’s Preferred Sources Button To Your Website appeared first on Search Engine Journal .

## 原文正文

How To Add Google's Preferred Sources Button To Your Website Skip to content

- SEJ

- ⋅

- SEO

## How To Add Google’s Preferred Sources Button To Your Website

Learn how to add Google's Preferred Sources button to a website, compare the embed and deeplink, and build a WordPress widget with light or dark themes.

Google’s new Preferred Sources embed removes one action from the process of adding a publication as a Preferred Source.

With the embed, a reader adds the site and returns to the article. A deeplink sends the reader to Google’s source preferences tool, where the site still has to be selected and confirmed.

This simple guide shows how to add the button to your website and provides WordPress widget code you can use.

### What Google’s Preferred Sources Feature Does

Preferred Sources affects what an individual Google user sees after selecting your publication. It does not improve your site’s rankings for everyone or guarantee that your articles will appear in Top Stories .

According to Google’s documentation , it is available globally for Top Stories in the languages where Google Search is available. Preferred sources can also be highlighted in AI Overviews and AI Mode where those experiences are available.

See also: Google’s Liz Reid: Personalization Can Help Small Publishers

### Check Eligibility Before You Add The Button

First, search for your publication in Google’s source preferences tool . If it does not appear there, adding the button will not solve the eligibility issue.

Google supports domains and subdomains, but not subdirectories. These are valid targets:

- example.com

- news.example.com

This is not a valid target:

- example.com/blog

If the publication lives on a subdomain, use that host rather than assuming the root domain is interchangeable.

### Add The Standard Preferred Sources Button

Google recommends its standard JavaScript implementation because it is localized automatically and returns the reader to the page where they started.

#### Standard Button Vs. Deeplink: What I Observed

I tested both routes on mobile. With the embedded button, Google opens a publication-specific confirmation page. The source is already identified, the reader taps Add , and Google returns them to the article. After the initial click on your website, it is a single-action flow.

The embed button opens a publication-specific page where the reader only needs to tap Add. (Image from author, August 2026)

The deeplink is different. It opens the general Source preferences screen with the publication search filled in, but the reader still has to select the publication’s checkbox. Google also does not automatically return them to the article. In practice, the embed removes one extra action, so it creates less friction.

Image from author, August 2026

The deeplink opens the general Source preferences page, where the reader still needs to select the publication.

This is why I would use the standard button on a website if it is possible. The deeplink still makes sense in email, social posts, or a CMS where the script cannot be added.

Load the library once from the application shell, theme, or a small site plugin, preferably in the document’s <head> :

<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>

Then place the button container where you want the control to appear:

<div google-add-preferred-source-btn></div>

The library detects the attribute and renders the interface. You do not need to hard-code the publication’s domain in the standard button.

#### Choose A Light Or Dark Theme

The light theme is the default. For a dark background, add the data-theme attribute:

<div google-add-preferred-source-btn data-theme="dark"></div>

Google’s Preferred Sources button in the default light theme. (Image from author, August 2026)

Google’s Preferred Sources button with the dark theme enabled. (Image from author, August 2026)

#### Override The Language Only When Necessary

The button uses the reader’s browser language by default. If a page requires a specific supported language, add data-lang :

<div google-add-preferred-source-btn data-lang="en"></div>

### Use The Deeplink When You Cannot Add JavaScript

The deeplink is an ordinary link, so you can add it through any CMS or HTML editor. It works without JavaScript.

https://www.google.com/preferences/source?q=example.com

You can add it as an ordinary link:

<p> <a href="https://www.google.com/preferences/source?q=example.com"> Add Example as a Preferred Source </a> </p>

The same URL can be used in page content, email, social posts, or promotions.

### Add The Button To WordPress

This example creates a WordPress widget that can be added to any widget area, such as an article sidebar or footer. The widget settings let an editor select Google’s Light or Dark color theme and align the button left, center, or right.

Add the code to a small custom plugin or a child theme’s functions.php file:

class Site_Preferred_Sources_Widget extends WP_Widget { public function __construct() { parent::__construct( 'site_preferred_sources', 'Google Preferred Sources', array( 'description' => 'Displays the Google Preferred Sources button.' ) ); } private function get_alignment( $value ) { return in_array( $value, array( 'left', 'center', 'right' ), true ) ? $value : 'center'; } public function widget( $args, $instance ) { $theme = isset( $instance['theme'] ) && 'dark' === $instance['theme'] ? 'dark' : 'light'; $alignment = $this->get_alignment( isset( $instance['alignment'] ) ? $instance['alignment'] : 'center' ); $justify_content = array( 'left' => 'flex-start', 'center' => 'center', 'right' => 'flex-end', ); echo $args['before_widget']; echo '<div style="display:flex;width:100%;justify-content:' . esc_attr( $justify_content[ $alignment ] ) . ';">'; echo '<div google-add-preferred-source-btn'; if ( 'dark' === $theme ) { echo ' data-theme="dark"'; } echo '></div>'; echo '</div>'; echo $args['after_widget']; } public function form( $instance ) { $theme = isset( $instance['theme'] ) && 'dark' === $instance['theme'] ? 'dark' : 'light'; $alignment = $this->get_alignment( isset( $instance['alignment'] ) ? $instance['alignment'] : 'center' ); ?> <p> <label for="<?php echo esc_attr( $this->get_field_id( 'theme' ) ); ?>"> <?php esc_html_e( 'Color theme' ); ?> </label> <select class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'theme' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'theme' ) ); ?>" > <option value="light" <?php selected( $theme, 'light' ); ?>>Light</option> <option value="dark" <?php selected( $theme, 'dark' ); ?>>Dark</option> </select> </p> <p> <label for="<?php echo esc_attr( $this->get_field_id( 'alignment' ) ); ?>"> <?php esc_html_e( 'Alignment' ); ?> </label> <select class="widefat" id="<?php echo esc_attr( $this->get_field_id( 'alignment' ) ); ?>" name="<?php echo esc_attr( $this->get_field_name( 'alignment' ) ); ?>" > <option value="left" <?php selected( $alignment, 'left' ); ?>>Left</option> <option value="center" <?php selected( $alignment, 'center' ); ?>>Center</option> <option value="right" <?php selected( $alignment, 'right' ); ?>>Right</option> </select> </p> <?php } public function update( $new_instance, $old_instance ) { $instance = array(); $instance['theme'] = isset( $new_instance['theme'] ) && 'dark' === $new_instance['theme'] ? 'dark' : 'light'; $instance['alignment'] = $this->get_alignment( isset( $new_instance['alignment'] ) ? sanitize_key( $new_instance['alignment'] ) : 'center' ); return $instance; } } function site_register_preferred_sources_widget() { register_widget( 'Site_Preferred_Sources_Widget' ); } add_action( 'widgets_init', 'site_register_preferred_sources_widget' ); function site_preferred_sources_widget_script() { if ( ! is_active_widget( false, false, 'site_preferred_sources', true ) ) { return; } wp_enqueue_script( 'google-preferred-sources', 'https://news.google.com/swg/js/v1/publisher.js', array(), null, array( 'strategy' => 'async', 'in_footer' => true, ) ); $tracking_script = <<<'JS' (function () { if ( window.__preferredSourceButtonTrackingBound ) { return; } window.__preferredSourceButtonTrackingBound = true; function isPreferredSourceClick( event ) { var path = typeof event.composedPath === 'function' ? event.composedPath() : []; for ( var i = 0; i < path.length; i += 1 ) { var node = path[i]; if ( node && node.nodeType === 1 && typeof node.hasAttribute === 'function' && node.hasAttribute( 'google-add-preferred-source-btn' ) ) { return true; } } return Boolean( event.target && typeof event.target.closest === 'function' && event.target.closest( '[google-add-preferred-source-btn]' ) ); } function hasGoogleTagManager() { if ( ! window.google_tag_manager ) { return false; } return Object.keys( window.google_tag_manager ).some( function ( key ) { return key.indexOf( 'GTM-' ) === 0; } ); } document.addEventListener( 'click', function ( event ) { if ( ! isPreferredSourceClick( event ) ) { return; } if ( hasGoogleTagManager() && Array.isArray( window.dataLayer ) ) { window.dataLayer.push( { event: 'preferred_source_button_click' } ); return; } if ( typeof window.gtag === 'function' ) { window.gtag( 'event', 'preferred_source_button_click' ); } }, true ); }()); JS; wp_add_inline_script( 'google-preferred-sources', $tracking_script, 'after' ); } add_action( 'wp_enqueue_scripts', 'site_preferred_sources_widget_script' );

After adding the code, open Appearance > Widgets, add Google Preferred Sources to the sidebar or footer, then choose the color theme and alignment. WordPress loads the library once even if the widget is used in more than one widget area.

#### Track Preferred Sources Button Clicks In GA4

The widget uses one delegated click listener because Google renders the badge after the page loads. It records a click that starts the Preferred Sources flow; it does not confirm that the reader completed the selection in Google.

If a Google Tag Manager container is present, the listener pushes one event to the default dataLayer :

window.dataLayer.push( { event: 'preferred_source_button_click' } );

In GTM, create a Custom Event trigger named preferred_source_button_click . Use it to fire a GA4 Event tag with the same event name.

If GTM is not detected but gtag.js is installed, the listener uses Google’s gtag.js event command instead:

window.gtag( 'event', 'preferred_source_button_click' );

Use GTM Preview or GA4 DebugView to confirm the event once before publishing the change. You can also use this event as a KPI in your SEO reporting.

### In Summary

Preferred Sources is not a direct ranking factor, but it can increase repeat visibility among readers who explicitly choose your publication. That gives publishers a practical way to build a returning audience in Top Stories and, where available, AI Overviews and AI Mode.

The SEO benefit is not a universal ranking boost. It is the chance to earn more visibility with the readers who already value your work.

More Resources:

- Preferred Sources & AI Mode Are Creating Filter Bubbles – A New Discovery Problem

- Google Preferred Sources Hit 345K, Expand Into AI Search

- Google’s Preferred Sources Is Now A Global SEO Signal

Featured Image: Vahan Petrosyan/Search Engine Journal

Category SEO Technical SEO WordPress

Read Full Bio

SEJ STAFF Vahan Petrosyan Director of Technology at Search Engine Journal

As Director of Technology at Search Engine Journal, I lead the organization’s technology strategy and technical operations. I oversee technical ...

## 原文链接

[Read original](https://www.searchenginejournal.com/add-google-preferred-sources-button-website/586908/)
