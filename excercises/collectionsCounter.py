from collections import Counter

numberOfShoes = int(input())
shoeSizes = Counter(map(int,input().split()))
customersNumber = int(input())
moneyEarned = 0
for i in range (0,customersNumber):
    shoeNumber, moneyPaied = map(int,input().split())
    if(shoeSizes[shoeNumber]>0):
        shoeSizes[shoeNumber] -= 1
        moneyEarned += moneyPaied
print(moneyEarned)
