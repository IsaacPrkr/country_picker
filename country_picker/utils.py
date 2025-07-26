# country_picker/utils.py

from typing import Any

def parse_country_names(data: Any) -> list[str]:
    """
    Extract a list of country names from the API JSON response.
    """
    try:
        return [entry['name'] for entry in data if 'name' in entry]
    except Exception:
        return []
