import numpy

N, M = input().split()
arr = numpy.array([list(map(int, input().split())) for i in range(0,int(N))])
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis= 0))
print(round(numpy.std(arr),11))
