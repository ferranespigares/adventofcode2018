import re
import math
import sys
import itertools
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

with open(r"/home/user/Devel/adventofcode2018/D6/sample.txt") as f:
    input = f.readlines()

#Calculates manhattan distance between two coords
def mdist(coord1,coord2):
    distance=math.fsum(tuple(abs(x-y) for x,y in zip(coord1,coord2)))
    return distance

#Returns closer index in coords array to target
def closer(target,coords):
    min_dist=9999
    index=9999
    for i in range(len(coords)):
        dist=mdist(target,coords[i])
        if dist<min_dist:
            min_dist=dist
            index=i
            continue
        if dist==min_dist:
            index=None
    return index

def isfinite(minx,miny,maxx,maxy,coords,canvas):
    b1=[]
    for x in range(minx,maxx+1):
        if canvas[miny][x] not in b1:
            b1.append(canvas[miny][x])
        if canvas[maxy][x] not in b1:
            b1.append(canvas[maxy][x])        
    for y in range(miny,maxy+1):
        if canvas[y][minx] not in b1:
            b1.append(canvas[y][minx])
        if canvas[y][maxx] not in b1:
            b1.append(canvas[y][maxx])
    selector=[]
    for i in range(len(coords)):
        if i in b1:
            selector.append(True)
        else:
            selector.append(False)

    selector=[not i for i in selector] # keep the non-infinite
    return list(itertools.compress(coords,selector))

coords=[]
maxy=0
maxx=0
minx=9999
miny=9999

#Parse input strings to tuples
for i in input:
    coords.append(eval(i.translate(None,' ')))
    if coords[-1][0]>maxx:
        maxx=coords[-1][0]
    if coords[-1][1]>maxy:
        maxy=coords[-1][1]
    if coords[-1][0]<minx:
        minx=coords[-1][0]
    if coords[-1][1]<miny:
        miny=coords[-1][1]

canvas=[[0 for x in range(maxx+2)] for y in range(maxy+2)] #initialize canvas

#Determine wich coordinate is closer to each canvas location
for y in range(maxy+2):
    for x in range(maxx+2):
        canvas[y][x]=closer((x,y),coords)

#Filter out the infinite area coords
finitecoords=isfinite(minx,miny,maxx,maxy,coords,canvas)
finiteindexes=[coords.index(x) for x in finitecoords]

max_area=0
for i in finiteindexes:
    area=sum(x.count(i) for x in canvas)
    if area>max_area:
        max_area=area

print("Result",max_area)

#Draw nice map
X = np.array(canvas,dtype=np.float)
fig,ax=plt.subplots()
im=ax.imshow(X, interpolation='bilinear', origin='upper', cmap='plasma')
plt.show()

#for y in range(maxy+2):
#    sys.stdout.write(hex(y))
#    sys.stdout.write(" ")
#    for x in range(maxx+2):
#        if(canvas[y][x] is None):
#            sys.stdout.write(".")
#        else:
#            sys.stdout.write(str(canvas[y][x]))
#        sys.stdout.write(" ")
#    print("")