---
title: "It Was There A Minute Ago via @sejournal, @pedrodias"
source: "Search Engine Journal"
published: 2026-09-16T19:00:44+00:00
fetched_at: 2026-09-16T23:41:51.317632+00:00
url: "https://www.searchenginejournal.com/it-was-there-a-minute-ago/589500/"
guid: "https://www.searchenginejournal.com/it-was-there-a-minute-ago/589500/"
author: "Pedro Dias"
categories:
  - "AI Search"
  - "SEO"
---

# It Was There A Minute Ago via @sejournal, @pedrodias

- Source: Search Engine Journal
- Published: 2026-09-16
- URL: https://www.searchenginejournal.com/it-was-there-a-minute-ago/589500/
- Author: Pedro Dias
- Categories: AI Search, SEO

## RSS 摘要

A model can know the right answer and still defer to a wrong tool result. What does that mean for your visibility report? The post It Was There A Minute Ago appeared first on Search Engine Journal .

## 原文正文

It Was There A Minute Ago Skip to content

- SEJ

- ⋅

- SEO

## It Was There A Minute Ago

A missing brand mention gives you a result. The explanation attached to it deserves a much harder look.

Since late last year, browsing arXiv and reading research papers has become something of a hobby. I enjoy connecting findings across papers, seeing what they might help explain about the still opaque world of AI visibility. The studies ask narrower questions than we tend to ask in Search, but reading them together gives me a better way to question the explanations we’re offered.

One recent example starts with a model that had already answered correctly. Then a tool returned the wrong information, and the model went along with it.

MemToC tests what happens when a language model’s own answer conflicts with information returned by an external tool.

The tool supplies information for the model to use in its answer, much as retrieval supplies passages in RAG . Here, the researchers test executed-tool returns specifically.

Researchers first required the models to give their best answers to factual questions without tools, then asked again with controlled tool returns. They examined cases where an instruction-tuned model had answered correctly, and the tool supplied an incorrect answer. Across the four models, correct-answer retention ranged from 6.5% to 17.1%, with results pooled over three instruction wordings.

The model had just given the correct answer. That makes “it doesn’t know” a poor explanation on its own. But getting a fact right once doesn’t tell us how reliably the model has learned it, or whether that answer will survive conflicting information.

Now imagine that all you can see is the final answer, and the missing fact concerns your brand. You get a red cell in a visibility report . Someone has to explain it at the next client meeting.

I want to know how that explanation gets chosen. A count of appearances tells you what happened in the answers you collected. Calling the red cell an authority problem requires evidence the count doesn’t contain. It does, conveniently, suggest some work to invoice.

### The Answer Changed, What Else Changed?

MemToC’s researchers can compare the final answer with the model’s earlier response and the controlled tool return. That lets them test whether a correct answer survives contradictory evidence. In a separate annotation sample of 120 responses to incorrect tool returns, covering five models and both conflict cases, none explicitly acknowledged disagreement. That result is limited to the inspected responses; it cannot establish that models never flag conflicts.

These were controlled tests, principally on open-weight models with 7-9 billion parameters. The percentages cannot be applied to ChatGPT search or Google AI Overviews.

I have already written about retrieval contamination . MemToC adds a complication: the model can give the correct answer and still defer to the wrong information returned by a tool.

Perhaps the correct answer is easier to displace when the model has learned the fact less reliably. Stronger learning could make it more resistant to conflicting information. The model might also give the tool’s answer more weight because of how that information is presented. The retention figures alone don’t tell us which explanation applies.

That leaves a useful question to test: Does strengthening what the model learns improve both its answers without tools and its ability to hold onto correct information when a tool contradicts it?

A content deficiency and a source conflict could produce the same missing mention in a visibility report. If the next slide recommends another page, I’d like to know how we settled on a content problem. Counting the absence again won’t answer that.

Even without a competing source, the inference from silence to missing knowledge is shaky. Empty Shelves or Lost Keys? tests the gap between reproducing a fact with strong contextual cues and answering questions about it reliably.

The authors count a fact as “encoded” if the model reproduces it under either of two strong contextual probes. Their reliable-answering test is stricter: it requires correct answers across all four variants, covering two phrasings and both directions of a factual relationship. That difference in the pass criteria helps shape the measured gap. Neither test directly inspects the weights.

GPT-5 and Gemini-3 pass the encoding probes for 95-98% of the benchmark’s facts, while reliable recall remains weaker. Rare facts and reverse questions are particular problems. Thinking recovers a substantial share of failures.

The study uses Wikipedia-derived facts, so it cannot tell us how often this happens with commercial brand recommendations. If a helpful cue brings an answer back, calling the fact absent is too simple. Further learning might still make the answer more reliable. I’d want to see that tested before the proposal turns into an invoice.

