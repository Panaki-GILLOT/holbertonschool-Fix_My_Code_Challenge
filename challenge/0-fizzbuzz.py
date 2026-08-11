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
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(' '.join(result))
