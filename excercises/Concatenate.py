import numpy

N, M, P = input().split()
array_1 = numpy.array([list(map(int, input().split())) for _ in range (0,int(N))])
array_2 = numpy.array([list(map(int, input().split())) for _ in range (0,int(M))])
print(numpy.concatenate((array_1, array_2)))
