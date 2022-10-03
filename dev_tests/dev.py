import gmshparser

mesh = gmshparser.parse(r'A:\Projects\XFEMPy\Reference\XFEM_Fracture2D\JOBS_LIBRARY\_mesh_files (can be placed in Input_Mesh folder of job)\2holes2crack_buchard2003_fine_4.1.msh')
print(mesh)