import sys

def main():
    x1=float(input("x1: "))
    x2=float(input("x2: "))
    y1=float(input("y1: "))
    y2=float(input("y2: "))
    z1=float(input("z1: "))
    z2=float(input("z2: "))
    print(f"D squared = {((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**2 }")
    return 0
if __name__ == "__main__":
    sys.exit(main())