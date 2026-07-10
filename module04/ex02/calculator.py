#!/usr/bin/env python3

def clean(n):
    if n == int(n):
        return int(n)
    return n

a = float(input("Give me the first number: "))
b = float(input("Give me the second number: "))

print("Thank you!")
print(f"{clean(a)} + {clean(b)} = {clean(a + b)}")
print(f"{clean(a)} - {clean(b)} = {clean(a - b)}")
print(f"{clean(a)} / {clean(b)} = {clean(a / b)}")
print(f"{clean(a)} * {clean(b)} = {clean(a * b)}")
