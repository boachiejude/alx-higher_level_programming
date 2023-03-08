#!/usr/bin/python3

def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            print("{:c}".format(ord(string[i]) - 32), end="")
        else:
            print("{:c}".format(ord(string[i])), end="")
