#!/usr/bin/python
# Read mesh data from foam case and create vtk files
# that can be used to visualize polygonal mesh
datapath_read_points="constant/polyMesh/points"
datapath_read_faces="constant/polyMesh/faces"
datapath_write="VTK/1.vtk"

file_read_points=open(datapath_read_points,'r')
file_read_faces=open(datapath_read_faces,'r')
file_write=open(datapath_write,'w')
#----------------------------------------------------
#Header
file_write.write("# vtk DataFile Version 3.1\n" )
file_write.write("Visualization for polyMesh\n" )
file_write.write("ASCII\n" )
file_write.write("DATASET UNSTRUCTURED_GRID\n" )

#----------------------------------------------------

l_points=file_read_points.readlines()
numPoints=l_points[18]
numPoints=numPoints.replace("\n"," ")
file_write.write("POINTS " + numPoints + "float\n" )
for line in l_points[20:20+int(numPoints)]:
    line=line.replace("(","")
    line=line.replace(")","")
    file_write.write(line)

#----------------------------------------------------
l_cells_=file_read_faces.readlines()
numCells=l_cells_[18]
numCells=numCells.replace("\n"," ")
#------------------------------------------
l_cells_=l_cells_[20:]

while l_cells_[-1]!=')\n':
      l_cells_.pop()

l_cells=[]
for line in l_cells_:
     
    if line=="(\n":
       l_cells[-1]+="("
       continue
     
    if line==")\n":
       l_cells[-1]+=")\n"
       continue

    if line=="\n":
       l_cells.append("")
       continue

    if len( line.split('(') )>1:
       l_cells.append(line)
       continue    
    
    if len(l_cells)==0:
       l_cells.append(line.replace("\n"," "))
       continue 

    l_cells[-1]+=line.replace("\n"," ")
      
#------------------------------------------
numSize=0;
for line in l_cells:
    if line=="":
       continue 
    line=line.split('(');
    numSize+=int(line[0])+1;

file_write.write("CELLS " + numCells + str(numSize) +"\n")
for line in l_cells:
    if line=="":
       continue 
    line=line.replace("("," ")
    line=line.replace(")","")
    file_write.write(line)

#----------------------------------------------------
file_write.write("CELL_TYPES "+numCells + "\n" )
file_write.write("7 "*int(numCells))

file_read_points.close()
file_read_faces.close()
file_write.close()
#----------------------------------------------------


