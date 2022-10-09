# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    output = True
    for i in range(0,n):
        subSet = set(map(int, input().split()))
        isSubset = (len(subSet.difference(A))==0 
            and len(A.difference(subSet))>0)
        output = output and isSubset
    print(output)
