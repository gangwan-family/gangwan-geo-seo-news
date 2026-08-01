---
layout: post
title: "How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers) via @sejournal, @suganthan"
date: 2026-07-29T12:01:39+00:00
source: "Search Engine Journal"
source_slug: "search-engine-journal"
generated_from: "GEO-SEO News/Search Engine Journal/2026-07-29/How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers) via @sejournal, @suganthan.md"
original_url: "https://www.searchenginejournal.com/how-perplexity-actually-picks-sources-i-read-the-stream-not-the-answers/583769/"
author: "Suganthan Mohanadasan"
categories:
  - "Generative AI"
  - "SEO"
  - "_src_search-engine-journal"
---

# How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers) via @sejournal, @suganthan

- Source: Search Engine Journal
- Published: 2026-07-29
- URL: https://www.searchenginejournal.com/how-perplexity-actually-picks-sources-i-read-the-stream-not-the-answers/583769/
- Author: Suganthan Mohanadasan
- Categories: Generative AI, SEO

## RSS 摘要

Perplexity never skips the web, so every query is winnable. Here's what its live answer stream reveals about citations, video, and local. The post How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers) appeared first on Search Engine Journal .

## 原文正文

How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers) Skip to content

🔥 SEJ Pro Course: Own Your Brand’s Promo Code & Coupon Search Results Before Parasites Do

REGISTER NOW

- SEJ

- ⋅

- Generative AI

## How Perplexity Actually Picks Sources (I Read The Stream, Not The Answers)

I read Perplexity's raw answer stream to see how it picks sources, which domains get cited by intent, and how to show up in and get cited by Perplexity.

I promised this one at the end of the ChatGPT teardown . I’ve since had to go back to ChatGPT again in a follow-up because it moved under me while the post was still fresh. Perplexity was next, so here it is.

The question hasn’t changed, only the logo. “ How do I show up in Perplexity? ”

And the answer comes back just as vague. Be a credible source, get cited , go do Reddit. Same play, different engine.

So I did the same thing I did to ChatGPT.

I read what Perplexity streams to my browser underneath the answer, on my own logged-in Pro account, while the reply was still rendering.

One difference up front, because it sets the tone for the rest of the article.

With ChatGPT, you can pull the finished conversation back from its API and read it at your leisure.

Perplexity doesn’t let you.

The answer is a live stream that’s gone the moment it finishes, and trying to re-fetch it just throws an error. So I hooked window.fetch before hitting enter and teed the stream as it arrived.

Before you quote a number from this, read this. It’s one person, one logged-in Perplexity Pro account, build 7fe6ad4 , captured on 25 June 2026. 8 captures in all, 7 query types (informational, commercial, comparison, news, local, shopping, how-to) plus one Deep Research run. Single user, Dubai geo. The structural findings, the fields Perplexity uses and how they behave, are firm, because you only need to see a field once to know it’s real. The numbers, any percentage or ranking or “YouTube wins”, come from that tiny single-user sample and my own SaaS, tech and local query choice skews them. Treat those as direction, not measurement. I flag which is which throughout. One more date for the record. Before publishing I re-ran 3 spot-check captures on 21 July 2026, build df49f17 , roughly four weeks and several builds after the originals. The structure held except where I say otherwise in the body, and one thing changed enough to earn its own section, the trust field.

### How To Rank In Perplexity On 1 Screen

Every row is unpacked with the evidence further down. The right column is the move.

What The Wire Shows

The GEO/AI SEO Move

A 16-head classifier routes every query, with fixed thresholds and a topic label.

Read which surface your money queries trigger (maps, video, image, finance) and compete there, not just in blue links.

Web results can carry a written trust note, credible or trusted, scoped per domain.

Become the unambiguous first-party source for your patch, then check whether your domain carries an entry.

skip_search is always false, and how-tos escalate to Study mode with a video tab.

