import sys
import turtle

def draw_triangle():
    print("Drawing a triangle")
    turtle.pencolor("purple")
    turtle.fillcolor("green")

    turtle.begin_fill()
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.end_fill()
    turtle.done()
def main():
    draw_triangle()

    return 0

if __name__ == "__main__":
    sys.exit(main())