if __name__ == '__main__':
    N = int(input())
    countryStamps = set()
    for i in range(0, N):
        countryStamps.add(input())
    print(len(countryStamps))
    
