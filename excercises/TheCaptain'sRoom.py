if __name__ == '__main__':
    K = int(input())
    roomNumbers = list(map(int, input().split()))
    roomSet = set(roomNumbers)
    for el in roomSet:
        roomNumbers.remove(el)
    print(*roomSet.difference(set(roomNumbers)))
