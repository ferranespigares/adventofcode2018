import math

with open(r"/home/user/Devel/adventofcode2018/D6/input.txt") as f:
    input = f.readlines()

#Calculates manhattan distance between two coords
def mdist(coord1,coord2):
    distance=math.fsum(tuple(abs(x-y) for x,y in zip(coord1,coord2)))
    return distance

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

#Determine the distance of each canvas location to each coordinate
area=0
for y in range(maxy+2):
    for x in range(maxx+2):
        dist=sum([mdist((x,y),c) for c in coords])
        if dist<10000: #Problem requirement
            area+=1
        canvas[y][x]=dist

print("Result",area)
