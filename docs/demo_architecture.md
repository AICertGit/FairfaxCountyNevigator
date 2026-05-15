# Fairfax Resource Navigator Demo Architecture

Date: 2026-05-15

## Purpose

Fairfax Resource Navigator is a local Google ADK demo that shows how a civic service-routing assistant could help staff or residents identify the right Fairfax County service path. The demo prioritizes reliability, privacy, official-source citations, and human escalation over autonomous decision-making.

## Current Architecture

The current demo has two working local paths: a static resident UI for fast review, and an ADK proof path that exercises the same routing logic inside the Google ADK agent structure. The cloud deployment path is scaffolded but intentionally not required for review.

![Fairfax Resource Navigator architecture flow preview](assets/architecture-flow-preview.png)

```mermaid
flowchart LR
    reviewer["Resident / Reviewer"]:::person
    pages["GitHub Pages Entry<br/>index.html"]:::surface
    ui["Resident Demo UI<br/>frontend/index.html"]:::surface
    js["Deterministic UI Router<br/>frontend/app.js"]:::logic
    output["Resident-Facing Answer<br/>route, urgency, next steps, citations"]:::answer

    playground["ADK Playground<br/>local proof view"]:::surface
    agent["FairfaxServiceNavigatorAgent<br/>app/agent.py"]:::logic
    route["route_request()<br/>service domain + urgency"]:::logic
    response["generate_response()<br/>source-grounded response"]:::logic

    sources["Official Fairfax Sources<br/>docs/source_inventory.md<br/>docs/raw/ snapshots"]:::source
    catalog["Demo Service Catalog<br/>docs/demo_service_catalog.md"]:::source

    future["Future Agent Engine Path<br/>app/agent_engine_app.py"]:::future
    vertex["Vertex AI Agent Engine<br/>optional deployment"]:::future

    reviewer --> pages
    pages --> ui
    ui --> js
    js --> output
    js -. cites .-> sources
    js -. uses .-> catalog

    reviewer --> playground
    playground --> agent
    agent --> route
    route --> response
    response --> output
    response -. cites .-> sources
    response -. uses .-> catalog

    agent -. later deploy .-> future
    future -. optional .-> vertex

    classDef person fill:#f7fbff,stroke:#071f2c,stroke-width:2px,color:#071f2c;
    classDef surface fill:#eaf3f7,stroke:#123446,stroke-width:1.5px,color:#071f2c;
    classDef logic fill:#fff7e8,stroke:#b67822,stroke-width:1.5px,color:#17212b;
    classDef answer fill:#eef7ed,stroke:#4d7b4a,stroke-width:1.5px,color:#17212b;
    classDef source fill:#f4f7f8,stroke:#5d6874,stroke-width:1.5px,color:#17212b;
    classDef future fill:#f2eef8,stroke:#6f5f94,stroke-width:1.5px,color:#17212b;
```

## Request Flow

```mermaid
sequenceDiagram
    autonumber
    participant User as Resident or Reviewer
    participant UI as Local Demo UI
    participant Router as Routing Logic
    participant Guardrails as Safety and Privacy Guardrails
    participant Sources as Fairfax Source Catalog
    participant Answer as Response Panel

    User->>UI: Enters a plain-language need
    UI->>Router: Combines prompt with optional non-PII context
    Router->>Guardrails: Checks emergency and sensitive-topic rules
    Guardrails-->>Router: Emergency route or normal triage
    Router->>Sources: Selects service citations and catalog entries
    Sources-->>Router: Department, program, and source snippets
    Router->>Answer: Builds route, destination, urgency, next steps, citations
    Answer-->>User: Shows source-grounded guidance
```

## Runtime Behavior

- The local resident UI runs from `frontend/` and performs deterministic routing in `frontend/app.js`.
- The ADK agent runs deterministic routing in `app/agent.py`.
- The demo does not call OpenAI, Gemini, Gemma, or any live model API during normal chat.
- Vertex Agent Engine scaffolding exists for later deployment, but the current demo can be reviewed locally without cloud deployment.

## Service Routing Layer

