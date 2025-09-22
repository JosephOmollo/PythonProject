import sys
import math

class Circle:
        units = 'cm'

        def __init__(self, radius,angle = 70, position = (0,0)):
            self.radius = radius
            self.position = position
            self.diameter = 2 * radius
            self.area = 3.142 * self.radius * self.radius
            self.perimeter = 3.142 * (2 * self.radius)
            self.arc_length = self.radius * angle
        def __str__(self):
           return f"I am a circle of size {self.radius}{self.units} located at {self.position}."

def perimeter(circle):
    return 2 * math.pi * circle.radius * circle.arc_length

def main():
        circle = Circle(radius=5)
        print(circle)
        circle.position = (30,-50)
        print(circle)
        circle.radius = 17
        print(str(circle))
        print(f"My diameter is {circle.diameter}{circle.units}")
        print(f"My area is {circle.area}{circle.units}")
        print(f"My perimeter is {circle.perimeter}{circle.units}")
        print(f"My arc_length is {circle.arc_length}{circle.units}")

        return 0

if __name__ == '__main__':
    sys.exit(main())