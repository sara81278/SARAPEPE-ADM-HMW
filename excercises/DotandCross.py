import numpy

N = int(input())
A = numpy.array([list(map(int, input().split())) for i in range (0,N)])
B = numpy.array([list(map(int, input().split())) for i in range (0,N)])

print(numpy.dot(A, B))

