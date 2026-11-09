# web-joshuel

Personal site of Joshuel, at [joshuel.com.br](https://joshuel.com.br): SRE and DevOps profile, experience, stack, credentials and contact. English only.

| | |
|---|---|
| Runtime | `cloudfront` (static, no build): the files in `site/` are what is published |
| Name | the apex of the platform's zone, given to this app by `global/platform` (`zone_owners`); the site issues its own certificate |
| Deploy | merge to `main` → the platform's `deploy-app`: the site's infrastructure, the files, an invalidation |

## Design system

Built from the Jonoma IT emblem: its black is the canvas, its blue → violet → orange gradient is the signature, used sparingly (the brand line, one headline word, section marks, the contact loop).

```
site/css/tokens.css      primitives (brand colors sampled from the emblem, ink neutrals) → semantic tokens; dark first, light by system preference or the toggle
site/css/base.css        reset, text, reveal on scroll (everything visible without JavaScript or with reduced motion)
site/css/components.css  brand line, loop, emblem, buttons, status, eyebrow, gradient text, card, chips
site/css/sections.css    header, hero, timeline, stack, credentials, languages, contact, footer
```

Fonts: Geist and Geist Mono (OFL), served locally. No trackers, no external requests.

`design/` keeps the original emblem files; `site/img/` the web versions (WebP, favicon, Apple touch icon).

## Run locally

```bash
cd site && python3 -m http.server 8790
```
