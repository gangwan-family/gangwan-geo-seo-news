---
title: "Google Went ‘Not Provided’ In 2011 And Blinded Us, ChatGPT Just Shipped Its Version via @sejournal, @DuaneForrester"
source: "Search Engine Journal"
published: 2026-07-23T12:00:13+00:00
fetched_at: 2026-07-23T22:31:00.448317+00:00
url: "https://www.searchenginejournal.com/google-went-not-provided-in-2011-and-blinded-us-chatgpt-just-shipped-its-version/582839/"
guid: "https://www.searchenginejournal.com/google-went-not-provided-in-2011-and-blinded-us-chatgpt-just-shipped-its-version/582839/"
author: "Duane Forrester"
categories:
  - "Generative AI"
  - "SEO"
---

# Google Went ‘Not Provided’ In 2011 And Blinded Us, ChatGPT Just Shipped Its Version via @sejournal, @DuaneForrester

- Source: Search Engine Journal
- Published: 2026-07-23
- URL: https://www.searchenginejournal.com/google-went-not-provided-in-2011-and-blinded-us-chatgpt-just-shipped-its-version/582839/
- Author: Duane Forrester
- Categories: Generative AI, SEO

## RSS 摘要

Waiting for ChatGPT to prove your ROI? The not-provided lesson says stop. Here's the measurement work you can own instead. The post Google Went ‘Not Provided’ In 2011 And Blinded Us, ChatGPT Just Shipped Its Version appeared first on Search Engine Journal .

## 原文正文

Google Went 'Not Provided' In 2011 And Blinded Us, ChatGPT Just Shipped Its Version Skip to content

- SEJ

- ⋅

- SEO

## Google Went ‘Not Provided’ In 2011 And Blinded Us, ChatGPT Just Shipped Its Version

The organic attribution you keep asking for structurally isn’t coming, and OpenAI’s own documentation shows why. Here’s what to measure instead.

The attribution you are waiting for from ChatGPT is coming, and it is not coming to you. I ran a survey this month ( it’s still open; please take it ) asking whether dedicated AI visibility platforms are worth paying for, and I deliberately never asked about attribution. It showed up anyway. One consultant wrote that the whole problem is tying visibility, citations, and mentions to dollars. An agency owner managing over a dozen clients answered the “what’s your biggest-unanswered-question” prompt with a single word and an exclamation point: attribution! Another respondent put it more wearily: that tracking is only the first step, so what comes next.

Image Credit: Duane Forrester

Two different frustrations hide inside that one word, attribution. One is whether a tracker reads your AI visibility accurately at all. The other is whether that visibility can be tied to revenue. This piece is about the second. The first runs underneath it, and I come back to it at the end.

That corner has stayed dark for a reason, and it is not the reason most people think. The instinct is to treat missing attribution as a gap some vendor will eventually fill, the way rank tracking filled in twenty years ago. It will not fill in that way. The click-path attribution that organic search practitioners were trained to expect, the deterministic line from impression to session to conversion, is gone, and AI did not kill it. Referral traffic from AI answers is real but tiny, under one percent of total traffic on most sites, which means the thing people are asking for was never going to be answered by watching their own analytics. So let me toss a flashlight at the corner. Here is where attribution stands, why it stands there, and an idea about what you do starting tomorrow.

### The Deterministic Era Was Ending Before A Single LLM Shipped

Third-party cookies went into slow deprecation, Apple’s App Tracking Transparency cut off a huge slice of mobile signal, Google Analytics moved to modeled conversions rather than counted ones, and media mix modeling, a technique older than most of the people now using it, came roaring back precisely because the clean deterministic path had frayed. Every one of those shifts happened for its own reasons and none of them involved ChatGPT. LLMs did not break attribution. They arrived after the break and made it impossible to keep pretending. The measurement world you are standing in was already modeled, probabilistic, and permission-dependent before answer engines entered the picture, and that is the ground we are now building on.

### Now The Part That Will Annoy You, Because It Is Both Simple And Deliberate

Attribution from the platforms is coming, but it is arriving through the ads door, not the webmaster-tools door. The signal a paying advertiser needs and the signal a free organic practitioner wants are the same signal. A platform will build that signal for the person spending money and withhold it from the person who is not, because there is no business reason to give away for free what someone else will pay for.

