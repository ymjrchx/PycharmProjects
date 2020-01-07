'''
Created on 2018年10月10日

@author: Administrator
'''
# coding=utf-8
class A(object):
    def show(self):
        print("a.show")
class B(A):
    def show(self):
        print("b.show")
class C(A):
    def show(self):
        print("c.show")
        super(C, self).show()
class D(object):
    def show(self):
        print("d.show")
a=A()
a.show()
b=B()
b.show()
c=C()
c.show()
d=D()
d.show()

if __name__ == '__main__':
    pass