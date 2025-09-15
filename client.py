import asyncio
from fastmcp import Client

client = Client("server.py")

print(f'Client: {client}')

async def main():
    async with client:
        print(f"Client connected: {client.is_connected()}")

        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        if any(tool.name == "multiply" for tool in tools):
            result = await client.call_tool("multiply", {"a": 4, "b": 7})
            print(f"multiply result: {result}")

    print(f"Client connected: {client.is_connected()}")

if __name__ == "__main__":
    asyncio.run(main())