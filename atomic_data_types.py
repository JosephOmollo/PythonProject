import sys
from operator import truediv


def main():
    numerical = int(input("int1: "))
    numerical2 = float(input("float2: "))

    if numerical > numerical2:
        print("int1 > float2")
    else:
        print("float2 > int1")



    print(f"{numerical = }")
    print(f"{numerical2 = }")

if __name__ == '__main__':
    sys.exit(main())