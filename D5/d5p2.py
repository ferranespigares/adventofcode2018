#import re #Wanted to do a REGEX, but unfortunately python does not support inline modifiers for REGEX on the standard re module :(
import regex # requires pip install regex --user
from string import ascii_lowercase

with open("/home/user/Devel/adventofcode2018/D5/input.txt") as f:
    input = f.readlines()

def react(polymer):
    last=len(polymer)
    cur=0
    while last!=cur:
        last=len(polymer)
        match =regex.sub(r"(?V1)([A-Z])(?!\1)(?i)\1","",polymer)
        polymer=regex.sub(r"(?V1)([a-z])(?!\1)(?i)\1","",match)
        cur=len(polymer)
    return polymer

polymer=input[0].strip() #strip the damn CR

result_matrix={}
for c in ascii_lowercase:
    test_polymer=polymer.translate(None, c+c.upper())
    test_result=len(react(test_polymer))
    result_matrix[c]=test_result

result=min(result_matrix, key = lambda x: result_matrix.get(x) )

print("Result",result_matrix[result])