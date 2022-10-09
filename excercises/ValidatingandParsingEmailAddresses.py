import email.utils
import re

pattern = r"^[A-Za-z].+[\@]{1}([A-Za-z])+[\.]{1}[a-z]{1,3}$"

n = int(input())
for i in range(0,n):
    inp = input()
    r = re.search(pattern, email.utils.parseaddr(inp)[1])
    if r:
        print(inp)