Every query is winnable here, and instructional content gets a page slot plus a video slot.

The default fan-out is 1 round of conservative variants on your literal phrasing.

Optimize for the exact words people type, not a cloud of adjacent topics.

Retrieved and cited are different lists, and the winners flip by intent.

Fresh “best X, current year” listicles for commercial, your own vs page for comparisons, your changelog for news.

YouTube gets cited heavily while Reddit gets retrieved and ignored.

Make the video, because the ChatGPT Reddit playbook doesn’t transfer.

Local citations go to place-entities when the maps index binds.

Google Business Profile and place indexing first, listicle presence as the fallback.

Deep Research reads 2 to 4 pages in full and they dominate the citations.

Be the most comprehensive page on the topic, because the snippet won’t save you there.

### 2 Confidence Levels, Same Rule As Last Time

If you read the ChatGPT piece you know the drill.

I split everything into two piles and I don’t let them touch.

Structural facts (high confidence). A field exists and this is what it’s named, read straight off the wire. The classifier scorecard. The step log. The meta_data.client channel. The trust scope notes. Study-mode escalation. The privacy defaults. One clean capture proves each of these, and a prompt study, however big, can’t see any of them, because they never reach the answer.

Frequency observations (directional only). Anything with a number. “6 of 7 queries ran a single search,” “YouTube got cited 38 times,” “the listicles got nothing,” That’s a handful of data points on one account, in one city, on the queries I happened to pick. Read it as the shape, not the measurement. Where a direction has a mechanical reason behind it, like Perplexity quoting a video so YouTube earns the citation, trust the direction and ignore the exact count.

### The Boring Bit: Why This Is Harder Than ChatGPT

Skip this if you don’t care how the sausage gets made.

Perplexity’s answer arrives as a Server-Sent-Events stream, a POST to /rest/sse/perplexity_ask with content-type: text/event-stream . The catch is that a finished SSE body isn’t replayable. Once it’s done, it’s done, and asking for it again gets you an aborted request rather than the text. The stream only exists while it’s streaming.

That’s why the hook has to go in before you submit. You override window.fetch , clone the response, and read the clone as it comes in. The stream itself is a run of progressive full-state snapshots, each event a near-complete copy of the growing answer object, so by the end a single answer has buffered to about 1 MB across 200-plus events. The richest payload is the largest data: block near the end. You parse that, not the terminal done marker.

Two dead ends, so you don’t repeat them. An isolated automated Chrome gets hard-walled by Cloudflare within a few queries; the “verifying you’re human” loop just spins forever, so use your real Chrome with your real session. And the keepalive ping streams are also event-streams that never close, so don’t sit waiting on the wrong one for a “done” flag that never flips. Target the snapshot that actually carries a classifier_results field.

I went down the Wireshark hole first, same as the ChatGPT post, and gave up for the same reason. The bodies are TLS encrypted on the wire. The readable layer is the browser, after decryption. (I know, I know lol.)

A July addition to the dead-end list. On the current build, the answer socket doesn’t close when the answer finishes; it just goes quiet and stays open, so a script that waits for the stream to end waits forever. That’s what quietly killed the first version of my capture script between June and July. The one further down reads the stream as it arrives instead.

### Perplexity Hands You Its Router

This is the part that doesn’t exist in ChatGPT, and it’s the best thing in the whole capture.

Before Perplexity searches, it runs your query through a classifier, and it ships the entire scorecard to your browser in a field called classifier_results.mhe_predictions_full . Not the decision. The whole working-out.

There are sixteen heads. Each one is a possible widget or intent, weather, places, shopping, video, image generation, a finance card, and so on. Each carries a probability, a fixed threshold it has to clear to fire, and a true/false. On top sits a domain_subdomain label, Perplexity’s topic taxonomy for the query.

Image Credit: Suganthan Mohanadasan

Here’s the scorecard for “explain the TLS handshake like I’m five,” trimmed to the interesting heads.

