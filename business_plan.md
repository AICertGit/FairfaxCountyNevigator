# Fairfax Service Navigator + 311 Triage Copilot Business Plan

## Problem Statement

Fairfax County residents and businesses often enter county service channels with questions that cut across agency boundaries: taxes, permitting, trash and recycling, code complaints, health and human services, FOIA, parks, libraries, transportation, and non-emergency public safety. Staff must interpret the request, identify the owning agency or workflow, locate the correct source page or form, and draft a clear response. This creates avoidable transfers, inconsistent answers, repeated lookup time, and limited visibility into recurring content gaps.

The Fairfax Service Navigator MVP will test whether an internal staff-facing pilot can provide service-routing intelligence grounded only in approved Fairfax County sources. The tool will recommend routing, cite sources, draft resident-facing responses, draft internal CRM/ticket notes, and flag low-confidence or sensitive requests for human review.

## Why Now

Fairfax County's current IT planning and advisory priorities point toward customer experience modernization, AI/ML, data analytics, cybersecurity, cloud/application modernization, and more seamless digital service delivery. Public web content, service pages, IT planning documents, and budget materials are already available for a low-risk first corpus. A two-month prototype is feasible because the MVP can start with approved public content, synthetic evaluation cases, and a narrow internal advisory workflow rather than requiring production CRM integration or use of confidential resident data.

The opportunity is timely because staff-facing responsible AI can be evaluated before any public chatbot expansion. This creates a reusable responsible AI pattern: approved-source grounded responses, human-in-the-loop controls, auditability, evaluation metrics, and privacy-aware logging.

## Strategic Alignment

- DIT and FY 2026 IT Plan themes: digital government, data architecture and analytics, cybersecurity, business applications, planning and land use modernization, public safety systems, health and human services technology, and cloud/application modernization.
- ITPAC FY 2027 direction: customer portals, One Account/One Experience, AI/ML, data analytics, agile delivery, data governance, and IT optimal state.
- Customer experience modernization: help staff provide faster, more consistent routing and responses across common service areas.
- Data analytics: capture repeated request patterns, low-confidence categories, content gaps, and possible transfer-reduction opportunities.
- Cybersecurity and governance: use public/sanitized data first, require citations, preserve human review, and avoid autonomous service decisions.
- One Account/One Experience: demonstrate a cross-agency service-navigation layer that could later inform unified service entry and customer portal strategy.

## MVP Scope

The MVP is an internal staff-facing pilot, not a public chatbot.

Core capabilities for later phases:

- Staff enters a resident/business request or sanitized past-ticket text.
- System classifies intent, service area, likely owning agency, urgency, and sensitivity.
- System retrieves relevant Fairfax-approved public content.
- System generates recommended routing, resident-ready response, internal ticket note, citations, confidence score, and escalation guidance.
- Dashboard summarizes top request categories, low-confidence topics, repeated content gaps, and potential deflection or transfer-reduction opportunities.
- Logs preserve prompt, retrieved sources, generated answer, confidence, user decision, and feedback for audit and evaluation.

Phase 0 and 0.5 only:

- Create the business plan, project context log, source inventory, and initial project folders.
- Identify official Fairfax County or Fairfax-hosted source URLs.
- Do not build the application, retrieval pipeline, taxonomy, evaluation set, or governance packet yet.

## Non-Goals

- No public-facing chatbot in the MVP.
- No autonomous eligibility, enforcement, legal, benefits, health, public safety, or case decisions.
- No ingestion of confidential resident data unless explicitly approved later.
- No CRM, identity, document management, or service catalog integration during initialization.
- No cloud deployment decision until approved model access, hosting, security, and procurement constraints are confirmed.
- No use of non-Fairfax sources unless the project owner approves.
- No use of county resources, nonpublic data, or county code for personal startup activity.

## Target Users and Stakeholders

- Primary users: customer service staff, 311-style intake staff, web/contact-center staff, agency liaisons, and DIT prototype evaluators.
- Secondary users: service owners who maintain web pages, knowledge base content, forms, and routing rules.
- Stakeholders: DIT leadership, agency business owners, Office of Public Affairs, privacy/security reviewers, records/FOIA stakeholders, accessibility/language access stakeholders, and pilot staff supervisors.
- Resident/business beneficiaries: people seeking clearer routing, faster answers, and fewer transfers.

## Feasibility Logic for a Two-Month MVP

- Public Fairfax County pages provide enough source material for a safe initial corpus.
- A narrow set of high-volume categories keeps routing taxonomy manageable.
- Synthetic service requests can support early evaluation without resident PII.
- A local prototype can demonstrate the workflow without production integration.
- Human-in-the-loop review reduces risk while preserving useful staff augmentation.
- Metrics can focus on routing accuracy, groundedness, confidence calibration, content gaps, and estimated transfer reduction.

