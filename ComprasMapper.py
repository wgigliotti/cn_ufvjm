#!/usr/bin/env python

import sys
import nltk
import string

from base import Mapper

class ComprasMapper(Mapper):
	
	def __init__(self, infile=sys.stdin, separator="\t"):
		super(ComprasMapper, self).__init__(infile, separator)

		
	def map(self):
		for line in self:
			line = line.split("\t")
			valor = line[2].rstrip()
			if valor:
				if float(valor) > 0:
					self.emit(line[3], valor)
			


if __name__ == "__main__":
	mapper =  ComprasMapper()
	mapper.map()
