import math

radius = float(input('enter radius'))
height = float(input('enter height'))

def Vol():
    Volume = math.pi * radius * radius * height
    return Volume

print(Vol())
