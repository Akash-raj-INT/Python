class person:
    def __init__(self,name,roll):
        self.name =name
        self.roll=roll

    def detail(self):
        print("my name is: ",self.name, "and the roll no is",self.roll)  

person1 = person("akash", "45")
person2 = person("Shubham", "71")


person1.detail()

person2.detail()
print(id(person1))
print(id(person2))





