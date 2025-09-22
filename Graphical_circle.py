import math
import sys
import turtle


class Circle:
    units = 'cm'
    def __init__(self, radius, position = (0,0), fill_color = "red", stroke_color = "blue"):
        self.radius = radius
        self.position = position
        self.fill_color = fill_color
        self.stroke_color = stroke_color

    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def bounding_box(self):
        return self.position[0] - self.radius, self.position[1] - self.radius, self.position[0] + self.radius, self.position[1] + self.radius

class Text:
    def __init__(self, text, position = (0,0), color = "purple", font=("Arial", 14, "normal")):
        self.text = text
        self.position = position
        self.color = color
        self.font = font

    def draw(self, pen):
        """Draw the text using a turtle.Turtle() pen."""
        pen.penup()
        pen.goto(self.position)
        pen.pencolor(self.color)
        pen.write(self.text, align="center", font=self.font)
        pen.penup()

class Canvas:
    def __init__(self, width, height, color = "white"):
        self.width = width
        self.height = height
        self.color = color

signature = Text('Panther Ralph', (50, 100), color="red")
print(type(signature))




def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()
    signature.draw(pen)
    turtle.done()


def main():
    circle = Circle(radius = 100, position = (50, 70))
    print(f"My area is {circle.area()}{circle.units}")
    print(f"My perimeter is {circle.perimeter()}{circle.units}")
    print(f"My bounding box is {circle.bounding_box()}")
    print({signature})

    draw_circle()

    return 0

if __name__ == '__main__':
    sys.exit(main())