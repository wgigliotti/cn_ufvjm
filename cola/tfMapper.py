#!/usr/bin/env python

import sys
import nltk
import string
from nltk.stem.snowball import SnowballStemmer
import config

from base import Mapper

class TermFrequencyMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator=config.KEY_SEPARATOR):
		super(TermFrequencyMapper, self).__init__(infile, separator)
		

	def map(self):
		
		for pair in self.readKeyValue():
			key = pair[0]
			value = pair[1]
			for token in value.split(config.TOKENS_SEP):
				z = key + config.DOC_TOKEN_SEP + token
				self.emit(z.encode("utf-8"), 1)

if __name__ == "__main__":
	mapper = TermFrequencyMapper()
	mapper.map()
