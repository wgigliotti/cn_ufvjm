#!/usr/bin/env python

import sys
import nltk
import string

from base import Mapper

class TokenizeMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t"):
		super(TokenizeMapper, self).__init__(infile, separator)

		self.punctuation = string.punctuation

	def exclude(self, token):
		return token in self.punctuation

	def normalize(self, token):
		return token.lower()

	def tokenize(self, value):
		for token in nltk.wordpunct_tokenize(value):
			token = self.normalize(token)
			if not self.exclude(token):
				yield token

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			self.emit(key, " ".join(self.tokenize(value)).encode("utf-8"))

if __name__ == "__main__":
	mapper =  TokenizeMapper()
	mapper.map()
