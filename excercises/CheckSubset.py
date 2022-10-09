# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    T = int(input())
    for i in range(0,T):
        aSize = int(input())
        aNumb = set(map(int, input().split()))
        bSize = int(input())
        bNumb = set(map(int, input().split()))
        print(len(aNumb.difference(bNumb))==0)
