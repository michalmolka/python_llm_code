# MCP Server

A simple MCP server exposing two tools from `mcp.ipynb`:

- `retrieve_iowa_data` – reads local Parquet files from the `data/iowa_parquet` directory.
- `ai_well_architected_framework` – queries a local LlamaIndex index stored in the `storage/ai_well_architected_framework` directory.

## Running the Server

First, prepare the LlamaIndex storage:

```bash
prepare_index_llama.ipynb
```

Then start the MCP server:

```bash
cd /path/to/python_llm_code
.venv/bin/python mcp_server/server.py
```

The server communicates over stdio and is ready to be used as a local MCP server.

## Example Client Configuration

```json
{
  "mcpServers": {
    "iowa-ai-architecture": {
      "command": "/path/to/python_llm_code/.venv/bin/python",
      "args": [
        "/path/to/python_llm_code/mcp_server/server.py"
      ]
    }
  }
}
```

## OpenAI-Compatible Endpoint Requirement

The `ai_well_architected_framework` tool requires a locally running OpenAI-compatible endpoint:

```text
http://localhost:1234/v1
model: openai/gpt-oss-20b
```

You can override the model name passed to LM Studio:

```json
"env": {
  "LM_STUDIO_MODEL": "openai/gpt-oss-20b"
}
```
