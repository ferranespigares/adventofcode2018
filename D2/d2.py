from collections import Counter
with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D2\\input.txt") as f:
    boxids = f.readlines()

boxids = [x.rstrip() for x in boxids]
counts = [Counter(x) for x in boxids]

count2=0
count3=0
for count in counts:
    if 2 in count.values():
        count2+=1
    if 3 in count.values():
        count3+=1
print(count2*count3)