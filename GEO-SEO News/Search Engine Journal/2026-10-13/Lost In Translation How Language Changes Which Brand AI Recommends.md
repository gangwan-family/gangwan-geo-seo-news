---
title: "Lost In Translation: How Language Changes Which Brand AI Recommends"
source: "Search Engine Journal"
published: 2026-10-13T12:00:05+00:00
fetched_at: 2026-10-14T00:25:47.157666+00:00
url: "https://www.searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585/"
guid: "https://www.searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585/"
author: "Reza Moaiandin"
categories:
  - "AI Search"
  - "International Search"
---

# Lost In Translation: How Language Changes Which Brand AI Recommends

- Source: Search Engine Journal
- Published: 2026-10-13
- URL: https://www.searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585/
- Author: Reza Moaiandin
- Categories: AI Search, International Search

## RSS 摘要

Your AI visibility check was probably in English. However, new research across 1,650 responses shows AI recommends different brands in different languages. The post Lost In Translation: How Language Changes Which Brand AI Recommends appeared first on Search Engine Journal .

## 原文正文

Lost In Translation: How Language Changes Which Brand AI Recommends Skip to content

SEJ Pro Sign In

Webinar: The Link Building Graveyard: What to Bury & What Still Wins

Reserve Your Seat

- SEJ

- ⋅

- AI Search

## Lost In Translation: How Language Changes Which Brand AI Recommends

Your English-only AI visibility checks can miss how brand recommendations change when AI answers the same buying questions in five different languages.

Chances are you’ve already got some idea of your brand’s visibility in AI responses . But I’m willing to bet those visibility checks were carried out in just one language: English.

If a customer in Singapore asks an AI chatbot a buying question in Simplified Chinese, and a customer in Kazakhstan asks the same question of the same AI in Russian, would they get the same recommendation? What about a customer in Riyadh asking in Arabic or a customer in Los Angeles asking in Persian?

These aren’t hypothetical customers. According to Statcounter’s August 2026 figures, ChatGPT was responsible for roughly three-quarters of website visits that came from AI chatbots in Saudi Arabia , Kazakhstan , and Singapore . Add in Claude and Gemini, and these three U.S.-based models accounted for more than 90% of AI referrals in each market.

Of course, you don’t need to leave the U.S. to find customers whose first language isn’t English. More than half of Los Angeles County residents speak another language at home, including around 74,000 Persian speakers, according to the latest Census estimates . I’d be surprised if they all switched to English every time they opened ChatGPT .

But when somebody asks an AI chatbot a question in another language, the response won’t simply be a translation of the answer it would give in English. The AI reasons and composes its response in that language . And that brings a whole slew of cultural values and other factors to bear on how the model responds.

### Why The Choice Of Language Matters In AI

I’m not the first person to write for Search Engine Journal on how brand visibility and messaging in AI can come across differently in languages beyond English. In April, Duane Forrester explained why AI visibility strategies built in English don’t transfer easily to other markets. For a start, ChatGPT and Gemini aren’t accessible in China at all, while Claude isn’t officially offered in mainland China, Russia, or Iran. Instead, your brand’s AI visibility in some countries may depend on regional, homegrown models, such as Baidu’s ERNIE in China, Naver in South Korea, Mistral in France, and so on. As Forrester explains, each of these models evolved from a different starting point entirely: a national corpus, a specific cultural identity, and in some cases a government mandate. If you haven’t read his article, I’d bookmark it now to read after this one .

However, as we’ve seen, Western AI models like Claude, ChatGPT, and Gemini are still widely used in plenty of locations where other languages are spoken, not to mention all the diaspora communities around the world.

In July, Anthropic published a report on Claude’s values across languages and models . By values, we’re talking about the factors that shape responses where there is no definitive right answer. For example, are responses more likely to display deference or caution, warmth or rigor, depth or brevity, candor or execution?

The researchers sampled just under 310,000 real conversations across the 20 most common languages, equally split between three models (Sonnet 4.6, Opus 4.6, Opus 4.7). They found that the values Claude demonstrated shifted according to the language it was addressed in, such as leaning toward greater warmth in Hindi and Arabic and toward greater rigor in English and Russian.

The effect is this: Two people could submit the exact same query in different languages – say, whether they should upgrade to the new iPhone Duo – and come away with quite different impressions of what they should do and how good it is.

