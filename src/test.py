# coding: utf-8

'''
https://stackoverflow.com/questions/25615741/how-to-use-the-spanish-wordnet-in-nltk

http://python.6.x6.nabble.com/attachment/2743017/0/Python%252520Text%252520Processing%252520with%252520NLTK%2525202.0%252520Cookbook.pdf
https://www.pybonacci.org/2015/11/24/como-hacer-analisis-de-sentimiento-en-espanol-2/


http://www.tsc.uc3m.es/~miguel/MLG/adjuntos/NLTK.pdf
'''

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

tokenizer=nltk.data.load(‘tokenizers/punkt/spanish.pickle’)

frase='''Trabajo  básicamente en  el  apartado    de  la  comedia.    Me  gustaría    
estar   en  Diseño  de  Programación,   pero    por desgracia   aprobé  el  bachillerato.'''

sent_tokenize(frase)
tokenizer=nltk.data.load('tokenizers/punkt/spanish.pickle')
tokenizer.tokenize(frase)
word_tokenize(frase)

spanish_stemmer=SnowballStemmer("spanish")
tokens = nltk.word_tokenize(frase)

[spanish_stemmer.stem(t) for t in tokens]



