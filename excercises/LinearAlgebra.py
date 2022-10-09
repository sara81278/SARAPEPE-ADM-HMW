import numpy

N = int(input())
arr = numpy.array([list(map(float, input().split())) for i in range(0,N)], float)
print(round(numpy.linalg.det(arr),11))
