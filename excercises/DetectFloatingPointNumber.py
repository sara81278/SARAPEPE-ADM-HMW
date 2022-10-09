import re

T = int(input())
regex = '^[+-]?[0-9]*\.[0-9]+$'
print(*[re.match(regex, input())!=None for i in range(0,T)], sep = '\n')
