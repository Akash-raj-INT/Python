def count(lisOfName):

    even = 0
    odd  = 0    
    for i in listOfNum:
        if i % 2 == 0:
            even += 1
    else: 
        odd +=1
    return even, odd


listOfNum = ["atul", "subham"]       

even,odd = count(listOfNum)
print(even)
print(odd)
