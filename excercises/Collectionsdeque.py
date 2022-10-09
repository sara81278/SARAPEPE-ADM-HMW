from collections import deque

n = int(input())
q = deque()

for i in range(0,n):
    com, *el = input().split()
    if(com == 'append'):
        q.append(int(*el))
    elif(com == 'appendleft'):
        q.appendleft(int(*el))
    elif(com == 'pop'):
        q.pop()
    elif(com == 'popleft'):
        q.popleft()
print(*q, sep = ' ')
