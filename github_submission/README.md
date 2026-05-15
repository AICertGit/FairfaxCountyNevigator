# GitHub Submission Packet

This folder collects the files and notes to review before publishing the Fairfax Resource Navigator repo to GitHub.

## Primary Review Files

- `../README.md` - GitHub-facing project overview and run/test notes.
- `../index.html` - GitHub Pages entry point that presents and embeds the local demo UI.
- `../FINAL_SUBMISSION_ONE_PAGER.md` - short project narrative for reviewers.
- `../docs/demo_architecture.md` - architecture, Mermaid flow diagrams, privacy model, data flow, and deployment path.
- `../docs/demo_service_catalog.md` - service domains, routing categories, and triage rules.
- `../docs/demo_wrap_up_notes.md` - API status, deployment notes, and secret hygiene.

## Current Publish Plan

1. Review the primary Markdown files.
2. Open `index.html` locally and confirm the embedded UI looks correct.
3. Run local tests that do not require Google cloud credentials.
4. Run the secret scan.
5. Initialize Git, add the GitHub remote, commit, and push.
6. Enable GitHub Pages from the repository root if a public static demo page is desired.

## Repository Target

Planned remote:

```text
https://github.com/AICertGit/FairfaxCountyNevigator.git
```

This local folder is not currently initialized as a Git repository, and GitHub CLI is not installed in this environment.
