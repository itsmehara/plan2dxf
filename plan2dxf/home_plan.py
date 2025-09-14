"""Small runnable example that creates a DXF file using PlanBuilder.

Run:
python examples/home_plan.py

This will create `examples/home_plan.dxf` which you can open in AutoCAD.
"""


from plan2dxf import PlanBuilder
from plan2dxf.utils import parse_feet_inches, feet_to_inches
from plan2dxf.builder import Room
import os