One thing the Anthropic research doesn’t test is whether the choice of language also impacts whether Claude mentions, cites or recommends your brand in the first place .

So, I decided to run some tests of my own.

See also: Your AI Visibility Strategy Doesn’t Work Outside English

### 6 Questions, 5 Languages, 1,650 Answers

I picked six shopping or booking scenarios where someone might use an AI chatbot to research their options before making a decision:

- A hotel in Tenerife.

- A return flight from London to Tenerife.

- Noise-canceling headphones under £400.

- A robot vacuum under £500.

- A CRM for a small U.K. business.

- Project management software for a 50-person UK firm.

As Anthropic’s research was the catalyst for these tests, I decided to test Claude Sonnet 5 first, with web search turned off. Using DataForSEO’s LLM Responses API , I queried Claude on each of the scenarios in five languages:

- English.

- Arabic.

- Russian.

- Simplified Chinese.

- Persian.

In each instance, I asked the model to:

- Name three options (brands).

- Say which one would be its recommendation.

This gave me the core dataset: six scenarios × five languages × 40 runs = 1,200 responses.

For comparison, I also used the same setup to test two of the scenarios (hotel and PM software) with web search turned on to see if allowing the model to search the open web made a measurable difference to the answers. Finally, I tested the same two scenarios in ChatGPT and Gemini to see if other AI models behave the same way . I’ll return to these comparison questions later.

Eventually, I had data from 1,650 responses to crunch.

Luckily, most of the mentioned brand names were rendered in Latin script, even in Arabic, Russian, Chinese, and Persian responses. As there’s no Arabic or Chinese word equivalent to a brand name like “Zoho,” the model writes it as-is. This meant I could set up a straightforward text-matching pipeline to capture and build a list of the brand names mentioned in each category.

However, while this held up consistently for five of the six categories, airlines proved to be an exception. Because they’re truly international businesses, some brands have established local-language forms. For example, roughly 5% of the Chinese responses wrote “英国航空” for British Airways (literally “Britain Aviation”) or “易捷航空” for easyJet, with no Latin form nearby. Some Arabic responses did the same with phonetic transliterations, writing “جت2” for Jet2 and “إيزي جت” for easyJet. Because of this, I had to add those Chinese and Arabic strings as extra patterns to the brand-matching list.

Identifying the winning brand pick in each response involved looking for the typical words and phrases used by each model in each language when making a recommendation (such as “my recommendation,” “التوصية النهائية,” “最佳选择,” a trophy emoji, and so on).

This method resolved cleanly for 99.8% of responses. But before I trusted the final data, I manually checked a sample of roughly 40 responses across every method tier.

I’ve excluded three responses from the results because they ended without naming a final pick. As a result, two of the percentage scores in the tables below are derived from 39 responses instead of 40. (The fourth came from the web search tests.)

### What The Data Showed

The most startling disparities occurred in queries related to the second scenario – airline recommendations for a return flight from London to Tenerife.

In Persian, Claude picked British Airways 52.5% of the time, and easyJet only 12.5%. However, in Russian, Claude overwhelmingly opted for easyJet (72.5%) – a staggering 60-point swing – while it didn’t recommend British Airways even once.

AIRLINES

Overall

English

Arabic

Russian

Chinese

Persian

British Airways

24.0%

12.5%

45.0%

10.0%

52.5%

Jet2

31.5%

45.0%

22.5%

25.0%

32.5%

easyJet

37.5%

35.0%

17.5%

72.5%

50.0%

12.5%

TUI Airways

5.5%

2.5%

12.5%

2.5%

7.5%

2.5%

Ryanair

1.5%

5.0%

2.5%

Same model, same scenario, same question, same afternoon. The only difference was the language.

For hotels, the number of properties in Tenerife meant Claude had a much wider field of options than it would for, say, robot vacuums, leading to a much more varied range of recommendations in each language.

However, while this meant the percentages were lower overall, the disparities between languages were still quite stark. Bahía del Duque was the top pick in 43.6% of Chinese responses but only won in 7.7% of Arabic ones. And while Hotel Botánico accounted for nearly a third of recommendations in English, it disappeared without trace in Russian.

HOTELS

Overall

English

Arabic

Russian

Chinese

Persian

Bahía del Duque

23.3%

25.0%

7.7%

17.5%

43.6%

22.5%

Hotel Botánico

13.6%

32.5%

17.9%

