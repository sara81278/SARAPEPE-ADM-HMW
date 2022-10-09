studentNumber, sbjNumber = map(int, input().split())
average = [] 
gradeList = []

for i in range(0,sbjNumber):
    gradeList.append(list(map(float,input().split())))

for i in zip(*gradeList):
    print(sum(i)/sbjNumber)
