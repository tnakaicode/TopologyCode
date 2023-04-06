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
    
    shell = Shell.HyperbolicParaboloidRectangularDomain(uSides=32, vSides=32)
    shell = Topology.Triangulate(shell)
    vertices = Topology.Vertices(shell)
    selectors = []
    for v in vertices:
        intensity = Vertex.Z(v)
        d = Dictionary.ByKeysValues(["intensity"], [intensity])
        selectors.append(Topology.SetDictionary(v, d))
    
    shell = Topology.TransferDictionariesBySelectors(shell, selectors=selectors, tranVertices=True)
    Topology.Show(shell, intensityKey="intensity", colorScale="rainbow", faceOpacity=1, renderer="browser")

    #plotlyData = data01 + data02
    #fig = Plotly.FigureByData(plotlyData, width=950 * 2, height=500 * 2)
    #Plotly.Show(fig, renderer="browser")
#
    ## Convert the topology to a BRep string
    #einstein_brep = Topology.String(einstein, version=1)
    #hexagons_brep = [Topology.String(h, version=1) for h in hexagons]
#
    ## Read the BRep String from the Brep string
    #einstein_shpe = breptools.ReadFromString(einstein_brep)
    #hexagons_shpe = [breptools.ReadFromString(b) for b in hexagons_brep[:-1]]
    #print(einstein_shpe)
#
    #display, start_display, add_menu, add_function_to_menu = init_display()
    #display.DisplayShape(hexagons_shpe)
    #display.DisplayShape(einstein_shpe, color="BLUE1")
    #display.FitAll()
    #start_display()
