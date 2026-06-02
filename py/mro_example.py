class A:
    def hello(self):
        print("A hello")

class B:
    def hello(self):
        print("B hello")

class C(A,B):
    pass

class D(B,A):
    pass

print(C.mro())
c = C()
c.hello()

print(D.mro())
d = D()
d.hello()
