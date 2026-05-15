# Fairfax Resource Navigator

## One-Page Final Submission

**Project:** Fairfax Resource Navigator  
**Build target:** Google ADK starter pack with Agent Engine deployment target  
**Demo URLs:** Resident web UI at `http://localhost:5173`; ADK playground at `http://localhost:8501`  
**Status:** Working local prototype, mock-first routing, source-grounded citations, resident-facing UI draft  
**API status:** The demo chat path does not call OpenAI, Gemini, Gemma, or any other live model API. Vertex/Agent Engine code is present for later deployment only.

## Problem

Residents often know what they need, but not which Fairfax County service, agency, portal, or phone number should handle it. High-friction topics like vehicle taxes, code complaints, permits, urgent housing help, basic needs, and public safety can span multiple departments and require careful escalation.

The risk is not only inconvenience. A civic navigation assistant must avoid giving legal, tax, eligibility, safety, or enforcement advice while still helping people reach the right official channel quickly.

## Solution

Fairfax Resource Navigator is a human-in-the-loop civic service-routing agent. It accepts plain-language resident questions, classifies the likely service route, identifies urgency and sensitivity, and returns a concise next-step response with citations from official Fairfax County or Fairfax-hosted sources.

The current prototype is intentionally mock-first. The routing and response generation are deterministic so the demo works reliably in the ADK playground before adding production retrieval, CI/CD, observability, or cloud deployment polish.

Because deployment can take longer than the demo window, the recommended submission path is the local resident UI plus the ADK playground. Cloud deployment should be treated as a follow-up step, not a blocker for the one-page demo story.

## What Works Now

- ADK starter-pack repo created as `fairfax-service-navigator`.
- Resident-facing web UI runs from `frontend/` at `http://localhost:5173`.
- Local ADK playground runs at `http://localhost:8501`.
- Agent code lives in `app/agent.py`.
- UI prototype lives in `frontend/` and provides the main Google ADK demo surface for resident intake, service routing, urgency display, confidence, and citations.
- Fairfax project materials copied into the starter repo:
  - `business_plan.md`
  - `project_status_and_plan.md`
  - `docs/source_inventory.md`
  - `docs/taxonomy_v1_recommendation.md`
  - `docs/raw/`
- The local UI and ADK agent cover the core Fairfax service catalog:
  - Housing and basic needs: CSP, emergency food, rent/utilities, affordable housing, LIHTC/waitlists, shelters, homelessness.
  - Taxes and revenue: car/personal property tax, tax relief, real estate assessments/payments/appeals.
  - Health and human services: CSB crisis/addiction/opioid support, public health, older adults, Meals on Wheels, childcare, Head Start.
  - Parks, recreation, and youth: Parktakes, FCPA/NCS camps, camp matching by age/interests/location/budget, Sully/Lorton/community hubs.
  - Land use, permits, and code: DCC complaints, tall grass, hoarding, illegal construction, boarding houses, PLUS permits/zoning.
  - Public works and utilities: trash/recycling, purple glass bins, hazardous waste, water/sewer routing.
  - Transportation: Fairfax Connector, Metro integration context, Fastran, roads, potholes.
  - Public safety: non-emergency police, noise complaints, animal control, Fire and Rescue inspections/outreach.

## Demo Script

Open the resident web UI at `http://localhost:5173` and try:

1. `I need help with my Fairfax car tax bill.`
2. `My neighbor is doing unpermitted construction. What should I do?`
3. `I need urgent housing or safety help tonight.`
4. `Are there still good summer camps in Fairfax County for my 9-year-old who likes sports and AI or STEM?`
5. `My parent needs Meals on Wheels or aging-in-place help.`
6. `I need subsidized childcare or Head Start information.`
7. `Where do I report a pothole or find Fairfax Connector help?`
8. `There is a sewer backup or missed trash pickup. Where do I start?`

For the ADK proof view, open `http://localhost:8501`, select the `app` agent, and use the same prompts.

Expected output includes:

- Route
- Destination
- Urgency guidance
- Recommended next steps
- Citations to official Fairfax County or Fairfax-hosted sources

## Source Grounding

The prototype uses the source inventory and local snapshots in `docs/raw/`. Example cited sources include:

- Fairfax County Vehicle Taxes & Fees
- Fairfax County Code Compliance violation reporting
- Fairfax-hosted PLUS portal routing
- Coordinated Services Planning
- Basic Needs and Assistance
- Public safety non-emergency routing
- Fairfax County Park Authority camps
- Neighborhood and Community Services camps
- Sully Summer Sports Camp

## Current Limitation

The prototype now includes a first-pass Parks and Recreation / youth camps route, but it does not yet perform live seat availability search or registration filtering. It gives a source-grounded route and asks for ZIP code, preferred weeks, budget, transportation needs, and activity preference.

The next iteration should connect the UI to a backend endpoint, add lightweight retrieval over `docs/raw/`, add live availability/search where appropriate, and broaden the source inventory for deeper department-specific citations.

## GitHub and Secrets Note

Do not commit real API keys, `.env` files, service account JSON, access tokens, ADK saved chats, logs, or local credential files. `.gitignore` already excludes `.env`, local logs, `.adk/`, and saved chats; run a final secret scan before pushing to GitHub. If model integration is added later, keep keys in environment variables only.

## Why It Matters

This project demonstrates a practical public-sector AI pattern:

- Start with official public sources.
- Keep high-risk topics conservative.
- Cite every routing recommendation.
- Use human escalation for emergencies, safety, eligibility, enforcement, tax, or account-specific questions.
- Build a reliable local demo before spending time on CI/CD, observability, or production deployment.

## Next Steps

1. Expand deterministic routes from the taxonomy v1 document.
2. Add lightweight retrieval over `docs/raw/`.
3. Add confidence scores and escalation flags.
4. Create evaluation examples for the top service categories.
5. Deploy to Agent Engine after the local demo path is stable.
6. Run a final secret scan, then push the repo to GitHub for submission review.
