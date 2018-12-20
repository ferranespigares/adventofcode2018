import re

with open(r"/Users/user/Documents/devel/adventofcode2018/D7/sample.txt") as f:
    input = f.readlines()

steptime=1
nworkers=2 #you+1 worker
totaltime=0
def lettertime(l):
    return ord(l)-64

w = {}
for l in input:
    m=re.search(r"Step ([A-Z]) must be finished before step ([A-Z]).*",l) #parse string
    p=m.group(2)
    c=m.group(1)
    if(p not in w): w[p]=[]
    if(c not in w): w[c]=[]
    w[p].append(c)  # w now contains a dict with all elements, plus a list of all inmediate parents for each
    
result = ''
workers=[(None,0) for x in range(nworkers)] #Initialize workers array
e=[]
cleanup=[]

while len(w) > 0:

    for i in w.items(): 
        if len(i[1])==0:
#            i[1].append(lettertime(i[0])) #add task effort based on letter
            e.append(i) #add all tasks with no dependancy
    f=sorted(e) #sort priority by alphabetical order

    for i in range(len(workers)):
        if (workers[i][0] is None) and (len(f)) > 0:
            workers[i]=(f[0][0],lettertime(f[0][0]))
            del w[f[0][0]]
            cleanup+=f[0]
            del f[0]

    totaltime+=steptime

    for k in w:
        if cleanup in w[k]: w[k].remove(f)
    result +=  cleanup

print("Result:",totaltime)