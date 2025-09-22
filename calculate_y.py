import sys

def main():
    x = float(input())
    print(type(x))
    y = 2 * x ** 4 + 3
    print(y)


if __name__ == "__main__":
    sys.exit(main())