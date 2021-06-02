class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, other):
        return Juice(self.name + ' & ' + other.name, self.capacity + other.capacity)

x = Juice('orange', 6)
y = Juice('mango', 4)
z =x + y
print(z)

#juice maker 