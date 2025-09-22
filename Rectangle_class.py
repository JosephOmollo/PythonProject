import sys
import turtle

class Rectangle:
    units = 'cm'
    def __init__(self, width, height, position = (0,0), fill_color = "black", stroke_color = "green"):
        self.width = width
        self.height = height
        self.position = position
        self.fill_color = fill_color
        self.stroke_color = stroke_color

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def bounding_box(self):
        return self.position[0], self.position[1], self.width, self.height

class Canvas:
    def __init__(self, width, height, color = "white"):
        self.width = width
        self.height = height
        self.color = color


def draw_rectangle():
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.done()


def main():
    rectangle =  Rectangle(width=100, height=100)
    print(f"My area is {rectangle.area()}{rectangle.units}")
    print(f"My perimeter is {rectangle.perimeter()}{rectangle.units}")
    print(f"My diagonal is {rectangle.diagonal()}{rectangle.units}")
    print(f"My bounding box is {rectangle.bounding_box()}")

    draw_rectangle()
    return 0

if __name__ == "__main__":
    sys.exit(main())
