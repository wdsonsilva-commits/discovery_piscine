#!/usr/bin/env python3
 
import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)
 
# Só continua se o número de parâmetros reais for exatamente 1
if len(sys.argv) - 1 == 1:
    parametro = sys.argv[1]  # guarda o parâmetro passado
 
    # Pede ao utilizador para escrever uma palavra, e guarda o que ele escrever
    resposta = input("What was the parameter? ")
 
    # Compara a resposta do utilizador com o parâmetro original
    if resposta == parametro:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    # Se não for exatamente 1 parâmetro, mostra "none"
    print("none")
