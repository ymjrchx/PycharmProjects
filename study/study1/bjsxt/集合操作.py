# help('sys')


class A(object):
    i = 10


a = A()
print(a.i)
a.i = 20
print(a.i)
print(A.i)
del a.i
setattr(a, 'i', 30)
print(a.i)
print(A.i)
dir()
import math
print(math.sqrt(8) %1)
print(issubclass(A,A))
if __name__ == '__main__':
    pass
