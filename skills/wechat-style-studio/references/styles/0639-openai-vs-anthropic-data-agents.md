---
name: xv-0639-openai-vs-anthropic-data-agents
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# OpenAI对决Anthropic两个内部数…风格双技能

源文章：OpenAI 对决 Anthropic：两个内部数据 Agent —— 相同的经验，不同的构建

- Skill ID：`xv-0639-openai-vs-anthropic-data-agents`
- 作者：Dmitry Petrov (@FullStackML)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/openai-vs-anthropic-data-agents
- 原文：https://x.com/FullStackML/status/2062587219156832718
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0639-openai-vs-anthropic-data-agents.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0639-openai-vs-anthropic-data-agents.jpg`
- 数据：曝光 492265，点赞 95，收藏 162

## Skill Name

OpenAI对决Anthropic两个内部数…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：清单型爆款教程
- 主题域：AI工具/Agent
- 开头机制：用数字、收益或结果开场，把可信度和阅读收益前置。
- 结构骨架：以一个总承诺开场，随后逐条拆解，每条保持同一节奏和信息颗粒度。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：他们的共识 / 他们的差异 / 我的看法（在构建了面向非结构化数据而非 SQL 的“数据 Agent”之后） / 向这里的数据同行提问
- 文本规模：约 495 字符，6 个段落，4 个标题，5 个列表项，0 个引用块
- 爆款承诺：了解 OpenAI 和 Anthropic 如何构建其内部数据 Agent，以及为什么实现 95% 准确率的秘诀不在于模型，而在于上下文。

### 可复用文章提示词

```text
请使用「OpenAI对决Anthropic两个内部数…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用数字、收益或结果开场，把可信度和阅读收益前置。
2. 类型：采用「清单型爆款教程」；主题域优先靠近「AI工具/Agent」。
3. 结构：以一个总承诺开场，随后逐条拆解，每条保持同一节奏和信息颗粒度。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：他们的共识 / 他们的差异 / 我的看法（在构建了面向非结构化数据而非 SQL 的“数据 Agent”之后） / 向这里的数据同行提问
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「了解 OpenAI 和 Anthropic 如何构建其内部数据 Agent，以及为什么实现 95% 准确率的秘诀不在于模型，而在于上下文。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：2000x800，比例 2.50:1
- 主色板：#f4f1ea white 71% / #f4f1e9 white 8% / #ded8ce cream 7% / #f5f1eb white 5% / #f3f1ea white 5%
- 明暗/饱和/对比：brightness 237，saturation 14，contrast 20
- 构图策略：留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "OpenAI 对决 Anthropic：两个内部数据 Agent —— 相同的经验，不同的构建".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #f4f1ea (white), #f4f1e9 (white), #ded8ce (cream), #f5f1eb (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "OpenAI对决Anthropic两个内部数…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
