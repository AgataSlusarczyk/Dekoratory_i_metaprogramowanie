class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punkt(1, 2)
p2 = Punkt(3, 4)
print(p1 + p2)  # (4, 6)
