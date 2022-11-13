numbers = [1,2,3,4,5,2,6]
#in the above list, find value 2, if it is present,replace it will 200, only update the first occurance
 
indx = numbers.index(2)
numbers[indx] = 200
print(numbers)
