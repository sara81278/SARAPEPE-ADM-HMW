n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0, N):
    command, *el = input().split()
    if(command == 'pop'):
        s.pop()
    if(command == 'discard'):
        s.discard(int(*el))
    if(command == 'remove'):
        s.remove(int(*el))
print(sum(s))
