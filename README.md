# Continuum Mechanics — Companion Site

Quarto website scaffold pairing lecture theory with interactive visualizations.

## Structure

```
.
├── _quarto.yml              # site config, nav
├── styles.css                # minimal iframe styling
├── index.qmd                 # landing page
├── lectures/
│   ├── 01-stress-strain.qmd
│   ├── 02-decomposition.qmd
│   ├── 03-yield-criteria.qmd
│   ├── 04-elastic-constants.qmd
│   └── stress_strain_curve.png
├── interactives/              # self-contained HTML/JS visualizations
│   ├── strain_decomposition.html
│   ├── pi_plane_yield.html
│   ├── lame_constants.html
│   ├── poisson_intuition.html
│   └── lame_intuition.html
└── .github/workflows/publish.yml
```

## Local preview

```
quarto preview
```

## First-time GitHub setup

1. Create a new repo on GitHub, push this folder to `main`.
2. In the repo's **Settings → Pages**, set the source to the `gh-pages` branch
   (the Actions workflow creates/updates this branch automatically on push).
3. Edit `_quarto.yml` — replace `YOUR_USERNAME/YOUR_REPO` in the GitHub navbar link.
4. Push to `main`. The `publish.yml` workflow renders the site and deploys it —
   no local Quarto install strictly required after that, though `quarto preview`
   locally is much faster for iterating.

## Adding a new lecture page

1. Add a `.qmd` file under `lectures/`.
2. Add its entry to the `navbar` list in `_quarto.yml`.
3. To embed a new interactive visualization, drop the self-contained `.html` file
   in `interactives/` and reference it:
   ```
   ```{=html}
   <iframe class="interactive-frame" src="../interactives/your_file.html"></iframe>
   ```
   ```
