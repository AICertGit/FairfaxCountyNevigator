"""Generate the Fairfax Resource Navigator architecture diagram.

Usage:
    python github_submission/architecture_diagram.py

Outputs:
    github_submission/assets/fairfax_resource_navigator_architecture.png
    github_submission/assets/fairfax_resource_navigator_architecture.pdf

Requires:
    pip install graphviz

You may also need the Graphviz system package installed:
    https://graphviz.org/download/
"""

from __future__ import annotations

from pathlib import Path

from graphviz import Digraph


ROOT = Path(__file__).resolve().parent
ASSET_DIR = ROOT / "assets"
OUTPUT_BASE = ASSET_DIR / "fairfax_resource_navigator_architecture"


def add_node(
    graph: Digraph,
    node_id: str,
    label: str,
    fill: str,
    border: str = "#123446",
    font: str = "#071f2c",
) -> None:
    graph.node(
        node_id,
        label=label,
        shape="rect",
        style="rounded,filled",
        fillcolor=fill,
        color=border,
        penwidth="2",
        fontcolor=font,
        fontsize="16",
        fontname="Arial",
        margin="0.18,0.12",
    )


def build_diagram() -> Digraph:
    graph = Digraph(
        "fairfax_resource_navigator",
        comment="Fairfax County Resource Navigator architecture",
        graph_attr={
            "rankdir": "LR",
            "bgcolor": "#f4f7f8",
            "pad": "0.45",
            "nodesep": "0.65",
            "ranksep": "0.9",
            "splines": "ortho",
            "fontname": "Arial",
            "label": (
                "<<B>Fairfax County Resource Navigator</B><BR/>"
                "<FONT POINT-SIZE='16'>Zero-PII semantic routing from resident intent "
                "to official county services</FONT>>"
            ),
            "labelloc": "t",
            "fontsize": "28",
            "fontcolor": "#071f2c",
        },
        node_attr={
            "fontname": "Arial",
            "fontsize": "15",
            "height": "0.8",
        },
        edge_attr={
            "fontname": "Arial",
            "fontsize": "12",
            "color": "#385568",
            "fontcolor": "#385568",
            "arrowsize": "0.8",
            "penwidth": "2",
        },
    )

    with graph.subgraph(name="cluster_request") as request:
        request.attr(
            label="Resident Request Flow",
            color="#d9e1e8",
            penwidth="2",
            style="rounded,filled",
            fillcolor="#ffffff",
            fontname="Arial",
            fontsize="18",
            fontcolor="#071f2c",
        )
        add_node(
            request,
            "resident",
            "Resident / Staff User\\nplain-language service need",
            "#f7fbff",
            "#071f2c",
        )
        add_node(
            request,
            "streamlit",
            "Streamlit UI\\nquestion + safe context",
            "#eaf3f7",
        )
        add_node(
            request,
            "privacy",
            "Zero-PII Guardrail\\nZIP, age, household size only",
            "#fff7e8",
            "#b67822",
        )
        add_node(
            request,
            "embedding",
            "Local NLP Embedding\\nHugging Face SentenceTransformers",
            "#fff7e8",
            "#b67822",
        )

    with graph.subgraph(name="cluster_data") as data:
        data.attr(
            label="Shadow Database And Matching Layer",
            color="#d9e1e8",
            penwidth="2",
            style="rounded,filled",
            fillcolor="#ffffff",
            fontname="Arial",
            fontsize="18",
            fontcolor="#071f2c",
        )
        add_node(
            data,
            "shadow_db",
            "Pandas Shadow Database\\nservice catalog + eligibility hints",
            "#f4f7f8",
            "#5d6874",
        )
        add_node(
            data,
            "semantic_match",
            "Semantic + Structured Match\\nintent, age, ZIP, urgency, category",
            "#fff7e8",
            "#b67822",
        )
        add_node(
            data,
            "citations",
            "Official Fairfax Sources\\nURLs, snippets, department owners",
            "#f4f7f8",
            "#5d6874",
        )

    with graph.subgraph(name="cluster_response") as response:
        response.attr(
            label="Response And Deployment",
            color="#d9e1e8",
            penwidth="2",
            style="rounded,filled",
            fillcolor="#ffffff",
            fontname="Arial",
            fontsize="18",
            fontcolor="#071f2c",
        )
        add_node(
            response,
            "answer",
            "Resident-Friendly Route\\nprogram, why it matched, next steps",
            "#eef7ed",
            "#4d7b4a",
        )
        add_node(
            response,
            "cloud_run",
            "Container-Ready Deployment\\nGoogle Cloud Run",
            "#f2eef8",
            "#6f5f94",
        )
        add_node(
            response,
            "future",
            "Future Managed Services\\nCloud Storage, BigQuery, Vertex AI Search",
            "#f2eef8",
            "#6f5f94",
        )

    graph.edge("resident", "streamlit", label="asks in natural language")
    graph.edge("streamlit", "privacy", label="strip/avoid PII")
    graph.edge("privacy", "embedding", label="normalize query")
    graph.edge("embedding", "semantic_match", label="query vector")
    graph.edge("shadow_db", "semantic_match", label="service records")
    graph.edge("citations", "semantic_match", label="grounding")
    graph.edge("semantic_match", "answer", label="ranked match")
    graph.edge("answer", "streamlit", label="display guidance")
    graph.edge("streamlit", "cloud_run", label="same app container", style="dashed")
    graph.edge("shadow_db", "future", label="scale data layer", style="dashed")
    graph.edge("cloud_run", "future", label="production hardening", style="dashed")

    return graph


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    graph = build_diagram()
    graph.render(str(OUTPUT_BASE), format="png", cleanup=True)
    graph.render(str(OUTPUT_BASE), format="pdf", cleanup=True)
    print(f"Wrote {OUTPUT_BASE.with_suffix('.png')}")
    print(f"Wrote {OUTPUT_BASE.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
