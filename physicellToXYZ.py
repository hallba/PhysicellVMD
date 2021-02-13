import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd
import math
'''
#Contains "basic_agents"
cells = loadmat("output00000064_cells.mat")
#contains "multiscale_microenvironment"
microenvironment = loadmat("output00000064_microenvironment0.mat")
'''
def filenameFormat(n):
    result = "data/output{:08d}_cells_physicell.mat".format(n)
    return(result)

def writeXYZ(firstFrame,lastFrame):
    with open("organoid.xyz",'w') as output:
        for frame in range(firstFrame,lastFrame+1):
            #Transposed so we can iterate
            allCells = loadmat(filenameFormat(frame))['cells'].transpose()
            #filter out absorbed organoids
            cellData = allCells[(allCells[:,4] > 0)]
            print(len(cellData),file=output)
            print("Physicell organoid simulation",file=output)
            for cell in cellData:
                '''
                Modified xyz format- could be extended further
                x y z user2 user3 vx vy user

                user is radius- important for size rendering
                '''
                x = cell[1]
                y = cell[2]
                z = cell[3]
                #convert from the volume
                radius = (3*cell[4]/(4*math.pi))**(1/3) #user
                #why are the volumes in frame 64 mostly 2494? Dead, single cell organoids?
                #suspect diffcells and stem cells are mixed up- 2494 organoids have 0 diffcells and 1 stemcell
                #what are 0 volume organoids?
                stemcells = cell[29] #user2
                diffcells = cell[28] #user3
                attached = cell[27]
                fusions = cell[31]
                #do not change the position of x,y,z and radius
                result = "CA {x} {y} {z} {user2} {user3} {vx} {vy} {user}".format(x=x,y=y,z=z,user2=stemcells,vx=diffcells,user3=attached,vy=fusions,user=radius)
                print(result,file=output)

writeXYZ(0,65)

