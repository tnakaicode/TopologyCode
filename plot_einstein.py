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
from topologicpy.DGL import DGL # not exist Dictionary
from topologicpy.Dictionary import Dictionary
from topologicpy.Edge import Edge
#from topologicpy.EnergyModel import EnergyModel # not exist Topology
from topologicpy.Face import Face
from topologicpy.Graph import Graph
# from topologicpy.Graph_Export import Graph_Export # unexpected indent
from topologicpy.Grid import Grid
from topologicpy.Helper import Helper
# from topologicpy.Honeybee import Honeybee # install honeybee, honeybee_energy
from topologicpy.Matrix import Matrix
# from topologicpy.Neo4jGraph import Neo4jGraph # py2neo
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


if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--pxyz", dest="pxyz",
                        default=[0.0, 0.0, 0.0], type=float, nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)
    
    columns = 2
    rows = 2
    r = 1
    sides = 6
    d = np.cos(np.deg2rad(30))*r
    
    hexagon = Wire.Circle(radius=r, sides=sides)
    hexagon = Topology.Rotate(hexagon, degree=90)
    hexagons = []
    for column in range(columns):
        dx = column * (r*1.5)
        if column %2 == 0:
            yOffset = 0
        else:
            yOffset = d
        for row in range(rows):
            dy = row*(d*2)
            hexagons.append(Topology.Translate(hexagon, dx, dy+yOffset,0))
    
    einstein = Wire.Einstein(radius=r, placement="Center")
    data01 = Plotly.DataByTopology(einstein, edgeWidth=5, showVertexLegend=False, showEdgeLegend=False, showFaceLegend=False)
    data02 = Plotly.DataByTopology(Cluster.ByTopologies(hexagons[:len(hexagons)-1]))

    plotlyData = data01 + data02
    fig = Plotly.FigureByData(plotlyData, width=950 * 2, height=500 * 2)
    Plotly.Show(fig, renderer="browser")
