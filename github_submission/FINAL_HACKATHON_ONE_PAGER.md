# Fairfax County Resource Navigator

## Purpose And Vision

Fairfax County residents often know what they need but not what the county calls it, which department owns it, or where the correct service page lives. Critical help can be scattered across PDFs, department pages, portals, and program-specific websites. That fragmented discovery creates civic service deserts: residents with the least time, language access, transportation, or digital familiarity can spend the longest searching for housing assistance, youth programs, behavioral health support, tax help, or transportation services.

Fairfax County Resource Navigator reframes service discovery around resident intent instead of county bureaucracy. A resident can ask in natural language, share only safe demographic context such as age range, ZIP code, household size, or program interests, and receive a source-grounded route to the right county service. This supports the spirit of One Fairfax by reducing navigation friction, improving equitable access to public services, and making the first step toward help faster, clearer, and safer without collecting personally identifiable information.

## Architecture Breakdown

The prototype is designed as a lightweight, privacy-preserving semantic search application. The Streamlit UI collects a resident question and optional non-PII context such as ZIP code, age, household size, service interest, urgency, and budget sensitivity. It does not ask for names, exact addresses, account numbers, Social Security numbers, or other sensitive identifiers. That context is passed into the local application layer where the resident query is normalized and embedded with a Hugging Face SentenceTransformers model.

The embedding is compared against a Pandas-based Shadow Database: a curated local service catalog containing Fairfax County service records, eligibility hints, safe demographic tags, departments, routing categories, source URLs, and citation snippets. The Shadow Database is not a resident database; it is a public-service metadata layer that helps match intent and demographic proxies to the right program. Matching combines semantic similarity, rule-based emergency overrides, and structured filters such as age range, ZIP code relevance, and service category. The response layer returns a concise recommendation, why the route matched, 1-2 next steps, and official Fairfax source citations.

This architecture is container-ready for Google Cloud Run because the runtime can be packaged as a stateless Python web service. Streamlit serves the UI, SentenceTransformers and the Shadow Database load at startup, and each request is handled without storing resident PII. The application can run with local files for the hackathon demo and later move the Shadow Database to Cloud Storage, BigQuery, AlloyDB, or Vertex AI Search if Fairfax County wants stronger governance, observability, and managed retrieval.

## Why This Wins

- **Immediate citizen impact:** Residents can describe needs in plain language and reach the right service faster.
- **Privacy by design:** The system uses safe demographic proxies and explicitly avoids PII collection.
- **Rapid deployment:** The prototype can run locally for demos and containerize cleanly for Cloud Run.
- **Equity alignment:** It lowers discovery friction for residents navigating complex service ecosystems.
- **Grounded public-sector pattern:** Recommendations are tied to official service records and citations, not unsupported model guesses.

## Demo Narrative

1. A resident asks: "Are there affordable summer camps near me for my 9-year-old who likes sports and STEM?"
2. The app embeds the query locally and compares it to the Shadow Database.
3. The matcher boosts youth camp records matching age, interests, affordability, and location.
4. The response recommends a specific Fairfax program, explains why, and points to the right next step.
5. No name, exact address, or sensitive personal identifier is collected or stored.

## Recommended Next Steps

1. Expand the Shadow Database to all high-volume Fairfax County service domains.
2. Add multilingual query support for major county language-access needs.
3. Add human review workflows for low-confidence or sensitive matches.
4. Containerize for Google Cloud Run with environment-based configuration.
5. Add monitoring, evaluation sets, and service-owner review before public release.
