from collections import namedtuple

N = int(input())

Student = namedtuple('Student', input().split())

students = [Student(*input().split()) for i in range(0,N)]

print(sum([int(el.MARKS) for el in students])/N)
