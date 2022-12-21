# creat a class without using method and function in python
class MyClass:
    attribute1 = "attribute1"
    attribute2 = "attribute2"
my_object = MyClass()
print(my_object.attribute1)
class MyClass:
    attribute1 = "attribute1"
    attribute2 = "attribute2"
    
    def my_method(self):
        print("This is a method of MyClass.")
my_object = MyClass()
my_object.my_method()