10.3%

7.5%

Royal Hideaway Corales

34.2%

27.5%

20.5%

47.5%

25.6%

50.0%

Iberostar Selection Sábila

13.7%

2.5%

25.6%

25.0%

12.8%

2.5%

Vincci Selección La Plantación del Sur

5.1%

20.5%

5.0%

Hotel Jardín Tropical

5.6%

12.5%

2.6%

7.7%

5.0%

Royal Garden Villas

1.0%

5.0%

Iberostar Selection Anthelia

1.0%

2.6%

2.5%

Iberostar Grand Salomé

1.0%

2.6%

2.5%

Sheraton La Caleta

0.5%

2.5%

Suite Hotel Fañabé Costa Sur

0.5%

2.5%

Bahia Principe Sunlight Costa Adeje

0.5%

2.5%

If there’s one industry where a brand would need to engage with customers in multiple languages, it would be travel and tourism. But if an airline CMO or hotel marketing manager only tested their brand’s AI visibility in one language, they would get a completely inaccurate picture of how their brand is recommended (or not) in other valuable territories.

The other four categories didn’t reveal the same volatility, with the same brand winning across all five languages. Here, it’s the scale of that win and the battle for second place that becomes more interesting.

For example, in the headphones category, English was the outlier, as the only language where Sony had serious competition. To a lesser extent, the same is also true in the CRM software category.

HEADPHONES

Overall

English

Arabic

Russian

Chinese

Persian

Sony

87.0%

50.0%

97.5%

100.0%

87.5%

100.0%

Bose

10.0%

42.5%

2.5%

5.0%

Bowers & Wilkins

3.0%

7.5%

7.5%

CRM SOFTWARE

Overall

English

Arabic

Russian

Chinese

Persian

HubSpot CRM

13.0%

22.5%

2.5%

15.0%

20.0%

5.0%

Zoho CRM

85.5%

75.0%

92.5%

85.0%

80.0%

95.0%

Pipedrive

1.0%

5.0%

Microsoft Dynamics 365

0.5%

2.5%

The final two categories saw no real outliers, with the story playing out much the same across all five languages.

If you’re after a robot vacuum for under £500, it seems that whichever language you use, AI will almost always recommend Roborock.

ROBOT VACUUMS

Overall

English

Arabic

Russian

Chinese

Persian

Roborock

91.5%

87.5%

97.5%

90.0%

95.0%

Eufy

3.0%

7.5%

5.0%

2.5%

Xiaomi

0.5%

2.5%

Ecovacs

4.0%

5.0%

2.5%

5.0%

2.5%

iRobot (Roomba)

0.5%

2.5%

Shark

0.5%

2.5%

Meanwhile, the project management software category is a real two-horse race across the board. But even here, Monday.com consistently scored a few more recommendations than closest rival Asana.

PM SOFTWARE

Overall

English

Arabic

Russian

Chinese

Persian

Asana

38.5%

37.5%

40.0%

32.5%

45.0%

Smartsheet

3.0%

12.5%

2.5%

Monday.com

51.0%

45.0%

55.0%

47.5%

55.0%

52.5%

Wrike

7.5%

5.0%

12.5%

2.5%

So, what does this all mean? What can we take from this?

### Why Might This Be Happening?

For now, I can only guess at why some categories are stable across all languages while others see such huge variations.

Perhaps, because some categories draw on a much smaller list of global brands, it’s easier for one or two leaders to dominate. Where the world broadly agrees, language might not be as big a factor. But what about when there isn’t such a broad consensus?

For example, Russian was the only language where Claude didn’t recommend British Airways even once. One explanation might be that, in February 2022 , Russia banned all U.K.-registered aircraft from its airspace, and British Airways suspended its Moscow route the same day. But easyJet and Jet2 are also British airlines, and they account for 97.5% of all Russian recommendations.

Maybe the question isn’t why British Airways was excluded in Russian. Maybe the more interesting question is why easyJet scored so high – by far the highest score in this category across all languages – effectively pushing other airlines lower (or out)?

Whatever the reason, the lesson is the same. When you ask AI a question in a particular language, you’re not just choosing a vocabulary. You’re giving the model additional context that influences and shapes the answers you get back.

But whether that context is regional, political, cultural, or purely linguistic won’t be easy to unpick.

