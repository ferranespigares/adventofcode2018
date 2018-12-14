import re
import math

with open("/home/user/Devel/adventofcode2018/D6/sample.txt") as f:
    input = f.readlines()

def mdist(coord1,coord2):
    distance=abs(math.fsum(tuple(x-y for x,y in zip(coord1,coord2))))
    return distance

coords=[]
for i in input:
    coords.append(eval(i.translate(None,' ')))

print(coords)

w,h=1000,1000
canvas=[[0 for x in range(w)] for y in range(h)] #initialize canvas to 0