{ "domain_subdomain": { "label": "TECHNOLOGY/CYBERSECURITY", "probability": 0.727 }, "image_preview": { "probability": 0.318, "threshold": 0.42, "is_true": false }, "video_preview": { "probability": 0.073, "threshold": 0.50, "is_true": false }, "places_search_intent": { "probability": 0.044, "threshold": 0.85, "is_true": false }, "shopping_intent": { "probability": 0.0002, "threshold": 0.80, "is_true": false }, "image_generation_intent": { "probability": 0.002, "threshold": 0.98, "is_true": false }, "skip_personal_search": { "probability": 1.0, "threshold": 0.95, "is_true": true } }

Read that, and you can watch the machine think.

The query got filed under TECHNOLOGY/CYBERSECURITY at 0.73 confidence. Every widget head came back well under its bar, so none fired. image_preview reached 0.318 against a 0.42 threshold, the closest miss, which is why an image strip nearly showed up and didn’t.

ChatGPT showed me one label per query, the turn_use_case bucket, and that was the end of it.

Perplexity shows the probability and the bar for every surface it could have triggered, on every single query. That’s a lot more of the routing logic than I expected to see exposed.

The thresholds don’t move. They were identical across all 7 queries in June, and identical again on a different build 26 days later, so this is the real decision boundary, not a per-query mood.

Widget/Intent Head

Threshold To Fire

image_generation

0.98

skip_personal_search

0.95

places_search_intent

0.85

shopping_intent

0.80

time_widget

0.80

finance_agent

0.70

finance_widget

0.53

video_preview

0.50

image_preview

0.42

weather_widget

0.40

calculator_widget

0.30

The domain label moved with the query, exactly as you’d hope.

“best AI SEO tools 2026” came in as TECHNOLOGY/ARTIFICIAL_INTELLIGENCE at 0.86.

“Ahrefs vs Semrush” got BUSINESS/DIGITAL_MARKETING at 0.94, the most confident call in the run.

The news query, “latest Google algorithm update,” scored the lowest, TECHNOLOGY/INTERNET_TECHNOLOGIES at 0.49, because news resists a single tidy topic.

#### The AI SEO/GEO Takeaway

Map your priority queries to their domain label and the head most likely to fire, because that tells you which surface you’re actually competing for. A “best X near me” query is going to clear the places threshold and put you in a maps fight, not a blue-links fight. A how-to is going to pull a video tab. You can stop guessing which game you’re playing and read it off the classifier.

### It Tells You Which Domains It Trusts, And For What

In the June captures, there was no trust signal anywhere in the stream. An even earlier free-tier capture had carried a trust field on every source, sitting empty, and build 7fe6ad4 dropped the field entirely.

I’d written the negative up for this article: no per-source quality signal reaches the browser; source ranking is server-side and invisible.

Then I re-ran the captures on July 21, build df49f17 , and the field is back. With values in it.

"trust": { "level": 1, "name": "credible", "description": "is credible for first-party information about Discount Tire's U.S. tire and wheel retail stores, services, warranties, and related offerings." }

That’s a real entry from the flat-tyre capture, attached to discounttire.com. Sources on the current build can carry a trust object with a numeric level, a tier name, and a written scope.

I saw two tiers in my captures, level 1 credible and level 2 trusted , the second sitting on goodyear.eu, “trusted for official Goodyear tyre product information” and on into its EMEA and fleet business.

The description is the interesting part. It’s a sentence about what the domain can be believed on, not a score. caranddriver.com is credible for “long-established, professionally edited” automotive coverage. aaa.com is credible for “official information about AAA’s own membership services.”

Every entry I captured has that same first-party shape. A domain is trusted about its own products, services, and patch, not trusted in general.

Image Credit: Suganthan Mohanadasan

Coverage tells its own story. On the how-to run, six of 15 sources carried a trust entry, and they were the big official domains, the RAC, AAA, Goodyear, Car and Driver. The six YouTube results carried nothing, and neither did any of the 15 sources on my local run, which were all small editorial sites.

