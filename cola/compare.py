

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
from sets import Set


def getKeySet(fileName):
	fileObj = open(fileName, "r")
	conjunto = Set();

	for line in fileObj:
		line = line.rstrip().split("\t")
		key = line[0].decode("utf-8")

		if key in conjunto:
			print "Encontrado termo %s ja existente no conjunto no arquivo %s" % (key.encode("utf-8"), fileName)
			
		conjunto.add(key)
	return conjunto

fileA = getKeySet("resultados/01-processados.csv.sort")
fileB = getKeySet("tfReducer.csv")

AnotInB = fileA.difference(fileB)
BnotInA = fileB.difference(fileA)

print AnotInB
print BnotInA




