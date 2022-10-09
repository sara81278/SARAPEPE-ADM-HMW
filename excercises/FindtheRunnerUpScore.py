if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrToList = list(arr)
    y = max([i for i in arrToList if i != max(arrToList)])
    print (y)
