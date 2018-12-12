import re

def react(str):
    if len(str) == 1:
        return str
    else:
        if(str[0]==str[1]):
            react(str[2:])

with open("sample.txt") as f:
    record = f.readlines()
