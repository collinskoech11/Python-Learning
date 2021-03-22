celcius = int(input())

def convert(c):
    F = 9/5 * celcius + 32
    return F

farheit = convert(celcius)
print(farheit)
