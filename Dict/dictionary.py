#myDictionary = {
    #"name":"Akash",
    #"age": 18,
    #"class": "KOC28",
    #"CGPA": "10"
#}

#print(myDictionary)

#print(len(myDictionary))

#a=myDictionary.get("name")
#print(a)

#print(myDictionary.keys())

#print(myDictionary.values())

#z =myDictionary["age"]=18
#print(z)

#print(myDictionary.update({"age":18}))

#print(myDictionary.pop("CGPA"))

myDictionary ={
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python": 90,
                "web" : 95
            }
        }
    } 
}

print(myDictionary["class" ]["student"]["marks"]["web"])



