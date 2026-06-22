# Mindfulness Check-in Visual Style

## Source Materials

This reference captures the visual DNA for the generated cards. Local reference images or private prompt notes may be useful when authoring variants, but they are optional and should not be uploaded to the image API by default.

## Style DNA

- Format: vertical 3:4 social card, commonly `1080x1440` or `1440x1920`.
- Background: smooth abstract gradient, soft radial glow, pale yellow / light green / warm orange, low texture, gentle paper grain.
- Layout: large empty field, centered text block, text often slightly above center or around optical center.
- Typography: large black Chinese text, calm but strong; optional small English subtitle below.
- Mood: soothing, lucky, grateful, grounded, affirming, spacious, clean.
- Content: one sentence only; no tutorial density, no stickers, no high-clickbait layout.
- Important: the local reference screenshots have Xiaohongshu watermarks. Never reproduce or transfer those marks.

## Palette Variants

Use one of these when the user gives no palette:

- `yellow`: pale lemon edges, deeper warm yellow center.
- `green`: pale mint edges, luminous lime center.
- `orange`: warm yellow top, soft orange lower-left glow, creamy right side.
- `auto`: choose `yellow` for comfort/gratitude/luck, `green` for presence/life/moment, `orange` for courage/energy/warmth.

## Prompt Add-ons

Use for the background:

```text
soft abstract luminous gradient, gentle radial glow, pale yellow and warm cream, subtle paper grain, no hard shapes, no objects, lots of negative space
```

Use for text:

```text
elegant high-contrast black Chinese typography, large readable centered lines, optional smaller English subtitle below, generous line spacing
```

Use for strict watermark control:

```text
No watermark, no logo, no Xiaohongshu mark, no app badge, no account ID, no handle, no QR code, no signature, no bottom-right text, no platform UI, no extra captions.
```

## Few Shots

User sentence:

```text
每一个当下，都是生命中最美好的时刻
```

Expected behavior:

```text
Generate a 3:4 card with a pale green luminous center, large black Chinese text split into 2-3 centered lines, and no watermark or platform mark.
```

User sentence:

```text
我感恩一切，高峰，低谷，挫折，回归。
```

Expected behavior:

```text
Generate a warm yellow 3:4 card with the Chinese line as the focus and a small English subtitle such as "I'm thankful for everything." below.
```

User sentence:

```text
我是一个超级幸运的人
```

Expected behavior:

```text
Generate a cream-to-orange 3:4 card, centered text, optional subtitle "I am an incredibly lucky person.", with no account text at the bottom.
```
