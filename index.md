---
layout: default
title: "GEO-SEO News"
description: "GEO、SEO、AI Search 相关博客资源汇总"
---

<div class="hero">
  <h1>GEO-SEO News</h1>
  <p>GEO、SEO、AI Search 相关博客资源汇总，可按日期筛选</p>
</div>

<div class="container">
  {% assign sorted_posts = site.posts | sort: 'date' | reverse %}
  {% assign grouped_dates = sorted_posts | group_by_exp: "post", "post.date | date: '%Y-%m-%d'" %}

  <section class="filter-panel">
    <div class="filter-row">
      <label for="date-filter">筛选日期</label>
      <select id="date-filter">
        <option value="all">全部日期</option>
        {% for group in grouped_dates %}
        <option value="{{ group.name }}">{{ group.name }} ({{ group.items | size }})</option>
        {% endfor %}
      </select>
      <label for="source-filter">筛选来源</label>
      <select id="source-filter">
        <option value="all">全部来源</option>
        {% assign grouped_sources = sorted_posts | group_by: "source" | sort_natural: "name" %}
        {% for group in grouped_sources %}
        <option value="{{ group.name }}">{{ group.name }} ({{ group.items | size }})</option>
        {% endfor %}
      </select>
      <button type="button" id="date-filter-reset" class="filter-reset">清除筛选</button>
    </div>
    <p class="filter-summary">共 {{ sorted_posts | size }} 篇文章，{{ grouped_dates | size }} 个日期目录。</p>
  </section>

  <section id="post-list" class="post-list">
    {% for post in sorted_posts %}
    <div class="post-card">
      <div class="date-col">{{ post.date | date: "%m-%d" }}</div>
      <div class="content-col" data-post-date="{{ post.date | date: '%Y-%m-%d' }}" data-post-source="{{ post.source }}">
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <div class="post-meta-inline">
          <span class="tag">{{ post.source }}</span>
          <span class="meta-date">{{ post.date | date: "%Y-%m-%d" }}</span>
        </div>
        {% if post.excerpt %}
        <p class="excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
        {% endif %}
        {% if post.categories %}
        <div class="post-tags">
          {% for cat in post.categories %}
          <span class="tag">{{ cat }}</span>
          {% endfor %}
        </div>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </section>

  <p id="post-empty-state" class="filter-empty" hidden>当前日期下暂无文章。</p>

  {% if sorted_posts.size == 0 %}
  <p style="color:var(--muted); text-align:center; padding:40px 0;">暂无文章，请先同步新闻数据。</p>
  {% endif %}
</div>

<script>
  (function () {
    var dateSelect = document.getElementById('date-filter');
    var sourceSelect = document.getElementById('source-filter');
    var reset = document.getElementById('date-filter-reset');
    var emptyState = document.getElementById('post-empty-state');
    if (!dateSelect || !sourceSelect || !reset) return;

    var cards = Array.prototype.slice.call(document.querySelectorAll('.post-card'));

    function applyFilter() {
      var selectedDate = dateSelect.value;
      var selectedSource = sourceSelect.value;
      var visibleCount = 0;

      cards.forEach(function (card) {
        var content = card.querySelector('[data-post-date]');
        var postDate = content ? content.getAttribute('data-post-date') : '';
        var postSource = content ? content.getAttribute('data-post-source') : '';
        var dateMatch = selectedDate === 'all' || postDate === selectedDate;
        var sourceMatch = selectedSource === 'all' || postSource === selectedSource;
        var visible = dateMatch && sourceMatch;
        card.hidden = !visible;
        if (visible) visibleCount += 1;
      });

      if (emptyState) {
        emptyState.hidden = visibleCount !== 0;
      }
    }

    dateSelect.addEventListener('change', applyFilter);
    sourceSelect.addEventListener('change', applyFilter);
    reset.addEventListener('click', function () {
      dateSelect.value = 'all';
      sourceSelect.value = 'all';
      applyFilter();
    });
  })();
</script>
