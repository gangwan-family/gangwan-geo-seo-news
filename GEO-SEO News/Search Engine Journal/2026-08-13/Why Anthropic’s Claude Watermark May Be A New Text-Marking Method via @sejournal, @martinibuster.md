---
title: "Why Anthropic’s Claude Watermark May Be A New Text-Marking Method via @sejournal, @martinibuster"
source: "Search Engine Journal"
published: 2026-08-13T15:23:00+00:00
fetched_at: 2026-08-13T22:08:47.953145+00:00
url: "https://www.searchenginejournal.com/why-anthropics-claude-watermark-may-be-a-new-text-marking-method/585703/"
guid: "https://www.searchenginejournal.com/why-anthropics-claude-watermark-may-be-a-new-text-marking-method/585703/"
author: "Roger Montti"
categories:
  - "AI Search"
  - "Content Creation"
  - "News"
---

# Why Anthropic’s Claude Watermark May Be A New Text-Marking Method via @sejournal, @martinibuster

- Source: Search Engine Journal
- Published: 2026-08-13
- URL: https://www.searchenginejournal.com/why-anthropics-claude-watermark-may-be-a-new-text-marking-method/585703/
- Author: Roger Montti
- Categories: AI Search, Content Creation, News

## RSS 摘要

Anthropic has revealed enough about Claude's watermark to identify how it might work. A new research paper may be the clue. The post Why Anthropic’s Claude Watermark May Be A New Text-Marking Method appeared first on Search Engine Journal .

## 原文正文

Why Anthropic's Claude Watermark May Be A New Text-Marking Method Skip to content

SEJ Live: AI Search Visibility for Local Business

Register Now

- SEJ

- ⋅

- AI Search

## Why Anthropic’s Claude Watermark May Be A New Text-Marking Method

Claude's watermark is still a secret, but Anthropic has disclosed enough details to pin down how it might work.

Several research papers align closely to Anthropic’s newly announced text watermarking. One research paper stands out because it is a very close match to everything Claude has disclosed so far, including brand new information recently published on Anthropic’s Transparency page.

### Clues To Anthropic’s Watermarking

There are two pages on Anthropic’s website that offer clues to what their watermarking algorithm is and how it works.

The first set of clues are on the official watermarking announcement which details six qualities of the watermarking technology. The second page shares that the technology was developed at a university. Together, both sets of clues help identify a strong candidate for the technology.

### Six Qualities Of Anthropic’s Watermarking

Here are the six qualities of Anthropic’s watermarking:

- It’s embedded directly into the generated text

- It cannot be perceived by looking at the text.

- The watermark does not change the “meaning, quality, or readability” of the generated text.

- The watermarking is generated at the model level.

- It may be detected after the text has been edited.

- Users and third parties will be able to detect it.

### Second Clue: Developed At A University

There’s another clue buried away in Anthropic’s transparency page . That web page was updated on July 23rd. The new version contains the following brand new clue:

“We have worked across industry and academia to explore and stay abreast of technological developments for watermarking and are preparing for compliance with applicable laws by the relevant legal deadlines.”

That wording did not exist prior to July 23rd, as can be verified on Archive.org .

The previous version of that section used to say that Anthropic did not provide watermarking.

#### Previous Version

“Transparency of AI Generation

Claude currently has multimodal input capabilities and text-based outputs, including text-based artifacts and text-to-speech voice output. While watermarking is most commonly applied to image outputs, which we do not currently provide, we continue to work across industry and academia to explore and stay abreast of technological developments in this area.”

#### Universities License Technology

Many people assume that technology companies build and patent their own technologies. But the reality is that university researchers can offer to license the technologies they develop and receive royalty payments from it. And that’s what may be happening here because Anthropic’s web transparency page says they’re working with industry and academia. And in the case of a technology called MirrorMark, the researchers are members of both industry and academia.

### Unbiased Watermarking

There is an approach to watermarking that’s called unbiased watermarking. An example is in a research paper from 2025 about MCmark. MCmark is an unbiased watermarking method that embeds a hidden statistical signal into AI-generated text during token generation. It preserves the model’s original output distribution, so text quality stays mostly unchanged. The watermark can later be detected without access to the original prompt or model API, and it is designed to remain detectable after some text modification.

MCmark is a strong candidate for Anthropic’s watermarking. If I’m going to rate it on a scale of one to five for likeliness of it being a match, I’d give it a score of 4.5. The reason I deduct a half point is that paraphrasing can drop the true-positive rate (TPR) to 11% with a false positive rate (FPR) of 1%. Under GPT rephrasing it scored 48% TPR and 1% FPR.

There is another approach called MirrorMark that can remain detectable with paraphrasing, although with heavy paraphrasing the true-positive rate can drop to about 57.8% with a 1% false positive rate. But that’s kind of expected, given that paraphrasing rewrites the AI-generated text. The point is that MirrorMark may be more resilient against adversarial tricks to defeat the watermarking than MCmark, although it has to be noted that the two papers did not use exactly the same testing methods.

MirrorMark is a close match for what Anthropic described and is distinctive because it mirrors the LLM’s random sampling in text generation.

The research paper explains:

“Experiments show that MirrorMark matches the text quality of non-watermarked generation while achieving substantially stronger detectability: with 54 bits embedded in 300 tokens, it improves bit accuracy by 8–12% and correctly identifies up to 11% more watermarked texts at 1% false positive rate.”

### MirrorMark: A Distortion-Free Multi-Bit Watermark for Large Language Models

A 2026 research paper from George Mason University describes a unique approach called MirrorMark. The team that published MirrorMark were also responsible for a 2025 watermarking approach called StealthInk, which I investigated as well, but discovered it made a tradeoff that made it less reliable in short sequences of text.

