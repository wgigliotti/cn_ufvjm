import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import numpy as np
from base import Mapper
from contexto import Contexto
import math

class Classificacao(Mapper):
	def __init__(self, infile=sys.stdin, separator="\t", simFile="resultados/tfidfSim.csv", naoFile="resultados/tfidfNao.csv"):
		super(Classificacao, self).__init__(infile, separator)
		self.contexto = Contexto()
		self.sim = self.loadFile(simFile)
		self.nao = self.loadFile(naoFile)

	def getKeyValor(self, arquivoInput):
		for line in arquivoInput:
			yield line.split("\t", 1)

	def loadFile(self, arquivoTreino):
		arquivoTreino = open(arquivoTreino, "r")
		return self.contexto.loadData(self.getKeyValor(arquivoTreino))

	def map(self):
		verificacao = self.contexto.loadData(self.readKeyValue())
		respSim = verificacao * self.sim.T
		respNao = verificacao * self.nao.T
	
		for x in range(0, 12):
			print ("============= %d" % (x))
			maxS = max(respSim.getrow(x).toarray()[0])
			maxN = max(respNao.getrow(x).toarray()[0])
			print ("%f vs %f"%(maxS, maxN))
			if maxS > maxN:
				print("Sim")
			else:
				print("Nao")

if __name__ == "__main__":
	mapper = Classificacao()
	mapper.map()
	
			
