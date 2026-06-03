import json
import os
import sys
from pathlib import Path
from typing import Literal

import pandas as pd
from mcp.server.fastmcp import FastMCP

print("MCP server starting.", file=sys.stderr)
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data" / "iowa_parquet"
STORAGE_DIR = PROJECT_DIR / "data" / "storage" / "azure-well-architected-ai-local"
MODELS_DIR = PROJECT_DIR / "models"
LM_STUDIO_MODEL = os.environ.get("LM_STUDIO_MODEL", "openai/gpt-oss-20b")
EMBEDDING_MODEL_DIR = (
    MODELS_DIR
    / "models--BAAI--bge-small-en-v1.5"
    / "snapshots"
    / "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
)

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

DatasetName = Literal[
    "iowa_item",
    "iowa_store",
    "iowa_date",
    "iowa_category",
    "iowa_vendor",
]

ALLOWED_DATASETS: set[str] = set(DatasetName.__args__)

mcp = FastMCP("iowa-ai-architecture")


@mcp.tool()
def retrieve_iowa_data(file_name: DatasetName, limit: int = 100) -> list[dict]:
    """
    Retrieve rows from one of the allowed Iowa parquet datasets.

    Args:
        file_name: Dataset name without extension. Allowed values are:
            iowa_item, iowa_store, iowa_date, iowa_category, iowa_vendor.
        limit: Maximum number of rows to return.

    Returns:
        Dataset rows as JSON-serializable records.
    """
    if file_name not in ALLOWED_DATASETS:
        allowed = ", ".join(sorted(ALLOWED_DATASETS))
        raise ValueError(f"Unknown dataset: {file_name}. Allowed datasets: {allowed}")

    safe_limit = max(1, min(limit, 1000))
    dataset_path = DATA_DIR / f"{file_name}.snappy.parquet"

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset file does not exist: {dataset_path}")

    df = pd.read_parquet(dataset_path).head(safe_limit)
    return json.loads(df.to_json(orient="records", date_format="iso"))


def ask_pdf_with_sources(question: str, top_k: int = 5) -> dict:
    from llama_index.core import Settings, StorageContext, load_index_from_storage
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.llms.openai_like import OpenAILike

    if not STORAGE_DIR.exists():
        raise FileNotFoundError(f"Index storage directory does not exist: {STORAGE_DIR}")
    if not EMBEDDING_MODEL_DIR.exists():
        raise FileNotFoundError(f"Embedding model directory does not exist: {EMBEDDING_MODEL_DIR}")

    Settings.embed_model = HuggingFaceEmbedding(
        model_name=str(EMBEDDING_MODEL_DIR),
        cache_folder=str(MODELS_DIR),
        device="cpu",
    )

    Settings.llm = OpenAILike(
        model=LM_STUDIO_MODEL,
        api_base="http://localhost:1234/v1",
        api_key="lm-studio",
        is_chat_model=True,
        temperature=0,
    )

    storage_context = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(similarity_top_k=top_k)
    response = query_engine.query(question)

    sources = []
    for node in response.source_nodes:
        sources.append(
            {
                "score": node.score,
                "page": node.node.metadata.get("page"),
                "file_name": node.node.metadata.get("file_name"),
                "text": node.node.get_content()[:800],
            }
        )

    return {
        "answer": str(response),
        "sources": sources,
    }


@mcp.tool()
def ai_well_architected_framework(q: str) -> dict:
    """
    Answer questions about the Azure Well-Architected Framework for AI workloads.

    This tool queries a local RAG index built from the Azure Well-Architected AI PDF.
    Use it for questions about AI workload architecture, design principles,
    application design, data design, grounding data, operations, reliability,
    security, cost optimization, performance efficiency, and operational excellence.

    Args:
        q: Question to answer using the indexed Azure Well-Architected AI PDF.

    Returns:
        A dictionary with the answer and supporting source snippets, including
        page numbers and similarity scores.
    """
    return ask_pdf_with_sources(q)


if __name__ == "__main__":
    mcp.run()
