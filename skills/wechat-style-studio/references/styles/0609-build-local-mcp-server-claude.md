---
name: xv-0609-build-local-mcp-server-claude
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 如何为Claude构建本地MCPServer…风格双技能

源文章：如何为 Claude 构建本地 MCP Server：文件、命令、截图与应用控制

- Skill ID：`xv-0609-build-local-mcp-server-claude`
- 作者：Swati Gupta (@hrswatigupta)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/build-local-mcp-server-claude
- 原文：https://x.com/hrswatigupta/status/2062521856528371966
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0609-build-local-mcp-server-claude.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0609-build-local-mcp-server-claude.jpg`
- 数据：曝光 1013868，点赞 72，收藏 224

## Skill Name

如何为Claude构建本地MCPServer…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：步骤型深度指南
- 主题域：AI工具/Agent、编程/产品/工程
- 开头机制：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
- 结构骨架：多章节长文，约 14 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：短段落、高换行、句子像社媒 thread，适合制造滑动阅读感。
- 语气判断：工具箱型：信息密度高，靠列表、步骤和模板提供收藏价值。
- 小标题样本：开始构建之前的一点说明 / 为什么这套架构值得学习 / 我们要构建的设计 / 技术栈 / 实际的服务器 / 为什么这些工具要这样设计
- 文本规模：约 3756 字符，123 个段落，14 个标题，90 个列表项，8 个引用块
- 爆款承诺：为 Claude 构建安全的本地 MCP Server，直接从桌面端实现文件管理、截图及应用控制的自动化。

### 可复用文章提示词

```text
请使用「如何为Claude构建本地MCPServer…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用个人观察或亲历故事开场，再把私人经验上升为普遍方法。
2. 类型：采用「步骤型深度指南」；主题域优先靠近「AI工具/Agent、编程/产品/工程」。
3. 结构：多章节长文，约 14 个小节，适合用罗马数字/编号标题推进。
4. 节奏：短段落、高换行、句子像社媒 thread，适合制造滑动阅读感。
5. 语气：工具箱型：信息密度高，靠列表、步骤和模板提供收藏价值。
6. 小标题参考：开始构建之前的一点说明 / 为什么这套架构值得学习 / 我们要构建的设计 / 技术栈 / 实际的服务器 / 为什么这些工具要这样设计
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「为 Claude 构建安全的本地 MCP Server，直接从桌面端实现文件管理、截图及应用控制的自动化。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：1983x793，比例 2.50:1
- 主色板：#f9e9db cream 21% / #f9efe6 white 18% / #fbf4ed white 17% / #fcf8f2 white 16% / #f4e9e0 cream 14%
- 明暗/饱和/对比：brightness 230，saturation 27，contrast 30
- 构图策略：留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "如何为 Claude 构建本地 MCP Server：文件、命令、截图与应用控制".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #f9e9db (cream), #f9efe6 (white), #fbf4ed (white), #fcf8f2 (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "如何为Claude构建本地MCPServer…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
