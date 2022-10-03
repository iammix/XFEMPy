import os
import gmshparser


def read_mesh_file(mesh_fileType: str):
    cBCNod = []
    cBCCrd = []
    # TODO Develop GSM file reader
    # labels: enhancement
    # assignees: iammix
    # milestone: v0.1.0_rc1
    if mesh_fileType == 'gmsh':
        mesh = gmshparser.parse(mesh_filseType)



