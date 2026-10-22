---
title: "Google Images & Discover Previews Don’t Support JPEG XL via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-10-21T13:00:00+00:00
fetched_at: 2026-10-22T00:03:56.030283+00:00
url: "https://www.searchenginejournal.com/google-images-discover-previews-dont-support-jpeg-xl/593816/"
guid: "https://www.searchenginejournal.com/google-images-discover-previews-dont-support-jpeg-xl/593816/"
author: "Matt G. Southern"
categories:
  - "News"
  - "SEO"
---

# Google Images & Discover Previews Don’t Support JPEG XL via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-10-21
- URL: https://www.searchenginejournal.com/google-images-discover-previews-dont-support-jpeg-xl/593816/
- Author: Matt G. Southern
- Categories: News, SEO

## RSS 摘要

Chrome and Firefox now display JPEG XL, but Google says it isn't currently supported in Google Images or Discover previews. The post Google Images & Discover Previews Don’t Support JPEG XL appeared first on Search Engine Journal .

## 原文正文

Google Images & Discover Previews Don't Support JPEG XL Skip to content

SEJ Pro Sign In

Webinar: Will AI shopping agents recommend your top products?

Save Your Spot

- SEJ

- ⋅

- SEO

## Google Images & Discover Previews Don’t Support JPEG XL

- Google says JPEG XL isn't currently supported in Google Images or Discover previews.

- Chrome and Firefox now display JPEG XL, joining Safari.

- Mueller says a picture element with a supported img fallback would work for search engines.

Chrome and Firefox now display JPEG XL, but Google says it isn't currently supported in Google Images or Discover previews. Keep a supported fallback.

JPEG XL images aren’t currently supported in Google Images or as previews in Discover, Google Search Advocate John Mueller said on Bluesky .

His post came as browsers added the format. JPEG XL support arrived in Chrome 155 , which Google began rolling out widely on Oct. 6 after early releases to a small percentage of users starting Sept. 23. Firefox followed with Firefox 158 on Oct. 13.

In a reply, Mueller explained that serving JPEG XL through a picture element should work with any search engine, since the element includes a regular img element.

### What Mueller Said

Mueller posted on Oct. 15 in a thread regarding JPEG XL. The post contained Mueller’s link to the image SEO documentation of Google; Mueller also stated:

“FWIW if you’re hoping to get images shown in Google Images & as previews in Discover, etc – JPEG-XL is currently not supported”

Google Chrome developer advocate Barry Pollard responded with a message stating that it is good practice for developers to include fallback options for their websites because JPEG XL is new to both Chrome and Firefox. Pollard also asked if Search would be able to handle those fallbacks in a picture element.

Mueller answered:

“The picture element includes an img element, so that would work for any search engine (or other page parsing setup). I have not heard of any problems with people doing this kind of progressive enhancement”

### What Google’s Documentation Lists

Google’s image SEO best practices page carries the format list Mueller pointed to:

“Google Search supports images referenced in the src attribute of img in the following file formats: BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF.”

According to the same page, Google will be able to find images that are located within the src attribute of an img tag even if they’re contained by other tags such as the picture tag. Also according to the same page, it is recommended to include a fallback URL for the src attribute of the img element, as some browsers and crawlers do not support or cannot read picture or srcset.

In addition, Google’s list of file types it can index includes the same seven image formats listed above, but both pages did not mention JPEG XL. The image SEO page was most recently updated on March 2; there were no entries regarding JPEG XL in the Search Central documentation changelog as of Oct. 20.

Regarding Discover, Google’s recommendations include adding a larger size preview image using either schema.org markup or the og:image meta-tag; it states this can influence what image Discover displays as a thumbnail.

### Where Browser Support Stands

JPEG XL is supported in Safari beginning with version 17 in 2023.

The browser-support tracker webstatus.dev indicates that JPEG XL has a “limited” availability status, with no Edge release noted.

Chrome’s team says JPEG XL provides “30-50% better compression than JPEG” and lossless compression capabilities. In addition, they say it supports HDR. They recommend testing both AVIF and JPEG XL.

They believe that JPEG XL will have greater value for users requiring either lossless compression or higher fidelity images, particularly when compressing photographs.

AVIF was introduced into Search by Google approximately four years after it was first introduced into Chrome.

In August 2020, Chrome 85 was released with AVIF support. On Aug. 30, 2024, Google announced that AVIF was now supported by Search. That statement indicated that AVIF is currently being supported by every major web browser; according to webstatus.dev, the last of these was Edge, in January 2024.

### Why This Matters

An image that is a .jxl will show up in both Chrome and Firefox; yet, according to Google, Images and Discover do not currently support .jxl.

As long as you serve your JPEG XL image as a picture source (with your JPEG, WebP or AVIF as the img source) then one of Google’s listed formats will be in the “src” attribute of the img tag, which is where Google states their documentation shows they look for pictures. Also, you should make sure that your og:image and schema.org image links to a format from this list as well because these are the types of tags Google’s Discover guide recommends for preview images.

### Looking Ahead

Watch the format list on Google’s image SEO page and the Search Central blog, where Google announced AVIF support in 2024. Neither Mueller’s post nor the image SEO page gives a timeline for JPEG XL.

Featured Image: Koshiro K/Shutterstock

Category News SEO

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

Follow on YouTube. Matt G. Southern is the Senior News Writer at Search Engine Journal, where he’s covered Google, SEO, ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-images-discover-previews-dont-support-jpeg-xl/593816/)
