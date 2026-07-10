#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)


# Define a função "downcase_it", que recebe um parâmetro chamado "texto"
def downcase_it(texto):
    # Devolve o texto em minúsculas
    return texto.lower()


# Guarda só os parâmetros reais, sem o nome do script
parametros = sys.argv[1:]

# Se não houver nenhum parâmetro, mostra "none"
if len(parametros) == 0:
    print("none")
else:
    # Percorre cada parâmetro e aplica a função downcase_it a cada um
    for parametro in parametros:
        print(downcase_it(parametro))
