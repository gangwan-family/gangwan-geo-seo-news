---
title: "Introducing the Agents API"
source: "OpenAI News"
published: 2026-09-10T00:00:00+00:00
fetched_at: 2026-09-10T23:17:04.219816+00:00
url: "https://openai.com/index/introducing-the-agents-api"
guid: "https://openai.com/index/introducing-the-agents-api"
categories:
  - "Product"
---

# Introducing the Agents API

- Source: OpenAI News
- Published: 2026-09-10
- URL: https://openai.com/index/introducing-the-agents-api
- Categories: Product

## RSS 摘要

Build and launch cloud agents with the Agents API, a managed service powered by the Codex harness for orchestration, long-running sessions, and tool use.

## 原文正文

Introducing the Agents API | OpenAI

Try ChatGPT (opens in a new window)

- Foundation (opens in a new window)

Try ChatGPT (opens in a new window)

OpenAI

September 10, 2026

Product API

## Introducing the Agents API

Build and run cloud agents with the Codex harness, fully managed by OpenAI.

Loading…

As we’ve scaled Codex and ChatGPT for Work to millions of people around the world, we’ve learned what it takes to make long-running agents work well in practice. Useful agents need a powerful harness that manages context, uses tools efficiently, and coordinates subagents. They also need infrastructure that keeps them running reliably for days, with environments where they can work with files, run code, and save intermediate results.

Today, we’re introducing the Agents API ⁠ (opens in a new window) in public beta, bringing that same harness and infrastructure that powers Codex to developers through a simple, flexible API.

### Build cloud agents with a single API call

With the Agents API, you can create a production-ready agent in a single API call by specifying the task, model, tools, and environment:

##### JavaScript

import OpenAI from "openai" ;

const client = new OpenAI ();

