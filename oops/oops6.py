class car:
    wheels = 5
    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil



car1=car("Tesla", 10)    
car2=car("BMW", 8)  

car1.wheels = 3
car2.wheels = 4

print(car1.brand, car1.mil, car1.wheels)
print(car2.brand, car2.mil, car2.wheels)
