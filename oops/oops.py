class laptop:

    def config(self):
        print("ASUS", "i7", "1TB")

laptop1 = laptop()        
laptop2 = laptop()

print(id(laptop1))
print(id(laptop2))

laptop1.config()
laptop2.config()

