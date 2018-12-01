from __future__ import print_function
with open("input.txt") as f:
    lines = f.readlines()
freq=0
freq_h=[0]
lines_len=len(lines)
i=0
print("GO!")
while True:
    freq+=int(lines[i])
    if freq in freq_h:
        break
    freq_h.append(freq)
    if i==(lines_len-1):
        i=0
        print(".",end='')
    else:
        i+=1

# for line in lines:
#    freq+=int(line)
#    if freq in freq_h:
#        break
#    freq_h.append(freq)
print(freq)