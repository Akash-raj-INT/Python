class A:
    def method1(self):
        print("This is method 1")

class B(A):
    def method2(self):
        print("this is method 2")

class C(B):
    def method3(self):
        print("this is method3")
class D(C):
    def method4(self):
        print("this is method4")        
objA = A()
objB = B()
objC = C()
objD = D()
objD.method4()
print(objD)        
