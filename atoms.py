import sys

def main():
    #A
    x1 = int(input("x1:"))
    y1 = int(input("y1:"))
    z1 = int(input("z1:"))

    #B
    x2 = int(input("x2:"))
    y2 = int(input("y2:"))
    z2 = int(input("z2:"))

    print(f"D = {((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5}")
    return 0

if __name__ == "__main__":
        sys.exit(main())