Two queries is a directional sample, but the shape looks like a curated registry being rolled out from the head of the web downwards, not a score computed for every URL on demand.

Before you build a strategy on it, two caveats. A missing entry clearly doesn’t keep you out of the answer, because YouTube had no trust object and still took 14 of the 40 citations on that query.

And this exact field has gone from present-but-empty to absent to populated across three builds in about two months, so treat the tier names and the wording as a snapshot of a system mid-rollout, not a stable API.

#### The AI SEO/GEO Takeaway

Perplexity is writing scoped, first-party trust notes on domains, so the winning question stops being “how do I look authoritative” and becomes “what’s my domain the unambiguous first-party source for.” Make that thing legible: your products, your data, your services, your changelog, because the scope sentences describe what a domain owns, not how big it is. And run the capture script below on your own money queries to see whether your domain carries an entry yet.

### It Never Skips The Web

The single most useful finding in the ChatGPT teardown was the text bucket, the discovery that ChatGPT answers how-to and definition queries straight from training and never searches at all. If your query gets filed as text , no page on earth gets in, because no page gets fetched.

Perplexity doesn’t do that. skip_search was false on all 7 queries. Every one hit the web, including “how do I change a flat tyre step by step,” the exact query ChatGPT answered from memory with an empty network tab.

What Perplexity does instead is quietly change mode.

The flat-tyre query didn’t run as a normal search. It escalated to Study mode, model: pplx_study , search_mode: STUDY , Perplexity’s step-by-step teaching mode, and it fired a video answer tab on top. Same silent-escalation instinct as ChatGPT, opposite outcome. ChatGPT decided it already knew and shut the door.

Perplexity decided to teach you and opened a video. (I re-ran this exact query on the July build. Same escalation, same video tab, video head at 0.988.)

Image Credit: Suganthan Mohanadasan

#### The AI SEO/GEO Takeaway

In Perplexity, every query is contestable, because it always fetches. That’s a structural advantage over ChatGPT for anyone making instructional or definitional content.

In ChatGPT, a how-to can be a closed box you can’t get into at any price. In Perplexity, that same how-to is a live search with a video tab attached, so there’s a page slot and a video slot to win.

### The Fan-Out Is Shallow By Default, Deep Only When It Has To Be

Perplexity writes the searches it runs into the stream too, as a step log in final.text . It reads like a little program.

INITIAL_QUERY → SEARCH_WEB { engine: web, query: "...", limit: 8 } → SEARCH_RESULTS → FINAL

For six of my seven queries, that’s the whole sequence. It ran a single SEARCH_WEB step with the query near-verbatim, then answered. “best AI SEO tools 2026” went to the web as best AI SEO tools 2026 and came back with 10 results. “Ahrefs vs Semrush” went out as Ahrefs vs Semrush , untouched. It didn’t expand the query or chase tangents.

Set that against ChatGPT. It rewrote my queries and injected brand names it already knew, turning one comparison into roughly 40 sub-queries and chasing tools I’d never mentioned.

Perplexity searched the literal string I typed. It retrieves what matches your actual phrasing, not what it can dream up around it.

The one exception was local. “best specialty coffee shops near DIFC Dubai” ran 4 searches across 2 rounds, and round 2 went hunting for specific businesses by name.

That’s genuine entity discovery, and it was the only query in the set that did it. I’ll come back to it, because the result is the sharpest GEO finding in the whole capture.

A July footnote on the fan-out. When I re-ran the commercial query on build df49f17 , the single step carried three queries instead of one: the verbatim string plus two close variants, and one of them was “AI SEO tools Dubai pricing.” My city, folded straight into the expansion. So the fan-out has widened a touch since June, and it’s personalized. It’s still a different sport from ChatGPT’s 40-query brand injection; the head query stays your literal phrasing, but “barely rewrites” is drifting toward “rewrites conservatively.”

