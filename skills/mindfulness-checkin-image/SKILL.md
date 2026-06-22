---
name: mindfulness-checkin-image
description: Use when the user wants a 3:4 正念打卡图, mindfulness affirmation card, one sentence turned into an image, or an article/passage rewritten into 微信贴图文字 under 1000 Chinese characters. Trigger on phrases like "正念打卡", "打卡图", "贴图文字", "每天念", "积极暗示", "把这句话做成图", "一句话生成图片", "apiyi", "chatgptimage 2", or "gpt-image-2".
---

# Mindfulness Check-in Image

Handle two related workflows:

1. Sentence to image: generate a vertical 3:4 mindfulness check-in image from a short sentence. The default look is a calm abstract quote poster: soft luminous gradient, lots of negative space, one centered Chinese affirmation, optional small English line, no logos or watermarks.
2. Article to text: rewrite a longer article or passage into 微信贴图文字 under 1000 Chinese characters. Do not generate an image in this mode unless the user explicitly asks for image generation afterward.

## Inputs

Expected input:

- `sentence`: the exact sentence to place as the main text, when the user already provides a short poster-ready line.
- `source_text`: a longer article, paragraph, markdown draft, or transcript to rewrite into 贴图文字.
- Optional: English subtitle, palette, output folder, model, or whether to actually call the API.

If the user gives only one short sentence, infer it as `sentence` and use Sentence to image mode. If the user gives a longer passage, markdown draft, or asks for "文章", "贴图文字", or "1000字以内", infer it as `source_text` and use Article to text mode. Do not ask for missing style details unless the source itself is unclear.

## Local References

Load only when needed:

- Visual DNA: `references/visual-style.md`.
- Optional local reference images may exist on the user's machine, but they are not required.
- APiYi implementation pattern: use this skill's bundled script at `scripts/generate_mindfulness_image.py`.

Do not upload the local reference images to the image API by default; the source images contain Xiaohongshu watermarks and are for style inspection only.

## Workflow

### Step 1: Choose The Mode

Choose exactly one mode before acting.

Use **Sentence to image** when:

- The user gives one short poster-ready sentence.
- The user says "生成图片", "把这句话做成图", "正念打卡图", or similar.
- The text is already concise enough to render cleanly on a card.

Use **Article to text** when:

- The user gives a multi-paragraph article, markdown draft, transcript, outline, or long note.
- The user asks for "贴图文字", "文章转文字", "1000字以内", or copy for a WeChat 贴图 post.
- The source is too long to render cleanly on one image.

When the input is long or ambiguous, prefer Article to text and do not call the image API.

### Step 2A: Sentence To Image Text

Use this only in Sentence to image mode.

Use the user's sentence exactly as the main Chinese text unless the user asks for rewriting. If no subtitle is provided:

- For Chinese input, create a short natural English gloss.
- For non-Chinese input, either use the sentence as-is or create a short Chinese companion only if it improves the card.

Keep all in-image text minimal. Avoid long paragraphs.

### Step 2B: Article To 贴图文字

Use this only in Article to text mode. Do not generate an image in this mode.

Rewrite the source into a WeChat 贴图 title and post text under 1000 Chinese characters.

The title should:

- Be one clear WeChat 贴图 title, usually 8-20 Chinese characters.
- Name the central tension or insight, not tease vaguely.
- Avoid clickbait punctuation, exaggerated promises, and generic motivational wording.

The 贴图文字 should:

- Preserve the source's core argument, not summarize every section.
- Be readable as a standalone WeChat 贴图 caption or body text.
- Stay under 1000 Chinese characters; prefer 300-700 characters when enough.
- Keep strong original phrases, but remove scaffolding, caveats, examples, and repetitive explanation.
- Use short paragraphs with air between them.
- Prefer concrete conceptual contrast: "不是 X，而是 Y", "你卡住的不是 X，是 Y", or "真正的问题是 X".
- Avoid clickbait, therapy jargon, slogan padding, moralizing, or over-polished motivational language.

Also extract 3 short 可上图金句. Each should fit comfortably on a 3:4 poster: usually 18-42 Chinese characters, and at most 3 short lines.

For the user's business-closure source text, strong 可上图金句 include:

```text
你不是懒。
你是太擅长打开世界，
但商业要求你把世界关小一点。
```

```text
商业里的信任，
不是关系好，
而是降低对方的不确定性。
```

```text
商品化，
就是把无限可能，
压成一个可购买的承诺。
```

Return Article to text mode in this shape:

```text
## 标题
<标题>

## 贴图文字
<1000字以内正文>

## 可上图金句
1. <一句>
2. <一句>
3. <一句>
```

### Step 3: Build The Image Prompt

Use this only in Sentence to image mode.

Use this structure:

```text
Create a vertical 3:4 mindfulness affirmation poster, 1440x1920.

Main text, render exactly in Chinese:
"<sentence>"

Small subtitle, render exactly:
"<english-subtitle>"

Visual style: soft abstract luminous gradient background, calm poster for a daily mindfulness check-in, warm yellow / pale green / soft orange light fields, gentle radial glow, subtle paper grain, lots of clean negative space. Center the text block slightly above the optical center. Use elegant high-contrast black Chinese typography, large and readable, with a smaller serif or clean sans English subtitle below.

Composition: minimal, editorial, peaceful, generous margins, no characters, no objects unless the user asks.

Strictly avoid: any watermark, logo, Xiaohongshu mark, app badge, QR code, signature, account ID, copyright line, bottom-right text, platform UI, sticker, frame, border, extra captions, misspelled text, clutter, photorealistic scene, stock imagery.
```

For palette variants, read `references/visual-style.md`.

### Step 4: Generate The Image

Use this only in Sentence to image mode.

Use the bundled script:

```bash
python3 "$HOME/.agents/skills/mindfulness-checkin-image/scripts/generate_mindfulness_image.py" \
  --text "<sentence>" \
  --translation "<english-subtitle>" \
  --output-dir "$HOME/Desktop/正念打卡/generated"
```

Defaults:

- API base: `https://api.apiyi.com/v1`
- Model: `gpt-image-2`
- Generation size: `1440x1920`
- Final size: `1080x1440`
- Quality: `high`
- Output format: JPEG

Require one of these environment variables before an actual API call:

```bash
export APIYI_API_KEY="..."
# or
export YI_API_KEY="..."
```

For a no-cost preview, add `--dry-run`.

### Step 5: Validate The Image

Use this only in Sentence to image mode.

Check:

- Output is 3:4 and final card is `1080x1440`.
- Main text is present and readable.
- No logo, watermark, account ID, QR code, or bottom-right platform mark.
- Background is soft abstract gradient with quiet negative space.
- No extra decorative objects unless requested.

If the generated image has any watermark-like mark, rerun with stronger negative wording and do not present it as final.

## Output Shape

Return:

For Sentence to image mode:

```text
## 正念打卡图
- 文案：<sentence>
- 英文小字：<english-subtitle>
- 输出文件：<final-image-path>
- 原始图：<raw-image-path>

## 检查结果
- 比例/尺寸：
- 文字：
- 水印：
- 风格：
```

For Article to text mode:

```text
## 标题
<标题>

## 贴图文字
<1000字以内正文>

## 可上图金句
1. <一句>
2. <一句>
3. <一句>
```
