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

    torus1 = Topology.ByImportedBRep("./shp/torus.brep")
    # torus1 = Topology.Triangulate(torus1)

    torus2 = Topology.RemoveCoplanarFaces(torus1, angTolerance=0.1)

    wires = Cell.Wires(torus1)
    offsetWires = []
    for w in wires:
        offsetWires.append(Wire.ByOffset(w, offset=0.02))

    torus3 = Cluster.ByTopologies(offsetWires + [torus2])

    torusData = Plotly.DataByTopology(torus1,
                                      faceColor="red", faceOpacity=0.5, vertexColor=2)
    
    print(Topology.OCCTShape(torus1))

    s0 = time.ctime()
    ifc1 = Topology.ByImportedIFC("./shp/A_IFC_model.ifc")
    #ifc1 = Topology.Triangulate(ifc1)
    #ifc1Data = Plotly.DataByTopology(ifc1)

    plotlyData = [Plotly.DataByTopology(c) for c in ifc1]
    fig = Plotly.FigureByData(plotlyData, width=950 * 2, height=500 * 2)
    Plotly.SetCamera(fig,
                     camera=[1.5, 1.5, 1.5], target=[0, 0, 0], )
    Plotly.Show(fig, renderer="browser")
    print(time.ctime() - s0)
