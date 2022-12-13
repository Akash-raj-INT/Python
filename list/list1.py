l=input("names: ").split(',')
l1=[]
x=0
for i in l:
    l1.append(x)
    x+=2

for i in range(len(l)):
      print(l1[i],l[i])