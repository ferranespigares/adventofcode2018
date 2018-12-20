import re
with open(r"/Users/user/Documents/devel/adventofcode2018/D7/input.txt") as f:
	input = f.readlines()

w = {}
for l in input:
	m=re.search(r"Step ([A-Z]) must be finished before step ([A-Z]).*",l) #parse string
	p=m.group(2)
	c=m.group(1)
	if(p not in w): w[p]=[]
	if(c not in w): w[c]=[]
	w[p].append(c)

# w now contains a dict with all elements, plus a list of all inmediate parents for each
result = ''
while len(w) > 0:
	e=[]
	for i in w.items(): 
		if len(i[1])==0:
			e.append(i)
	f=sorted(e)[0][0] #f contains the items with no dependent parents, we select the first one *sorted*
	del w[f]
	for k in w:
		if f in w[k]: w[k].remove(f)
	result +=f
print("Result:",result)