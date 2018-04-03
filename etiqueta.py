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
    archivo = {'file': open(raiz + archivo, mode='rb')}
    params = {'outf': outf, 'format': formato}
    url = 'http://www.corpus.unam.mx/servicio-freeling/analyze.php'
    req = requests.post(url, files=archivo, params=params)
    return req.json()

if __name__ == '__main__':
    main()