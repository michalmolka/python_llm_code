# Python LLM & AI Engineering Code Snippets

A practical collection of Jupyter notebooks, scripts, and hands-on examples covering core AI Engineering and LLM topics in Python:
- **LLM API Calls, Structured Outputs, Tool Calling & LangGraph**
- **Retrieval-Augmented Generation (RAG)** — Fixed-size vs. Markdown Section-based chunking, FAISS vector search, Cross-Encoder reranking, and neighbor chunk expansion
- **Model Context Protocol (MCP) Server** — Custom `FastMCP` server exposing Parquet dataset tools and a local LlamaIndex RAG tool
- **LoRA Fine-Tuning on Apple Silicon (`mlx-lm`)** — Fine-tuning `Qwen3-8B-MLX-bf16` on custom domain data
- **Elasticsearch & Neo4j** — Full-text search, aggregations, and graph database queries with Python

---

## Repository Structure

```text
python_llm_code/
├── llm_calls_code_snippets.ipynb   # LLM calls, Structured Outputs, LangGraph, Tool Calling, Hugging Face Inference
├── log_probs.json                  # Example OpenAI-compatible Responses API call & logprobs output
├── rag_fixed_and_section/          # RAG chunking & retrieval comparison
│   ├── rag.ipynb                   # Fixed-size vs. Section-based chunking + FAISS + Reranker + Neighbor expansion
│   └── iowa_sales_rag_documentation_en.md
├── mcp_server/                     # Model Context Protocol (MCP) server & client runbook
│   ├── server.py                   # FastMCP server exposing data & RAG tools over stdio
│   ├── mcp_runbook.ipynb           # Preparing the LlamaIndex store and invoking MCP tools via LLM
│   ├── README.md                   # MCP server setup & client configuration instructions
│   └── data/                       # Iowa Parquet files, Azure Well-Architected AI PDF & persisted index
├── fine-tuning/                    # Local LoRA fine-tuning on Apple Silicon using MLX
│   ├── fine_tuning.ipynb           # Data split, LoRA training with mlx_lm, base vs. fine-tuned evaluation
│   └── data/                       # JSONL datasets (train, valid, test) for Iowa Sales domain
├── elasticsearch.ipynb             # Bulk loading Parquet data with Polars/PyArrow & running Elasticsearch queries
├── elasticsearch-docker.yaml       # Docker Compose setup for Elasticsearch 9.4.2 & Kibana
└── neo4j.ipynb                     # Neo4j Docker setup, Cypher queries, constraints/indexes & Python driver usage
```

---

## Modules Overview

### 1. LLM Calls, Structured Outputs, LangGraph & Tool Calling
- **File:** [`llm_calls_code_snippets.ipynb`](./llm_calls_code_snippets.ipynb), [`log_probs.json`](./log_probs.json)
- Demonstrates:
  - Basic chat invocations with `langchain_openai` (`ChatOpenAI`) and local OpenAI-compatible servers (e.g., LM Studio).
  - Enforcing **Structured Outputs** using Pydantic (`BaseModel`) and `response_format={"type": "json_schema", ...}`.
  - Building stateful workflows with **LangGraph** (`StateGraph`).
  - Multi-step **Function / Tool Calling** loops with the OpenAI Python SDK.
  - Querying remote open-weights models via **Hugging Face `InferenceClient`**.
  - Inspecting token log probabilities (`top_logprobs`) in [`log_probs.json`](./log_probs.json).

### 2. RAG: Fixed-Size vs. Section-Based Chunking
- **Directory:** [`rag_fixed_and_section/`](./rag_fixed_and_section/)
- Compares two chunking and retrieval pipelines over the Iowa Sales star-schema documentation ([`iowa_sales_rag_documentation_en.md`](./rag_fixed_and_section/iowa_sales_rag_documentation_en.md)):
  1. **Fixed-Size Chunking** (`RecursiveCharacterTextSplitter`)
  2. **Markdown Section-Aware Chunking** (`MarkdownHeaderTextSplitter` + fallback `RecursiveCharacterTextSplitter`)
- Both pipelines include:
  - Local embeddings (`sentence-transformers/all-MiniLM-L6-v2`) with in-memory **FAISS** vector search.
  - **Cross-Encoder Reranking** (`cross-encoder/ms-marco-MiniLM-L-6-v2`).
  - **Neighbor Window Expansion** (fetching adjacent chunks within the same document/section for richer context).

### 3. Model Context Protocol (MCP) Server
- **Directory:** [`mcp_server/`](./mcp_server/)
- A complete local MCP server built with `FastMCP` ([`mcp_server/server.py`](./mcp_server/server.py)) exposing two tools:
  - `retrieve_iowa_data`: Reads allowed Iowa Liquor Sales Parquet datasets (`iowa_item`, `iowa_store`, `iowa_date`, `iowa_category`, `iowa_vendor`).
  - `ai_well_architected_framework`: Queries a local **LlamaIndex** RAG store built from the Azure Well-Architected Framework for AI Workloads PDF.
- See [`mcp_server/README.md`](./mcp_server/README.md) and [`mcp_server/mcp_runbook.ipynb`](./mcp_server/mcp_runbook.ipynb) for index preparation and client execution examples.

### 4. LoRA Fine-Tuning with MLX (`mlx-lm`)
- **Directory:** [`fine-tuning/`](./fine-tuning/)
- Demonstrates local LoRA fine-tuning of `Qwen3-8B-MLX-bf16` on Apple Silicon using `mlx_lm`:
  - Preparing `train.jsonl`, `valid.jsonl`, and `test.jsonl` splits from domain-specific Q&A data (`iowa_sales_finetuning_2500_rich_unique.jsonl`).
  - Training LoRA adapters (`mlx_lm lora --train ...`).
  - Side-by-side comparison of responses from the base model vs. the fine-tuned model.

### 5. Elasticsearch & Neo4j
- **Elasticsearch** ([`elasticsearch.ipynb`](./elasticsearch.ipynb), [`elasticsearch-docker.yaml`](./elasticsearch-docker.yaml)):
  - Spinning up a local single-node Elasticsearch & Kibana stack via Docker Compose.
  - Streaming bulk ingestion of Parquet data using `pyarrow`, `polars`, and `elasticsearch.helpers.streaming_bulk`.
  - Running `match`, fuzzy `multi_match` with highlighting, and bucket/metric aggregations.
- **Neo4j** ([`neo4j.ipynb`](./neo4j.ipynb)):
  - Running Neo4j in Docker, creating nodes/relationships (`Continent -> Country -> City`), adding uniqueness constraints and indexes in Cypher, and querying the graph from Python with the `neo4j` driver.

---

## Prerequisites

Most examples use a locally running OpenAI-compatible inference server (such as **LM Studio** on `http://localhost:1234/v1`) or Docker for database services (Elasticsearch, Neo4j).

Common Python dependencies used across the notebooks:
```bash
pip install openai langchain-openai langchain-community langchain-huggingface langchain-text-splitters \
            langgraph faiss-cpu sentence-transformers llama-index llama-index-embeddings-huggingface \
            llama-index-llms-openai-like mcp pandas polars pyarrow pypdf huggingface_hub elasticsearch neo4j mlx-lm
```
