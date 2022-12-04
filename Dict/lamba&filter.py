from functools import reduce
def isEven(i):
    return i%2==0


list1 = [3,2,8,16,11,34,17]
output = list(filter(isEven,list1))
output = list(filter(lambda i : i>15 ,list1))
print(output)

output2 = list((lambda i: i**2, list1))
print(output2)
output3 = reduce(lambda a,b:a+b,list1)
print(output3)