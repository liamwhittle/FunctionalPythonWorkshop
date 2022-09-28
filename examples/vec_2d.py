class Vec2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    
    def __eq__(self, other) -> bool:
        return abs(self) == abs(other)
    
    def __leq__(self, other) -> bool:
        return abs(self) <= abs(other)

if __name__ == "__main__":
    a = Vec2D(1.2, 3.2)
    b = Vec2D(4.2, -3.2)
    print(a <= b)
    