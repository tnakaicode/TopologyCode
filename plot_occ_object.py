import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import platform
import time
import io
import argparse
from linecache import getline, clearcache, updatecache

# "./img/IMG-20230106-001.png"

sys.path.append(os.path.join("./"))
import topologicpy
# import topologic

from topologicpy.Aperture import Aperture
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Color import Color
from topologicpy.Context import Context
# from topologicpy.DGL import DGL
from topologicpy.Dictionary import Dictionary
from topologicpy.Edge import Edge
# from topologicpy.EnergyModel import EnergyModel
from topologicpy.Face import Face
from topologicpy.Graph import Graph
# from topologicpy.Graph_Export import Graph_Export
from topologicpy.Grid import Grid
# from topologicpy.Helper import Helper
# from topologicpy.Honeybee import Honeybee
from topologicpy.Matrix import Matrix
# from topologicpy.Neo4jGraph import Neo4jGraph
from topologicpy.Plotly import Plotly
from topologicpy.Process import processCell
from topologicpy.Shell import Shell
# from topologicpy.Speckle import Speckle
# from topologicpy.SQL import SQL
from topologicpy.Topology import Topology
# from topologicpy.UnitTest import UnitTest
from topologicpy.Vector import Vector
from topologicpy.Vertex import Vertex
from topologicpy.Wire import Wire

# ./img/topologicpy.jpg
# conda install pytorch torchvision torchaudio cpuonly -c pytorch
# conda install -c dglteam dgl
# conda install -c plotly plotly
# pip install openstudio
# pip install honeybee, honeybee_energy
# pip install specklepy requests_toolbelt

# conda env create -f py39_math.yaml


# from base import plot2d, plot3d
# from base_occ import dispocc

from OCC.Display.SimpleGui import init_display
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepTools import breptools
from OCC.Core.Message import Message_ProgressRange
from OCC.Core.Quantity import Quantity_Color, Quantity_NOC_ALICEBLUE, Quantity_NOC_ANTIQUEWHITE

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--pxyz", dest="pxyz",
                        default=[0.0, 0.0, 0.0], type=float, nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)

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
    print(torus2_topo, torus2_topo.Type(), topologicpy.topologic.Face.Type())
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
