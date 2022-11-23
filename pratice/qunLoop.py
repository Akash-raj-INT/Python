#write a program to display only those numbers
#from a list that satisfy following condition

#number must be divisible by 5
#if the number is greater than 150, then skip it ans move to nect number
#if the number is greater than 500, stop yje loop
#number = [12, 75, 150, 180, 145]

num = [12, 75, 150, 180, 145]
for i in num:
    
      if i >150:
        continue
print(i)


