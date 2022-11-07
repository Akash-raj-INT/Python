# creat a function in suach a way that we can pass any number of argument to this and it should display each argument's value.

def name(*args):
   for i in args:
      print(i)
   print(*args)   

name("akash", "raj", "from", "bihar")    