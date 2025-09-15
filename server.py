from smithery.decorators import smithery
from fastmcp import Context, FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP(name="calculator")

class ConfigSchema(BaseModel):
    unit: str = Field("celsius", description="Temperature unit (celsius or fahrenheit)")

@smithery.server(config_schema=ConfigSchema)
def create_server(config: ConfigSchema):
    """Create and return a FastMCP server instance with session config."""
    
    server = FastMCP(name="Weather Server")

    @server.tool()
    def get_weather(city: str, ctx: Context) -> str: 
        """Get weather for a city."""
        # Access session-specific config through context
        session_config = ctx.session_config 
        
        # Use the configured temperature unit
        unit = session_config.unit
        formatted_temp = f"22°C" if unit == "celsius" else "72°F"

        return f"Weather in {city}: {formatted_temp}"

    return server

# @mcp.tool : 해당 함수를 MCP 도구로 등록
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"

if __name__ == "__main__":
    mcp.run()
    

  