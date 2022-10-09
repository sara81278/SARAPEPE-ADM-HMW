import re

N = int(input())
for i in range(0,N):
    string = input()
    print("YES" if re.search(r"^[789]{1}[0-9$]{9}$",string) else "NO")
