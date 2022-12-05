#def fact(n):
    #if n ==0:
        #return 1
# num=fact(5)    
#print(num)

def fact(n):
    if n == 1:
       return 1
    else:
      return n*fact(n-1)
num=fact(6)     
print(num) 



