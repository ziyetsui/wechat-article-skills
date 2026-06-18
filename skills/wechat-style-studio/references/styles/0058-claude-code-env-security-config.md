---
name: xv-0058-claude-code-env-security-config
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 防止ClaudeCode泄露密钥的env配置…风格双技能

源文章：防止 Claude Code 泄露密钥的 .env 配置指南（含完整配置）

- Skill ID：`xv-0058-claude-code-env-security-config`
- 作者：darkzodchi (@zodchiii)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/claude-code-env-security-config
- 原文：https://x.com/zodchiii/status/2049779422291460576
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0058-claude-code-env-security-config.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0058-claude-code-env-security-config.jpg`
- 数据：曝光 1702425，点赞 1315，收藏 5872

## Skill Name

防止ClaudeCode泄露密钥的env配置…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：步骤型深度指南
- 主题域：AI工具/Agent、编程/产品/工程
- 开头机制：用明确问题和强承诺开场，快速说明读者为什么该继续读。
- 结构骨架：多章节长文，约 8 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：为什么 CLAUDE.md 规则保护不了你 / 你的秘密泄露的 3 种方式 / 真正有效的拒绝规则 / 阻止运行时泄露 / 能捕获一切的 pre-commit 钩子 / 容器隔离（终极方案）
- 文本规模：约 1904 字符，34 个段落，8 个标题，6 个列表项，0 个引用块
- 爆款承诺：通过这份必备的安全配置指南，防止 Claude Code 泄露你的 API 密钥和数据库密码。

### 可复用文章提示词

```text
请使用「防止ClaudeCode泄露密钥的env配置…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用明确问题和强承诺开场，快速说明读者为什么该继续读。
2. 类型：采用「步骤型深度指南」；主题域优先靠近「AI工具/Agent、编程/产品/工程」。
3. 结构：多章节长文，约 8 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：为什么 CLAUDE.md 规则保护不了你 / 你的秘密泄露的 3 种方式 / 真正有效的拒绝规则 / 阻止运行时泄露 / 能捕获一切的 pre-commit 钩子 / 容器隔离（终极方案）
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「通过这份必备的安全配置指南，防止 Claude Code 泄露你的 API 密钥和数据库密码。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：1396x558，比例 2.50:1
- 主色板：#f4f3ee white 78% / #b6b0a9 cream 8% / #f3f3ed white 7% / #f9f9f5 white 4% / #f5f3ee white 3%
- 明暗/饱和/对比：brightness 234，saturation 11，contrast 35
- 构图策略：留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "防止 Claude Code 泄露密钥的 .env 配置指南（含完整配置）".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #f4f3ee (white), #b6b0a9 (cream), #f3f3ed (white), #f9f9f5 (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "防止ClaudeCode泄露密钥的env配置…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
