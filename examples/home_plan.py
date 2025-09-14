"""Small runnable example that creates a DXF file using PlanBuilder.

Run:
    python examples/home_plan.py

This will create `examples/home_plan.dxf` which you can open in AutoCAD.
"""

from plan2dxf import PlanBuilder
from plan2dxf.utils import parse_feet_inches, feet_to_inches
from plan2dxf.builder import Room
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUT_DIR, exist_ok=True)

# Convert feet-inch strings quickly
def f(s: str) -> float:
    return feet_to_inches(parse_feet_inches(s))

# Create the builder
pb = PlanBuilder()

# Outer boundary 32' x 38'3"
outer_w = f("32'")
outer_h = f("38'3\"")
pb.add_wall_frame(0, 0, outer_w, outer_h, thickness=6.0)

# Living room: 16'1.5" x 10'0" placed near bottom-left (example positions)
living_w = f("16'1.5\"")
living_h = f("10'")
living_room = Room(name="LIVING\n16'1.5\" x 10'0\"", x=12, y=12, width=living_w, height=living_h)
pb.add_room(living_room)

# Dining
pb.add_room(Room(name="DINING\n14'6\" x 10'0\"", x=living_w+24, y=12, width=f("14'6\""), height=f("10'")))

# Kitchen
pb.add_room(Room(name="KITCHEN\n10'10.5\" x 10'0\"", x=12, y=living_h+36, width=f("10'10.5\""), height=f("10'")))

out = os.path.join(OUT_DIR, "home_plan.dxf")
pb.save(out)
print("Saved:", out)
