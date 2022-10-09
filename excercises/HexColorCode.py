import re


pattern = re.compile(r"[\s:](#(?:[0-9A-Fa-f]{3}){1,2})")
n = int(input())

for i in range(n):
    s = input()
    colourCodes = pattern.findall(s)
    for colour in colourCodes:
        print(colour)
   
