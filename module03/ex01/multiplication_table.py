#!/usr/bin/env python3
number = int(input("Enter a number\n"))
contador = 0

while contador <=9:
        resultado = contador * number
        print(f"{contador} x {number} = {resultado}")
        contador +=1 

#outra opcao 
"""number = int(input("Enter a number\n"))
for i in range(0, 10)
    result = number * i
    print(f"{i} x {number} = {result}")"""
