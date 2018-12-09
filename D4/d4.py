import re
import numpy as np

with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D3\\input.txt") as f:
    records = f.readlines()

for record in records:
    match=re.search(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] Guard #(\d+) begins shift",record) #parse claim string
    year,month,day,hour,minute,id=match.group(1,2,3,4,5,6) #map strings to ints

dtype=[('mont',int),('day',int),('guardid',int)]    