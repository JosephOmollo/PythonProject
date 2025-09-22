import sys

def main():
    my_list = list()
    my_list.append(1)
    my_list.append(2)
    my_list.append('hey')
    my_list.insert(0, 10)
    my_list [0:3]

    print(my_list)
    print(my_list[0])
    print(my_list[0:3])

    return 0

if __name__ == "__main__":
    sys.exit(main())