### InvisibleID And Commercialization

MirrorMark is a close match to Anthropic’s announcement because it matches Anthropic’s six watermarking qualities. And perhaps not coincidentally, all three researchers involved with MirrorMark are part of George Mason’s InvisibleID, an entity for commercializing that technology. So that’s another clue that MirrorMark could be available for licensing.

### Overview Of How MirrorMark Works

MirrorMark is a technology that inserts a watermark without disturbing the token choice patterns of the LLM. The generated text remains indistinguishable from non-watermarked text. Surviving editing and paraphrasing (insertions, deletions, and substitutions), with the use of what they call CABS, are one of the design goals of MirrorMark. And, similar to what Anthropic described, the watermark is inserted at the point of text generation.

The research paper explains:

“CABS not only reduces the risk of empty or highly imbalanced allocations but also improves resilience to editing operations such as insertion, deletion, and substitution.”

MirrorMark influences the generative AI’s token choices so that the generated text contains a hidden statistical pattern that repeats, which is the watermark. The system works in three steps.

The watermark is not something that is visible and it’s not a hidden character. It’s a statistical pattern that’s inserted at the moment of token selection.

Step 1: Mirroring

LLMs don’t simply choose the likeliest next word. There’s a certain amount of random sampling that happens when the AI chooses the next word in a sequence. MirrorMark takes advantage of this aspect of how words are chosen by mirroring the random sampling in order to insert a specific symbol, without noticeably changing the quality or meaning of the text.

Step 2: Context-Anchored Balanced Scheduler (CABS)

CABS chooses which “symbol” is inserted at each step of the process of text generation. The placement of the symbol is tied to the surrounding context, which makes the pattern harder to disrupt.

Step 3: Detecting The Watermark

A decoder uses CABS to “replay” the process and recover the “token-to-position assignments,” and all the decoded values together are used to detect the watermark.

This is how the paper describes the process:

“In this paper, we propose a multi-bit and distortion-free watermarking framework, MirrorMark, which combines three complementary components to embed and recover multi-bit messages without altering the output distribution of LLMs.

First, a mod-1 mirroring transformation encodes an m-bit symbol by reflecting each u value around a message-specific pivot.

Next, the Context-Anchored Balanced Scheduler (CABS) determines which symbol is embedded at each generation step by mapping tokens to message positions in a balanced and context-dependent manner.

Finally, during decoding, CABS is replayed to recover token-to-position assignments, each symbol is decoded from the mirrored u values using the appropriate score function, and all decoded values over the tokens are aggregated to detect the watermark.”

### How Closely Does MirrorMark Match Anthropic’s Six Watermarking Qualities?

1. It’s embedded directly into the generated text.

MirrorMark embeds the watermark at the token generation point. As explained earlier, an LLM does not choose the likeliest next word in a sequence of words. It chooses the next word in a sequence with a randomness factor (the sampling randomness). MirrorMark modifies the sampling randomness that is used to choose each next token. This is why it’s called MirrorMark: the paper says the encoder mirrors the “sampling randomness.”

2. It cannot be perceived by looking at the text because it’s an “imperceptible watermark”

MirrorMark is a distortion-free watermark approach to text. Its main claim is that it embeds the watermark without changing the token probability distribution. The generated text remains statistically the same as the regular text generation.

3. The watermark does not change the “meaning, quality, or readability” of the generated text.

MirrorMark strongly matches this quality. The research paper says MirrorMark “preserves natural linguistic diversity.” This is by design.

4. The watermarking is “applied at the model level”

MirrorMark does its work during the text generation part, not afterward. It happens as the text is generated.

5. The watermark may still be detected after the text has been edited.

MirrorMark was tested with copy-paste, deletion, insertion, paraphrasing, and substitution. The research paper says “improves resilience” to deletion, insertion, and substitution. As for paraphrasing, it says that it “maintains strong separability between watermarked and non-watermarked samples …since paraphrasing changes the surface form of sentences but often preserves underlying semantic and statistical patterns that still carry weak watermark signals. ” That means that the watermark signal is still there and can be detected.

6. Users and third parties will be able to detect it.

The research paper says that the watermark is detectable in the text when it’s decoded.

The paper explains:

“Finally, during decoding, CABS is replayed to recover token-to-position assignments, each symbol is decoded from the mirrored u values using the appropriate

score function, and all decoded values over the tokens are aggregated to detect the watermark.”

There is an entire section of the research paper that is devoted to decoding and detection of the watermark (section 3.3), where it says:

“The text is declared watermarked if the score exceeds a predefined threshold.”

### Is This Claude’s Watermarking Solution?

Claude is understandably not explaining what the solution is that they’re using. The value of understanding MirrorMark is that it shows that there are alternate methods of watermarking that go beyond statistical patterns in the generated text and instead embed the watermark in the randomness used to choose each next token.

It may very well be that what Claude is using is something closer to MCmark or something else entirely. But MirrorMark is worth looking into simply because of the way it goes about watermarking.

The InvisibleID web page has information about other watermarking approaches, too. The 2026 MirrorMark paper can be accessed here . StealthInk, a 2025 paper by the MirrorMark researchers, can be read here . And the 2025 MCmark research can be read here .

Featured Image by Shutterstock/Melinda Nagy

Category News AI Search Content Creation

Read Full Bio

SEJ STAFF Roger Montti Owner - Martinibuster.com at Martinibuster.com

I have 25 years hands-on experience in SEO, evolving along with the search engines by keeping up with the latest ...

## 原文链接

[Read original](https://www.searchenginejournal.com/why-anthropics-claude-watermark-may-be-a-new-text-marking-method/585703/)
