# def add(a,b,c = 0):
#     return a+b+c
# print(add(1,2))   
# print(add(1,2,3))

# class rect: 
#     def calculateArea(self, length = None, breadth = None):
#         if length !=None and breadth != None:
#             return length * breadth
#         elif length != None:    
#             return length * length
# rectangle = rect()
# print(rectangle.calculateArea(2,3)) 
# print(rectangle.calculateArea(2))       
 
 
# class birds:
#     def category(self):
#         print("This is category of bird")
#     def size(self):
#         print("the size is 6")  
#     def fly(self):
#         print("sorry, i fly")      
# class ostrich(birds):
#     pass
# class sparrow(birds):
#     pass
# class crow(birds):
#     pass
# objcrow=crow()
# objsparrow=sparrow()
# objostrich=ostrich()
# objcrow.category()
# objcrow.size()
# objcrow.fly()
class vehicle:
    def seat(self):
        print("4 seater")
class car1(vehicle):
     pass
class car2(vehicle):
    pass
class truck(vehicle):
    def seat(self):
        print("20 seat")
 
objcar1=car1()
objcar2=car2()
objcar3=truck()
objcar1.seat()
objcar3.seat()
