#!/usr/bin/env python

"""Este programa toma los discursos en formato txt y regresa un JSON
etiquetado para cada uno de ellos

Returns:
    json -- archivo en formato json de los discursos. Es una lista de listas
    donde cada una es a su vez una lista de objetos. Cada objeto es una
    palabra etiquetada usando el servicio de freeling hospedado en:
    http://www.corpus.unam.mx/servicio-freeling.
    El objeto palabra contiene el siguiente formato:
        'token': str -- la cadena como aparece en el texto
        'lemma': str -- el lema del token (puede tener errores)
        'tag': str -- etiqueta en formato eagles que contiene información
               morfosintáctica de la palabra.
        'prob': str -- cadena de un flotante  entre 0 y 1 que contiene la
                certeza de la etiqueta asignada.
"""

__author__ = 'NetzSoOc'
__date__ = '2018-04-03'

import os
import json
import requests


def main():
    raiz = 'Datos/Crudos/'
    for archivo in os.listdir(raiz):
        etiquetado = etiqueta_archivo(raiz, archivo)
        with open('Datos/Etiquetados/{}'.format(archivo), mode='w', 
                  encoding='utf8') as f:
            json.dump(etiquetado, f)


def etiqueta_archivo(raiz, archivo, outf='tagged', formato='json'):
    """Utiliza la API de http://www.corpus.unam.mx/servicio-freeling para
    tokenizar y etiquetar un texto.
    
    Arguments:
        raiz {str} -- directorio raiz donde se encuentra el archivo que se va
                      a etiquetar.
        archivo {str} -- archivo que se va a etiquetar
    
    Keyword Arguments:
        outf {str} -- tipo de etiquetado que se desea, puede ser 'tagged',
                      'parsed', 'dep'. (default: {'tagged'})
        formato {str} -- formato de la respuesta, puede ser 'plain', 'json',
                         'html'. (default: {'json'})
    
    Returns:
        json -- objeto tipo json que contiene el documento etiquetado.
    """
    archivo = {'file': open(raiz + archivo, mode='rb')}
    params = {'outf': outf, 'format': formato}
    url = 'http://www.corpus.unam.mx/servicio-freeling/analyze.php'
    req = requests.post(url, files=archivo, params=params)
    return req.json()

if __name__ == '__main__':
    main()