---
layout: default
title: "原始数据"
description: "GEO-SEO News 原始 Markdown 归档目录"
permalink: /GEO-SEO News/
---

<div class="container page-shell">
  <section class="page-intro">
    <p class="page-eyebrow">Raw archive</p>
    <h1>原始数据</h1>
    <p class="page-summary">这里保留工作流抓取后的原始 Markdown 归档，按来源和发布日期存放，适合排查抓取结果或直接查看原始文件结构。</p>
    <div class="page-stats">
      <span>{{ site.data.sources.sources | size }} 个来源</span>
      <span>{{ site.posts | size }} 篇文章</span>
      <span>按日期目录归档</span>
    </div>
  </section>

  <section class="raw-archive-note">
    <div class="raw-archive-block">
      <h2>目录结构</h2>
      <pre><code>GEO-SEO News/
  &lt;blog 来源&gt;/
    &lt;YYYY-MM-DD&gt;/
      &lt;blog 标题&gt;.md</code></pre>
      <p>例如：<code>GEO-SEO News/OpenAI News/2026-07-20/Safety and alignment in an era of long-horizon models.md</code></p>
    </div>

    <div class="raw-archive-block">
      <h2>当前来源</h2>
      <div class="raw-source-list">
        {% for source in site.data.sources.sources %}
        <article class="raw-source-item">
          <div class="raw-source-head">
            <h3>{{ source.name }}</h3>
            <span class="tag">{{ site.posts | where: "source", source.name | size }} 篇</span>
          </div>
          <p class="raw-source-url">{{ source.homepage }}</p>
        </article>
        {% endfor %}
      </div>
    </div>

    <div class="raw-archive-block">
      <h2>同步说明</h2>
      <p>来源配置保存在 <code>_data/sources.json</code>。抓取脚本会读取 RSS 或 XML，只写入新增文章，去重状态保存在 <code>_state/seen.json</code>。</p>
      <p>工作流默认同步最近 7 天内发布的文章，并限制每个来源每次最多写入 20 篇。</p>
      <p>若原文正文抓取失败，归档文件中会保留失败原因，后续运行会继续尝试补抓。</p>
    </div>

    <div class="raw-archive-block">
      <h2>手动同步</h2>
      <pre><code>rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py</code></pre>
      <p>只预览不写入：</p>
      <pre><code>rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py --dry-run</code></pre>
      <p>临时扩大抓取范围：</p>
      <pre><code>rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py --lookback-days 30 --max-per-source 50</code></pre>
    </div>
  </section>
</div>
