import re

S = input()
matches = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", S, flags=re.IGNORECASE)
print(*[m for m in matches] if matches else [-1], sep = '\n')
