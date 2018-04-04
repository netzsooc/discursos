#!/usr/bin/env python

"""Programa diseñado para sacar cuentas de las cosas de los candidatos
"""

__author__ = 'NetzSoOc'
__date__ = '2018-04-03'


import json
import os
from collections import defaultdict


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
        Palabra más representativa: {mas_comun}
        Top-10 palabras más representativas: {top_ten}
        """.format(oraciones=num_oraciones, palabras=num_palabras,
        mas_comun=mas_comun, top_ten=top_ten,
        promedio=num_palabras/num_oraciones, prom_palabra=prom_palabra)
        )

class Proceso(object):
    def __init__(self, etiquetado):
        self.num_oraciones = len(etiquetado)
        mis_palabras = self.mide_palabras(etiquetado)
        self.num_palabras = len(mis_palabras)
        self.prom_palabra = sum(mis_palabras)/self.num_palabras
        self.mas_comun = self.palabras_comunes(etiquetado)[0]
        self.top_ten = self.palabras_comunes(etiquetado)[:10]
    
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
        for oracion in etiquetado:
            oracion
            pass
        return [0]


if __name__ == '__main__':
    main()