import sys

def main():
    name = input("What is your name? ")
    if name != name.capitalize():
        print("Your name is not grammatically correct!")
    else:
        print(f"Your name is {name}")

    return 0

if __name__ == '__main__':
    sys.exit(main())