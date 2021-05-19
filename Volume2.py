import math

def Vol(r, h):
    Volume = math.pi * r * r * h
    return Volume

print("The volume of the cylinder is: " + str(Vol(7, 7)))
