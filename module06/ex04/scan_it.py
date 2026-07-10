#!/usr/bin/env python3

import sys  # dá acesso aos parâmetros passados no terminal (sys.argv)
import re   # módulo de expressões regulares, usado para procurar o texto

# Só continua se o número de parâmetros reais for exatamente 2
if len(sys.argv) - 1 == 2:
    palavra_chave = sys.argv[1]  # a palavra que queremos procurar
    texto = sys.argv[2]          # o texto onde vamos procurar

    # re.escape evita problemas se a palavra tiver caracteres especiais de regex
    # re.findall devolve uma lista com todas as vezes que a palavra aparece
    ocorrencias = re.findall(re.escape(palavra_chave), texto)

    # Se a palavra não aparecer nenhuma vez, mostra "none"
    if len(ocorrencias) == 0:
        print("none")
    else:
        # Mostra quantas vezes a palavra apareceu no texto
        print(len(ocorrencias))
else:
    # Se não forem exatamente 2 parâmetros, mostra "none"
    print("none")
