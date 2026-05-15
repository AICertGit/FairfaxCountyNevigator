# Demo Wrap-Up Notes

Date: 2026-05-15

## Deployment

- Deployment to Vertex Agent Engine is optional for the demo and may take too long for the hackathon wrap-up.
- The recommended demo path is the local resident UI at `http://localhost:5173` plus the ADK playground at `http://localhost:8501`.
- `deployment_metadata.json` currently shows no deployed remote Agent Engine.

## API Usage

- The current resident UI and ADK agent response path are mock-first and deterministic.
- The demo does not call OpenAI, Gemini, Gemma, or a live model API during normal chat.
- Vertex imports and deployment utilities exist for later Agent Engine deployment, not for the local demo response path.

## Secrets and GitHub

- Do not commit real OpenAI keys, Google API keys, service account JSON, OAuth tokens, `.env` files, saved chats, or local logs.
- `.gitignore` excludes `.env`, `.adk/`, `.saved_chats`, playground logs, and frontend server logs.
- Before pushing, run a secret scan or at minimum search for `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `AIza`, `sk-`, `Bearer`, and `private_key`.

## One-Pager Framing

- Position the app as a human-in-the-loop Fairfax County service-routing prototype.
- Emphasize official-source citations, conservative escalation handling, and no eligibility/legal/tax promises.
- Be explicit that the demo is local and mock-first so reviewers understand why it is fast, stable, and safe.
