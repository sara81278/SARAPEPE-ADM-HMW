# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    N = input()
    engStud = set(input().split())
    B = input()
    frStud = set(input().split())
    
    print(len(engStud.union(frStud)))
