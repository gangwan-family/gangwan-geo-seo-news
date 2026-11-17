---
title: "Strengthening the fight against online child sexual abuse with new tools and support"
source: "OpenAI News"
published: 2026-11-16T17:00:00+00:00
fetched_at: 2026-11-17T04:02:00.145005+00:00
url: "https://openai.com/index/strengthening-online-child-safety"
guid: "https://openai.com/index/strengthening-online-child-safety"
categories:
  - "Safety"
---

# Strengthening the fight against online child sexual abuse with new tools and support

- Source: OpenAI News
- Published: 2026-11-16
- URL: https://openai.com/index/strengthening-online-child-safety
- Categories: Safety

## RSS 摘要

New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.

## 原文正文

Strengthening the fight against online child sexual abuse with new tools and support | OpenAI

Try ChatGPT (opens in a new window)

- Foundation (opens in a new window)

Try ChatGPT (opens in a new window)

OpenAI

November 16, 2026

Safety

## Strengthening the fight against online child sexual abuse with new tools and support

New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.

Today, we’re releasing a new tool to detect child sexual abuse material (CSAM), interventions that interrupt harmful behavior and point people toward help, practical resources for developers, and support for child-safety law enforcement investigators. These efforts build on our Child Safety Blueprint and our ongoing work to detect, block, and report abuse . For parents, the goal is simple: technology that helps keep children safe, with people in control.

It is well ⁠ (opens in a new window) established ⁠ (opens in a new window) that combatting online child predators requires coordination across many organizations. Individual companies like OpenAI have a responsibility to prevent our technology from being exploited by predators to harm children, and we also must work together with the broader industry, child safety organizations and law enforcement to advance our collective efforts to protect children online.

### Helping more organizations detect abusive material

We’re building on our current protections with the release of a new image classifier that can detect potential CSAM, including AI-generated material. This new classifier looks for visual signs of abuse, helping teams identify novel images that may not have been seen before. It returns scores that help reviewers decide which images may need attention first. This is the first CSAM classifier with broad availability that has a specific signal on indicating if CSAM may be AI generated.

Our teams trained, evaluated, and designed the classifier for real-world deployment with assistance from the National Center for Missing and Exploited Children (NCMEC) ⁠ (opens in a new window) , a nonprofit that operates the CyberTipline, a centralized reporting hub for the online exploitation of children.

We’re offering access to the classifier to vetted organizations through the OpenAI API at no cost, making CSAM detection more accessible to child safety organizations and the broader industry, including those with teams of varying sizes.

Child safety is an industry-wide issue that requires strong collaboration across organizations and a variety of solutions. We’ve engaged the Tech Coalition ⁠ (opens in a new window) and ROOST ⁠ (opens in a new window) to help us share access to this new tool, and we are strong supporters of tools developed by others such as Thorn’s Safer ⁠ (opens in a new window) CSAM detection system. In addition, we recently began participating in the Tech Coalition's Lantern program ⁠ (opens in a new window) , where we will share and receive signals relating to online child sexual exploitation and abuse to strengthen cross- platform collaboration.

We’ve tested the classifier internally and with early partners to measure how much abusive material it detects, how often it flags other images, and how it can support safety teams. Their feedback helped us identify weaknesses and improve the system.

#### Results

Early tests suggest the classifier can help reviewers focus on abusive images while reducing review of false positives. In an evaluation of user-uploaded images, we compared the new classifier with our current protections and found:

The new classifier could reduce review work: we estimated that it would flag 48% fewer images while finding roughly the same number of abusive images as the existing tool.

Images flagged by the new classifier were about twice as likely to contain abuse.

Early access partners have also evaluated how the classifier supports their own safety teams. In fal ⁠ (opens in a new window) ’s testing on human-reviewed production images, reviewers confirmed 72% of the classifier’s high-confidence flags as novel CSAM. invideo AI ⁠ (opens in a new window) ’s testing showed one in four flagged cases led to a ban. In SafetyKit ⁠ (opens in a new window) ’s evaluations involving drawings or animations that sexualize children, the classifier detected 90% of cases.

More information about the classifier is available in the CSAM classifier model card ⁠ (opens in a new window) . Organizations interested in the classifier will be able to request access through our intake form ⁠ . We’ll continue improving the classifier with feedback from those that use it.

