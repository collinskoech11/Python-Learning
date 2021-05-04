class animals:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(animals):
    def mew(self):
        print('meaw!')

class Dog(animals):
    def bark(self):
        print('woof!')

fido = Cat("lexy", "white")
print(fido.name)
fido.mew()

dido = Dog("daisy", "black")
print(dido.name)
print(dido.color)
dido.bark()
