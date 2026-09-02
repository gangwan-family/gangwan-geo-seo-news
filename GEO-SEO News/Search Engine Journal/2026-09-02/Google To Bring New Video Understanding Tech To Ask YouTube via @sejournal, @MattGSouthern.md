---
title: "Google To Bring New Video Understanding Tech To Ask YouTube via @sejournal, @MattGSouthern"
source: "Search Engine Journal"
published: 2026-09-02T14:08:29+00:00
fetched_at: 2026-09-02T23:26:23.154190+00:00
url: "https://www.searchenginejournal.com/google-video-understanding-ask-youtube/588123/"
guid: "https://www.searchenginejournal.com/google-video-understanding-ask-youtube/588123/"
author: "Matt G. Southern"
categories:
  - "News"
  - "YouTube"
---

# Google To Bring New Video Understanding Tech To Ask YouTube via @sejournal, @MattGSouthern

- Source: Search Engine Journal
- Published: 2026-09-02
- URL: https://www.searchenginejournal.com/google-video-understanding-ask-youtube/588123/
- Author: Matt G. Southern
- Categories: News, YouTube

## RSS 摘要

Google says a new Gemini system that inspects frames, audio, and transcripts on demand will power Ask YouTube on video watch pages. The post Google To Bring New Video Understanding Tech To Ask YouTube appeared first on Search Engine Journal .

## 原文正文

Google To Bring New Video Understanding Tech To Ask YouTube Skip to content

AMA with Reddit Experts: what's working, and how to get into AI-cited threads. Exclusive for SEJ Pro members.

Save 20% with OGS20

- SEJ

- ⋅

- YouTube

## Google To Bring New Video Understanding Tech To Ask YouTube

- Google launched agentic video understanding for three Gemini Flash models through its API.

- It lets Gemini pick which frames, audio, or transcript sections to inspect.

- Google says the system will power Ask YouTube on watch pages in the coming months.

Google says a new Gemini system that inspects frames, audio, and transcripts on demand will power Ask YouTube on video watch pages.

Google is bringing a new video analysis feature to Ask YouTube that allows Gemini to focus on specific video segments for inspection, instead of sampling the entire video at a fixed rate.

Called agentic video understanding, the system will power Ask YouTube on the video watch page “in the coming months,” Google says , so the feature can answer from what’s shown on screen. It’s already accessible to developers via the Gemini API in Google AI Studio and the Gemini Enterprise Agent Platform, supporting both uploaded and YouTube videos.

### Coming To Ask YouTube

Google’s post says the watch-page version of Ask YouTube will get the new processing, “leveraging Gemini to deliver higher-quality answers grounded in the visuals.” The post doesn’t give a date beyond “the coming months” and doesn’t say which regions or languages will see it first.

The ask feature on the watch page appears as a button below videos, letting viewers get answers as they’re watching. This feature is separate from the version of Ask YouTube accessible through the search bar, which offers a summary with cited videos. I previously discussed that version in April , and Brooke Osmundson mentioned its I/O announcement in May. YouTube’s help page says it’s an experiment for a limited group of U.S. users searching in English and says it’s expanding to more users.

In July, Sundar Pichai shared during Alphabet’s Q2 earnings call that more than 140 million users engaged with the watch-page feature in June. He also said Google is bringing “that Ask experience to the wider search experience on YouTube.”

### How The New Processing Works

Gemini’s default video mode, called static processing, captures one frame per second and supplies each frame to the model, as detailed in Google’s API documentation . Developers can modify the frame rate, but the model still processes the full video.

Agentic video understanding uses a dynamic loop in which the model selectively loads parts of the video, adjusts the frame rate, and decides whether to include frames, audio, or transcripts for specific segments. According to Google, this method offers several benefits, such as locating split-second moments, searching multi-hour videos, spotting visual glitches, and counting repeated actions or objects.

Google reports that in its testing on standard video benchmarks, agentic video understanding reduces token usage by up to 88%, lowers analysis costs by up to 66%, and improves accuracy by up to 7% compared to static processing. The gains are largest with longer videos, though the API docs note the new mode may slightly slow the start of a response on clips shorter than five minutes.

### Why This Matters

Google’s update will change how the watch-page feature can inspect the video you’re currently watching. The post doesn’t say whether the search version of Ask YouTube will undergo the same processing.

Back in April, I noticed that YouTube hadn’t explained what makes a video the main citation in an Ask YouTube search response instead of a supporting one, or why it might be omitted. As of September 2, YouTube’s help page for the search version states that its ranking system “prioritizes relevance, engagement, and quality,” which they say is similar to the regular YouTube search. That’s as far as YouTube’s help pages go on selection, and the September 1 post offers no additional details. It also doesn’t address rankings, recommendations, citations, or creator tools, nor does it give any guidance on adapting videos for AI systems.

### Looking Ahead

Google’s timeline puts the new video mode in the Gemini app “soon” and in the watch-page feature “in the coming months,” though no exact dates are provided.

Monitor the watch-page help page for updates once the rollout starts. As of September 2, that page states responses are derived from YouTube and the web, but it doesn’t describe how the video itself gets analyzed.

Featured Image: Nwz/Shutterstock. YouTube logo: Source: YouTube.

Category News YouTube

Read Full Bio

SEJ STAFF Matt G. Southern Senior News Writer at Search Engine Journal

See short video versions of news stories on YouTube and TikTok. Matt G. Southern is the Senior News Writer at ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-video-understanding-ask-youtube/588123/)
