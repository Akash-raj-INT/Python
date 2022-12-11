class laptop:

    def __init__(self, name, processor):
        self.name = name
        self.processor = processor   

    def printoutput(self):
        print("My laptop name is: ", self.name, "and the processor is: ", self.processor)    


laptop1 = laptop("Asus", "Ryzen7")        
laptop2 = laptop("HP", "i7")
laptop3 = laptop("Dull","null")

print(id(laptop1))
print(id(laptop2))
print(id(laptop3))

laptop1.printoutput()
laptop2.printoutput()
laptop3.printoutput()


