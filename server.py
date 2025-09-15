from fastmcp import FastMCP

mcp = FastMCP(name="calculator")

# @mcp.tool : 해당 함수를 MCP 도구로 등록
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

if __name__ == "__main__":
    mcp.run()