Image Credit: Suganthan Mohanadasan

#### The AI SEO/GEO Takeaway

Optimize for the literal query, because Perplexity leads with your exact phrasing, expands it only conservatively, and won’t invent its way to you. ChatGPT’s habit of expanding a query gives a tangential page a chance to get pulled in.

Perplexity doesn’t hand you that. Exact-match relevance to the phrasing real people type matters more here than it does in ChatGPT, and the deep multi-query fan-out you might be hoping for is a Deep Research behavior, not default search.

### Retrieved Isn’t Cited, And The Pattern Changes With Intent

Two things happen to a source, and they’re not the same thing. Retrieved means it came back in web_results , Perplexity pulled it into the candidate set. Cited means it earned an inline [N] marker in the answer, the clickable footnote.

Plenty of pages get retrieved and never cited . That gap is where the GEO/AI SEO lives.

Here’s the whole set at a glance.

Query

Domain Label @ confidence

Searches

Retrieved

Cited

Extra Surface

informational (TLS handshake)

TECHNOLOGY/CYBERSECURITY 0.73

n/a

Image

commercial (best AI SEO tools 2026)

TECH/ARTIFICIAL_INTELLIGENCE 0.86

Image

comparison (Ahrefs vs Semrush)

BUSINESS/DIGITAL_MARKETING 0.94

Image

news (latest Google algorithm update)

TECH/INTERNET_TECHNOLOGIES 0.49

Image

local (coffee near DIFC)

FOOD/RESTAURANT_RECS 0.66

Maps

shopping (earbuds under $150)

CONSUMER_GOODS/AUDIO 1.00

Image

how-to (change a flat tyre)

CONSUMER_GOODS/AUTOMOTIVE 0.91

Video

Now the per-intent patterns, each with the bit you can act on.

Commercial, “best X 2026.” It retrieved 10 and cited six. The winners were fresh current-year listicles and mid-tier SEO blogs, onelittleweb, eesel.ai, vezadigital, manysphere. The big brand pages, semrush and designrush, were retrieved and never cited.

onelittleweb.com 36 cited eesel.ai 34 cited vezadigital.com 24 cited seranking.com 16 cited manysphere.com 8 cited linkedin.com 2 cited semrush.com retrieved, not cited designrush.com retrieved, not cited

Brand size isn’t the gate here; freshness and being in the “best [category] [year]” listicle is. Get into those lists and keep them dated current.

Comparison, “X vs Y.” This one’s almost funny.

For “Ahrefs vs Semrush,” the single most-cited domain was ahrefs.com, 18 times across two of its own URLs. The vendor’s own comparison page won the comparison query. Backlinko’s well-known Ahrefs-vs-Semrush post and a Reddit thread were both retrieved and cited not once.

If there’s a “[you] vs [competitor]” query you care about, publish your own honest comparison page, because the named vendor’s own page is what gets cited.

News, “latest X.” It retrieved 10 and cited only three, and all three were Google’s own properties: the Search Status Dashboard, the Search Central docs, and blog.google. A Search Engine Land piece that was three days old was retrieved and never cited.

status.search.google.com 12 cited developers.google.com 6 cited blog.google 4 cited searchengineland.com (3 days old) retrieved, not cited searchenginejournal.com retrieved, not cited

For news, the official primary source wins, and freshness alone doesn’t. You can’t out-rank someone’s own announcement for their own news, so own your changelog and status pages and stop trying to beat the source.

#### The Big One: YouTube And Reddit Swap Places

If you took one lesson from the ChatGPT teardown, it was probably this.

ChatGPT cites Reddit and almost never cites YouTube, because it fetches a YouTube page and gets the metadata, not the transcript, so there’s no text to bind a citation to. Reddit is all text, so Reddit gets quoted.

Perplexity is the exact inverse.

