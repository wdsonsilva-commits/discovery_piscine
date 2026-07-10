#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)

# Só continua se o número de parâmetros reais for exatamente 1
if len(sys.argv) - 1 == 1:
    texto = sys.argv[1]  # guarda a string passada como parâmetro

    # count() conta quantas vezes o caractere "z" aparece na string
    quantidade_de_z = texto.count("z")

    # Se não houver nenhum "z", mostra "none"
    if quantidade_de_z == 0:
        print("none")
    else:
        # "z" * quantidade_de_z repete o caractere "z" o número de vezes necessário
        # (ex: 3 ocorrências vira "zzz"), tudo numa única linha
        print("z" * quantidade_de_z)
else:
    # Se não for exatamente 1 parâmetro, mostra "none"
    print("none")