### Interrupting harmful behavior and pointing people toward help

We already prohibit CSAM , train our models to refuse requests for it, and take action against accounts that violate our policies. We’re building on those safeguards with new product warnings in ChatGPT that interrupt attempts to find abusive material, explain the consequences, and point people toward help to stop harmful behavior.

The warning makes clear that sexualizing children causes harm, including when the requested material is AI-generated. Alongside the warning, we’ll remove the flagged conversation and pause access to ChatGPT for 24 hours, while keeping specialist support available to help people stop harmful behavior. Repeated violations may lead to longer restrictions and ultimately account closure or reports to authorities.

We developed this approach with input from organizations and academic advisors that research and develop programs to prevent child sexual abuse, including Protect Children ⁠ (opens in a new window) , the Lucy Faithfull Foundation ⁠ (opens in a new window) , Dr. Caoilte Ó Ciardha, Researcher & Honorary Reader in Forensic Psychology at the University of Kent and Joel Scanlan at the University of Tasmania, who independently evaluated a trial ⁠ (opens in a new window) of deterrent messages.

### Practical support for developers

The protection of children online doesn’t end with detection. We’ve published CSAM guidance ⁠ (opens in a new window) to give developers practical steps to prevent abuse, detect harmful content, and act on it. Developed with input from the Tech Coalition ⁠ (opens in a new window) , Thorn ⁠ (opens in a new window) , NCMEC ⁠ (opens in a new window) , and the Internet Watch Foundation ⁠ (opens in a new window) , it is designed for organizations at different stages of building their safety systems.

The guidance provides clear rules, ways for users to report concerns, detection tools, and processes for reviewing and reporting suspected abuse. It also explains how safety identifiers can help developers connect misuse to individual users and how to support the people reviewing sensitive content. Developers can use it alongside tools such as our new image classifier, Moderation API ⁠ (opens in a new window) , ROOST’s self-hosted review console Coop ⁠ (opens in a new window) , and dedicated CSAM detection services such as Thorn’s Safer ⁠ (opens in a new window) .

Our commitment to collaboration and supporting the broader developer ecosystem also is reflected in our work with Anthropic and Google to jointly commission new guidance on responding to disclosures of child sexual exploitation and abuse in AI systems. Recently published by the Tech Coalition ⁠ (opens in a new window) , this guidance provides developers with practical recommendations for addressing these sensitive situations.

We’ve already seen this guidance lead to increased numbers of developers accessing child safety tooling and registering to report CSAM to NCMEC.

### Supporting child-safety law enforcement units

Protecting children also means supporting the specialist child safety investigators working to find victims and stop abuse. As we’ve discussed publicly with Thorn ⁠ (opens in a new window) , AI can help investigators organize and prioritize information and reduce unnecessary exposure to abusive material.

We’re also supporting child-safety law enforcement units with new tools and trainings on how to use AI in their investigations, including dedicated plugins, investigative tools, and complex data analysis, with access managed by program administrators. At launch, the first tool will help investigators review lengthy chat logs and legal process returns, identify potential connections, and create timelines, with findings linked to source material.

The initial training is planned as an overview and demonstration, supported by a practical field guide that teams can refer to afterward. It will introduce the tools and how they fit into investigative work. Access will depend on agency authorization and program requirements. Future iterations of the training will be proposed at regional, national and international conferences.

### Continuing the work together

These efforts share one goal: preventing harm to children and strengthening the response when abuse occurs. We’ll continue improving our safeguards while empowering child protection organizations, developers, researchers, and investigators with the tools, resources, and expertise they need to protect children, combat exploitation, and bring perpetrators to justice. By working together, we can harness the power of AI to make a meaningful difference in the fight against child sexual exploitation and abuse.

- 2026

- User Safety & Control

### Author

OpenAI

### Keep reading

View all

Our first phase of embedded assessments

Safety Nov 16, 2026

Control Room: A new way to track and stop AI workloads

Safety Nov 9, 2026

GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

Product Nov 5, 2026

“ Technology has an essential role to play in helping identify child sexual abuse material (CSAM) and, ultimately, the children who may be depicted in it. This new classifier gives more organizations access to tools that can help detect previously unidentified CSAM, strengthen reporting and provide critical information to those working to identify and protect victims. We’re grateful for OpenAI's investment to develop technology that strengthens the broader child safety ecosystem. ”

