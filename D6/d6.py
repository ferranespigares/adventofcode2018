import re
import math
import sys

with open(r"C:\Users\User\Documents\dev\adventofcode2018\D6\sample.txt") as f:
    input = f.readlines()

def mdist(coord1,coord2):
    distance=abs(math.fsum(tuple(x-y for x,y in zip(coord1,coord2))))
    return distance

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
            break
    return index
            
coords=[]
maxy=0
maxx=0
minx=9999
miny=9999
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

canvas=[[0 for x in range(maxx+1)] for y in range(maxy+1)] #initialize canvas

for y in range(maxy+1):
    for x in range(maxx+1):
        canvas[y][x]=closer((x,y),coords)

print(coords)

for y in range(maxy+1):
    sys.stdout.write(str(y))
    sys.stdout.write(" ")
    for x in range(maxx+1):
        sys.stdout.write(str(canvas[y][x]))
        sys.stdout.write(" ")
    print("")