#!/usr/bin/env python

from base import Reducer

class DocumentFrequencyReducer(Reducer):
	
	def reduce(self):
		for key, values in self:
			total = sum(int(value) for value in values)
			self.emit(key.encode("utf-8"), total)


if __name__ == '__main__':
	reducer = DocumentFrequencyReducer();
	reducer.reduce();

