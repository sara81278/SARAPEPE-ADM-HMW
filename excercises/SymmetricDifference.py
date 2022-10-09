# Enter your code here. Read input from STDIN. Print output to STDOUT

def getSimmetricDifference(mSet, nSet):
    array = [int(i) for i in mSet if not(i in nSet)]
    array.extend([int(j) for j in nSet if not(j in mSet)])
    array.sort()
    return '\n'.join(list(map(str,array)))

if __name__ == '__main__':
    M = input()
    mSet = set(input().split())
    N = input()
    nSet = set(input().split())
    print(getSimmetricDifference(mSet, nSet))
    
