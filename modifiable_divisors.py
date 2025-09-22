import sys

def get_joint_divisors():
    n = int(input("n:  "))
    m = int(input("m:  "))
    return n,m

def main():
    y = int(input("y:  "))
    n,m = get_joint_divisors()
    joint_divisors = list()
    other = list()

    for number in range(y):
        if number % n == 0 and number % m == 0:
            joint_divisors.append(number)
        else:
            other.append(number)

            print(f"{joint_divisors = }")
            print()
            print(f"{other = }")

    return 0

if __name__ == '__main__':
    sys.exit(main())