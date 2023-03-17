import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import platform
import time
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
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
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

    torus1 = Cell.Torus()
    torus1 = Topology.Triangulate(torus1)
    
    box1 = BRepPrimAPI_MakeBox(10., 20., 30.).Shape()
    
    torus1_shp = Topology.OCCTShape(torus1)
    
    print(torus1_shp)
    print(topologicpy.topologic.TopologyFactoryManager.GetDefaultFactory(box1.ShapeType()))
    print(Topology.ByOCCTShape(box1))

    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(Topology.OCCTShape(torus1), update=True)
    start_display()
