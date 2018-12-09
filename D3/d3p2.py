import re
import numpy as np
with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D3\\input.txt") as f:
    claims = f.readlines()

w,h=1000,1000
canvas=[[0 for x in range(w)] for y in range(h)] #initialize canvas to 0
for claim in claims:
    match=re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",claim) #parse claim string
    id,xs,ys,w,h=map(int,match.group(1,2,3,4,5)) #map strings to ints
    for y in range(ys,ys+h):
        for x in range(xs,xs+w):
            canvas[x][y]+=1

for claim in claims:
    match=re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",claim) #parse claim string
    id,xs,ys,w,h=map(int,match.group(1,2,3,4,5)) #map strings to ints
    tainted=False
    for y in range(ys,ys+h):
        if tainted:
            break
        for x in range(xs,xs+w):
            if canvas[x][y]>1:
                tainted=True
                break
    if not tainted:
        print("Result",id)

print("End")
