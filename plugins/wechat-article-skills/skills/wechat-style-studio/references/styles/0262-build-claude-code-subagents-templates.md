---
name: xv-0262-build-claude-code-subagents-templates
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 如何在15分钟内构建你的第一个ClaudeC…风格双技能

源文章：如何在 15 分钟内构建你的第一个 Claude Code Subagent（内含精确模板）

- Skill ID：`xv-0262-build-claude-code-subagents-templates`
- 作者：rody (@0x_rody)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/build-claude-code-subagents-templates
- 原文：https://x.com/0x_rody/status/2061019244595233135
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0262-build-claude-code-subagents-templates.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0262-build-claude-code-subagents-templates.jpg`
- 数据：曝光 1058588，点赞 383，收藏 1651

## Skill Name

如何在15分钟内构建你的第一个ClaudeC…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：清单型爆款教程
- 主题域：AI工具/Agent、编程/产品/工程
- 开头机制：用数字、收益或结果开场，把可信度和阅读收益前置。
- 结构骨架：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：短段落、高换行、句子像社媒 thread，适合制造滑动阅读感。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：子 Agent 到底是什么（30 秒） / 子 Agent 文件的构成 / 模板 1：代码审查者（5 分钟） / 模板 2：测试编写者（5 分钟） / 模板 3：文档生成器（5 分钟） / 模板 4：安全扫描器（5 分钟）
- 文本规模：约 1276 字符，34 个段落，10 个标题，0 个列表项，0 个引用块
- 爆款承诺：利用这 5 个即用型 Claude Subagent 模板，在几分钟内实现代码审查、测试和安全扫描的自动化，优化你的编码工作流。

### 可复用文章提示词

```text
请使用「如何在15分钟内构建你的第一个ClaudeC…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用数字、收益或结果开场，把可信度和阅读收益前置。
2. 类型：采用「清单型爆款教程」；主题域优先靠近「AI工具/Agent、编程/产品/工程」。
3. 结构：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
4. 节奏：短段落、高换行、句子像社媒 thread，适合制造滑动阅读感。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：子 Agent 到底是什么（30 秒） / 子 Agent 文件的构成 / 模板 1：代码审查者（5 分钟） / 模板 2：测试编写者（5 分钟） / 模板 3：文档生成器（5 分钟） / 模板 4：安全扫描器（5 分钟）
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「利用这 5 个即用型 Claude Subagent 模板，在几分钟内实现代码审查、测试和安全扫描的自动化，优化你的编码工作流。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：黑白或低饱和 editorial 插画/照片
- 原图尺寸：1428x571，比例 2.50:1
- 主色板：#f4f3ee white 47% / #1d1d1d charcoal 31% / #f2f3ed white 11% / #f9f8f4 white 5% / #abaaa5 gray 5%
- 明暗/饱和/对比：brightness 175，saturation 9，contrast 95
- 构图策略：中等密度，适合一个主视觉隐喻配少量标题文字。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "如何在 15 分钟内构建你的第一个 Claude Code Subagent（内含精确模板）".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 黑白或低饱和 editorial 插画/照片. Use a palette inspired by #f4f3ee (white), #1d1d1d (charcoal), #f2f3ed (white), #f9f8f4 (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 中等密度，适合一个主视觉隐喻配少量标题文字。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "如何在15分钟内构建你的第一个ClaudeC…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
