#!/usr/bin/python3

import sys

def main():
    """Main function
    """
    num_args = len(sys.argv) - 1
    sum = 0

    for i in range(1, num_args + 1):
        sum += int(sys.argv[i])

    print("{:d}".format(sum))

if __name__ == "__main__":
    main()
