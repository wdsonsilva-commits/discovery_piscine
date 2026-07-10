#!/usr/bin/env python3

import sys

parametros = sys.argv[1:]

#so continua se houver pelo menos 2 parametros
if len(parametros) >= 2: 
    #[::-1] inverte a ordem da lista
    parametros_invertidos = parametros [::-1]
    #Percorre a lista j'a invertida e mostra cada parametro numa linha

    for parametro in parametros_invertidos:
        print(parametro)
else:
    #se houver menos de 2 parametros, mostra "nome"
    print("nome")

