import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import numpy as np

class Contexto(object):
	
	def __init__(self):
		self.vocabulary = {}
			
		
	def loadData(self, valores):
		indptr = [0]
		indices = []
		data = []

		for pair in valores:
			tokens = pair[1]
			for term, tfidf in map(lambda x: x.split("|"), tokens.split(" ")):
				index = self.vocabulary.setdefault(term, len(self.vocabulary))
				indices.append(index)
				data.append(float(tfidf))

			indptr.append(len(indices))
		
		matrix = csr_matrix((data, indices, indptr))
		return csr_matrix((data, indices, indptr), shape=(matrix.shape[0], 30000))

