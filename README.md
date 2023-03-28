# TopologyCode

```bash
conda env export > py39_math.yaml
conda env create -f py39_math.yaml
```

<https://topologic.app/topologicpy_doc/topologic_pdoc/>

## UnitTest

- [x] 01Vertex.py
- [x] 02Edge.py
- [x] 03Wire.py
- [x] 04Face.py
- [x] 05Shell.py
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

- reply

File IOを介さず、stringでデータを渡すのは良いアイデアです。修正したコードを残します。
1つ問題があります。pythonoccで作ったTorus(コード中torus2)を、Plotly.DataByTopologyに入れると、Python全体のProcessが停止します。Debugモードで起動してもDebuggerそのものが停止します。コメントアウト部分をアクティブにして実行してみてください。

Passing data as a string instead of through File IO is a good idea. I will leave the modified code.
There is one problem: when I put Torus (torus2 in the code) created in pythonocc into Plotly.DataByTopology, the whole Python process stops. even if I start it in Debug mode, the Debugger itself stops. Try running it with the commented out part active.

```python
import sys
import os

sys.path.append(os.path.join("./"))
import topologicpy
# import topologic

from topologicpy.Cell import Cell
from topologicpy.Topology import Topology

from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Core.BRepTools import breptools

# torus1: Topologicpy -> OCC
torus1 = Cell.Torus()
torus1 = Topology.Triangulate(torus1)
print(torus1)
torus1_Data = Plotly.DataByTopology(torus1,
                                   faceColor="blue", faceOpacity=0.5, vertexColor=2)

# Convert the topology to a BRep string
torus1_brep = Topology.String(torus1, version=1)

# Read the BRep String from the Brep string
torus1_shpe = breptools.ReadFromString(torus1_brep)
print(torus1_shpe)

# box1: OCC -> Topologicpy
box1 = BRepPrimAPI_MakeBox(1.0, 2.0, 3.).Solid()
box1_brep = breptools.WriteToString(box1)
box1_topo = Topology.ByString(box1_brep)
print(box1_topo)
box1_Data = Plotly.DataByTopology(box1_topo,
                                    faceColor="red", faceOpacity=0.5, vertexColor=2)
    
# torus2: OCC -> Topologicpy
torus2 = BRepPrimAPI_MakeTorus(gp_Ax2(gp_Pnt(0, 0, 1), gp_Dir(0, 0, 1)),
                               0.5, 0.125).Face()
torus2_brep = breptools.WriteToString(torus2)
torus2_topo = Topology.ByString(torus2_brep)
print(torus2_topo)
#torus2_Data = Plotly.DataByTopology(torus2_topo,
#                                    faceColor="red", faceOpacity=0.5, vertexColor=2)

plotlyData = torus1_Data + box1_Data
fig = Plotly.FigureByData(plotlyData, width=950 * 2, height=500 * 2)
Plotly.SetCamera(fig,
                 camera=[1.5, 1.5, 1.5], target=[0, 0, 0], )
Plotly.Show(fig, renderer="browser")

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(torus1_shpe, color="BLUE1")
display.DisplayShape(torus2, color="RED")
display.DisplayShape(box1, color="RED")
display.FitAll()
start_display()
```

pythonoccのViewerの様子は以下の通りです。赤いTorusがtorus2で、Topologicpyとは違い表面は曲面として描画されます。
