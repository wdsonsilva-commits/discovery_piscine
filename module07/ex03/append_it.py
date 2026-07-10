#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)

# Guarda só os parâmetros reais, sem o nome do script
parametros = sys.argv[1:]

# Se não houver nenhum parâmetro, mostra "none"
if len(parametros) == 0:
    print("none")
else:
    # Percorre cada parâmetro passado
    for parametro in parametros:
        # find() devolve a posição onde "ism" aparece, ou -1 se não encontrar.
        # Aqui verificamos se a palavra JÁ TERMINA em "ism":
        # a posição de "ism" tem de ser exatamente o fim da palavra.
        posicao = parametro.find("ism")
        termina_em_ism = posicao != -1 and posicao == len(parametro) - 3

        # Se já terminar em "ism", é ignorado (skip); senão, mostra com "ism" no fim
        if not termina_em_ism:
            print(parametro + "ism")
