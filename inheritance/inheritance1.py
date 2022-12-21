class A:
    def __init__(self):
        print("This is method 1")
    def method(self):
        print("this is method 2")    

class B(A):
    def method2(self):
        print("this is method2")
    def __init__(self):
        super().__init__()
        print("this is method")
obj1 = B()        



#class C(B):
  #  def method3(self):
   #     print("this is method3")
