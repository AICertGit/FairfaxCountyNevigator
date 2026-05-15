# Fairfax Resource Navigator Web UI

This is a resident-facing mock UI for the Fairfax Resource Navigator prototype.

It is intentionally static for the demo: no build step, no API key, and no network dependency beyond opening cited Fairfax County source links.

## Run Locally

From the repo root:

```powershell
.\.venv\Scripts\python.exe -m http.server 5173 -d frontend
```

Open:

```text
http://localhost:5173
```

## Demo Questions

- `I need help with my Fairfax car tax bill.`
- `My neighbor is doing unpermitted construction. What should I do?`
- `I need urgent housing or safety help tonight.`
- `Are there still good summer camps in Fairfax County for my 9-year-old who likes sports and AI or STEM?`
- `What Fairfax resources can help with food, rent, utilities, and basic needs?`
- `Where do I go for trash, recycling, or a missed pickup in Fairfax County?`

## Triage Inputs

The client profile captures non-PII routing signals:

- Parent/guardian age
- Household ZIP code
- Household size
- Number of kids
- Approximate income range
- Urgency
- Service areas wanted
- Child age and interests, when youth programs are relevant

## Notes

- The UI mirrors the mock-first routing in `app/agent.py`.
- The next version should call a local backend endpoint and share source data with the ADK agent instead of duplicating route snippets in JavaScript.