On “best noise-cancelling earbuds under $150,” it retrieved 10 sources and cited two, and the two were YouTube and a niche eartips brand’s review page, 38 citations each. Three separate Reddit threads came back in the retrieved set and got cited not once.

Image Credit: Suganthan Mohanadasan

On the flat-tyre how-to, YouTube was cited 22 times across three videos.

youtube.com 38 cited complyfoam.com 38 cited reddit.com (×3) retrieved, not cited zdnet.com retrieved, not cited

The mechanism is simple.

Perplexity quotes the video; ChatGPT couldn’t.

How-to and product queries fire that video answer tab, and the video sources behind it get cited like any text source would.

#### The AI SEO/GEO Takeaway

The ChatGPT Reddit playbook doesn’t transfer to Perplexity, and video is first-class GEO real estate here . For instructional and product queries especially, a decent YouTube video is doing the citation work that a Reddit thread does over in ChatGPT. If you’ve been pouring everything into Reddit for AI visibility, Perplexity is telling you to go make the video too.

### Local Means Be In The Maps Index, Full Stop

This is the finding I’d put on the first slide of a client deck if they sold anything location-based.

“best specialty coffee shops near DIFC Dubai” fired places_search_intent at 0.996 against its 0.85 threshold, the first widget head to fire in the whole run. That kicked off the 2-round fan-out from earlier. Round 1 was a normal web search. Round 2 switched to a map engine and searched the specific businesses it had just found, through a different retrieval channel, meta_data.client: "search_api_local" instead of the usual web .

Round 1 engine=web "best specialty coffee shops near DIFC Dubai" → 10 web results Round 2 engine=map "specialty coffee near DIFC Dubai" engine=map "Encounter Coffee Roasters DIFC" → 5 place results engine=map "Nomad Day Bar DIFC specialty coffee"

Of 15 sources retrieved, five were cited, and all five were the business place-entities from the local API, eight citations each. The 10 editorial “best coffee in Dubai” listicles that came back in round one – traveltodubai, tripadvisor, wheretoeatdubai and the rest – were cited not once.

ChatGPT looked like it capped local at two results on a local_results_limit I found sitting in its config, but I’ve since walked that one back . The config went dark, and the map payload turned out to carry 12 to 28 places even when only a couple render. Perplexity cited five, all of them businesses, none of them blogs. Same lesson underneath either way.

One more thing worth grabbing while you’re in there.

In the June capture, the cited place links carried a ?ct-referrer=perplexity parameter on the outbound URL, Perplexity’s version of ChatGPT’s ?utm_source=chatgpt.com . Worth a filter in your analytics either way, with the caveat that my July re-run rendered no place links at all, so I couldn’t re-confirm it. Which brings me to the wrinkle.

Image Credit: Suganthan Mohanadasan

The July re-run made the lesson sharper. Same query, same 0.996 on the places head, and the map engine actually got promoted; it ran first this time, three rewritten variations before the web search instead of after.

But that session hadn’t shared location with Perplexity, and the Places tab, which is new since June, came back with “No places match this query”. No place-entities bound at all. And with no places to cite, the citations fell straight back to the round-2 web results, the same class of listicle that got blanked in June: wanderlog, novacircle, brewatlas, difc.com.

So the two runs bracket the mechanism. When the places index delivers, the businesses take every citation, and the listicles watch. When it can’t deliver, the listicles inherit the whole answer.

#### The AI SEO/GEO Takeaway

To win “near me” in Perplexity, be in the maps and local index first, your Google Business Profile and your site indexed as a place, and treat listicle presence as the fallback slot. In June, the place-entities took every citation, and the roundups got nothing. In July, with no places bound, the roundups inherited the answer. The primary path runs through the local index, and the editorial layer only collects when that path fails.

### Deep Research Is A Different Engine, And It Deep-Reads

Everything above is default Pro search. Flip the composer from Search to Deep Research, and you’re talking to pplx_alpha , which behaves nothing like the others.

