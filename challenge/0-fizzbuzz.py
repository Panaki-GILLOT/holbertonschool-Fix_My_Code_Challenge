#!/usr/bin/python3
"""
FizzBuzz
"""
if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        print("Usage: {} number".format(argv[0]))
        exit(1)

    n = int(argv[1])
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
    print()
