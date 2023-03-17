# TopologyCode

```bash
conda env export > py39_math.yaml
conda env create -f py39_math.yaml
```

<https://topologic.app/topologicpy_doc/topologic_pdoc/>

## UnitTest

- [x] 02Edge.py
- [x] 03Wire.py
- [x] 04Face.py
- [ ] 05Shell.py
- [x] 06Cell.py
- [x] 07CellComplex.py
- [x] 08Cluster.py
- [x] 09Topology.py
- [x] 10Dictionary.py
- [x] 11Grid.py
- [x] 12Matrix.py
- [x] 13Graph.py

## Issue

### Issue#17

pythonocc-core(<https://github.com/tpaviot/pythonocc-core>)というOpenCASCDAEのPython Warpperでtopologicpyで作ったTorusをTopology.ByOCCTShape()で変換して、描画しようとしたのですがErrorが出てしまいます。
Topology.ByOCCTShape()の変換で、型がtopologic.TopoDS_Shapeであることが原因なのでですが、なにか解決方法はないでしょうか？

I am trying to convert Torus created with topologicpy by Topology.ByOCCTShape() and tried to draw it in OpenCASCDAE's Python Warpper called pythonocc-core (<https://github.com/tpaviot/pythonocc-core>), but I get an Error.
That because type is still topologic.TopoDS_Shape converting by Topology.ByOCCTShape().

Is there any way to solve this problem?

my code is following:

```python

import sys
import os

sys.path.append(os.path.join("./"))
import topologicpy
# import topologic

from topologicpy.Cell import Cell
from topologicpy.Topology import Topology

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

torus1 = Cell.Torus()
torus1 = Topology.Triangulate(torus1)
torus1_shp = Topology.OCCTShape(torus1)

#box1 = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()

print(torus1_shp)
#print(Topology.ByOCCTShape(box1))

#display, start_display, add_menu, add_function_to_menu = init_display()
#display.DisplayShape(Topology.OCCTShape(torus1), update=True)
#start_display()
```