The travel industry aside, what these findings mean to you will mostly depend on which category your business is in. Most of you reading this will be in industries and product categories that don’t map to the six scenarios we’ve tested, in which case, I recommend running some research of your own.

But if you carry out some tests and do find significant variations between languages, can you do anything about it?

The results from my next round of tests suggest there might be a way.

### What Happens When The Model Searches The Open Web?

Because I wanted to get as clear a picture as possible of each model’s own behavior in different languages, free of outside factors, I initially tested Claude with web search switched off. That way, responses could only draw on the model’s own memory and training datasets . Any variations between languages could only be a product of the model.

However, most people use these AI tools with web search switched on. Therefore, I also tested two of the scenarios (hotel and PM software) across the same five languages with web search turned on to see if, and by how much, the recommendations might change.

Out of these 10 language and category combinations, the winning brand was different in seven.

In the hotel category, the winning hotel changed in all five languages. Even more striking is that many hotels that had previously received recommendations completely disappeared once web search was switched on, while ten new hotel names appeared for the first time, including the overall winner. JOIA by Iberostar easily won the most recommendations in three languages, taking 31% of picks overall and 60% in English.

Interestingly, this isn’t a new hotel that’s popped up since Claude’s last training run. In July 2024 , a rebrand saw Iberostar’s Grand tier hotels become JOIA by Iberostar. When working from memory, Claude used the old Iberostar Grand name dropped by the company two years earlier. Of course, that’s exactly why you want AI to access the live web.

But the name change isn’t why this is interesting. With web search off, Claude recommended an Iberostar Grand hotel just twice in 198 responses. But with web search on, JOIA by Iberostar easily became the most recommended hotel in the category. Claude didn’t just pick up the new name and perform a find/replace. Something in what it found online pushed that hotel to the top.

Meanwhile, in the project management software category, only Persian and Arabic saw the winning brand change. Arabic opted for Wrike 46.7% of the time, despite only recommending it in 5% of responses when web search was off.

In Persian, Asana (40%) finally won over Monday.com (26.7%), despite scoring lower than it had with web search off. This was again due to a much stronger score for Wrike (33.3%) than before, turning the category into a three-horse race.

I should add a caveat here, because I don’t want to overstate these findings. With web search enabled, 42.7% of the responses hit the output limit before finishing. Truncated responses were particularly common in Persian (83%) and Arabic (63%). Thankfully, because the model names its top pick before it elaborates on the reasons why, I could still capture the brand recommendations from nearly every response. But it does mean I can’t rule out the possibility of these numbers being soft.

Even so, the trend is still clear – live web search has an impact . This is important because it suggests that these language variations are fluid and can be influenced.

Obviously, you can’t do anything about an AI training run from last year. That’s fixed and beyond your reach. But with web search switched on, the AI model supplements that training data with new information and context from the open web. This is where your marketing team can become proactive, developing strategies and publishing content to hopefully improve your brand visibility in each region .

Of course, what those strategies might be will depend on a more thorough understanding of why these variations happen. That’s a whole other topic.

See also: Why International SEO Needs A Global Knowledge Integrity Strategy

### Testing ChatGPT And Gemini

You’re probably thinking, “This is all well and good, but how do we know this phenomenon isn’t exclusive to Claude?” That’s why I tested the same two scenarios in ChatGPT (gpt-5.6-sol) and Gemini (gemini-3.5-flash), also with web search off, to see how they compare.

Out of the 10 language and category combinations, Gemini matched Claude in five. ChatGPT matched Claude in only one.

In the core dataset, project management software was one of the more stable categories, with Monday.com consistently winning the most recommendations in all five languages. Gemini also preferred Monday.com, recommending the brand between 53% and 100% of the time in English, Arabic, Russian, and Chinese. Only in Persian did it switch its recommendation to Asana.

However, the story is very different in ChatGPT, with Monday.com not winning a single language. Wrike was very much an also-ran in the initial Claude tests, but in ChatGPT Wrike won the most recommendations in four languages, with only Arabic giving Asana the edge.

PM SOFTWARE (models)

Claude

ChatGPT

Gemini

English

Monday.com

45.0%

Wrike

60.0%

Monday.com

93.3%

Arabic

Monday.com

55.0%

Asana

46.7%

Monday.com

73.3%

Russian

Monday.com

47.5%

Wrike

40.0%

Monday.com

53.3%

Chinese

Monday.com

55.0%

Wrike

86.7%

Monday.com

