# GEO-SEO News

这个目录用于保存每日同步的 GEO、SEO、AI Search 相关博客资源。

## 存放规则

文章按来源和发布时间归档：

```text
GEO-SEO News/
  <blog 来源>/
    <YYYY-MM-DD>/
      <blog 标题>.md
```

例如：

```text
GEO-SEO News/OpenAI News/2026-07-20/Safety and alignment in an era of long-horizon models.md
```

## 当前来源

- Google Search Central Blog
- OpenAI News
- Search Engine Journal
- Google AI Blog
- Semrush Blog

来源配置在 `sources.json`。脚本会读取 RSS/XML，只保存新增文章，去重状态保存在 `_state/seen.json`。

为避免第一次运行导入大量历史文章，脚本默认只同步最近 7 天内发布的文章，并限制每个来源每次最多写入 20 篇。

该仓库按私有知识库使用，脚本会在 RSS 摘要之外继续抓取原文页面，并把正文写入每篇 Markdown 的 `## 原文正文` 小节。若某篇文章页面结构变化或请求失败，文件中会记录失败原因，后续运行会尝试补抓。

## 手动同步

在仓库根目录执行：

```bash
rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py
```

只预览不写入：

```bash
rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py --dry-run
```

如需临时扩大范围：

```bash
rtk /usr/bin/env python3 scripts/fetch_geo_seo_news.py --lookback-days 30 --max-per-source 50
```

## 定时同步

GitHub Actions 会每天北京时间 10:00 运行一次。由于 GitHub Actions cron 使用 UTC，workflow 中配置为 `0 2 * * *`。

脚本只提交 `GEO-SEO News/` 下的新增内容；当天没有新文章时不会产生提交。
