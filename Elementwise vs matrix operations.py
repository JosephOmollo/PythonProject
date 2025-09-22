import sys

def main():
    #A = [
    # [a,b],
    # [c,d];
    # ]
    a11 = int(input("a11: "))
    a12 = int(input("a12: "))
    a21 = int(input("a21: "))
    a22 = int(input("a22: "))

    A = [
        [a11, a12],
        [a21, a22],
    ]

    #B
    b11 = int(input("b11: "))
    b12 = int(input("b12: "))
    b21 = int(input("b21: "))
    b22 = int(input("b22: "))

    B = [
        [b11, b12],
        [b21, b22],
    ]

    # Elementwise multiplication
    # [a11 * b11, a12 * b12]
    # [a21 * b21, a22 * b22]

    Elementwise_multiplication =[
        [a11 * b11, a12 * b12],
        [a21 * b21, a22 * b22],
    ]
    # Elementwise addition
    # [a11 + b11, a12 + b12],
    # [a21 + b21, a22 + b22],

    Elementwise_addition = [
        [a11 + b11, a12 + b12],
        [a21 + b21, a22 + b22],
    ]
    # Matrix product = [
    #     [a11 * b11 + a12 * b21, a11 * b12 + a12 * b22],
    #     [a21 * b11 + a22 * b21, a21 * b12 + a22 * b22],
    # ]

    Matrix_product =[
        [(a11 * b11) + (a12 * b21), (a11 * b12) + (a12 * b22)],
        [(a21 * b11) + (a22 * b21), (a21 * b12) + (a22 * b22)],
    ]

    print(f"A: {A}")
    print(f"B: {B}")
    print(f"Elementwise multiplication: {Elementwise_multiplication}")
    print(f"Elementwise addition: {Elementwise_addition}")
    print(f"Matrix product: {Matrix_product}")

    return 0

if __name__ == "__main__":
    sys.exit(main())