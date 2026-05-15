# GitHub Repository Guide

## Ideal Folder Structure

```text
fairfax-county-resource-navigator/
  app.py
  requirements.txt
  README.md
  Dockerfile
  .gitignore
  data/
    service_catalog.csv
    service_catalog_schema.md
  src/
    embeddings.py
    matcher.py
    privacy.py
    response_builder.py
  docs/
    architecture.md
    source_inventory.md
    governance_notes.md
  github_submission/
    FINAL_HACKATHON_ONE_PAGER.md
    REPOSITORY_GUIDE.md
    architecture_diagram.py
    assets/
      fairfax_resource_navigator_architecture.png
      fairfax_resource_navigator_architecture.pdf
  tests/
    test_matcher.py
    test_privacy.py
    test_routes.py
```

## Suggested `requirements.txt`

```text
streamlit
pandas
numpy
sentence-transformers
scikit-learn
graphviz
```

## Suggested `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

## README Pitch Section

### Why Fairfax County Resource Navigator Wins

Fairfax County Resource Navigator is a public-sector AI prototype with immediate resident value: it lets people ask for help in plain language and find the right county service without knowing agency names, portal names, or program terminology. Instead of forcing residents through static PDFs and fragmented department pages, it uses semantic search to route intent to official service records.

The project is built for rapid deployment and responsible governance. It can run locally for hackathon review, containerize cleanly for Google Cloud Run, and scale later into managed Google Cloud services such as Cloud Storage, BigQuery, and Vertex AI Search. Most importantly, it is privacy-by-design: the Shadow Database is a service metadata layer, not a resident database, and the user flow avoids full names, exact addresses, account numbers, and other PII.

This project advances the One Fairfax equity vision by reducing service discovery friction for residents who may face digital access, language, transportation, disability, or time barriers. It shows a practical pattern for public-sector AI: use natural language to simplify access, keep humans in the loop for sensitive decisions, ground outputs in official sources, and avoid collecting data the system does not need.

## Cloud Run Deployment Path

1. Build the container.

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/fairfax-resource-navigator
```

2. Deploy to Cloud Run.

```bash
gcloud run deploy fairfax-resource-navigator \
  --image gcr.io/PROJECT_ID/fairfax-resource-navigator \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

3. Replace `PROJECT_ID` and region with the approved project settings.

## Privacy And Safety Notes

- Do not store raw resident prompts if they may include PII.
- Do not request names, exact addresses, account numbers, Social Security numbers, or documents.
- Use demographic proxies only where they improve routing: ZIP code, age range, household size, urgency, and program interests.
- Route emergencies to 911 or the appropriate crisis hotline.
- Use official county source citations for service recommendations.
