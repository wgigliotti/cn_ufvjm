#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer

from base import Mapper

class DocumentFrequencyMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t"):
		super(DocumentFrequencyMapper, self).__init__(infile, separator)
		

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			value = value.split(" ", 1)

			totalTokens = value[0]
			tokens = value[1]

			for token in tokens.split(" "):
				token = token.split("|")
				self.emit(token[0].encode("utf-8"), 1)

if __name__ == "__main__":
	mapper = DocumentFrequencyMapper()
	mapper.map()