Ask about a named brand and you have already supplied the brand. Asking a buyer’s category question leaves the system to produce the name. I wouldn’t treat those as interchangeable evidence of visibility, and this benchmark provides no basis for doing so.

### Even Opening The Model Doesn’t Settle It

From Parameters to Answers examines the computation inside the model. The researchers ask country-continent questions, then estimate internal signals associated with the country being asked about and its continent. They remove or reverse parts of those signals while keeping the model’s weights fixed.

Researchers can read a signal before their changes to it have a detectable effect on the answer. In paired-country tests, the answer depends less on one shared request signal at later layers, while measured content still affects it. Estimate the request signal differently, though, and changing it can still affect the answer late in the computation.

The conclusion depends on which signal is measured and how it is changed. It gives us no universal diagram of how every model fetches a fact from memory. A slide labelling your problem a “recall failure” would need evidence of its own.

Even with access to the model’s internal computation, researchers have to separate what they can detect from what they can show affects the answer. Compare that with diagnosing a missing brand name from the response alone. Adding technical vocabulary to the slide doesn’t supply the missing experiment.

None of these studies measures the same thing. MemToC tests responses to conflicting tool evidence; Empty Shelves compares strongly cued reproduction with reliable answering; From Parameters intervenes on internal activations. Combining them into a tidy funnel would create a model none of the papers tested.

### The Chart Can Be Right

A company may reasonably care whether buyers encounter its name, regardless of the internal mechanism. A carefully defined sample of answers can describe an outcome worth watching. You don’t need to locate a fact inside a model to count a mention.

I have a personal contribution to this problem. Two months ago, I announced on LinkedIn that I was the “world’s most renowned AI visibility expert.” The appointment process was surprisingly quick.

Image Credit: Pedro Dias

People searching for [worlds most renowned ai visibility expert] are still finding my original post cited in Google AI Overviews. It’s probably because I am 😅.

Image Credit: Pedro Dias

Many have also been trying similar experiments of their own. Edward Sturm asked me whether this would have worked without my 20-plus years of experience in SEO and information retrieval. I told him probably not. That’s my judgement, though. The result alone doesn’t tell us what part that experience played.

The answer can explicitly describe the title as a joke I gave myself and still name me and cite the post.

A counter recording only whether my name appeared would tick that answer just as happily as an outright endorsement. Explaining why people are calling me an expert is enough to register a mention. Before putting that in an authority report, someone should probably read the sentence.

The query matters too. It repeats the distinctive wording of my post. This tells us little about whether a buyer asking an ordinary question about AI visibility would encounter me. Nor does it establish that the claim entered a model’s weights or that Google’s answer changed through the mechanism tested in MemToC.

My earlier criticism of AI visibility measurement needs that qualification. We can count appearances. We still need evidence that the sample represents buyers’ experiences, and further evidence to explain a change.

Suppose your brand appears in fewer answers this month. Repeated sampling might show that the difference is larger than ordinary variation under the tested conditions. That would establish a change in the measured outcome, while leaving its cause open.

Perhaps the model changed, or the supplied sources did . Different questions could also matter. “We appeared less often” doesn’t tell you which of those possibilities to pursue.

Get the diagnosis wrong, and a competent team can spend weeks on work that never addresses the failure. A claim that the content is inadequate will probably send the budget towards more content work . If the proposed problem is that the model hasn’t learned the brand, the conversation turns to training data .

A team can have good reasons to test an intervention before it has a complete explanation. Better learning might improve reliable recall or help correct answers survive conflicting information. Those are outcomes worth testing across different questions and conditions.

A controlled improvement would give the work a defensible commercial basis, even if the mechanism remained partly unclear. It wouldn’t automatically prove the original diagnosis. “We have a hypothesis worth testing” is a perfectly respectable starting point for a proposal.

If you’re recommending more content, show me what makes a content problem the better explanation. These papers say what they tested and where their conclusions stop. I don’t see why a commercial claim deserves an exemption.

If you’re selling me a remedy for that red cell, what evidence tells you which problem I have?

More Resources:

- Schema, LLMs & The Low Bar For ‘Evidence’ In GEO

- Your AI Visibility Tracker Is Quietly Breaking Your Analytics And Your Strategy

- Mt. Stupid Has A Pricing Page

This post was originally published on The Inference .

Featured Image: Roman Samborskyi/Shutterstock

Category SEO AI Search

Read Full Bio

Pedro Dias Independent Consultant at Visively

I help companies design systems that make their content findable — by both search engines and AI (Artificial Intelligence). I’m ...

## 原文链接

[Read original](https://www.searchenginejournal.com/it-was-there-a-minute-ago/589500/)
