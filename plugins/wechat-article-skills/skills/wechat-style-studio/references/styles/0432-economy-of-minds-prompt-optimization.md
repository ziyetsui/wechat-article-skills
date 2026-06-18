---
name: xv-0432-economy-of-minds-prompt-optimization
description: "Use when recreating the writing voice and cover direction of a YouMind viral article for Chinese public-account drafts and cover prompts."
---

# 思维经济学Multi-Agent提示词优化详…风格双技能

源文章：思维经济学：Multi-Agent 提示词优化详解

- Skill ID：`xv-0432-economy-of-minds-prompt-optimization`
- 作者：AVB (@neural_avb)
- 原始语言：英文
- YouMind：https://youmind.com/zh-CN/landing/x-viral-articles/economy-of-minds-prompt-optimization
- 原文：https://x.com/neural_avb/status/2062930609861976454
- 本地文章：`2026-06-15-youmind-x-viral-articles-all/articles/0432-economy-of-minds-prompt-optimization.md`
- 本地封面：`2026-06-15-youmind-x-viral-articles-all/covers/0432-economy-of-minds-prompt-optimization.jpg`
- 数据：曝光 113612，点赞 315，收藏 764

## Skill Name

思维经济学Multi-Agent提示词优化详…风格双技能

## 文章 Skill

### 风格指纹

- 内容类型：爆款解释型文章
- 主题域：AI工具/Agent、个人成长/心理
- 开头机制：用第二人称直接点名读者处境，让读者马上把问题代入自己。
- 结构骨架：多章节长文，约 9 个小节，适合用罗马数字/编号标题推进。
- 段落节奏：中短段为主，解释和行动句交替，适合公众号快读。
- 语气判断：工具箱型：信息密度高，靠列表、步骤和模板提供收藏价值。
- 小标题样本：我为什么要关心这个？ / 方法 / 循环 1：收集经验 + 运行拍卖 / 循环 2：进化 Agent / 推理阶段，你实际交付的是什么？ / **
- 文本规模：约 4300 字符，73 个段落，9 个标题，28 个列表项，8 个引用块
- 爆款承诺：探索哈佛大学提出的全新“思维经济学”（Economy of Minds）如何利用市场拍卖机制，自动演化出超智能的 AI Agent 社会。

### 可复用文章提示词

```text
请使用「思维经济学Multi-Agent提示词优化详…风格双技能」的文章 skill 写一篇中文公众号文章。

主题：{填写新主题}
目标读者：{填写目标读者}
核心承诺：{读者读完会获得什么改变或判断}

写作方式：
1. 开头：用第二人称直接点名读者处境，让读者马上把问题代入自己。
2. 类型：采用「爆款解释型文章」；主题域优先靠近「AI工具/Agent、个人成长/心理」。
3. 结构：多章节长文，约 9 个小节，适合用罗马数字/编号标题推进。
4. 节奏：中短段为主，解释和行动句交替，适合公众号快读。
5. 语气：工具箱型：信息密度高，靠列表、步骤和模板提供收藏价值。
6. 小标题参考：我为什么要关心这个？ / 方法 / 循环 1：收集经验 + 运行拍卖 / 循环 2：进化 Agent / 推理阶段，你实际交付的是什么？ / **
7. 论证时先给判断，再给机制、例子或步骤；不要只堆观点。
8. 每个核心段落都要回答一个隐含问题：读者为什么现在要关心、怎么判断、下一步怎么做。
9. 结尾要把全文收束成一个可执行动作、一个判断标准，或一个值得收藏的清单。

避免：
- 不要写成泛泛鸡汤或百科说明。
- 不要把标题里的承诺摊薄，正文必须持续兑现「探索哈佛大学提出的全新“思维经济学”（Economy of Minds）如何利用市场拍卖机制，自动演化出超智能的 AI Agent 社会。」。
- 不要堆砌过多并列概念；每一节都要服务于主线。
- 不要使用夸张营销话术替代具体机制。
```

## 封面 Skill

### 风格指纹

- 画面类型：浅底极简信息图/产品幻灯片
- 原图尺寸：1894x758，比例 2.50:1
- 主色板：#ffffff white 78% / #c8c4c1 cream 8% / #eff7ec white 6% / #fefdfc white 4% / #fefffe white 4%
- 明暗/饱和/对比：brightness 248，saturation 2，contrast 21
- 构图策略：留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。
- 视觉隐喻：把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

### 可复用封面提示词

```text
Create a horizontal WeChat public-account article cover, 2.35:1 aspect ratio, for an article titled "思维经济学：Multi-Agent 提示词优化详解".

Central concept: 把抽象工具能力可视化为界面窗口、代码片段、节点网络、操作台、AI 工作流或发光的系统核心。

Style: preserve the reference cover's visual direction: 浅底极简信息图/产品幻灯片. Use a palette inspired by #ffffff (white), #c8c4c1 (cream), #eff7ec (white), #fefdfc (white). Keep the image editorial, conceptual, and readable as a small WeChat thumbnail.

Composition: 留白多，适合大标题、少量图标和清晰的左文右图/中心标题布局。 Keep the main subject and any essential title text inside the safe square crop, while using the full wide frame for atmosphere, secondary symbols, or directional motion.

Text strategy: use either no text or a very short headline fragment from the title. If text is used, make it large, clean, and integrated into the layout rather than pasted on top.

Mood: match the article skill "思维经济学Multi-Agent提示词优化详…风格双技能" -- useful, sharp, high-signal, and slightly more memorable than a normal tutorial thumbnail.

Avoid: photorealistic clutter unless the source cover is photo-led, fake logos, unreadable tiny text, generic gradient blobs, stock-office imagery, watermark-like marks, and literal screenshots unless the article is explicitly about software interfaces.
```

## 组合使用

先用文章 skill 确认文章的主承诺、段落节奏和结构骨架，再用封面 skill 提炼一个单一视觉隐喻。封面不要复述全文，要像文章第一屏的视觉钩子：一眼知道主题方向，但保留继续点开的悬念。
