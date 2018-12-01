from __future__ import print_function
with open("c:\\users\\user\\documents\\dev\\adventofcode2018\\D1\\input.txt") as f:
    lines = f.readlines()
freq=0
freq_h={}
lines_len=len(lines)
i=0
print("GO!")
while True:
    freq+=int(lines[i])
    if freq_h.get(freq,False):
        break
    else:
        freq_h[freq]=True
    if i==(lines_len-1):
        i=0
        print(".",end='')
    else:
        i+=1
print(freq)