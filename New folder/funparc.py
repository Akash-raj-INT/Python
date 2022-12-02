def name(x):
    return lambda a : a + x
    
num = name(15)
print(num(10))