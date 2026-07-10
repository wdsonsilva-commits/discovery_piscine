#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)

# Guarda só os parâmetros reais, sem o nome do script
parametros = sys.argv[1:]

# Se não houver nenhum parâmetro, mostra "none"
if len(parametros) == 0:
    print("none")
else:
    # Mostra quantos parâmetros foram passados no total
    print("parameters: " + str(len(parametros)))

    # Percorre cada parâmetro (obrigatório usar "for" neste exercício)
    for parametro in parametros:
        # Mostra o parâmetro seguido do seu comprimento (número de caracteres)
        print(parametro + ": " + str(len(parametro)))
