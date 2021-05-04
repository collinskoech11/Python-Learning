class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(3, 5)
second = Vector2D(10, 7)
final = first + second
print(final.x)
print(final.y)
        