100.0%

Persian

Monday.com

52.5%

Wrike

46.7%

Asana

46.7%

As for those Tenerife hotels, ChatGPT produced much more consistent results, with “Iberostar Selection Sábila” the outright winner, scoring between 46.7% and 86.7% across four of the five languages. Only Persian favored a different hotel, with the Vincci Selección La Plantación del Sur in front on 40%.

In Gemini, the picture was less certain but was still more consistent than Claude’s.

HOTELS (models)

Claude

ChatGPT

Gemini

English

Hotel Botánico

32.5%

Iberostar Selection Sábila

46.7%

Hotel Colón Guanahaní

66.7%

Arabic

Iberostar Selection Sábila

25.6%

Iberostar Selection Sábila

86.7%

Iberostar Selection Sábila

73.3%

Russian

Royal Hideaway Corales

47.5%

Iberostar Selection Sábila

73.3%

Hotel Colón Guanahaní

60.0%

Chinese

Bahía del Duque

43.6%

Iberostar Selection Sábila

53.3%

Iberostar Selection Sábila

60.0%

Persian

Royal Hideaway Corales

50.0%

Vincci Selección La Plantación del Sur

40.0%

Hotel Colón Guanahaní

80.0%

While we should treat these findings as suggestive rather than definitive, it does seem clear that variances between languages are not exclusive to any one AI model.

### The Limits Of This Research

The initial hypothesis I set out to test was that brand recommendations vary according to the language of the user. I think we can safely say the answer to that is “yes.”

Beyond that, we need to be cautious about reading too much into these numbers.

The above findings and my inferences are based on a small sample of responses, gathered on September 7, 2026, in a single afternoon, and targeting just a small handful of the AI models, product categories, and languages out there.

1,650 responses might sound like a decent dataset, but it’s barely a blip when you consider how many queries are entered into AI chatbots every second of every day.

The small size of the dataset is probably most noticeable in the hotel category. Tenerife has hundreds of hotels. With such a large range of potential answers, it’s not surprising that the number of recommendations (and the resulting percentages) for those hotels that did appear were lower than for the other categories with far fewer options. Statistically speaking, many of those numbers may sit well within the margin of error . Does one mention in 40 constitute evidence? No.

Elsewhere, factors such as truncated responses mean some numbers are softer than others.

Plus, without running the same tests again, there’s no reason to assume these numbers and patterns will hold true from one week to the next.

I say all this because I don’t want to overstate what we should take away from this research. These numbers give us just a tiny keyhole to look through. For now, they provide us with indications, and potential lines for further exploration.

What they don’t do is give us a complete picture of the multilingual AI landscape, let alone a map to confidently navigate it. This research isn’t the end of the story, but the start.

The best advice I can give you is to run your own tests. Take a handful of questions customers typically ask before they buy from your category. Then test them in multiple AI models in each of your target-market languages. Importantly, don’t do this once but repeat the process enough times to see which patterns emerge and how they change over time.

### What Now?

Back to where we started. I originally set out to answer a fairly narrow question: Would a customer in Singapore and a customer in Kazakhstan get the same recommendation from AI?

On the current evidence, the answer is sometimes reassuringly yes and sometimes emphatically no. I don’t want to say, “It depends,” but, well, it depends. Language is definitely a factor, but there are a lot of variables in play.

As a result, you’ll probably have no way of knowing how any of this applies to your category and your brand until you look.

Plus, we now have a bunch of fresh questions to explore. What are these variables? Are the numbers reasonably steady or do they fluctuate wildly from week to week? And can we do anything about it?

That last one is probably the biggest question of all. We saw that allowing AI to access the live web had a clear impact on the results, and I think that’s significant. It suggests that, instead of passively accepting any language gap, your marketing team might be able to influence future responses.

More Resources:

- How AI Chooses Which Brands To Recommend: From Relational Knowledge To Topical Presence

- How AI’s Geo-Identification Failures Are Rewriting International SEO

- Your Biggest AI Search Risk Is Conflicting Information About Your Brand

Featured Image: Roman Samborskyi/Shutterstock

Category AI Search International Search

Read Full Bio

Reza Moaiandin Co-founder at SALT.agency

Reza Moaiandin is the Co-Founder at SALT. A software engineer by training and certified white-hat hacker, Reza has spent more ...

## 原文链接

[Read original](https://www.searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585/)