const session = await client. beta . agents . sessions . create ({

agent : {

model : "gpt-6-astra" ,

tools : [

type : "mcp" ,

server_label : "observability" ,

transport : {

type : "http" ,

server_url : "https://observability.example.com/mcp" ,

multi_agent : { enabled : true , max_concurrent_subagents : 3 },

vault_ids : [ "vault_YOUR_VAULT_ID" ],

environment : {

type : "openai_hosted" ,

capability_directories : [ "/workspace/capabilities/skills" ],

input :

"Investigate service-api’s elevated 5xx rate over the last 30 minutes. " +

"Delegate deployment, error, and dependency analysis to subagents. " +

"Save findings, evidence, and recommended mitigation in /workspace/outputs." ,

});

OpenAI hosts and maintains the harness. You choose the agent’s compute environment: in an OpenAI-managed sandbox, on your own infrastructure, or with one of our sandbox partners. The Agents API gives you a strong foundation for building agents on top of our optimized agent harness and infrastructure, so you can focus on the tools, knowledge, and workflows that make your agent unique.

Agents API powers your agents with the same harness and infrastructure behind Codex.

### What our customers are saying about Agents API

1 of 8

“With the Agents API, our evaluation score went from 0.71 to 0.85. The subagent support in the API is great and drastically sped up our workflow. Previously it was pretty cumbersome to observe and orchestrate subagents in our old setup but the new APIs gave us a 4x latency reduction. We spent a long time trying to optimize for this and the subagent flows were a huge out-of-the-box lift.”

Jack Weissenberger, CTO, Ciridae

“Transforming real-world businesses means deploying AI into workflows of every shape. Agents API supplies the harness; the environment, context, and UX stay ours. With our AI platform Nexus we now stand up agents in hours across industries, from residential services to architecture.”

Rasmus Wissmann, CTO, Long Lake

“The Agents API has enabled us to think differently about how we can architect complex, multi-step workflows. We used to write prompt chains and manage our own set of tool calls, but now we can use agents directly in our code much like how Codex works on your laptop. It’s already helped us solve several problems that would’ve otherwise required us to build custom agent infrastructure.”

Cole Striler, Director of Engineering, WithCoverage

“After migrating our case review workflow to the Agents API, we saw a 60% reduction in cost per case, lower latency, and significantly improved token efficiency while maintaining existing performance.”

Bhavyansh Sabharwal, Member of Technical Staff, SafetyKit

“What stood out in our testing was how naturally the Agents API handled bursty workloads. We could fan out work across hundreds of agents, run them asynchronously, and collect the results later, without keeping infrastructure idle between peaks.”

Dmitry Khanukov, Co-founder & CTO, Dwelly

“Earning customers’ trust is critical in financial services. OpenAI’s Agents API enables us to build more reliable agents, giving customers the confidence to use them in production. By separating the agent harness from the sandbox, we reduced failed agent responses by 86%.”

Serhii Shchoholiev, Lead Engineer, Hypha

“The Agents API handled the implementation, independent review, remediation, and real-browser validation in a real, active repository. Overall, the agent’s engineering quality was very strong.”

Maks Operlejn, Senior ML Engineer, deepsense.ai

“At Nash, we deploy thousands of long-running AI agents that manage hundreds of millions of deliveries across global logistics networks. OpenAI’s Agents API gives us the durable session and orchestration layer we need for agents operating continuously in production managing context, recovery, and multi-step execution, while Nash provides the tools and execution environment that connect them to the physical world. This lets our agents reason, act, recover, and collaborate across complex workflows that can span hours or days. These agents are production infrastructure running mission-critical logistics operations for our partners.”

Aziz Alghunaim, Co-founder & CTO, Nash.ai

### Choose your agent environment

Different workloads need different compute, storage, and deployment options. The Agents API lets you choose a sandbox that fits your application.

We’re partnering with ecosystem providers ⁠ (opens in a new window) , including Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, and Vercel, to provide first-class integrations for a range of needs:

- Fully managed environments or deployments within your VPC

- Specific file and secret storage mechanisms

- Different CPU, GPU, and memory configurations, with performance, cold-start, and cost profiles to match your company’s workflow.

The Agents API offers first-class integrations with popular ecosystem providers.

### OpenAI hosted sandboxes

For developers who want to get started quickly and scale efficiently, we’re also introducing the OpenAI hosted sandbox ⁠ (opens in a new window) . This leverages the same sandboxing infrastructure that powers Codex and ChatGPT.

OpenAI provisions and manages the sandbox, giving your agent a secure and performant environment to run code, work with files, and produce artifacts. These sandboxes can be flexibly configured with your files, packages, skills and plugins to give the agent what it needs to complete the task.

### Build with an evolving Codex harness

Taking advantage of new model capabilities often means reworking your harness, taking valuable time away from improving your application. The Agents API provides versioned access to these capabilities with each model launch. We maintain and continuously improve the harness alongside our models, helping your agents get better performance from every upgrade. For example, recent improvements to the harness include:

#### Keep agents working across long sessions

To support models working for hours, we’ve built context management that helps agents carry relevant information across longer sessions. The Agents API automatically compacts ⁠ (opens in a new window) earlier context as a session approaches its context limit, preserving information the agent needs to continue. Developers can build workflows that span multiple context windows without implementing their own compaction logic.

#### Help agents efficiently use more tools

The Agents API helps agents find the right tools and use them efficiently. Tool search ⁠ (opens in a new window) loads relevant tool definitions as needed, helping reduce token usage and cost while preserving the model’s cache. Once tools are available, programmatic tool calling ⁠ (opens in a new window) lets agents run calls in parallel, chain related operations, and filter or combine results in code so they can work through large volumes of data while bringing only the relevant results back into context. The Agents API supports MCP, custom functions, and built-in tools like web search.

##### JSON

"agent" : {

"tools" : [

"type" : "mcp" ,

"server_label" : "openai_docs" ,

"transport" : {

"type" : "http" ,

"server_url" : "https://developers.openai.com/mcp"

} ,

#### Let agents parallelize work with subagents

With multi-agent support ⁠ (opens in a new window) , the Agents API can break complex tasks into independent pieces and delegate them to subagents that work in parallel. Each subagent maintains its own context, helping it stay focused on its assignment, while the main agent coordinates their work and brings the results together. This can speed up research, analysis, and coding tasks that benefit from parallel work, without requiring you to build your own orchestration.

##### JSON

"agent" : {

"model" : "gpt-6-astra" ,

"multi_agent" : {

"enabled" : true ,

"max_concurrent_subagents" : 3 ,

### An open-source foundation

The Agents API is powered by the open-source Codex harness, giving developers visibility into the core logic that coordinates model calls, tools, and context. With the Agents API, OpenAI operates and maintains that harness while developers can inspect and learn from its public codebase ⁠ (opens in a new window) .

### Start building

Agents API is available in public beta today to all developers. There are no additional fees for using the Agents API – you simply pay for the tokens and tools your agents use, as outlined on our pricing page ⁠ (opens in a new window) .

Explore the Agents API overview ⁠ (opens in a new window) to learn more, or follow the quickstart ⁠ (opens in a new window) to get started and bring the harness behind Codex into your own agents.

During the public beta, we’ll iterate quickly based on your feedback as we work toward general availability. Let us know what’s working, where you’re running into friction, and what you need to build and run your agents in production.

- API

- Codex

- 2026

### Author

OpenAI

### Keep reading

View all

Now everyone can put data to work

Product Sep 10, 2026

Introducing ChatGPT for Financial Services

Product Sep 10, 2026

Build more natural voice experiences with GPT‑Live‑1 in the API

Product Sep 10, 2026

## 原文链接

[Read original](https://openai.com/index/introducing-the-agents-api)