It’s slow on purpose. The run I captured took 181 seconds against 15 to 30 for normal search, and the stream ballooned to about 30 MB because it streams the report to you as it writes it.

The step log gets a much richer vocabulary.

INITIAL_QUERY → LOAD_SKILL { research } → SEARCH_WEB (3 queries) → SEARCH_RESULTS → GET_URL_CONTENT (reads 2 pages in full) → THOUGHT ×3 → RESEARCH_ANSWER → FINAL

A few things stand out. It loads a named research skill; you can see LOAD_SKILL {skill_names:["research"]} right there in the stream, so Perplexity’s agent architecture is sitting on the wire. It runs only about three reformulated searches, nowhere near the 40 that ChatGPT’s Thinking model fires, so the fan-out is modest. And then it does the thing default search never does. It calls GET_URL_CONTENT on two or three hand-picked URLs and reads the entire page body, not the snippet.

That last step decides the answer. Of 15 sources retrieved, four were cited, and the pages it chose to fetch in full dominated. One comparison article, superframeworks.com, took 20 of the 30 citation markers on its own. Two-thirds of the answer came from the page it decided to read properly.

Image Credit: Suganthan Mohanadasan

#### The AI SEO/GEO Takeaway

For research-grade queries, you win in two moves. Rank for the two or three obvious reformulations so you make the retrieved set, then be the single most comprehensive, best-structured page on the topic so it picks you to read in full. This is the one mode where the snippet doesn’t save you, and the full body does. A thin page that ranks gets retrieved and skipped. The deep, well-organized one gets read end to end and cited 20 times.

### What I Couldn’t See

The negatives, same as last time.

There’s still no ranking score on the wire. The trust tiers from the July build are the closest Perplexity has ever come to exposing one, and even they don’t rank anything: no number orders source 1 above source 2 inside an answer, and the most-cited source on my how-to run carried no trust entry at all.

Whatever sorts the retrieved set stays server-side. So the ChatGPT conclusion applies here: anyone selling you reverse-engineered “Perplexity ranking factors” is still guessing.

No vendor names either. ChatGPT used to stamp each result with the scraper that fetched it, bright , oxylabs , serp , labrador , until OpenAI deleted that field on July 21 . I covered the removal in the ChatGPT follow-up . Perplexity never exposed the equivalent in the first place. It only tells you the channel, web or search_api_local , naming its own internal API and never the company behind it. Cleaner for them, less interesting for us.

A privacy correction while I’m here. My earlier free-tier note said throwaway threads were world-readable by URL. On a logged-in Pro account, that’s wrong. Threads default to PRIVATE_READ . The world-readable behavior was a logged-out artifact, not the universal default.

And shopping is genuinely unsettled. shopping_intent fired at 0.996, comfortably over its bar, on the earbuds query, but no product or price widget ever rendered. Could be region-gated; I’m in the UAE. Could need stronger buy-intent. One query can’t tell me which, so I won’t pretend it can.

The big unprobed surface is the agentic one. In June, Deep Research upsold it; the stream carried a RUN_QUERY_IN_COMPUTER prompt steering you toward the Comet “Computer” agent.

By July, Computer had graduated to a first-class mode sitting next to Search in the composer, with suggested follow-ups routed to it. That’s a task-execution agent, not a retrieval pipeline, so it’s a separate study, not this one.

### Run It Yourself

You can’t replay a finished Perplexity stream, and since the July build, you can’t even wait politely for it to end, because the answer socket stays open after the reply completes. So the hook goes in before you ask, and it reads the stream as it arrives. Open perplexity.ai, open the DevTools Console, and paste this in first. This is the version I re-tested on build df49f17 on July 21, 2026.

