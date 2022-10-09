import numpy

N, M = input().split()

a = numpy.array([list(map(int, input().split())) for i in range (0,int(N))])
b = numpy.array([list(map(int, input().split())) for i in range (0,int(N))])

print(numpy.add(a, b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(a%b)
print(a**b)
