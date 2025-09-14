"""Small runnable example that creates a DXF file using PlanBuilder.

Run:
    python examples/home_plan.py

This will create `examples/home_plan.dxf` which you can open in AutoCAD.
"""

from plan2dxf import PlanBuilder
from plan2dxf.utils import parse_feet_inches, feet_to_inches
from plan2dxf.builder import Room
import os


# -----------------------------
# Helpers
# -----------------------------
def f2i(s: str) -> float:
    """Convert a feet-inch string like 16'1.5" to inches (float)."""
    return feet_to_inches(parse_feet_inches(s))


def get_output_dir() -> str:
    """Return the output directory path."""
    out_dir = os.path.join(os.path.dirname(__file__), "..", "output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


# -----------------------------
# Floor Plan Definition
# -----------------------------
def build_home_plan() -> PlanBuilder:
    """Builds and returns the sample home plan as a PlanBuilder object."""
    pb = PlanBuilder()

    # Outer boundary: 32' x 38'3"
    outer_w = f2i("32'")
    outer_h = f2i("38'3\"")
    pb.add_wall_frame(0, 0, outer_w, outer_h, thickness=6.0)

    # Rooms
    pb.add_room(Room(
        name="LIVING\n16'1.5\" x 10'0\"",
        x=12, y=12,
        width=f2i("16'1.5\""),
        height=f2i("10'")
    ))

    pb.add_room(Room(
        name="DINING\n14'6\" x 10'0\"",
        x=f2i("16'1.5\"") + 24,
        y=12,
        width=f2i("14'6\""),
        height=f2i("10'")
    ))

    pb.add_room(Room(
        name="KITCHEN\n10'10.5\" x 10'0\"",
        x=12,
        y=f2i("10'") + 36,
        width=f2i("10'10.5\""),
        height=f2i("10'")
    ))

    return pb


# -----------------------------
# Main entry point
# -----------------------------
def main():
    pb = build_home_plan()
    out_file = os.path.join(get_output_dir(), "home_plan.dxf")
    pb.save(out_file)
    print(f"Floor plan saved: {out_file}")


if __name__ == "__main__":
    main()
