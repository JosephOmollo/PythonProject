import sys
import cmath

def main():
    a = complex(input("a: "))
    b = complex(input("b :"))
    c = complex(input("c :"))

    d = b**2 - 4*a*c

    print(f" Discriminant ={d }")
    #roots
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
    print(f"x1: {x1}")
    print(f"x2: {x2}")

    return 0


if __name__ == '__main__':
    sys.exit(main())