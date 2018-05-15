#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer

from base import Mapper
import math


class DocCluster(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t", clusterFile="resultados/05-clusters.txt"):
		super(DocCluster, self).__init__(infile, separator)
		self.readClusters(clusterFile)

	def readClusters(self, clusterFile):
		fileObj = open(clusterFile)
		self.docToCluster = {}
		count = 1
		for line in fileObj:
			line = line.rstrip().decode("utf-8")
			for document in line.split(" "):
				self.docToCluster[document] = count
			count = count+1

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0].decode("utf-8")
			value = pair[1]
			cluster = self.docToCluster[key]

			self.emit(cluster, ("%s %s" % (key, value)).encode("utf-8"))

if __name__ == "__main__":
	mapper = DocCluster()
	mapper.map()
