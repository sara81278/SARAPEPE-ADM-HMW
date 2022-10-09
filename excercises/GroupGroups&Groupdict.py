import re

S = input()
res = re.search(r"([A-Za-z0-9])\1", S)
print(res.group()[0] if res else '-1')
