from collections import OrderedDict

N = int(input())

strings = OrderedDict()

for i in range(0,N):
    s = input()
    if(not s in strings.keys()):
        strings[s] = 0
    strings[s] +=1

print(len(strings))
print(*strings.values(), sep=' ')
