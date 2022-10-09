import re

n = int(input())
for _ in range(n):
    uid = input()
    
    digit = re.findall(r'\d', uid)
    alpha = re.findall(r'[A-Z]', uid)
    special = re.findall(r'[@_!#$%^&*()<>?/\|}{~:]', uid)
    
    if (len(alpha) < 3 or
        len(digit) < 3 or
        len(special) > 0 or
        len(set(uid)) != 10 or
        len(uid) != 10):
        print('Invalid')
    else:
        print('Valid')
        
