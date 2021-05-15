class table:
    def __init__(self, name, last):
        self.name = name
        self.last = last
    
    def bark(self):
        print('woof')

final = table("diana","ndinda")
print(final.last)
final.bark()
print(final.bark)          