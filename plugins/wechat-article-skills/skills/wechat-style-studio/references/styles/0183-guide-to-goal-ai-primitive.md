---
name: xv-0183-guide-to-goal-ai-primitive
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# /goal终极指南风格双技能

源文章：/goal 终极指南

- Skill ID：`xv-0183-guide-to-goal-ai-primitive`
- 作者：Shubham Saboo (@Saboo_Shubham_)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/guide-to-goal-ai-primitive
- 原文：https://x.com/Saboo_Shubham_/status/2054988166541770782
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0183-guide-to-goal-ai-primitive.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0183-guide-to-goal-ai-primitive.jpg`
- 数据：曝光 203171，点赞 970，收藏 2432

## Skill Name

/goal终极指南风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：步骤型深度指南
- 主题域：AI工具/Agent、个人成长/心理
- 开头机制：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
- 结构骨架：多章节长文，约 9 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：/goal 到底是什么 / 目前支持 /goal 的三个工具 / 环境设置 / Hermes 在 /goal 之上增加了什么 / 三个角色 / 一个真实的运行过程，端到端
- 文本规模：约 3553 字符，68 个段落，9 个标题，8 个列表项，0 个引用块
- 爆款承诺：告别对 AI Agent 的微观管理。了解 /goal 原语如何通过 Codex、Claude Code 和 Hermes 实现自主编码工作流。

### 可复用文章提示词

```text
请使用「/goal终极指南风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
2. 类型：采用「步骤型深度指南」；主题域优先靠近「AI工具/Agent、个人成长/心理」。
3. 结构：多章节长文，约 9 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：/goal 到底是什么 / 目前支持 /goal 的三个工具 / 环境设置 / Hermes 在 /goal 之上增加了什么 / 三个角色 / 一个真实的运行过程，端到端
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「告别对 AI Agent 的微观管理。了解 /goal 原语如何通过 Codex、Claude Code 和 Hermes 实现自主编码工作流。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：2048x819，比例 2.50:1
- 主色板：#fef2df white 21% / #fdefdb cream 20% / #a98472 gray 18% / #e4d2bc cream 18% / #f3e4ce cream 13%
- 明暗/饱和/对比：brightness 213，saturation 47，contrast 48
- 构图策略：画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "/goal 终极指南".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #fef2df (white), #fdefdb (cream), #a98472 (gray), #e4d2bc (cream). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "/goal终极指南风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
