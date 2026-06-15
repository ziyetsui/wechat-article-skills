# WeChat Article Skills

Codex skills for a WeChat Official Account article workflow:

- `wechat-rewrite`: rewrite raw materials into a Chinese WeChat article and generate titles.
- `wechat-cover-image`: generate article covers with APiYi GPT Image 2.
- `wechat-layout`: format rewritten articles into WeChat-ready HTML/TXT.
- `wechat-publish-draft`: upload formatted articles to the WeChat Official Account draft box.
- `wechat-article-pipeline`: coordinate rewrite, cover, layout, and draft upload.

## Install

Copy the skill folders into your local agent skills directory:

```bash
cp -R skills/wechat-* ~/.agents/skills/
```

## Configuration

Do not commit real API keys or WeChat credentials.

Required runtime environment variables are documented in the relevant skill files and examples:

- `APIYI_API_KEY` or `YI_API_KEY` for cover generation.
- `WECHAT_APPID` and `WECHAT_APPSECRET` for draft upload.

Use `skills/wechat-publish-draft/scripts/.env.example` as a template only.
