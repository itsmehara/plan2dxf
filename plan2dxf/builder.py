"""Core DXF builder functions using ezdxf.
This module provides a convenience PlanBuilder class that helps create rooms,
text labels, and basic layers for a floorplan. It intentionally keeps the API
simple so you can extend it later (doors/windows, furniture, auto-trace).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf import colors
from .utils import feet_to_inches


class Room:
    def __init__(self, name: str, x: float, y: float, width: float, height: float):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class PlanBuilder:
    """Build a DXF plan programmatically.

    Coordinates and sizes are expected in **inches** for the DXF modelspace.
    Use the `feet_to_inches()` helper to convert from feet.
    """
    def __init__(self, dxf_version: str = "R2010"):
        self.doc = ezdxf.new(dxfversion=dxf_version)
        self.msp = self.doc.modelspace()

        # Define default layers
        self._init_layers()

    # -----------------------------
    # Layer Management
    # -----------------------------
    def _init_layers(self):
        self._add_layer("WALLS", color=7)
        self._add_layer("TEXT", color=2)
        self._add_layer("DOORS", color=3)
        self._add_layer("WINDOWS", color=4)
        self._add_layer("FURNITURE", color=5)
        self._add_layer("DIMENSIONS", color=6)

    def _add_layer(self, name: str, color: int = 7):
        if name not in self.doc.layers:
            self.doc.layers.add(name, dxfattribs={"color": color})

    # -----------------------------
    # Core Primitives
    # -----------------------------
    def add_room(self, room: Room, wall_thickness: float = 4.0):
        """Add a room as a rectangle (outer wall polyline). wall_thickness in inches.

        The rectangle will be drawn as a closed LWPolyline on layer 'WALLS'.
        We do not currently generate inner offset for wall thickness — this is
        intentionally simple. If you want double-lined walls, call `add_wall_frame()`.
        """
        x, y, w, h = room.x, room.y, room.width, room.height
        coords = [(x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)]
        self.msp.add_lwpolyline(coords, dxfattribs={"layer": "WALLS", "closed": True})
        self.add_text(room.name, insert=(x + 6, y + 6))

    def add_text(self, text: str, insert: Tuple[float, float], height: float = 12.0):
        """Add a multiline text label on the TEXT layer.

        Use insert in inches.
        """
        # ezdxf recommends MText for multiline; fallback to simple Text entities
        msp = self.doc.modelspace()
        mtext = msp.add_mtext(text, dxfattribs={
            "style": "OpenSans",
            "char_height": 20,
            "width": 200  # set width here
        })
        mtext.set_location(insert, rotation=0)

    def add_wall_frame(self, x: float, y: float, w: float, h: float, thickness: float = 4.0):
        """Draw double-lined wall frame: outer and inner polyline offset by thickness.

        thickness in inches. This function is a simple helper and does not handle
        corner joins elegantly for complex shapes.
        """
        outer = [(x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)]
        inner = [(x+thickness, y+thickness), (x+w-thickness, y+thickness), (x+w-thickness, y+h-thickness), (x+thickness, y+h-thickness), (x+thickness, y+thickness)]
        self.msp.add_lwpolyline(outer, dxfattribs={"layer": "WALLS", "closed": True})
        self.msp.add_lwpolyline(inner, dxfattribs={"layer": "WALLS", "closed": True})

    # -----------------------------
    # Save
    # -----------------------------
    def save(self, filepath: str):
        self.doc.saveas(filepath)
