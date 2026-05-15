# Fairfax Resource Navigator

Fairfax Resource Navigator is a local Google ADK starter-pack demo for routing Fairfax County resident questions to the right county service area. It is designed as a human-in-the-loop civic AI prototype: source-grounded, privacy-conscious, and conservative around emergencies, eligibility, tax, legal, safety, and account-specific questions.

## Weblink
https://aicertgit.github.io/FairfaxCountyNevigator/

## Demo Status

- Local resident UI: `frontend/`
- ADK agent: `app/agent.py`
- Deployment target scaffold: Vertex AI Agent Engine
- Current chat path: deterministic/mock-first, no live OpenAI, Gemini, Gemma, or other model API calls
- Remote deployment: not yet deployed; `deployment_metadata.json` shows no Agent Engine ID

## What The Demo Covers

The UI and ADK agent route across the core Fairfax service catalog:

- Housing and basic needs: CSP, food, rent, utilities, shelters, homelessness, affordable housing, LIHTC, waitlists
- Taxes and revenue: vehicle tax, tax relief, real estate assessments, payments, appeals
- Health and human services: CSB crisis/addiction/opioid support, public health, older adults, Meals on Wheels, childcare, Head Start
- Parks, recreation, and youth: Parktakes, FCPA/NCS camps, camp matching, Sully/Lorton/community hubs
- Land use, permits, and code: DCC complaints, PLUS, permits, zoning, property-line questions
- Public works and utilities: trash, recycling, purple glass bins, hazardous waste, water/sewer
- Transportation: Fairfax Connector, Metro integration context, Fastran, potholes, roads, parking
- Public safety: 911, non-emergency police/fire/EMS, noise complaints, animal control, Fire and Rescue outreach

## Demo Script

Start with the resident UI and try these prompts:

1. `I need help with my Fairfax car tax bill.`
2. `My neighbor is doing unpermitted construction. What should I do?`
3. `I need urgent housing or safety help tonight.`
4. `Are there still good summer camps in Fairfax County for my 9-year-old who likes sports and STEM?`
5. `My parent needs Meals on Wheels or aging-in-place help.`
6. `I need subsidized childcare or Head Start information.`
7. `Where do I report a pothole or find Fairfax Connector help?`
8. `There is a sewer backup or missed trash pickup. Where do I start?`

Expected output includes route, destination, urgency guidance, next steps, confidence, and citations to official Fairfax County or Fairfax-hosted sources.

## Project Structure

```text
fairfax-service-navigator/
  app/                         ADK agent and Agent Engine wrapper
  frontend/                    Local resident-facing demo UI
  docs/                        Source inventory, service catalog, architecture, wrap-up notes
  tests/                       Unit and integration tests
  FINAL_SUBMISSION_ONE_PAGER.md
  business_plan.md
  project_status_and_plan.md
```

## Key Documents For Review

- `FINAL_SUBMISSION_ONE_PAGER.md` - short submission narrative and demo framing
- `docs/demo_architecture.md` - architecture, data flow, privacy, and deployment path
- `docs/demo_service_catalog.md` - covered routing domains and triage rules
- `docs/demo_wrap_up_notes.md` - deployment, API status, and GitHub secret hygiene

## Running Locally

Install dependencies and run the ADK playground:

```bash
make install
make playground
```

The frontend is a static local UI in `frontend/`. It can be served by any simple local static server.

## Testing

Local agent tests:

```bash
uv run pytest tests/integration/test_agent.py tests/unit/test_dummy.py
```

Full `uv run pytest` currently requires Google Application Default Credentials because the Agent Engine integration test imports the Vertex wrapper.

## GitHub And Secrets

Do not commit real API keys, `.env` files, service account JSON, OAuth tokens, ADK saved chats, logs, or local credential files. `.gitignore` excludes common local secret and runtime artifacts. Run a final secret scan before pushing to GitHub.

Suggested search before push:

```bash
rg -n "OPENAI_API_KEY|GOOGLE_API_KEY|AIza|sk-|Bearer|private_key" .
```
