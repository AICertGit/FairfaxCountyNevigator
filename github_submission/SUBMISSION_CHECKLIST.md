# Submission Checklist

## Review

- [ ] Review `README.md`.
- [ ] Review `FINAL_SUBMISSION_ONE_PAGER.md`.
- [ ] Review `docs/demo_architecture.md`.
- [ ] Review `docs/demo_service_catalog.md`.
- [ ] Review `index.html` in a browser.
- [ ] Confirm the Fairfax seal/logo treatment is acceptable for a prototype.

## Demo

- [ ] Open the full app from `frontend/index.html`.
- [ ] Test car tax routing.
- [ ] Test code complaint routing.
- [ ] Test urgent housing/basic needs routing.
- [ ] Test camp matching with age/interests/location/budget.
- [ ] Test older adult, childcare, public works, transportation, and public safety prompts.

## Secrets

- [ ] Confirm no `.env` files are staged.
- [ ] Confirm no service account JSON or credential JSON files are staged.
- [ ] Run:

```bash
rg -n "OPENAI_API_KEY|GOOGLE_API_KEY|AIza|sk-|Bearer|private_key" .
```

- [ ] Confirm only documentation reminder strings appear.

## GitHub

- [ ] Initialize Git locally.
- [ ] Add remote `https://github.com/AICertGit/FairfaxCountyNevigator.git`.
- [ ] Commit reviewed files.
- [ ] Push to GitHub after authentication is available.
- [ ] Enable GitHub Pages from the root branch/folder if using the static demo page.
