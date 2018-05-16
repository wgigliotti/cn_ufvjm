#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import numpy as np

from base import Mapper
import math


class Mastiga(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t", dfFile="resultados/document_frequency.csv", numeroDocFile = "resultados/numeroDocumentos.csv"):
		super(Mastiga, self).__init__(infile, separator)
		
		self.df = self.readFile(dfFile)


	def readFile(self, dfFile):
		fileObj = open(dfFile, "r")
		df = {}

		for line in fileObj:
			line = line.rstrip().split("\t")
			df[line[0].decode("utf-8")] = float(line[1])
	
		return df	

	def merge(self, origem, destino, clusters):
		if origem == destino:
			return

		if origem > destino:
			self.merge(destino, origem, clusters)
			return

		if clusters[origem]['redirect'] >= 0:
			self.merge(clusters[origem]['redirect'], destino, clusters)
		else:
			if clusters[destino]['redirect'] >= 0:
				self.merge(origem, clusters[destino]['redirect'], clusters)
			else :
				clusters[destino]['values'] = clusters[destino]['values'].union(clusters[origem]['values'])

		clusters[origem]['redirect'] = destino
		clusters[origem]['values'] = {}
		
	def map(self):
		docs = []
		clusters = []
		indptr = [0]
		indices = []
		data = []
		vocabulary = {}
		
		for pair in self.readKeyValue():
			key = pair[0]
			tokens = pair[1]
			docs.append(key)
			clusters.append({'redirect': -1, 'values': {key}})

			for term,tfidf in map(lambda x: x.split("|"), tokens.split(" ")):
				index = vocabulary.setdefault(term, len(vocabulary))
				indices.append(index)
				data.append(float(tfidf))
				
			indptr.append(len(indices))

		matrix = csr_matrix((data, indices, indptr))
	
		produtos = matrix * (matrix.T)

		produtos = produtos.toarray()

		
		i = 0
		while i < len(produtos):
			j = i + 1
			while j < len(produtos):
				if(produtos[i][j] > 0.5):
					self.merge(j,i,clusters)

				j=j+1
			i=i+1

		for cluster in clusters:
			if cluster['redirect'] == -1:
				print " ".join(cluster['values'])

			

if __name__ == "__main__":
	mapper = Mastiga()
	mapper.map()