—John Shehan, Senior Vice President, National Center for Missing & Exploited Children ⁠ (opens in a new window)

“ Protecting children from sexual abuse and exploitation in the digital age requires more than any single solution or organization. It takes multiple layers of protection to disrupt harmful behavior online while equipping investigators with tools to identify endangered children. We commend OpenAI for taking steps across these areas and working with organizations throughout the child protection ecosystem. Bringing together technology, expertise, and collaboration, will be foundational to creating a safer digital world. ”

—Melissa Stroebel, Vice President Research and Strategic Impact, Thorn ⁠ (opens in a new window)

“ To protect children from online sexual exploitation and abuse, companies need to work together. Through the Tech Coalition, teams across the industry are learning from each other and tackling shared child safety challenges. OpenAI’s team is an active contributor to this work, sharing tools and helping develop guidance that other companies can use. We’re glad to have OpenAI as such an engaged member of the Tech Coalition and our Board. ”

—Dr. Erin Saltman, President & CEO, Tech Coalition ⁠ (opens in a new window)

“ Child safety tools need to recognize abuse across different types of content. In our testing, OpenAI’s classifier is the best we’ve seen, catching unknown CSAM that hash matching misses, including strong performance on drawings and animations, with false positives below 1% on legal adult content. These encouraging results point to broader protection against harmful content while limiting disruption for legitimate users. ”

—Samuel Wang, Member of Technical Staff, SafetyKit ⁠ (opens in a new window)

“ The OpenAI classifier model helps us zero in on the cases that actually matter. Instead of wading through a pile of false positives, our trust and safety team gets a smaller, sharper set of cases to review, and a lot more of them turn out to need action. We want invideo to be a safe place to create content, and this helps us get there. ”

—Kirkston Dsouza, Product Manager, invideo AI ⁠ (opens in a new window)

“ For our safety team, a flag needs to provide a useful signal about where to focus attention. OpenAI’s classifier’s high-confidence flags gave us confidence in its potential to help our team identify previously unseen abusive material as our platform grows. ”

—Antonina Vykhrest, Director of Child Safety, fal ⁠ (opens in a new window)

“OpenAI’s moderation classifier has become a cornerstone of HeyGen’s child safety program. It gives our team a fast, reliable signal on harmful content, so we can act quickly and with confidence.”

—Mutasim Chowdhury, Engineer, HeyGen ⁠ (opens in a new window)

“Adobe is deeply committed to keeping children safe online. Continued innovation and collaboration with companies like OpenAI strengthen existing safeguards and give platforms more tools to detect harmful content.”

—Michael Draper, Vice President, Global Consumer Trust, Adobe ⁠ (opens in a new window)

“ OpenAI has deployed a best-practice example in ChatGPT of how a platform can deter and disrupt harmful online behaviours. OpenAI has engaged multiple external experts who have previously designed and evaluated warning messages, built the intervention with them through evidence-based co-design, and aims to redirect users to local support options in as many jurisdictions as possible. This has given the warnings the best chance of steering users away from harm and towards support. ”

—Joel Scanlan, Associate Professor, CSAM Deterrence Centre ⁠ (opens in a new window)

“ We know from our deterrence work that a warning succeeds or fails on timing, accuracy and tone. OpenAI has taken real care with all three. It’s a warning that interrupts people at the moment of risk, speaks plainly about the consequences, and points them to help. Importantly, the response becomes stronger when risky behaviour continues. Our Stop It Now helpline already regularly hears from people who say an AI chatbot sent them to us. Now that route to help is going global, connecting people to support in their own country. Every person who reaches out instead of acting on their impulses is a child protecte d. ”

—Frances Frost, Director of Advocacy and Communications, Lucy Faithfull Foundation ⁠ (opens in a new window)

“ As state attorneys general on the AI Task Force, our first priority is protecting kids. That needs to be the first priority of tech companies too. We must increase our defenses, and OpenAI and other tech companies must be thinking about and working around the clock to prevent synthetic child sex abuse material. We need to keep our children safe. ”

—Jeff Jackson, North Carolina Attorney General

## 原文链接

[Read original](https://openai.com/index/strengthening-online-child-safety)
