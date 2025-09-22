import sys

def main():
    a11 = int(input("a11: "))
    a12 = int(input("a12: "))
    a21 = int(input("a21: "))
    a22 = int(input("a22: "))

    A = [
    [a11, a12],
    [a21, a22],
    ]
    print(f"A: {A}")


    return 0

if __name__ == "__main__" :
    sys.exit(main())