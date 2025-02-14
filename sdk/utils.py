# sdk/utils.py

import json

def validate_data(data: dict, required_keys: list) -> bool:
    """Validate that all required keys are present in the data."""
    return all(key in data for key in required_keys)

def format_text(text: str, max_length: int = 100) -> str:
    """Truncate text to a maximum length."""
    return text[:max_length] + "..." if len(text) > max_length else text

def parse_json(json_string: str) -> dict:
    """Parse a JSON string into a dictionary."""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return {}