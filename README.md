
# plan2dxf

```markdown
A Python utility to convert **floor plan sketches, images, or dimensions** into clean **AutoCAD DXF files**.  
This helps architects, engineers, and DIY home designers quickly digitize layouts for use in AutoCAD or any CAD software that supports DXF.
```

---

## ✨ Features
- Generate **DXF files** programmatically from Python.
- Supports **room-level definitions** (walls, labels, dimensions).
- Clean separation of **layers** (Walls, Text, Furniture).
- Works with **feet & inches** (scaled in DXF).
- Extendable for windows, doors, furniture outlines.


## Current code = A structured DXF generator (from given dimensions).
It lets you digitize a plan if you already know the room dimensions.


## Objective 
A full-fledged utility that can take sketches or images and auto-convert them.

---

## 📂 Project Structure

```

plan2dxf/
├── examples/        # Sample scripts & generated DXF files
├── plan2dxf/        # Core source code
│    ├── **init**.py
│    ├── builder.py  # Functions to create rooms, walls, text
│    ├── utils.py    # Helpers (unit conversions, scaling)
├── README.md        # Project documentation
├── requirements.txt # Dependencies
└── setup.py         # Package setup (optional, if publishing)

```

---

## 🚀 Getting Started

### 1️⃣ Install dependencies
```bash
pip install ezdxf
````

### 2️⃣ Run the example script

```bash
python examples/home_plan.py
```

### 3️⃣ Output

A file named **`home_plan.dxf`** will be created in the project folder.
Open it with **AutoCAD, FreeCAD, DraftSight**, or any CAD software.

---

## 🛠 Example Code

```python
from plan2dxf.builder import PlanBuilder, Room
from plan2dxf.utils import parse_feet_inches, feet_to_inches


# Convert feet-inch strings quickly
def f2i(s: str) -> float:
    return feet_to_inches(parse_feet_inches(s))


# Build a small demo plan
pb = PlanBuilder()

# Outer boundary 32' x 38'3"
pb.add_wall_frame(0, 0, f2i("32'"), f2i("38'3\""), thickness=6.0)

# Add rooms
pb.add_room(Room(name="LIVING\n16'1.5\" x 10'0\"", x=12, y=12, 
                 width=f2i("16'1.5\""), height=f2i("10'")))

pb.add_room(Room(name="DINING\n14'6\" x 10'0\"", x=f2i("16'1.5\"") + 24, y=12, 
                 width=f2i("14'6\""), height=f2i("10'")))

pb.add_room(Room( name="KITCHEN\n10'10.5\" x 10'0\"", x=12, y=f2i("10'") + 36, 
                  width=f2i("10'10.5\""), height=f2i("10'")))

# Save output
pb.save("home_plan.dxf")
print(" DXF file generated: home_plan.dxf")
```

---

### 📦 Build & Install from Source

To build the package (wheel + source distribution), run:

```bash
pip install --upgrade build setuptools wheel
python setup.py sdist bdist_wheel
```

This will generate files under `dist/`, for example:

```
dist/
 ├── plan2dxf-0.1.0-py3-none-any.whl
 └── plan2dxf-0.1.0.tar.gz
```

To install locally from the wheel:

```bash
pip install dist/plan2dxf-0.1.0-py3-none-any.whl
```

Or in development/editable mode (recommended while coding):

```bash
pip install -e .
```

---

### ✅ Current Capabilities (what your code can already do)

1. **DXF Creation:** Uses `ezdxf` to generate valid AutoCAD DXF files.
2. **Outer Frame Drawing:** Can draw a house boundary rectangle (wall frame with thickness).
3. **Room Rectangles:** You can define rooms (name, x, y, width, height), and it creates rectangles for them.
4. **Room Labels:** Adds text (name + dimensions) inside each room, properly placed in the DXF.
5. **Utility Functions:** Includes helpers like `parse_feet_inches` and `feet_to_inches` for handling dimension strings like `16'1.5"`.
6. **Example Script:** `examples/home_plan.py` demonstrates how to build a small house plan and export as DXF.

---

### ❌ Not Yet Implemented (what’s missing vs. objective)

* 🚫 **Image-to-DXF Conversion:** No tracing of scanned sketches/photos yet.
* 🚫 **Auto Layout Extraction:** Doesn’t detect rooms, walls, or doors from images.
* 🚫 **Symbols (doors, windows, furniture):** Not added yet.
* 🚫 **Dimensioning Tools:** No auto-dimension lines or scale annotations.
* 🚫 **Config-driven Input:** No YAML/JSON or GUI input — rooms are still hardcoded in Python.

---

## 🔮 Roadmap

* [ ] Add **automatic tracing** from uploaded floor plan images (using OpenCV).
* [ ] Add support for **windows & doors**.
* [ ] Generate **3D extrusions** from DXF using Blender or Three.js.
* [ ] Build a **web UI** to upload an image and download DXF.

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License. Use freely for personal and commercial projects.

