def addtwice(func, arg):
    return func(func(arg))

def adddouble(x):
    return x+5

print(addtwice(adddouble, 10))