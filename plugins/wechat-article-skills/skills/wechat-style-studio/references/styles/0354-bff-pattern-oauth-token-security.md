---
name: xv-0354-bff-pattern-oauth-token-security
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 使用BFF模式将Token移出浏览器风格双技能

源文章：使用 BFF 模式将 Token 移出浏览器

- Skill ID：`xv-0354-bff-pattern-oauth-token-security`
- 作者：farstep (@farstep_)
- 原始语言：日文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/bff-pattern-oauth-token-security
- 原文：https://x.com/farstep_/status/2061282900679831620
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0354-bff-pattern-oauth-token-security.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0354-bff-pattern-oauth-token-security.jpg`
- 数据：曝光 294520，点赞 604，收藏 1119

## Skill Name

使用BFF模式将Token移出浏览器风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：技术实操拆解
- 主题域：编程/产品/工程
- 开头机制：用明确问题和强承诺开场，快速说明读者为什么该继续读。
- 结构骨架：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：技术讲解型：清楚、分步、偏工程笔记，重视可操作性。
- 小标题样本：前提条件 / 基于浏览器的应用中的 XSS 风险 / 不将令牌置于浏览器的设计 / 身份验证流程 / 必要的安全设置 / CSRF 防护不应仅依赖 SameSite
- 文本规模：约 1886 字符，23 个段落，10 个标题，34 个列表项，0 个引用块
- 爆款承诺：通过使用 Backend for Frontend (BFF) 模式将 OAuth token 移出浏览器，防止其因 XSS 攻击而泄露。

### 可复用文章提示词

```text
请使用「使用BFF模式将Token移出浏览器风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用明确问题和强承诺开场，快速说明读者为什么该继续读。
2. 类型：采用「技术实操拆解」；主题域优先靠近「编程/产品/工程」。
3. 结构：多章节长文，约 10 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：技术讲解型：清楚、分步、偏工程笔记，重视可操作性。
6. 小标题参考：前提条件 / 基于浏览器的应用中的 XSS 风险 / 不将令牌置于浏览器的设计 / 身份验证流程 / 必要的安全设置 / CSRF 防护不应仅依赖 SameSite
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「通过使用 Backend for Frontend (BFF) 模式将 OAuth token 移出浏览器，防止其因 XSS 攻击而泄露。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：1448x1086，比例 1.33:1
- 主色板：#fefefe white 51% / #cdcdcc cream 16% / #ffffff white 15% / #fefefd white 12% / #f2ffec white 6%
- 明暗/饱和/对比：brightness 238，saturation 1，contrast 38
- 构图策略：画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "使用 BFF 模式将 Token 移出浏览器".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #fefefe (white), #cdcdcc (cream), #ffffff (white), #fefefd (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "使用BFF模式将Token移出浏览器风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
