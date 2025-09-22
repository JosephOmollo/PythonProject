import sys
import turtle

def draw_pentagon():
    turtle.pencolor("orange")
    turtle.fillcolor("yellow")
# left angle will be 72 as we take 360/5
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.end_fill()
    turtle.write('Panther Ralph')
    turtle.done()


def main():
    draw_pentagon()
    return 0
if __name__ == "__main__":
    sys.exit(main())