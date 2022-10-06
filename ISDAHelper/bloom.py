from operator import mod
import numpy as py

def f1(x):
    return (x + 2) % 3

def f2(x):
    return (x-1) % 3

def main():
    while(True):
        num = (input("Number: "))
        if num == "":
            break

        num = float(num)

        print("f1: ", f1(num))
        print("f2: ", f2(num))
        print("\n")


main()