## Resource Needs

- Data and documents: public Fairfax County pages and PDFs; later, sanitized internal SOPs only if approved.
- Staff interviews: 311-style intake, agency liaisons, customer service representatives, web/content owners, and public-facing service owners.
- Architecture review: local prototype architecture, retrieval design, logging design, and future integration assumptions.
- Security/privacy review: data classification, PII handling, records retention, FOIA/public-records implications, model access, and logging controls.
- Hosting/runtime: local machine first; future low-cost cloud or enterprise path only after approval.
- Model access: approved Fairfax AI/model platform if available; otherwise local mock layer or project-owner-approved alternative.
- Vector/search layer: local files plus SQLite/FAISS/Chroma, or approved enterprise search if available.
- UI framework: simple local React/Vite, Next.js, Streamlit, or equivalent.
- Evaluation set: 100-200 synthetic or sanitized service requests.
- Pilot users: small internal reviewer group representing cross-agency intake scenarios.

## Free or Accessible Tooling Options

- Local development: Python or Node.js.
- Front end: Streamlit for quickest local workflow, or React/Vite for a richer staff UI.
- Retrieval: local markdown/PDF text extraction plus SQLite, FAISS, or Chroma.
- Evaluation: CSV/JSON test cases with scripted scoring for top-1/top-3 routing, citation coverage, and groundedness.
- Documents: public Fairfax County PDFs and pages stored in `docs/raw/`.
- Logging: local JSONL or SQLite audit log during prototype evaluation.
- Mock model path: deterministic templates or local fixtures if approved model access is not yet available.

## Leadership Phrases

- "Internal staff-facing pilot"
- "Human-in-the-loop"
- "Approved-source grounded responses"
- "Service-routing intelligence"
- "Customer experience modernization"
- "Measurable transfer reduction"
- "Reusable responsible AI pattern"
- "Narrow, evidence-based prototype before public exposure"
- "Analytics for service improvement, not agency blame"
- "Responsible AI guardrails from day one"

## Promotion Narrative for IT Data/AI Architect Role

This MVP positions the IT Data/AI Architect role as a practical bridge between strategy and delivery: translating AI/ML, data analytics, customer experience, governance, and service modernization goals into a working pattern that can be evaluated with evidence. The project demonstrates architecture judgment, cross-agency service thinking, responsible AI controls, evaluation discipline, and leadership communication.

## Future Startup-Shaped Opportunity

The general pattern of staff-facing service-routing copilots may have broader civic technology relevance. Any exploration must remain separate from county time, county systems, county code, county relationships, and nonpublic county data. The county MVP should be treated as county work for county benefit, with no transfer of confidential knowledge, resident data, internal SOPs, or procurement-sensitive information to outside use.

## Initial Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Source pages are outdated or inconsistent. | Maintain `docs/source_inventory.md` with owner, refresh cadence, and review status. |
| Service ownership is ambiguous. | Start with recommended routing and escalation notes, not automated assignment. |
| Generated answers may hallucinate. | Require citations, source-grounded response templates, and confidence thresholds. |
| Sensitive requests may be mishandled. | Flag public safety, health, benefits, legal, enforcement, juvenile, and PII-heavy topics for human review. |
| Logs may create privacy or records issues. | Use synthetic inputs first; define logging, retention, and FOIA assumptions before pilot expansion. |
| Staff may view AI as replacement. | Frame as staff augmentation and service improvement support. |
| Leadership may see "chatbot" risk. | Use "internal staff-facing pilot" and "human-in-the-loop service-routing intelligence." |
| Tooling or model access may be blocked. | Begin with local/no-cost prototype and ask for approved model/vector/search options. |

## Open Questions for Confirmation

- Model/tooling default is mock-first/local-first for early testing. Later confirmation needed for approved model access, if any: Azure OpenAI, Copilot Studio, AWS Bedrock, Google Vertex AI, or an internal LLM platform.
- Are there approved vector database, enterprise search, service catalog, document management, or CRM APIs available?
- Can sanitized CRM/ticket examples be used later, and what de-identification rules apply?
- Which staff group should define routing correctness for the first evaluation set?
- Are internal SOPs allowed in the prototype corpus, or should Phase 1 remain public-source only?
- Who signs off on privacy, security, records retention, FOIA, accessibility, and language access assumptions?
- Which 8-12 service categories should be included in the first taxonomy slice? A research task has been created in `docs/taxonomy_research_task.md`.
- Should the first local UI be Streamlit for speed or React/Vite for a more realistic staff interface?
- Phase 1 may download PDFs/pages into `docs/raw/` or use URL-only records, whichever best supports execution.
