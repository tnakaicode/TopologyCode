import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import platform
import time
import math
import argparse
from linecache import getline, clearcache, updatecache

sys.path.append(os.path.join("./"))
import topologicpy
# import topologic

from topologicpy.Aperture import Aperture
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Color import Color
from topologicpy.Context import Context
from topologicpy.DGL import DGL
from topologicpy.Dictionary import Dictionary
from topologicpy.Edge import Edge
from topologicpy.EnergyModel import EnergyModel
from topologicpy.Face import Face
from topologicpy.Graph import Graph
# from topologicpy.Graph_Export import Graph_Export # unexpected indent
from topologicpy.Grid import Grid
from topologicpy.Helper import Helper
# from topologicpy.Honeybee import Honeybee # install honeybee, honeybee_energy
from topologicpy.Matrix import Matrix
from topologicpy.Neo4jGraph import Neo4jGraph  # py2neo
from topologicpy.Plotly import Plotly
from topologicpy.Process import processCell
from topologicpy.Shell import Shell
# from topologicpy.Speckle import Speckle # install specklepy
from topologicpy.SQL import SQL
from topologicpy.Topology import Topology
# from topologicpy.UnitTest import UnitTest # invalid error
from topologicpy.Vector import Vector
from topologicpy.Vertex import Vertex
from topologicpy.Wire import Wire

# ./img/topologicpy.jpg
# conda install pytorch torchvision torchaudio cpuonly -c pytorch
# conda install -c dglteam dgl
# conda install -c plotly plotly
# pip install openstudio
# pip install honeybee, honeybee_energy
# pip install py2neo

# conda env create -f py39_math.yaml

# from base import plot2d, plot3d
# from base_occ import dispocc

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepTools import breptools

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--pxyz", dest="pxyz",
                        default=[0.0, 0.0, 0.0], type=float, nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)
    
    shp = EnergyModel.ByImportedOSM("./topologicpy/assets/EnergyModel/OSMTemplate-OfficeBuilding-3.5.0.osm")
    print(shp)
    