# Fairfax Resource Navigator Demo Checklist

## Before Recording or Presenting

- Confirm the resident web UI is reachable at `http://localhost:5173`.
- Confirm the ADK playground is reachable at `http://localhost:8501`.
- In the ADK Dev UI, select the `app` agent.
- Keep `FINAL_SUBMISSION_ONE_PAGER.md` open for the project narrative.
- Keep `docs/source_inventory.md` and `docs/taxonomy_v1_recommendation.md` ready if judges ask about source governance.

## Required Demo Prompts

```text
I need help with my Fairfax car tax bill.
```

Expected route: Taxes and fees: vehicle taxes.

```text
My neighbor is doing unpermitted construction. What should I do?
```

Expected route: Code compliance / neighborhood complaint.

```text
I need urgent housing or safety help tonight.
```

Expected route: Basic needs / housing or safety help.

```text
Are there still good summer camps in Fairfax County for my 9-year-old who likes sports and AI or STEM?
```

Expected route: Parks and recreation / youth camps.

## Talking Points

- This is a Fairfax research prototype, not an official county chatbot.
- The demo is mock-first so routing, citations, and escalation can be verified before adding more automation.
- Official Fairfax County and Fairfax-hosted sources are the only prototype citation sources.
- Sensitive topics are handled conservatively and routed to human or emergency channels.
- Parks and Recreation / youth camps is now a first-pass route in the UI and agent logic.

## GitHub Prep

Before pushing, avoid committing local runtime artifacts:

- `.venv/`
- `.adk/`
- `.pytest_cache/`
- `playground-cmd.log`
- `playground.err.log`
- `playground.out.log`
