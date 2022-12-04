def div(a,b):
    print(a/b)

def new_div(func):
    def innerfunc(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)    
    return innerfunc        

div(4,2)  