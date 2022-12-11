class person:
    def __init__(self):
         self.name ="akash"
         self.age = 18
    def updateName(self,name):
        self.name = name     
person1 = person()        
person2 = person() 

person1.updateName("ABC")
print(person1.name)
print(person2.name)
