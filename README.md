# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).

## Building (Nov 2026 redesign)

The site is static and pre-rendered per language. Edit the sources, then run `python3 build.py` and commit `public/`:

- `src/index.html`: home template (elements with `data-k` get their copy from `src/copy.json`)
- `src/copy.json`: home copy (TR + EN), agent list, statuses
- `src/content.py`: head meta, FAQ, agent pages
- `public/site.css`: shared styles

`build.py` writes `/`, `/en/`, the agent pages, `sitemap.xml`, `robots.txt` and `llms.txt`. The live agent's key comes from `netlify/functions/realtime-session.mjs` (needs `OPENAI_API_KEY` in Netlify).
