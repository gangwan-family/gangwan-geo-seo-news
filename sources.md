---
layout: default
title: "数据源"
description: "GEO-SEO News 的数据来源"
---

<div class="container page-shell">
  {% assign source_docs = site.data.sources.sources %}
  <section class="page-intro">
    <p class="page-eyebrow">Source directory</p>
    <h1>数据源</h1>
    <p class="page-summary">当前同步的文章来源目录。每个来源都保留官方入口，并展示最近收录的文章。</p>
    <div class="page-stats">
      <span>{{ source_docs | size }} 个来源</span>
      <span>{{ site.posts | size }} 篇文章</span>
    </div>
  </section>

  <section class="source-index">
    {% for source in source_docs %}
    {% assign source_posts = site.posts | where: "source", source.name | sort: "date" | reverse %}
    {% assign latest_post = source_posts | first %}
    <article class="source-item">
      <div class="source-item-head">
        <div class="source-name-block">
          <h2><a class="source-title-link" href="{{ '/source/' | append: source.slug | append: '/' | relative_url }}">{{ source.name }}</a></h2>
          <p class="source-homepage">{{ source.homepage }}</p>
        </div>
        <div class="source-item-actions">
          <span class="tag">{{ source_posts | size }} 篇</span>
          <a class="source-link" href="{{ source.homepage }}" target="_blank" rel="noopener noreferrer">访问官网 →</a>
        </div>
      </div>

      <div class="source-stats-line">
        {% if latest_post %}
        <span>最近更新 {{ latest_post.date | date: "%Y年%m月%d日" }}</span>
        {% else %}
        <span>暂无已发布文章</span>
        {% endif %}
      </div>

      {% if source_posts.size > 0 %}
      <div class="source-recent-list">
        {% for post in source_posts limit:3 %}
        <a class="source-recent-item" href="{{ post.url | relative_url }}">
          <span class="source-recent-date">{{ post.date | date: "%m-%d" }}</span>
          <span class="source-recent-title">{{ post.title }}</span>
        </a>
        {% endfor %}
      </div>
      {% endif %}
    </article>
    {% endfor %}
  </section>

  <section class="source-raw-note">
    <h2>原始数据</h2>
    <p>所有原始 markdown 文件存放在 <code>GEO-SEO News/</code> 目录下，可按来源和日期继续浏览。</p>
    <a class="source-link" href="{{ '/GEO-SEO News/' | relative_url }}" target="_blank" rel="noopener noreferrer">查看原始数据 →</a>
  </section>
</div>
