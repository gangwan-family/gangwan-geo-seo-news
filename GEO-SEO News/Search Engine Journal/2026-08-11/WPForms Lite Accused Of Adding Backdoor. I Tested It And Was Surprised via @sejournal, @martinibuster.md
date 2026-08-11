---
title: "WPForms Lite Accused Of Adding Backdoor. I Tested It And Was Surprised via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-11T09:03:14+00:00
fetched_at: 2026-08-11T22:10:16.282913+00:00
url: "https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/"
guid: "https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/"
author: "Roger Montti"
categories:
  - "News"
  - "WordPress"
---

# WPForms Lite Accused Of Adding Backdoor. I Tested It And Was Surprised via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-11
- URL: https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/
- Author: Roger Montti
- Categories: News, WordPress

## RSS 摘要

WPForms Lite WordPress plugin accused of adding a backdoor to new installs. I gave it and try and what happened was unexpected. The post WPForms Lite Accused Of Adding Backdoor. I Tested It And Was Surprised appeared first on Search Engine Journal .

## 原文正文

WPForms Lite Accused Of Adding Backdoor. I Tested It And Was Surprised Skip to content

🔥[Live 8/12 with Loren Baker] Ecommerce SEO : Own your "brand +promo code" search.

Register Now

- SEJ

- ⋅

- WordPress

## WPForms Lite Accused Of Adding Backdoor. I Tested It And Was Surprised

WPForms Lite WordPress plugin accused of adding a backdoor to new installations. I installed it and what happened was unexpected

A post on X posted by Sybre Waaijer (publisher of The SEO Framework plugin) recently stirred up a debate about the WPForms Lite WordPress plugin, alleging that it installs a backdoor on user’s websites. Some WordPress users agree that something unusual may be going on while others remain unconvinced.

The National Institute of Standards and Technology (NIST) defines a backdoor as:

“An undocumented way of gaining access to computer system. A backdoor is a potential security risk.”

### The Claim That WPForms Lite Inserts A Backdoor

Sybre Waaijer posted on X that a recent update to Awesome Motive’s WPForms Lite had inserted a backdoor into the plugin.

The claim is that WPForms Lite contains an onboarding wizard that walks a user through the configuration steps. The configuration wizard is alleged to issue a one-hour token that provides the makers of the plugin administrative access to the user’s website without first asking the user for permission or making it known that this is happening. According Waaijer, this access level enables Awesome Motive to do things like install and activate plugins.

Waaijer tweeted :

“Syed Balkhi (Awesome Motive) put a backdoor in WPForms Lite three weeks ago in version 2.0.0. The plugin runs on over 5 million sites.

The file: wpforms-lite/src/SetupWizard/Bridge.php.

What it does:

It takes over your browser and opens their app on WPForms’ servers. It hands that app a one-hour login token for your site. Their app can then act on your behalf on your site.

What they can do with it:

Their app can install and activate plugins. It can also turn on a switch that starts sending your form submissions to WPForms’ servers. The plugin never asks first and never warns you.

When it runs:

It kicks in automatically on a fresh install during setup, only for administrators. You won’t get a notice. The token expires at the end of setup, or after an hour.

What they can install:

Thirteen plugins from WordPress dot org: WP Mail SMTP, WPConsent, Uncanny Automator, AIOSEO, Universally, Duplicator, Reviews Feed, OptinMonster, MonsterInsights, ActiveLayer. Oddly (probably a bug), also Contact Form 7, Ninja Forms, and Pirate Forms.

They can also pull WPForms addons and WPForms Pro from their own servers. These servers are not moderated and could be used to push malicious code—which ought to be expected, given their track record.”

### Pushback From WordPress Community

One person responded that Awesome Motive is a trusted plugin developer and that this is something Waaijer should be discussing privately with them.

@BuildInBits tweeted :

“Awesome Motive has tons of plugins, and they are trusted plugins. For a decade, they have known how to do the work very well, and they are already on it. Your expression is a little unfair to go public like this.”

### Awesome Motive Is A Competitor To Waaijer

Waaijer’s response to @BuildInBitsse noted that Awesome Motive is a competitor, as both produce an SEO plugin. Awesome Motive publishes All In One SEO (AIOSEO) plugin which directly competes with Waaijer’s The SEO Framework.

Waaijer’s response :

“They deliberately built a second channel of admin power and dressed the .org zip up as Open Source while the real session and the package URLs live on their side.

For over a decade, WPBeginner has been the friendly face of that machine — tutorials that always somehow end at their own stack. Not a blog. A funnel.

For years, they’ve been cross-installing their plugins and deactivating their competitors’, including mine. I don’t respect them; they earned this.”

### Is It Really A Backdoor?

A backdoor is code that grants access by circumventing a site’s normal authentication and authorization checks, generally without the site owner’s knowledge, or as the NIST describes it, it’s an “undocumented way of gaining access to computer system.”

X user @marckranat challenged Waaijer’s backdoor characterization of the plugin’s onboarding functionality.

They wrote :

“”Backdoor” is doing a lot of rhetorical work here. It isn’t in the conventional sense. There’s no vendor-initiated access path, no auth bypass, and no hidden listener. It requires a logged-in administrator to actually trigger the wizard.”

@marckranat has a point that the vendor, Awesome Motive, likely cannot independently initiate access to a website that installs the plugin. That’s not what is happening when a user installs a the plugin.

### I Installed WPForms Lite. This Is What Happened

I already use the WPForms Lite plugin on one of my sites and decided to test it on another one. I installed it and was presented with a configuration wizard screen. I don’t recall clicking into the screen. Maybe that happened but I don’t recall that happening.

#### Screenshot of Welcome to WPForms page:

Now, here’s the thing, I thought I was still on my website. But I was already on another site.

#### Screenshot Of URL of Welcome Screen

This is the next screen:

#### Screenshot Of Configuration Wizard

I actually clicked Install and Continue, guess I wasn’t paying attention as I thought this was a part of the installation process. That’s on me, right?

#### Screenshot Of Select Your Features Screen

The screenshot shows that “AI Form Generation” and the “Privacy Compliance” boxes are ticked for installation and cannot be opted out. The “Accept Payments” box can be opted out of. At the bottom of the screen is a notice that the free “WPConsent” plugin will be installed, no way to opt out of that, either.

#### The Last Screen Of Setup Wizard

#### Screenshot Showing Three Plugins Installed

As you can see, WP Mail SMTP, WPConsent, and WPForms Lite were all installed. For most of these screens I had no idea that I was no longer on my site. I don’t recall seeing any notification that I was going to leave my site. I uninstalled the plugin and tried to reproduce the same workflow but it didn’t happen again.

### Takeaways

WPForms Lite does seem to send new users offsite for configuration in a way that I didn’t even realize I was on another site. Once you’re in the configuration wizard it obligates you to install two additional plugins because you cannot untick the boxes.

Sybre Waaijer says that the plugin drops a token that expires within an hour that enables WPForms Lite to make changes on the site, probably for importing data from other contact forms and also for installing those other plugins. That’s not a malicious purpose, it’s a reasonable and quite common with plugins. But it did feel weird to end up on another website without even knowing it.

Still, is it normal for a plugin’s setup wizard to take the user to another website? What do you have to say?

Featured Image by Shutterstock/Luis Molinero

Category News WordPress

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/)
