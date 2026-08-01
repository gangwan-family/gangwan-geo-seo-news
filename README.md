# gangwan-geo-seo-news.github.io

基于 Jekyll 的 GEO / SEO / AI Search 资讯站点，部署到 GitHub Pages。

站点目标：

- 自动抓取 `GEO-SEO News/` 下的来源文章
- 自动转换成 Jekyll `_posts/`
- 在 Pages 上按日期浏览和筛选文章

仓库结构

- `GEO-SEO News/`
  - 原始抓取结果，按 `来源 / 日期 / 文章.md` 存放
- `_posts/`
  - Jekyll 实际渲染输入，由脚本自动生成
- `scripts/fetch_geo_seo_news.py`
  - 抓取 RSS 和正文，更新 `GEO-SEO News/`
- `scripts/build_jekyll_posts.py`
  - 将 `GEO-SEO News/` 转换为 `_posts/`
- `.github/workflows/fetch-geo-seo-news.yml`
  - 定时抓取内容并生成 `_posts/`
- `.github/workflows/deploy-pages.yml`
  - 在 `main` 分支变更后构建并部署 GitHub Pages

工作流说明

1. 内容同步

- 触发文件：`.github/workflows/fetch-geo-seo-news.yml`
- 触发方式：
  - 每天定时执行
  - 手动执行 `workflow_dispatch`
- 执行内容：
  - 抓取最新文章到 `GEO-SEO News/`
  - 生成 `_posts/`
  - 自动提交并推送到 `main`

2. Pages 部署

- 触发文件：`.github/workflows/deploy-pages.yml`
- 触发方式：
  - `push` 到 `main`
  - 手动执行 `workflow_dispatch`
- 执行内容：
  - 安装 Ruby / Bundler 依赖
  - 执行 `bundle exec jekyll build`
  - 发布到 GitHub Pages

GitHub Pages 配置

请在仓库 Settings -> Pages 中确认：

- Build and deployment
  - Source: `GitHub Actions`

站点地址

- 生产地址：`https://gangwan-family.github.io/gangwan-geo-seo-news.github.io/`

本地使用

1. 生成文章

```bash
rtk python scripts/build_jekyll_posts.py
```

2. 抓取最新内容

```bash
rtk python scripts/fetch_geo_seo_news.py
```

3. 本地预览（需要本机安装 Ruby / Bundler / Jekyll）

```bash
bundle install
bundle exec jekyll serve
```

说明

- `_posts/` 是自动生成目录，不建议手工维护。
- 原始文章路径保留在每篇 post 的 `generated_from` 字段中。
- 原文外链使用 `original_url` 字段，避免与 Jekyll 自身 `page.url` 语义冲突。
