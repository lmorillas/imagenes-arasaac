# coding: utf-8


import mysql.connector
import re
import json


cnx = mysql.connector.connect(user='root', password='example',
                              host='127.0.0.1',
                              port="3307",
                              database='saac')

cursor = cnx.cursor()


cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")

def limpia(s):
    return re.findall(r'[^!,.?":;]+', s)[0]

def separa_campos(texto):
    '''Devuelve lista de tags. Están separados por {} en la bd
    '''
    try:
            _texto = texto.encode('1252').decode('utf-8')
    except:
        try:
            _texto = texto.encode('latin1').decode('utf-8')
        except:
            print('ERROR ENCODING', texto)
            return []
    try:
        return [limpia(c.strip()) for c in re.findall('{(.*?)}', _texto) if c.strip()]
    except:
        print ('ERROR EXTRACCION TAGS', texto)
        return []



sqlen = '''SELECT imagenes.imagen, GROUP_CONCAT(traducciones.traduccion)
FROM imagenes,palabras, palabra_imagen, traducciones WHERE
imagenes.id_imagen = palabra_imagen.id_imagen AND
palabra_imagen.id_palabra = palabras.id_palabra AND
palabras.id_palabra = traducciones.id_palabra AND
traducciones.id_idioma = '7'
GROUP BY imagenes.imagen'''


sqles = '''SELECT imagenes.imagen as imagen, GROUP_CONCAT(palabras.palabra) as palabras, 
imagenes.tags_imagen as tags
FROM imagenes,palabras, palabra_imagen WHERE
imagenes.id_imagen = palabra_imagen.id_imagen AND
palabra_imagen.id_palabra = palabras.id_palabra
GROUP BY imagenes.imagen'''



cursor.execute(sqles)
ims = {}

for im, kw, tags in cursor.fetchall():
    d = {'url': im}
    d['name'] = dict([('es', [dict([('keyword', k)]) for k in kw.split(',')])])
    if tags:
        _tags = separa_campos(tags)
        if _tags:
            d['tags'] = dict([('es', _tags)])
    ims[im] = d

cursor.execute(sqlen)

for im, kw in cursor.fetchall():
    if kw:
        ims[im]['name']['en'] = [dict([('keyword', k)]) for k in kw.split(',')]

cnx.close()

json.dump(list(ims.values()), open('lista_imagenes.json', 'w'))
