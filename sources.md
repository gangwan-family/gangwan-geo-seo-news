---
layout: default
title: "数据源"
description: "GEO-SEO News 的数据来源"
---

<div class="hero">
  <h1>数据源</h1>
  <p>当前同步的文章来源，所有链接均指向原始发布页面</p>
</div>

<div class="container">
  <div class="source-grid">
    <div class="source-card">
      <h3>Google Search Central Blog</h3>
      <div class="meta">https://developers.google.com/search/blog/</div>
      <a class="btn" href="https://developers.google.com/search/blog/" target="_blank">访问网站 →</a>
      <div class="meta" style="margin-top:10px; font-size:12px;">
        收录文章：{{ site.posts | where:"source", "Google Search Central Blog" | size }} 篇
      </div>
    </div>
    <div class="source-card">
      <h3>OpenAI News</h3>
      <div class="meta">https://openai.com/news</div>
      <a class="btn" href="https://openai.com/news" target="_blank">访问网站 →</a>
      <div class="meta" style="margin-top:10px; font-size:12px;">
        收录文章：{{ site.posts | where:"source", "OpenAI News" | size }} 篇
      </div>
    </div>
    <div class="source-card">
      <h3>Search Engine Journal</h3>
      <div class="meta">https://www.searchenginejournal.com/</div>
      <a class="btn" href="https://www.searchenginejournal.com/" target="_blank">访问网站 →</a>
      <div class="meta" style="margin-top:10px; font-size:12px;">
        收录文章：{{ site.posts | where:"source", "Search Engine Journal" | size }} 篇
      </div>
    </div>
    <div class="source-card">
      <h3>Google AI Blog</h3>
      <div class="meta">https://blog.google/innovation-and-ai/technology/ai/</div>
      <a class="btn" href="https://blog.google/innovation-and-ai/technology/ai/" target="_blank">访问网站 →</a>
      <div class="meta" style="margin-top:10px; font-size:12px;">
        收录文章：{{ site.posts | where:"source", "Google AI Blog" | size }} 篇
      </div>
    </div>
    <div class="source-card">
      <h3>Semrush Blog</h3>
      <div class="meta">https://www.semrush.com/blog/</div>
      <a class="btn" href="https://www.semrush.com/blog/" target="_blank">访问网站 →</a>
      <div class="meta" style="margin-top:10px; font-size:12px;">
        收录文章：{{ site.posts | where:"source", "Semrush Blog" | size }} 篇
      </div>
    </div>
  </div>
  
  <div style="margin-top:40px; padding-top:24px; border-top:1px solid var(--border);">
    <h3 style="font-size:16px; margin-bottom:12px;">原始数据</h3>
    <p style="color:var(--muted); font-size:14px;">
      所有原始 markdown 文件存放在 <code>GEO-SEO News/</code> 目录下，可按来源和日期浏览。
      <a href="{{ '/GEO-SEO News/' | relative_url }}" target="_blank">查看原始数据 →</a>
    </p>
  </div>
</div>
