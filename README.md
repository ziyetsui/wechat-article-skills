# WeChat Article Skills

830 viral writing and cover templates for WeChat Official Account articles.

This is a production-ready skill pack for turning raw source material into a publish-ready WeChat workflow: choose a proven style, rewrite the article, generate a cover direction, format the article, and upload it to the Official Account draft box. The built-in style studio is derived from YouMind viral article data and uses progressive disclosure, so an agent can recommend a few strong templates without loading the whole library.

## Template Library At A Glance

| 830 | 6 | 6 | 1 |
|---:|---:|---:|---:|
| style cards | article systems | cover systems | full WeChat pipeline |

| What you get | Why it matters |
|---|---|
| Viral article structure cards | Reuse hooks, section rhythm, argument patterns, and endings instead of starting from a blank page. |
| Cover direction cards | Reuse visual metaphors, palette, density, and composition for WeChat-friendly 2.35:1 covers. |
| Style mixing | Use one reference for the article voice and another for the cover system. |
| Agent-ready workflow | Works as separate skills or one orchestrated `@公众号流水线` flow. |

## Template Wall

Red-pick templates, Kimi/agent workflow references, and high-signal skill-template examples:

<table>
  <tr>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0607-opus-kimi-coding-cost-reduction.jpg" alt="Opus and Kimi Agent Swarm workflow cover" width="100%" /><br><b>Kimi Cost Stack</b><br><sub>AI agent workflow · high-saturation tech poster</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0620-kimi-2-6-agent-swarm-speed.jpg" alt="Kimi 2.6 agent swarm cover" width="100%" /><br><b>Kimi Agent Swarm</b><br><sub>300-agent system · modern WeChat cover</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0829-20-ai-skills-expertise-templates.jpg" alt="AI skills expertise templates cover" width="100%" /><br><b>Skill Templates</b><br><sub>20 reusable AI expertise templates</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0495-anthropic-claude-code-html-first.jpg" alt="Claude Code HTML-first cover" width="100%" /><br><b>HTML-First Output</b><br><sub>technical breakdown · interface collage</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0675-karpathy-claude-md-ai-coding.jpg" alt="Karpathy CLAUDE.md GitHub cover" width="100%" /><br><b>GitHub Playbook</b><br><sub>CLAUDE.md memory · code workflow</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0330-ai-design-workflow-2026-templates.jpg" alt="AI design workflow templates cover" width="100%" /><br><b>Design Workflow</b><br><sub>ready-to-use visual templates</sub></td>
  </tr>
</table>

Frontend, slide, GitHub, and product-page style references:

<table>
  <tr>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0104-generative-ui-frontend-architecture-patterns.jpg" alt="Generative UI frontend architecture cover" width="100%" /><br><b>Frontend Systems</b><br><sub>generative UI · architecture patterns</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0111-ai-remake-professional-slides.jpg" alt="AI remake professional slides cover" width="100%" /><br><b>Professional Slides</b><br><sub>slide transformation · step guide</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0049-open-source-magazine-ppt-skill.jpg" alt="Open-source magazine PPT skill cover" width="100%" /><br><b>Magazine PPT</b><br><sub>open-source design skill · cover system</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0115-github-repos-for-making-money.jpg" alt="GitHub repos for making money cover" width="100%" /><br><b>GitHub Directory</b><br><sub>repo roundup · high-signal resource page</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/showcase/0124-claude-skills-ecosystem-github-links.jpg" alt="Claude skills ecosystem GitHub links cover" width="100%" /><br><b>Skills Ecosystem</b><br><sub>GitHub link collection · long list format</sub></td>
    <td width="33%" valign="top"><img src="skills/wechat-style-studio/assets/covers/top/0346-x-advertising-platform-ai-rebuild.jpg" alt="Product brief cover system" width="100%" /><br><b>Product Brief</b><br><sub>minimal infographic · landing-page feel</sub></td>
  </tr>
</table>

Browse the full template gallery: [`skills/wechat-style-studio/references/style-gallery.md`](skills/wechat-style-studio/references/style-gallery.md).

## What It Does

