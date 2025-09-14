"""
Utility helpers: unit conversions, simple parsers, and small helpers.
"""
from typing import Tuple

def feet_to_inches(feet: float) -> float:
    """Convert feet (floating) to inches.

    Example: 16.125 (16'1.5") -> 16.125 * 12 = 193.5 inches
    """
    return feet * 12.0


def parse_feet_inches(text: str) -> float:
    """Parse a dimension string like `16'1.5\"` or `14'6"` or `10'` and return feet as float.

    Returns feet as float (e.g. "16'1.5\"" -> 16.125).
    Accepts variants: 16', 16'1", 16'1.5", 14'6" etc.
    """
    s = text.strip().replace('"', '').replace('”', '').replace('\u201d', '')
    # split on apostrophe
    if "'" in s:
        parts = s.split("'")
        try:
            feet = float(parts[0]) if parts[0] else 0.0
        except ValueError:
            raise ValueError(f"Can't parse feet component from: {text}")
        inches = 0.0
        if len(parts) > 1 and parts[1]:
            try:
                inches = float(parts[1])
            except ValueError:
                raise ValueError(f"Can't parse inches component from: {text}")
        return feet + inches/12.0
    else:
        # assume number is feet
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Can't parse dimension: {text}")