// Paste into the Console on perplexity.ai BEFORE you ask anything. // Tees Perplexity's answer stream into window.__cap as it arrives. // Reads only your own logged-in session. Nothing leaves your machine. const _fetch = window.fetch; window.__cap = []; window.__snap = (n = -1) => { const c = window.__cap.filter(x => x.url.includes('perplexity_ask')).at(n); if (!c) return null; const lines = c.buf.split('n').filter(l => l.startsWith('data:')); for (const l of lines.sort((a, b) => b.length - a.length)) { try { return JSON.parse(l.slice(5)); } catch (e) {} } return null; }; window.fetch = async (...args) => { const res = await _fetch(...args); const url = (args[0] && args[0].url) || String(args[0] || ''); const ct = res.headers.get('content-type') || ''; if (url.includes('perplexity_ask') || ct.includes('event-stream')) { const entry = { url, buf: '' }; window.__cap.push(entry); const reader = res.clone().body.getReader(); const dec = new TextDecoder(); (async () => { for (;;) { const { value, done } = await reader.read(); if (done) break; entry.buf += dec.decode(value, { stream: true }); } })(); } return res; }; console.log('Hooked. Ask something, let the answer finish, then read window.__snap().');

Then ask your question. When the answer finishes rendering, window.__snap() parses the richest snapshot for you: the classifier at .classifier_results.mhe_predictions_full , the step log in .text , the sources in the web-result block, and on the current build the trust objects on whichever sources carry one.

A couple of keepalive streams stay open forever, and now the answer stream does too. __snap() only looks at the ask stream, so you can ignore all of that. And if you want to watch pplx_alpha load its research skill and fetch full pages, switch the composer mode from Search to Deep research before you ask.

It reads only your own logged-in session, so nothing leaves your machine. And if you’d rather not babysit a console script, FanoutFox , my free Chrome extension, does this whole workflow for ChatGPT in one click.

### So, How Do You Show Up In Perplexity?

Perplexity behaves more like an actual search engine than ChatGPT does , which is oddly reassuring. It always searches, which means every query is winnable.

The router is right there in the traffic, so you can see the game before you play it. Depth beats snippet-gaming, because the deep-read step rewards the fullest page on the topic. And video and the maps index are first-class here in a way they simply aren’t in ChatGPT.

So classic relevance still matters. It’s just pointed at two specific targets, being the page Perplexity chooses to read, and being the entity that’s actually in the maps index.

Write the clean, deep, literal-match page, make the video, and get into the local index. Then watch your analytics for ?ct-referrer=perplexity .

And treat all of this, mine included, as a snapshot of a system that ships a new build most weeks. The structure holds. The numbers move.

The July re-check proved both halves of that in a single pass: the thresholds hadn’t moved by a digit in 26 days, and the trust field went from missing to live.

So, this article is the story, and the Perplexity research tracker is the running record. Every change I catch in the traffic goes there, dated, with what’s still true at the top. Check it before you act on anything above, because by then some of it will have moved.

Captured June 25, 2026 on build 7fe6ad4 , re-verified July 21, 2026 on build df49f17 , on my own logged-in Perplexity Pro account in Dubai. Eight captures, seven query types plus one Deep Research run. Structural findings are read straight from the stream and held at a single capture. Anything with a count is one account and directional.

Gemini’s next, and that capture’s already sitting in a folder.

More Resources:

- Google’s New AI Search Guide Calls AEO And GEO ‘Still SEO’

- Google AI Overview Citations From Top-Ranking Pages Drop Sharply

- Multi-Location SEO: How To Win Google & AI Search Visibility At Scale

This post was originally published on Suganthan .

Featured Image: Alonchik_73/Shutterstock

Category SEO Generative AI

Read Full Bio

Suganthan Mohanadasan Co-founder at Snippet Digital

I’m the Co-founder of Snippet Digital, A Search Journey Optimization agency helping brands win across every stage of modern discovery. ...

## 原文链接

[Read original](https://www.searchenginejournal.com/how-perplexity-actually-picks-sources-i-read-the-stream-not-the-answers/583769/)
