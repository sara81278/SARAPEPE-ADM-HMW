import numpy

N, M = input().split()
arr = numpy.array([list(map(int,input().split())) for i in range (0,int(N))])
print(numpy.transpose(arr))
print(arr.flatten())
