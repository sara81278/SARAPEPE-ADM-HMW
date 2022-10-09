#code
N = int(input())

for i in range (0,N):
    try:
        a, b = map(int,input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print ("Error Code:",e)
