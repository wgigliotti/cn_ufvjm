import os
import sys
from itertools import groupby
from operator import itemgetter
import config


class Streaming(object):
	
	@staticmethod
	def get_job_conf(name):
		name = name.replace(".", "-").upper()
		return os.environ.get(name)

	def __init__(self, infile=sys.stdin, separator = config.KEY_SEPARATOR):
		self.infile = infile
		self.sep = separator

	def status(self, message):
		sys.stderr.write("reporter:status:{}\n".format(message))

	def counter(self, counter, amount=1, group="Streaming"):
		msg = "reporter:counter:{},{},{}\n".format(group, counter, amount);

	def emit(self, key, value):
		sys.stdout.write("{}{}{}\n".format(key, self.sep, value));

	def read(self):
		for line in self.infile:
			try: 
				yield line.rstrip().decode("utf-8");
			except:
				pass

	def __iter__(self):
		for line in self.read():
			yield line

	def readKeyValue(self):
		for line in self:
			yield line.split(self.sep, 1)


class Mapper(Streaming):
	
	def map(self):
		raise NotImplementedError("Precisa sobrescrever o metodo map");

		


class Reducer(Streaming):
	
	def reduce(self):
		raise NotImplementedError("Precisa sobrescrever o metodo reduce");

	def __iter__(self):
		generator = (line.split(self.sep, 1) for line in self.read())
		for key, val in groupby(generator, itemgetter(0)):
			yield (key, (value[1] for value in val))


