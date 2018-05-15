#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer

from base import Mapper
import math


class TfIdfMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t", dfFile="resultados/03-document-frequency.csv", numeroDocFile = "resultados/numeroDocumentos.csv"):
		super(TfIdfMapper, self).__init__(infile, separator)
		
		self.df = self.readFile(dfFile)
		self.D = self.readDFile(numeroDocFile)

	def readDFile(self, numeroDocFile):
		fileObj = open(numeroDocFile)
		line = fileObj.read()
		line = line.rstrip().split(" ");

		return float(line[0])


	def readFile(self, dfFile):
		fileObj = open(dfFile, "r")
		df = {}

		for line in fileObj:
			line = line.rstrip().split("\t")
			df[line[0].decode("utf-8")] = float(line[1])
	
		return df	

	def tfIdf(self, totalTokens, token):
		term, tf = token.split("|")
		if term in self.df:
			return  (term.encode("utf-8"), (float(tf)/totalTokens)*math.log(self.D/self.df[term]))
		
	def computeLen(self, tfIdf):
		length = sum(map(lambda x: x[1]*x[1], tfIdf))
		return math.strq(length)
		
	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			value = value.split(" ", 1)

			totalTokens = float(value[0])
			tokens = value[1]

			tfIdf =  map(lambda x: self.tfIdf(totalTokens, x), tokens.split(" "))
			length = math.sqrt(sum(map(lambda x: x[1]*x[1], tfIdf)))

			tfIdfNorm = map(lambda x: "%s|%f" % (x[0], x[1]/length), tfIdf)

			self.emit(key.encode("utf-8"), " ".join(tfIdfNorm))

if __name__ == "__main__":
	mapper = TfIdfMapper()
	mapper.map()
