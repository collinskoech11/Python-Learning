class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("meaw!")

class Dog(Animal):
    def bark(self):
        print('woof!')

fido = Cat('daphne', 'white')
print(fido.name)
print(fido.color)
fido.purr()