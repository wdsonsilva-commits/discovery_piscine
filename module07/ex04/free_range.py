#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)

# Só continua se o número de parâmetros reais for exatamente 2
if len(sys.argv) - 1 == 2:
    numero1 = int(sys.argv[1])  # converte o 1º parâmetro para número
    numero2 = int(sys.argv[2])  # converte o 2º parâmetro para número

    # range(numero1, numero2 + 1) gera todos os números de numero1 até numero2,
    # incluindo o próprio numero2 (por isso o "+ 1", já que range() não inclui
    # o último valor por padrão)
    lista = list(range(numero1, numero2 + 1))

    # Mostra a lista completa
    print(lista)
else:
    # Se não forem exatamente 2 parâmetros, mostra "none"
    print("none")
