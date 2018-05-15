#!/usr/bin/env python

import sys
import nltk
import string

from base import Mapper

class StopWordsMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t", minLen = 3):
		super(StopWordsMapper, self).__init__(infile, separator)

		self.minLen = 3

		self.stopWords = nltk.corpus.stopwords.words("portuguese")

	def exclude(self, token):
		return token in self.stopWords or len(token) < self.minLen

	def clear(self, values):
		for token in values:
			if not self.exclude(token):
				yield token

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			self.emit(key, " ".join(self.clear(value.split(" "))).encode("utf-8"))

if __name__ == "__main__":
	mapper =  StopWordsMapper()
	mapper.map()
