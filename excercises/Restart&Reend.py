import re

S = input()
k = input()

pattern = re.compile(k)
output = pattern.search(S)
if not output: 
    print("(-1, -1)")
else:
    while output:
        print(f"({output.start()}, {output.end()-1})")
        output = pattern.search(S,output.start() + 1)
