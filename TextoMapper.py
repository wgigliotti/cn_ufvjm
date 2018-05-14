#!/usr/bin/env python

import sys
import nltk
import string

from base import Mapper

class TextoMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t"):
		super(TextoMapper, self).__init__(infile, separator)

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
		
		for line in self:
			for token in self.tokenize(line):
				self.emit(token.encode("utf-8"), 1) 

if __name__ == "__main__":
	mapper =  TextoMapper()
	mapper.map()
