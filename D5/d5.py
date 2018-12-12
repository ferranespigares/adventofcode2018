#import re #Wanted to do a REGEX, but unfortunately python does not support inline modifiers for REGEX on the standard re module :(
import regex

with open("/home/user/Devel/adventofcode2018/D5/input.txt") as f:
    polymer = f.readlines()


match2=polymer[0].strip() #damn CR
last=len(match2)
cur=0

while last!=cur:
    last=len(match2)
    match =regex.sub(r"(?V1)([A-Z])(?!\1)(?i)\1","",match2)
    match2=regex.sub(r"(?V1)([a-z])(?!\1)(?i)\1","",match)
    cur=len(match2)

print(match2)
print("Result",len(match2))