We have watched this movie. In 2011, Google encrypted organic search referrals and organic keyword data vanished into the not-provided bucket, while paid search advertisers kept getting richer and richer conversion data. Same query intent, same underlying behavior, monetized on one side and starved on the other. Organic SEO spent a decade angry about it. (Maybe you still are?)

ChatGPT just shipped its version, and you can read both halves of it in OpenAI’s own documentation. On the organic side, the controls OpenAI gives webmasters are switches, not meters. You can allow OAI-SearchBot so you appear in ChatGPT’s answers, or disallow GPTBot so your content is not used in training. Toggles. On or off. What you cannot do is measure via OpenAI. On the paid side, OpenAI has already built a full server-to-server conversions pipeline : a pixel, an events API keyed to an Ads Manager account, standard events like order_created carrying amount, currency, and item-level detail, deduplication between browser and server, and a privacy-preserving identifier to tie exposure to outcome. That is closed-loop conversion attribution. It exists right now. It sits behind an ad account. The organic operator on the same platform gets a robots.txt file and best wishes.

### The Sharper Cut Is This

Nobody at OpenAI needed to say Google’s name for this to happen. The not-provided lesson has been in plain sight for more than a decade, in every conference post-mortem and forum thread written since 2011, and the lesson is precise: taking access away costs you years of goodwill, so do not take it away; simply never grant it. Google paid for its mistake because it was a taking, and people fight takings . A designed absence generates no protest, only a low, unfocused unease. That knowledge was ambient. Any competent operator building an answer engine already had it.

Which is why this is not really an OpenAI story. Plot the model companies along a line by their stated reason to exist, a sell-to-serve spectrum if you want a handle for it, meaning where each one sits between built to sell and built to serve. OpenAI is running hard at commerce and ads, so it builds the paid measurement loop first and most visibly. Perplexity is chasing a slice of the discovery-and-shopping pie and moves in the same direction. Google already is an ad company. Anthropic frames itself around safety and long-term benefit and has the least structural reason to build an ads attribution layer at all. The doors differ, and the timing differs, but read the whole line and the conclusion holds in every seat: None of these companies has an incentive to hand free, item-level organic attribution to SEOs. The commercially driven ones gate it behind ad spend. The mission-driven ones simply have better things to build. Do not expect it from ChatGPT is the narrow version. The real version is do not expect it anywhere, sadly.

### So Stop Asking 1 Question That Is Actually 3

When practitioners say attribution, they are usually blending three different problems that have three different answers . The first is referral attribution , meaning did an AI answer link to you, did someone click, did that session convert. That one is measurable today, because the click carries a referrer into your own analytics. The second is incrementality , meaning not who clicked but whether your visibility caused lift you would not otherwise have gotten. The third is influence , the dark-funnel case, meaning the buyer read your brand inside an AI answer, never clicked, and showed up three weeks later through a branded search. Referral you can see now. Incrementality you can prove yourself. Influence is genuinely hard. The mistake is treating all three as one blocked pipe, when two of them are already flowing and need nothing from the platforms at all.

### Here Is The Work, And None Of It Requires Permission From OpenAI

Start with referral classification , and do it properly, because the default is wrong. AI sessions do not reliably self-label, and referrer strings alone will misfile a large share of them into direct or organic. Tag deliberately with UTMs where you control the link, build a classification rule that combines referrer with landing-page and query patterns rather than trusting the referrer field on its own, and treat the number you get as a floor, because unattributable and cross-window purchases bias every honest count downward. That gets you an accurate read on the one layer that is visible.

Then run incrementality yourself, which is the layer most teams skip because it takes design rather than a dashboard. Hold out a set of geographies and change nothing in them while you push visibility work everywhere else, or run on-off tests over defined windows, or track a fixed set of queries before and after a content push and watch what moves. This is causal measurement, and it belongs to you, not to the platform, which means the opacity of the black box does not touch it.

For the dark funnel, borrow the muscle B2B has used for twenty years, because this is not new-hard; it is old-hard wearing a new coat. Self-reported attribution, the how-did-you-hear-about-us field at the point of conversion, catches influence that no pixel will ever see. Branded-demand correlation, watching whether branded search and direct navigation rise as your AI visibility rises, gives you a defensible read at the aggregate level. Brand-lift studies do the same with more rigor when the budget is there. None of it is deterministic, and that is fine, because deterministic is not on the menu for anyone anymore.

