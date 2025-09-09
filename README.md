# GTM KB — Complete Starter (GitHub Pages ready)

This repository includes:
- MkDocs Material config (Ahead brand palette, features, emoji config)
- Global footer timestamp (client-side JS), homepage cards with timestamp
- Full Pain Points + Technical structure (with vendor ranks)
- GitHub Actions workflow for Pages deploy
- requirements.txt for reproducible builds

## How to use (GitHub Desktop)
1) Unzip this repo into a **new empty folder**.
2) GitHub Desktop → File → Add local repository → select the folder.
3) Click **Publish repository**.
4) On GitHub: Settings → Pages → Build & deployment = **GitHub Actions**.
5) Push any change; Actions will build and deploy your site.

> If you see link warnings in strict mode, fix paths or temporarily drop `--strict` in `.github/workflows/pages.yml`.
