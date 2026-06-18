---
name: xv-0032-claude-code-hacks-2026-workflow
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 我所知道的所有ClaudeCode技巧202…风格双技能

源文章：我所知道的所有 Claude Code 技巧（2026 年 3 月）

- Skill ID：`xv-0032-claude-code-hacks-2026-workflow`
- 作者：Matt Van Horn (@mvanhorn)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/claude-code-hacks-2026-workflow
- 原文：https://x.com/mvanhorn/status/2035857346602340637
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0032-claude-code-hacks-2026-workflow.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0032-claude-code-hacks-2026-workflow.jpg`
- 数据：曝光 916785，点赞 2371，收藏 8620

## Skill Name

我所知道的所有ClaudeCode技巧202…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：清单型爆款教程
- 主题域：AI工具/Agent、编程/产品/工程
- 开头机制：用逆向判断或否定常识开场，先制造轻微冲突，再给出替代框架。
- 结构骨架：多章节长文，约 13 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
- 小标题样本：1. 一有想法，立刻 /ce:plan 或 /ce:brainstorm / 2. 拥抱语音 / 3. 同时运行四到六个会话 / 4. 三个改变一切的设置 / 5. 计划之前先研究 / 6. 把任何会议变成 Plan.md
- 文本规模：约 7904 字符，102 个段落，13 个标题，7 个列表项，0 个引用块
- 爆款承诺：告别传统的 IDE 使用方式，通过这些 Claude Code 高阶技巧，利用计划文件和语音输入，以前所未有的速度构建软件。

### 可复用文章提示词

```text
请使用「我所知道的所有ClaudeCode技巧202…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用逆向判断或否定常识开场，先制造轻微冲突，再给出替代框架。
2. 类型：采用「清单型爆款教程」；主题域优先靠近「AI工具/Agent、编程/产品/工程」。
3. 结构：多章节长文，约 13 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：解释型：克制但有判断，先拆问题，再给框架和可执行建议。
6. 小标题参考：1. 一有想法，立刻 /ce:plan 或 /ce:brainstorm / 2. 拥抱语音 / 3. 同时运行四到六个会话 / 4. 三个改变一切的设置 / 5. 计划之前先研究 / 6. 把任何会议变成 Plan.md
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「告别传统的 IDE 使用方式，通过这些 Claude Code 高阶技巧，利用计划文件和语音输入，以前所未有的速度构建软件。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：高饱和海报/科技广告视觉
- 原图尺寸：1200x480，比例 2.50:1
- 主色板：#030804 black 26% / #0d130c black 22% / #2b422c charcoal 15% / #102415 charcoal 15% / #222a1e charcoal 12%
- 明暗/饱和/对比：brightness 34，saturation 117，contrast 33
- 构图策略：画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "我所知道的所有 Claude Code 技巧（2026 年 3 月）".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 高饱和海报/科技广告视觉. Use a palette inspired by #030804 (black), #0d130c (black), #2b422c (charcoal), #102415 (charcoal). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 画面信息量较高，适合用中心主体加左右辅助信息，保持缩略图可读。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "我所知道的所有ClaudeCode技巧202…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
