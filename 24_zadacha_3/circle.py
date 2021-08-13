import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def increase(self, k):
        self.radius *= k

    def is_crossing(self, some_circle):
        d = math.sqrt((self.x - some_circle.x) ** 2 + (self.y - some_circle.y) ** 2)
        if d > self.radius + some_circle.radius:
            return 'Круги не пересекаються'
        else:
            return 'Круги пересекаються'

    def info(self):
        return '\nДанные о круге \nх: {x} \ny : {y} \nRadius: {r} \nPerimeter: {p} \nSquare : {s}\n'.format(
            x=self.x,
            y=self.y,
            r=self.radius,
            p=self.perimeter(),
            s=self.square(),
        )
