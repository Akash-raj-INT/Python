a = int(input("enter the length of first side"))
b = int(input("enter the length of second side"))
c = int(input("enter the length of third side"))

p = (a+b+c)
s = p/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("are of triangle is:",area)
print("perimeter of triangle is",p)
print("semi perimeter of triangle is:",s)
