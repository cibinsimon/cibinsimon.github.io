# cibinsimon.gitlab.io

Personal site of Cibin Simon, solution architect.

- Edit the page in `src/page.html` (single file: styles, content and scripts).
- `python build.py` writes the deployable page to `public/index.html`.
- GitLab CI (`.gitlab-ci.yml`) runs the build and publishes `public/` with GitLab Pages
  on every push to the default branch.

Preview locally: `python build.py && python -m http.server -d public 8000`, then open http://localhost:8000.
