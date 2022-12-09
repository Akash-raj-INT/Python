#take input of age from 3 people
#determine the oldest and youngest

firstpeople = int(input("Enter age of first people:, "))
secondpeople = int(input("Enter age of second people:, "))
thirdpeople = int(input("Enter age of third people:,"))

if firstpeople > secondpeople and firstpeople > thirdpeople:
    print("Oldest is ", firstpeople)

elif secondpeople > firstpeople and secondpeople > thirdpeople:
    print("Oldest is",  secondpeople)

elif thirdpeople > firstpeople  and thirdpeople > secondpeople:
    print("oldest is", thirdpeople)