The routing layer maps plain-language resident prompts into primary service domains:

- Housing and basic needs
- Taxes and revenue
- Health and human services
- Parks, recreation, and youth
- Land use, permits, and code
- Public works and utilities
- Transportation
- Public safety

Each route includes:

- Destination department or program
- Urgency guidance
- One or more next steps
- Official Fairfax County or Fairfax-hosted citation snippets

## Camp Matching

Camp questions use a small official-demo catalog and score by:

- Child age
- Interests
- Location preference
- Budget or affordability concern

The demo explicitly explains why a camp is recommended. For example, STEM/robotics/coding interests route toward STEM Robo-Creators, while affordability concerns boost Rec-PAC.

## Emergency And Safety Handling

The emergency override routes severe crisis language to 911 or CSB Emergency Services at `703-573-5679`. Trigger terms include violence, self-harm, suicide, weapon, overdose, severe crisis, and immediate danger.

The assistant should not continue ordinary triage when an emergency override is triggered.

```mermaid
flowchart TD
    prompt["User prompt"]:::surface
    check{"Immediate danger,<br/>self-harm, violence,<br/>weapon, overdose,<br/>severe crisis?"}:::decision
    emergency["Emergency override<br/>Route to 911 or CSB Emergency Services<br/>703-573-5679"]:::critical
    normal["Normal service triage<br/>Pick primary and secondary domain"]:::logic
    pii["Privacy filter<br/>Use ZIP, age, household size,<br/>interests, urgency only"]:::guard
    route["Department or program route<br/>plus next steps and citations"]:::answer

    prompt --> check
    check -- Yes --> emergency
    check -- No --> normal
    normal --> pii
    pii --> route

    classDef surface fill:#eaf3f7,stroke:#123446,stroke-width:1.5px,color:#071f2c;
    classDef decision fill:#fff7e8,stroke:#b67822,stroke-width:1.5px,color:#17212b;
    classDef critical fill:#fff0f0,stroke:#a94442,stroke-width:2px,color:#17212b;
    classDef logic fill:#fff7e8,stroke:#b67822,stroke-width:1.5px,color:#17212b;
    classDef guard fill:#f4f7f8,stroke:#5d6874,stroke-width:1.5px,color:#17212b;
    classDef answer fill:#eef7ed,stroke:#4d7b4a,stroke-width:1.5px,color:#17212b;
```

## Privacy Model

The demo does not need names, exact home addresses, account numbers, Social Security numbers, or other sensitive identifiers.

Allowed low-risk routing context:

- ZIP code
- General neighborhood or cross street
- Age range or child age
- Household size
- Approximate income range
- Service interests
- Timing or urgency

## Data And Sources

The demo uses local source metadata and snapshots in:

- `docs/source_inventory.md`
- `docs/raw/`
- `docs/demo_service_catalog.md`

The source strategy is official-public-source-first. The demo avoids live eligibility, permit, tax, shelter placement, legal, or medical determinations.

## Deployment Path

The repo was created from the Google ADK starter pack with an Agent Engine deployment target. Deployment is intentionally not required for the demo because cloud setup can take longer than the review window.

Recommended sequence:

1. Review the local UI and ADK playground.
2. Review `FINAL_SUBMISSION_ONE_PAGER.md`.
3. Run local tests that do not require cloud credentials.
4. Run a secret scan.
5. Initialize Git and connect the GitHub remote.
6. Push only after review.

## Known Limits

- No live camp seat availability or registration search.
- No live backend endpoint connecting the static UI to the ADK agent yet.
- No production retrieval index over every raw source file yet.
- Full test suite requires Google Application Default Credentials because the Agent Engine integration test imports the Vertex wrapper.

## Review Checklist

- Confirm the one-pager accurately describes the demo.
- Confirm the service catalog matches the intended Fairfax routing categories.
- Confirm the logo/branding is acceptable for a prototype.
- Confirm no real API keys or credential files are present before GitHub push.
- Confirm whether to initialize Git and connect `https://github.com/AICertGit/FairfaxCountyNevigator.git`.
