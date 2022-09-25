import os


def read_mesh_file(mesh_fileType):
    cBCNod = []
    cBCCrd = []
    if mesh_fileType == 'gmsh':

