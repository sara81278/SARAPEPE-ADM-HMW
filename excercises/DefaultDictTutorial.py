from collections import defaultdict

n, m = map(int, input().split())
A = [input() for i in range (0,n)]
B = [input() for i in range (0,m)]

d = defaultdict(list)
for i in range(0,n):
    d[A[i]].append(i+1)

for el in B:
    if(len(d[el])):
        print(*d[el])
    else:
        print(-1)
    
