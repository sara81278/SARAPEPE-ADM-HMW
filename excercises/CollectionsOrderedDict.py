from collections import OrderedDict

N = int(input())

supermarketDic = OrderedDict()

for i in range(0,N):
    name, price = input().rsplit(maxsplit=1)
    if(not(name in supermarketDic.keys())):
        supermarketDic[name] = 0
    supermarketDic[name] += int(price) 

for key in supermarketDic.keys():
    print(key, supermarketDic[key], sep = ' ')
