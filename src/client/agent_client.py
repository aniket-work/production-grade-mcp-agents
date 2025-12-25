import asyncio
import sys
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    # We will connect to our own server script via stdio for this PoC
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["src/server/agent_server.py"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize connection
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print(f"Connected to server. Found {len(tools.tools)} tools.")
            
            # Call a tool
            print("\nExecuting search_web tool...")
            result = await session.call_tool("search_web", arguments={"query": "MCP adoption trends"})
            print(f"Result: {result.content[0].text}")

            # Read a resource
            print("\nReading resource config://app_settings...")
            resources = await session.read_resource("config://app_settings")
            print(f"Resource content: {resources.contents[0].text}")

if __name__ == "__main__":
    import os
    # Ensure we run from the project root for path resolution
    if os.path.basename(os.getcwd()) == "src":
        os.chdir("..")
        
    asyncio.run(run_client())
