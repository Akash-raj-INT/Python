class student:
    def __init__(self, marks1, marks2, marks3):
        self.web = marks1 
        self.python = marks2
        self.math = marks3
        
    def avgmarks(self):
        print((self.web + self.python + self.math)/3)

    #def getMarks(self):
       # return self.math  #Accessors

   # def setMarks(self, marks):
        #self.math =marks #Mutators    
        
        def classMethodExample(cls):
            return cls.numberofsubject

        def staticMethodExample()
            print("This is an example of static method")    

            

student1 = student(5,4,3)
student2 = student(7,8,9)
student3 = student(1,6,9)

#student1.avgmarks()
#student2.avgmarks()
#student3.avgmarks()

print(student.classMethod())
student.staticMethodExample()






        