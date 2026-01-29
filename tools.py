from langchain_core.tools import tool

@tool
def get_weather_for_location(location: str) -> str:
    """Get the weather for a given city."""
    return f"It's always sunny in {location}"

@tool
def get_current_location() -> str:
    """Get the user's current location."""
    return "Delhi"