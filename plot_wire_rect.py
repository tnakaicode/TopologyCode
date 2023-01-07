import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import platform
import time
import argparse
from linecache import getline, clearcache, updatecache

# "./img/IMG-20230107-001.png"

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
# from topologicpy.Face import Face
# from topologicpy.Graph import Graph
# from topologicpy.Graph_Export import Graph_Export
from topologicpy.Grid import Grid
# from topologicpy.Helper import Helper
# from topologicpy.Honeybee import Honeybee
# from topologicpy.Matrix import Matrix
# from topologicpy.Neo4jGraph import Neo4jGraph
from topologicpy.Plotly import Plotly
# from topologicpy.Process import Process
# from topologicpy.Shell import Shell
# from topologicpy.Speckle import Speckle
# from topologicpy.SQL import SQL
from topologicpy.Topology import Topology
# from topologicpy.UnitTest import UnitTest
# from topologicpy.Vector import Vector
from topologicpy.Vertex import Vertex
from topologicpy.Wire import Wire

# ./img/topologicpy.jpg
# conda install pytorch torchvision torchaudio cpuonly -c pytorch
# conda install -c dglteam dgl
# conda install -c plotly plotly
# pip install openstudio
# pip install honeybee

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
    
    rect1 = Wire.Rectangle(width=10, length=10)
    v1 = Vertex.ByCoordinates(0,-6,0)
    v2 = Vertex.ByCoordinates(0,6,0)
    e1 = Edge.ByVertices([v1, v2])
    rect1 = Topology.Boolean(rect1, e1, operation="slice")
    
    d = Dictionary.ByKeysValues(["offset"],[-1.5])
    v3 = Vertex.ByCoordinates(2.5, 5, 0)
    v4 = Vertex.ByCoordinates(-2.5, -5, 0)
    
    v3 = Topology.SetDictionary(v3, d)
    v4 = Topology.SetDictionary(v4, d)
    rect1 = Topology.TransferDictionariesBySelectors(rect1, [v3, v4], tranEdges=True, tolerance=0.1)
    
    rect1Data = Plotly.DataByTopology(rect1, vertexSize=3)
    fig = Plotly.FigureByData(rect1Data)
    Plotly.SetCamera(fig, camera=[0,0,2.5])
    Plotly.Show(fig)
