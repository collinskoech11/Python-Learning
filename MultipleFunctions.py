def addtwice(func, arg):
    return func(func(arg))

def adddouble(x):
    return x+x

print(addtwice(adddouble, 10))