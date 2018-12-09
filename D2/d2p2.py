from collections import Counter
import itertools
import difflib

with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D2\\input.txt") as f:
    boxids = f.readlines()

boxids = [x.rstrip() for x in boxids]

for a,b in itertools.combinations(boxids,2): #reduce the minimum
#    print a,b
    diff=list(difflib.ndiff(a,b)) #calculate difference between strings as char by char diff array
    res=[k for k in diff if '-' in k] #keep only the missing chars (contains '-')
    if len(res) == 1:
        print("Found:")
        filter1=([k for k in diff if '-' not in k]) #print only the coincident chars
        filter2=([k for k in filter1 if '+' not in k])
        print(''.join([x.strip(' ')for x in filter2]))
        break

#counts = [Counter(x) for x in boxids]
#count2=0
#count3=0
#for count in counts:
#    if 2 in count.values():
#        count2+=1
#    if 3 in count.values():
#        count3+=1
#print(count2*count3)
