"""Core DXF builder functions using ezdxf.
This module provides a convenience PlanBuilder class that helps create rooms,
text labels, and basic layers for a floorplan. It intentionally keeps the API
simple so you can extend it later (doors/windows, furniture, auto-trace).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
