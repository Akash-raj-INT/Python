class person:
    def __init__(self):
         self.name ="akash"
         self.age = 18

    def updateName(self,name):
        self.name = name 
    def compareage(self,other):
        if (self.age == other.age):   
            return True
        else:
            return False 
         
                
person1 = person()        
person2 = person()
person1.age=22

 # person2.name ="shub"
  # person1.updateName("ABC") 

#person1.updateName("ABC")
#print(person1.name)
#print(person2.name)
if person1.compareage(person2):
    print("They are of same age")
else:
    print("They are of different age")    
    