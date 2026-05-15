# Fairfax Service Navigator - Project Status and Plan

Date: 2026-05-15

## Short Answer

There is not a webpage yet. The project currently has planning documents, official Fairfax source downloads, a draft source inventory, and a first taxonomy recommendation. The next major step is to build the local prototype web app.

## What This Project Is

Fairfax Service Navigator is a research/prototype app for a staff-facing Fairfax County service-routing assistant. It is not a public chatbot.

The idea is to help staff triage resident or business questions by:

- Identifying the likely service area.
- Recommending the owning agency or routing path.
- Pulling from approved official Fairfax County sources.
- Drafting a resident-facing response.
- Drafting an internal ticket/CRM note.
- Showing citations and confidence.
- Flagging sensitive or low-confidence requests for human review.

For the hackathon, this can be framed as a civic AI research app: a responsible, human-in-the-loop service navigator that shows how generative AI could improve resident service routing without making autonomous decisions.

## What Has Been Created

### Planning and Project Control

- `fairfax_service_navigator_build_prompt.md`
  - Main operating brief and source of truth for the project.
- `business_plan.md`
  - Problem statement, strategic alignment, MVP scope, risks, resource needs, and leadership language.
- `project_context_log.md`
  - Running project memory: decisions, downloads, issues, lessons learned, and next steps.
- `project_status_and_plan.md`
  - This file; a concise status and plan for hackathon/project communication.

### Source and Research Files

- `docs/source_inventory.md`
  - Inventory of official Fairfax County / Fairfax-hosted sources.
- `docs/taxonomy_research_task.md`
  - Reusable research prompt for identifying the first service categories.
- `docs/taxonomy_v1_recommendation.md`
  - First recommended taxonomy slice for the MVP.
- `docs/raw/`
  - Downloaded official Fairfax source PDFs and HTML pages.
- `docs/raw/README.md`
  - Manifest for downloaded raw source files.

### Empty Project Areas Created

- `app/`
  - Reserved for the future local prototype web app.
- `eval/`
  - Reserved for synthetic test cases and evaluation scripts.
- `governance/`
  - Reserved for privacy, PII, risk, and human-review documentation.

## Downloaded Source Corpus

The project has downloaded core official Fairfax sources into `docs/raw/`, including:

- FY 2026 IT Plan Sections 1, 3, and 4.
- FY 2027 ITPAC Interim Letter.
- FY 2026 ITPAC Budget Letter.
- January 22, 2026 ITPAC meeting minutes.
- FY 2027 Advertised Budget Overview.
- Official service pages for:
  - Taxes.
  - PLUS/permitting.
  - Code compliance.
  - HHS/basic needs.
  - FOIA.
  - Parks.
  - Libraries.
  - Transportation.
  - Trash/recycling.
  - Non-emergency public safety.
  - Police.
  - Health.
  - Community Services Board.
  - Elections, as a seasonal/deferred planning source.

## Recommended MVP Taxonomy V1

The first version should focus on these service categories:

1. Public safety: 911 and non-emergency police/fire/EMS.
2. Taxes and fees.
3. Basic needs / human services.
4. PLUS, permitting, inspections, zoning, and land development.
5. Public health.
6. Code compliance / neighborhood complaints.
7. Transportation, roads, parking, Connector, and commuting.
8. Libraries.
9. Trash, recycling, disposal, carts, and collection ownership.
10. Mental health, substance use, developmental disability / CSB crisis, with strong escalation handling.

Near-follow:

- Parks and recreation.

Deferred or seasonal:

- Voting and elections.

## Hackathon Goal

For the Google hackathon, the best finish line is a working local demo that shows the end-to-end concept without needing confidential data or production integrations.

Target demo:

- User enters a resident question.
- App classifies service area and urgency.
- App recommends routing.
- App returns a short resident-ready response.
- App returns an internal staff note.
- App displays citations from official Fairfax sources.
- App shows confidence and escalation flags.
- App logs the test result locally.
- Small dashboard shows recent requests, categories, confidence, and feedback.

## Recommended Build Path

### Phase 1 - Corpus Preparation

- Extract text from downloaded PDFs and HTML files.
- Normalize each source into records with:
  - Title.
  - Source URL.
  - Local file path.
  - Department/owner.
  - Service category.
  - Sensitivity.
  - Last downloaded date.
- Create a simple searchable source index.

### Phase 2 - Local Web Prototype

Recommended quick stack:

- Front end: Streamlit or React/Vite.
- Back end: Python or Node.js.
- Retrieval: local keyword search first, then vector search if time allows.
- Model path: mock-first/local-first response generator, then optional approved model integration later.

Fastest hackathon option:

- Use Streamlit with local Python scripts.
- Use keyword/BM25-style search over extracted source text.
- Use deterministic/mock generation templates first.
- Add LLM/model integration only after the core workflow works.

### Phase 3 - Evaluation

- Create 50-100 synthetic resident requests.
- Score:
  - Top-1 routing accuracy.
  - Top-3 routing accuracy.
  - Citation coverage.
  - Escalation accuracy.
  - Groundedness.
- Log failures as content gaps or taxonomy gaps.

### Phase 4 - Governance Packet

- Document:
  - Public-source-only corpus.
  - No confidential resident data.
  - Human-in-the-loop workflow.
  - PII handling assumptions.
  - Sensitive-topic escalation.
  - Records/FOIA/logging questions.
  - Accessibility and language-access considerations.

### Phase 5 - Demo Story

Show three examples:

1. Routine routing:
   - "I need help paying my car tax."
2. Cross-agency routing:
   - "My neighbor is building something without a permit."
3. Sensitive escalation:
   - "I need help tonight with housing and I feel unsafe."

## What Is Not Done Yet

- No webpage/local app yet.
- No source text extraction yet.
- No retrieval index yet.
- No routing classifier yet.
- No mock response generator yet.
- No evaluation set yet.
- No dashboard yet.
- No governance packet yet.

## Immediate Next Steps

1. Extract text from the downloaded PDFs and HTML files.
2. Create normalized source metadata records.
3. Build a simple local search function.
4. Build the first UI in `app/`.
5. Add mock routing and response generation.
6. Add citations and confidence labels.
7. Add feedback buttons and local logging.
8. Create synthetic test cases in `eval/`.

## One-Sentence Pitch

Fairfax Service Navigator is a human-in-the-loop civic AI research prototype that helps staff route resident questions to the right Fairfax County service using only approved official sources, citations, confidence scoring, and escalation controls.
