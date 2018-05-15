#!/usr/bin/env python

from base import Reducer

class TfIdfReducer(Reducer):
	
	def reduce(self):
		totalTokens = 0
		docAtual = None
		soma = []

		for key, values in self:
			
			doc, token = key.split("@", 1)
			if not doc == docAtual:
				if docAtual is not None:
					self.emit(docAtual,  " ".join("%s|%d" % val for val in soma))

				docAtual = doc
				soma = []
				totalTokens = 0

			total = sum(int(value) for value in values)
			soma.append( (token.encode('utf-8'), total) );
			totalTokens = totalTokens + total;


if __name__ == '__main__':
	reducer = TfIdfReducer();
	reducer.reduce();

