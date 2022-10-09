# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    A = int(input())
    aNum = set(map(int,input().split()))
    N = int(input())
    for i in range (0,N):
        nOperation, nLen = input().split()
        nNum = set(map(int,input().split()))
        if(nOperation == 'update' or nOperation == '|='):
            aNum.update(nNum)
        elif (nOperation == 'intersection_update' or nOperation == '&='):
            aNum.intersection_update(nNum)
        elif (nOperation == 'difference_update' or nOperation == '-='):
            aNum.difference_update(nNum)
        elif (nOperation == 'symmetric_difference_update' or nOperation == '^='):
            aNum.symmetric_difference_update(nNum)
            
    print(sum(aNum))
    
