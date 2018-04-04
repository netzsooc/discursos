#!/usr/bin/env python

"""Programa diseñado para sacar cuentas de las cosas de los candidatos
"""

__author__ = 'NetzSoOc'
__date__ = '2018-04-03'


import json
import os
from math import log
from collections import defaultdict, Counter


def main():
    raiz = 'Datos/Etiquetados/'
    for archivo in os.listdir(raiz):
        with open(raiz + archivo, 'r', encoding='utf8') as f:
            mi_json = json.load(f)
        texto = Proceso(mi_json)
        print(archivo)
        num_oraciones = texto.num_oraciones
        num_palabras = texto.num_palabras
        mas_comun = texto.mas_comun
        top_ten = texto.top_ten
        prom_palabra = texto.prom_palabra

        print("""
        Cantidad de oraciones: {oraciones}
        Cantidad de palabras: {palabras}
        Promedio de oracion: {promedio}
        Promedio de palabra: {prom_palabra}
        Palabra más representativa: {mas_comun}\
        """.format(oraciones=num_oraciones, palabras=num_palabras,
        mas_comun=mas_comun, promedio=num_palabras/num_oraciones,
        prom_palabra=prom_palabra)
        )
        print('        Top-10 palabras representativas:')
        for palabra in top_ten:
            print('                {}'.format(palabra[0]))
        print()


class Proceso(object):
    def __init__(self, etiquetado):
        self.num_oraciones = len(etiquetado)
        mis_palabras = self.mide_palabras(etiquetado)
        comunes = self.palabras_comunes(etiquetado)
        self.num_palabras = len(mis_palabras)
        self.prom_palabra = sum(mis_palabras)/self.num_palabras
        self.mas_comun = comunes.most_common(1)[0][0]
        self.top_ten = comunes.most_common(10)
    
    def mide_palabras(self, etiquetado):
        longitud = []
        for oracion in etiquetado:
            for w in oracion:
                longitud.append(len(w['token']))
        return longitud
    
    def cuenta_palabras(self, etiquetado):
        cuenta = 0
        for oracion in etiquetado:
            cuenta += len(oracion)
        return cuenta
    
    def palabras_comunes(self, etiquetado):
        target_tags = ('A', 'R', 'PP', 'N', 'VM')
        palabras = Counter()
        for oracion in etiquetado:
            mis_palabras = [w['lemma'] for w in oracion if
                            w['tag'].startswith(target_tags)]
            palabras += Counter(mis_palabras)
        return palabras
        


if __name__ == '__main__':
    main()