# cibinsimon.github.io

Personal site of Cibin Mathew Simon, technical architect at Rappit.

- Edit the page in `src/page.html` (single file: styles, content and scripts).
- `python build.py` writes the deployable page to `public/index.html`.
- GitHub Actions (`.github/workflows/pages.yml`) runs the build and publishes `public/` with
  GitHub Pages on every push to `main`.

Preview locally: `python build.py && python -m http.server -d public 8000`, then open http://localhost:8000.
