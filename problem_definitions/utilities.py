import os
import gmshparser


def read_mesh_file(mesh_fileType: str):
    cBCNod = []
    cBCCrd = []
    if mesh_fileType == 'gmsh':
        mesh = gmshparser.parse(mesh_filseType)