### Before You Buy Anything In This Space, Run 1 Test On The Vendor

Ask what data source closes the loop, and listen carefully to the answer. If the honest answer is first-party, meaning their agents on your site, your Google Analytics 4, your CRM, then what they sell is real but bounded, and it lives at the referral layer. If the answer implies signal drawn from inside OpenAI or Anthropic, they are either misrepresenting a referrer-detection method or lying to you. There is no third source. That single question separates the credible from the theatrical faster than any feature list.

### This Is Where The Discipline Shows

Attribution counts orders from sessions you classified as AI-referred. Some of those buyers would have found you anyway. Incrementality measures the lift you actually caused, and it requires the experiments described above. Report attribution as attribution, and reserve the word incremental for the cases where you ran the test. The vendors who keep that distinction clean read as trustworthy. The ones who collapse it and promise to prove ROI are the 2026 reissue of guaranteed-first-page SEO, and they will age exactly as well, I think.

### Look At Who Is Doing This Credibly, And The Thesis Proves Itself

The players with defensible revenue measurement all sidestep the black box and run on first-party data. Some vendors compute attribution by joining their own storefront sessions to checkout events against a sitewide baseline, and the numbers that get reported vary wildly, which is the honest headline. Microsoft Clarity’s study of 1,200 publisher sites found AI-referred visitors converting to sign-ups at eleven times the rate of organic search, while the peer-reviewed work in Marketing Science , 973 sites and 20 billion dollars in revenue, found organic LLM traffic converting below every traditional channel except paid social. I think both are true, and that is the point. The channel is small, high-intent, and wildly uneven, and it is not even measured the same way twice. Others resolve the loop the same first-party way, routing through affiliate infrastructure or handing purchase reporting back to your own analytics. The pattern under all of it is the tell: Everyone credible closes the loop with data you already own, because that is the only door open.

### Give It 12 To 24 Months, And The Shape Is Predictable

Referral classification standardizes and gets boring, as the engines increasingly identify themselves and the analytics tools catch up. Attribution proper gets monetized as an ads product, gated and paid, exactly along the line OpenAI has already drawn in its documentation. And the honest vendors converge on the attribution-versus-incrementality language, because the market eventually punishes the ones who oversold. None of that returns free organic attribution to you, because none of it ever had a reason to.

### Which Brings Me Back To The Survey, And To The Thing Underneath The Thing

The attribution requests were loud, but they were the sharp, nameable tip of something larger and more corrosive. As I read the early open-text answers together, what surfaces is not mainly a demand for better numbers; it is a refusal to believe the numbers already on offer. Respondents said they do not trust the trackers, that they cannot tell whether any of it is accurate, that they are struggling to invest because they do not trust the results. That is not a feature gap. That is a trust deficit, and part of it is the correct read of a market built on designed absences and overselling. But I would be lying if I put all of it there. Some of that unease is old thinking meeting a new situation, practitioners carrying SEO reflexes into an environment that does not run on them and skipping the work of learning what actually changed, because “GEO = SEO” is a more comfortable story than the truth. I can’t tell you how big that share is and nobody can measure it cleanly; we read it off what we see and hear online, at conferences, etc. But if it is even a third of the industry’s working mindset, that is not something a vendor comes along and fixes. That is a literacy problem, and it belongs to all of us.

If you are wrestling with this in your own stack, tell me where your loop breaks, in the comments or directly, because the playbook here is still being written and the field’s real answers are coming from practitioners, not vendors. And if you want the longer argument for why the underlying systems, not the dashboards, are where this literacy has to live, that is the whole spine of The Machine Layer .

More Resources:

- The Web Is Eating Itself And Your Metrics Look Fine

- The Shortcut Behind Some AI Optimization Tools

- When Direct Means We Don’t Know: CMOs Need To Rethink Attribution In AI Search

This post was originally published on Duane Forrester Decodes .

Featured Image: Prostock-studio/Shutterstock

Category SEO Generative AI

Read Full Bio

Duane Forrester Founder and CEO at UnboundAnswers.com

Duane Forrester is the Founder and CEO of UnboundAnswers.com, a consultancy helping businesses adapt to the realities of AI-powered search ...

## 原文链接

[Read original](https://www.searchenginejournal.com/google-went-not-provided-in-2011-and-blinded-us-chatgpt-just-shipped-its-version/582839/)
