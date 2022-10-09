from collections import deque

T = int(input())

for i in range(0, T):
    k  = int(input())
    b = deque([int(a) for a in input().split()])
    res = []
    while b:
        if b[-1] >= b[0]:
            res.append(b.pop())
        else:
            res.append(b.popleft())
    sortedRes = sorted(res,reverse=True)
    if res == sortedRes:
        print('Yes')
    else:
        print('No')
