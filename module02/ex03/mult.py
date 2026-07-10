#!/usr/bin/env python3
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number:"))
result = n1 * n2
if result > 0:
    print(f"{n1} x {n2} = {result}")
    print("The result is positive.")
elif result < 0:
    print(f"{n1} x {n2} = {result}")
    print("The result is negative.")
else:
    print(f"{n1} x {n2} = {result}")
    print("The result is positive and negative.")

