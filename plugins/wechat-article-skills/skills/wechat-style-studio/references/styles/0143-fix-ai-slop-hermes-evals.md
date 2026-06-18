---
name: xv-0143-fix-ai-slop-hermes-evals
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 如何修复AI垃圾内容使用Hermes风格双技能

源文章：如何修复 AI 垃圾内容（使用 Hermes）

- Skill ID：`xv-0143-fix-ai-slop-hermes-evals`
- 作者：Machina (@EXM7777)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/fix-ai-slop-hermes-evals
- 原文：https://x.com/EXM7777/status/2060736517564477901
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0143-fix-ai-slop-hermes-evals.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0143-fix-ai-slop-hermes-evals.jpg`
- 数据：曝光 376688，点赞 999，收藏 2830

## Skill Name

如何修复AI垃圾内容使用Hermes风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：步骤型深度指南
- 主题域：AI工具/Agent
- 开头机制：用明确问题和强承诺开场，快速说明读者为什么该继续读。
- 结构骨架：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：思想随笔型：引用、概念和个人判断交替出现，语气有解释欲。
- 小标题样本：有些人就是能持续交付最好的软件、写出精彩的内容、生成惊人的图片……这其中是有原因的 / 你什么都试过了，除了那唯一的东西 / 为什么更好的提示词解决不了这个问题（以及为什么大家还是不断在尝试） / 垃圾输出隐藏的两个地方 / 地方 1：你的内容输出 / 地方 2：你的产品输出
- 文本规模：约 5780 字符，92 个段落，10 个标题，17 个列表项，8 个引用块
- 爆款承诺：停止发布低质量的 AI 内容，学习如何使用 Hermes Agent 构建自动化评估循环，以确保输出完美无缺。

### 可复用文章提示词

```text
请使用「如何修复AI垃圾内容使用Hermes风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用明确问题和强承诺开场，快速说明读者为什么该继续读。
2. 类型：采用「步骤型深度指南」；主题域优先靠近「AI工具/Agent」。
3. 结构：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：思想随笔型：引用、概念和个人判断交替出现，语气有解释欲。
6. 小标题参考：有些人就是能持续交付最好的软件、写出精彩的内容、生成惊人的图片……这其中是有原因的 / 你什么都试过了，除了那唯一的东西 / 为什么更好的提示词解决不了这个问题（以及为什么大家还是不断在尝试） / 垃圾输出隐藏的两个地方 / 地方 1：你的内容输出 / 地方 2：你的产品输出
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「停止发布低质量的 AI 内容，学习如何使用 Hermes Agent 构建自动化评估循环，以确保输出完美无缺。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：高饱和海报/科技广告视觉
- 原图尺寸：1983x793，比例 2.50:1
- 主色板：#100e0e black 29% / #010100 black 19% / #020100 black 17% / #0d0707 black 13% / #080101 black 12%
- 明暗/饱和/对比：brightness 15，saturation 106，contrast 28
- 构图策略：暗底强氛围，适合单一发光焦点、人物剪影或中央隐喻物。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "如何修复 AI 垃圾内容（使用 Hermes）".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 高饱和海报/科技广告视觉. Use a palette inspired by #100e0e (black), #010100 (black), #020100 (black), #0d0707 (black). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 暗底强氛围，适合单一发光焦点、人物剪影或中央隐喻物。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "如何修复AI垃圾内容使用Hermes风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
