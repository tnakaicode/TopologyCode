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

- answer

I am not sure what DisplayShape is expecting as input, but this method was meant to make topologic compatible with FreeCAD. It outputs a TopoDS_Shape as you pointed out. Please search your API for a method that converts that or if you can convert a BREP use Topology.String(torus1)

DisplayShapeが何を入力として想定しているかはわかりませんが、この方法はFreeCADとトポロジーの互換性を持たせるためのものでした。ご指摘の通りTopoDS_Shapeを出力しています。それを変換するメソッドをAPIで検索するか、BREPで変換できるのであればTopology.String(torus1)を使用してください。

- reply

DisplayShapeはOpenCASCADEで定義されているTopoDS_Shape(TopoDS_Shell, TopoDS_Face, ...)をInputに要求します。
非常に惜しいところまで来ていて、topologic.TopoDS_Shapeの"topologic."の部分がなければ、型が一致してpythonocc-coreでも描画可能になると推測しています。

Brepファイルに出力すれば見れるは確認しています。同じPythonで書かれたプログラムのため、外部ファイルを経由せずにデータの受け渡し方法がないかを模索しています。

DisplayShape requires the type of TopoDS_Shape(TopoDS_Shell, TopoDS_Face, ...) defined in OpenCASCADE to the Input.
It is very close, and I am guessing that without the "topologic." part of topologic.TopoDS_Shape, the types would match and pythonocc-core would be able to draw it.

I have confirmed that I can see it if I output it to a blp file. Since the programs are written in the same Python, I am looking for a way to pass the data without going through an external file.
