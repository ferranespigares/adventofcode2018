with open("input.txt") as f:
    lines = f.readlines()
freq=0
for line in lines:
    freq+=int(line)
print(freq)