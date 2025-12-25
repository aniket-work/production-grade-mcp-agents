# Production-Grade MCP Agents PoC

This repository demonstrates a Proof of Concept (PoC) for building production-ready AI agents using the **Model Context Protocol (MCP)**.

## Project Structure

```
├── src/
│   ├── server/
│   │   └── agent_server.py    # FastMCP server implementation
│   └── client/
│       └── agent_client.py    # Client demonstrating tool usage
├── requirements.txt           # Dependencies
└── README.md
```

## Setup & Running

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Client (which auto-starts the server)**
   ```bash
   python src/client/agent_client.py
   ```

## Key Concepts Demonstrated

- **FastMCP Server**: Using `mcp.server.fastmcp` for rapid development.
- **Typed Tool Definitions**: Using Python type hints for automatic schema generation.
- **Resource Exposure**: Serving static configuration via MCP resources.
- **Stdio Transport**: Robust local communication channel.
