import re
import numpy as np

with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D3\\input.txt") as f:
    records = f.readlines()


dtype=[('month',int),('day',int),('guardid',int)]    

for record in records:
    if re.search(r".*falls.*",record) is not None:

        continue
    if re.search(r".*wakes.*",record) is not None:
        continue
    
    match=re.search(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] Guard #(\d+) begins shift",record) #parse claim string
    year,month,day,hour,minute,id=match.group(1,2,3,4,5,6) #map strings to ints

