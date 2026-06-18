---
name: xv-0272-memos-agent-memory-reflect2evolve
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# AIAgent记忆的最优解深入解析MemOS风格双技能

源文章：AI Agent 记忆的最优解：深入解析 MemOS

- Skill ID：`xv-0272-memos-agent-memory-reflect2evolve`
- 作者：Yanhua (@yanhua1010)
- 原始语言：中文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/memos-agent-memory-reflect2evolve
- 原文：https://x.com/yanhua1010/status/2062345653079224458
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0272-memos-agent-memory-reflect2evolve.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0272-memos-agent-memory-reflect2evolve.jpg`
- 数据：曝光 123312，点赞 729，收藏 1573

## Skill Name

AIAgent记忆的最优解深入解析MemOS风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：爆款解释型文章
- 主题域：AI工具/Agent、学习/知识管理
- 开头机制：用逆向判断或否定常识开场，先制造轻微冲突，再给出替代框架。
- 结构骨架：问题-重构-方法-收束结构，靠连续段落建立说服力。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：现有的记忆方案，大多只是「搜旧聊天记录」 / 装完 MemOS Local Plugin 后，Hermes 告诉我的一番话 / 测试 1：教它写推特 / 测试 2：做两个产品页，看看风格会不会跨项目迁移 / 打开 Viewer 看看它学到了什么 / 一个核心，多个 Agent 共用
- 文本规模：约 3762 字符，57 个段落，7 个标题，4 个列表项，1 个引用块
- 爆款承诺：别再为你的 AI 手动编写指令了，了解 MemOS 如何利用 Reflect2Evolve 帮助 Agent 真正习得你的偏好。

### 可复用文章提示词

```text
请使用「AIAgent记忆的最优解深入解析MemOS风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用逆向判断或否定常识开场，先制造轻微冲突，再给出替代框架。
2. 类型：采用「爆款解释型文章」；主题域优先靠近「AI工具/Agent、学习/知识管理」。
3. 结构：问题-重构-方法-收束结构，靠连续段落建立说服力。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：现有的记忆方案，大多只是「搜旧聊天记录」 / 装完 MemOS Local Plugin 后，Hermes 告诉我的一番话 / 测试 1：教它写推特 / 测试 2：做两个产品页，看看风格会不会跨项目迁移 / 打开 Viewer 看看它学到了什么 / 一个核心，多个 Agent 共用
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「别再为你的 AI 手动编写指令了，了解 MemOS 如何利用 Reflect2Evolve 帮助 Agent 真正习得你的偏好。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：1983x793，比例 2.50:1
- 主色板：#f0e7da cream 33% / #f2eadf cream 25% / #f2e8dc cream 16% / #f5eee3 white 13% / #c0baaf cream 8%
- 明暗/饱和/对比：brightness 226，saturation 22，contrast 33
- 构图策略：留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "AI Agent 记忆的最优解：深入解析 MemOS".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #f0e7da (cream), #f2eadf (cream), #f2e8dc (cream), #f5eee3 (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "AIAgent记忆的最优解深入解析MemOS风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