- Recommends 3-5 suitable YouMind styles from 830 references by topic, article class, cover class, and engagement metrics.
- Lets you say “文章用 Dan Koe 那种风格，封面用黑白寓言风” or “我想选这种风格”.
- Splits each selected reference into an article skill and a cover skill, so writing and image direction can be mixed.
- Runs the whole WeChat production path: rewrite, cover prompt/generation, layout, and draft-box upload.
- Uses progressive disclosure: read `style-index.json`, then load only the selected style card.

## Style Library

The style studio contains:

- 830 style cards in [`references/styles/`](skills/wechat-style-studio/references/styles/).
- 6 article classes: 清单型爆款教程, 爆款解释型文章, 步骤型深度指南, 观点型解释分析, 技术实操拆解, 叙事型长文.
- 6 cover classes: 黑白/低饱和 editorial, 浅底信息图, 暗色电影感, 高饱和海报, 现代公众号题图, 细节拼贴/界面/图表.
- Compact index: [`style-index.json`](skills/wechat-style-studio/references/style-index.json).
- Quick shortlist: [`representative-styles.md`](skills/wechat-style-studio/references/representative-styles.md).

## Install

Claude Code plugin marketplace:

```bash
/plugin marketplace add ziyetsui/wechat-article-skills
/plugin install wechat-article-skills@wechat-article-skills
```

Codex plugin marketplace:

```bash
codex plugin marketplace add ziyetsui/wechat-article-skills
codex plugin add wechat-article-skills@wechat-article-skills
```

Generic agents that read `~/.agents/skills`:

```bash
npx skills add ziyetsui/wechat-article-skills -a '*' -g -y
```

Manual install:

```bash
cp -R skills/wechat-* ~/.agents/skills/
```

After installing, start a new agent session so the new skills are discovered.

## Use

Pick a style first:

```text
@公众号风格工作室
我想写一篇关于 AI agent 如何改变个人工作流的公众号文章。
先推荐 5 个数据高、适合技术创作者的 YouMind 风格。
```

Run the full workflow:

```text
@公众号流水线
素材：<paste notes, draft, transcript, or outline>
文章用 Dan Koe 那种强教练式清单风。
封面用黑白或低饱和 editorial 风格。
```

Mix article and cover directions:

```text
文章用 Claude Code 教程风，封面用高饱和科技广告视觉。
帮我改写成公众号文章，并生成封面。
```

Use the default personal WeChat style:

```text
@公众号改写
把这份素材改成一篇强判断、有个人体感的公众号文章。
```

## Included Skills

- `wechat-style-studio`: choose, recommend, and mix 830 YouMind article/cover styles.
- `wechat-rewrite`: rewrite materials into a high-conviction Chinese public-account article.
- `wechat-cover-image`: generate WeChat cover prompts/images with APiYi GPT Image 2.
- `wechat-layout`: format the rewritten article into WeChat-ready HTML/TXT.
- `wechat-publish-draft`: upload formatted content to the WeChat Official Account draft box.
- `wechat-article-pipeline`: orchestrate style selection, rewrite, cover, layout, and draft-box upload.

## Configuration

Do not commit real API keys or WeChat credentials.

Cover generation:

```bash
export APIYI_API_KEY="..."
# or
export YI_API_KEY="..."
```

Draft-box upload:

```bash
export WECHAT_APPID="..."
export WECHAT_APPSECRET="..."
```

Use [`skills/wechat-publish-draft/scripts/.env.example`](skills/wechat-publish-draft/scripts/.env.example) as a template only.

## Architecture

The style library is intentionally split into a compact index and full cards:

```text
skills/wechat-style-studio/
  SKILL.md
  references/style-index.json          # read first
  references/representative-styles.md  # quick shortlist
  references/style-gallery.md          # GitHub gallery
  references/styles/*.md               # 830 selected cards
  assets/covers/                       # lightweight gallery thumbnails
```

The marketplace plugin package lives in `plugins/wechat-article-skills/` and mirrors the root `skills/` directory. After changing root skills, run:

```bash
python3 scripts/sync_plugin_package.py
```

Regenerate the YouMind style studio from the extracted source folder:

```bash
python3 scripts/build_style_library.py \
  --source-root "/path/to/2026-06-15-youmind-x-viral-articles-all" \
  --repo-root .
python3 scripts/sync_plugin_package.py
```

## Safety

The upload skill creates backend drafts only. It must not publish publicly, mass-send, call freepublish APIs, or click a public publish button.
