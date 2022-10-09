import re
N = int(input())
for i in range(N):
    txt = input()
    s = re.sub(r'(?<=\s)&&(?=\s)',"and", txt)
    print(re.sub(r'(?<=\s)\|\|(?=\s)',"or",s))
