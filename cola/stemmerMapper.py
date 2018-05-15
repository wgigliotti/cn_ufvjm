#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer

from base import Mapper

class StemmerMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t"):
		super(StemmerMapper, self).__init__(infile, separator)
		
		self.stemmer = SnowballStemmer("portuguese")


	def exclude(self, token):
		return token in self.stopWords

	def normalize(self, token):
		return token.lower()

	def clear(self, values):
		for token in values:
			yield self.stemmer.stem(token)

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			self.emit(key, " ".join(self.clear(value.split(" "))).encode("utf-8"))

if __name__ == "__main__":
	mapper =  StemmerMapper()
	mapper.map()
