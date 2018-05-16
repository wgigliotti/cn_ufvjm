#!/usr/bin/env python

from base import Reducer
import config

class TermFrequencyReducer(Reducer):
	
	def reduce(self):
		totalTokens = 0
		docAtual = None
		soma = []
		cont = 0

		for key, values in self:
			
			doc, token = key.split(config.DOC_TOKEN_SEP, 1)
			if not doc == docAtual:
				if docAtual is not None:
					self.emit(docAtual, "%d %s" % (totalTokens, " ".join("%s|%d" % val for val in soma)))

				docAtual = doc
				soma = []
				totalTokens = 0
				cont = cont + 1



			total = sum(int(value) for value in values)
			soma.append( (token.encode('utf-8'), total) );
			totalTokens = totalTokens + total;

		if docAtual is not None:
			self.emit(docAtual, "%d %s" % (totalTokens, " ".join("%s|%d" % val for val in soma)))

if __name__ == '__main__':
	reducer = TermFrequencyReducer();
	reducer.reduce();

