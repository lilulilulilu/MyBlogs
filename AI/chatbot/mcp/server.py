# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", port=8002, host="0.0.0.0")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool(description="Subtract two numbers")
def sub(a: int, b: int) -> int:
    return a - b

@mcp.tool(description="Multiply two numbers")
def mul(a: int, b: int) -> int:
    return a * b


@mcp.tool(description="Get the weather of a city")
def get_weather(city: str) -> str:
    """Get the weather of a city"""
    return f"The weather of {city} is sunny"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}", description="Get a personalized greeting")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("file://documents/{name}", description="Read a document by name")
def read_document(name: str) -> str:
    """Read a document by name."""
    # This would normally read from disk
    return f"Content of {name}"


@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
   

