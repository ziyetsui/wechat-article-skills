---
name: xv-0531-gemini-live-api-voice-agents
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 利用GeminiLiveAPI构建更强大的语…风格双技能

源文章：利用 Gemini Live API 构建更强大的语音 Agent

- Skill ID：`xv-0531-gemini-live-api-voice-agents`
- 作者：Google AI Studio (@GoogleAIStudio)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/gemini-live-api-voice-agents
- 原文：https://x.com/GoogleAIStudio/status/1970545734736023564
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0531-gemini-live-api-voice-agents.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0531-gemini-live-api-voice-agents.jpg`
- 数据：曝光 308741，点赞 997，收藏 450

## Skill Name

利用GeminiLiveAPI构建更强大的语…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：技术实操拆解
- 主题域：AI工具/Agent、编程/产品/工程、个人成长/心理
- 开头机制：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
- 结构骨架：问题-重构-方法-收束结构，靠连续段落建立说服力。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：技术讲解型：清楚、分步、偏工程笔记，重视可操作性。
- 小标题样本：可靠性大幅提升 / 更自然的对话 / 借助"思考"能力实现更智能的响应 / 实际应用中的 Live API / 立即开始使用
- 文本规模：约 1711 字符，30 个段落，5 个标题，2 个列表项，16 个引用块
- 爆款承诺：了解 Google 全新 Gemini Live API 更新如何实现 2 倍更可靠的函数调用，并带来流畅、自然的语音交互体验。

### 可复用文章提示词

```text
请使用「利用GeminiLiveAPI构建更强大的语…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
2. 类型：采用「技术实操拆解」；主题域优先靠近「AI工具/Agent、编程/产品/工程、个人成长/心理」。
3. 结构：问题-重构-方法-收束结构，靠连续段落建立说服力。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：技术讲解型：清楚、分步、偏工程笔记，重视可操作性。
6. 小标题参考：可靠性大幅提升 / 更自然的对话 / 借助"思考"能力实现更智能的响应 / 实际应用中的 Live API / 立即开始使用
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「了解 Google 全新 Gemini Live API 更新如何实现 2 倍更可靠的函数调用，并带来流畅、自然的语音交互体验。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：高饱和海报/科技广告视觉
- 原图尺寸：2048x819，比例 2.50:1
- 主色板：#010205 black 20% / #050a17 black 19% / #0c1b36 charcoal 18% / #193765 charcoal 18% / #03050b black 15%
- 明暗/饱和/对比：brightness 32，saturation 184，contrast 45
- 构图策略：暗底强氛围，适合单一发光焦点、人物剪影或中央隐喻物。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "利用 Gemini Live API 构建更强大的语音 Agent".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 高饱和海报/科技广告视觉. Use a palette inspired by #010205 (black), #050a17 (black), #0c1b36 (charcoal), #193765 (charcoal). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 暗底强氛围，适合单一发光焦点、人物剪影或中央隐喻物。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "利用GeminiLiveAPI构建更强大的语…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
