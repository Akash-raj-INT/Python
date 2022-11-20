#write a program to accept a number from a user 
#calculate the sum of all the numbers from
# 1 to given number

#eg user input 10
#output shold be 55
# 1+2+3+4+5+6+7+8+9+10

count = 0
user = int(input("enter the number"))
for i in range(1, user+1):
    count+=i 
    print("total sum is : ", count)



