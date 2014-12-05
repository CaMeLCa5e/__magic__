#magic.py
from os.path import join

class FileObject:
	"""wrapper for file objects"""

	def __init__(self, filepath='~', filename='textFile.txt'):
		#open a file in filepath - read and write mode
		self.file = open (join(filepath, filename), 'r+')

	def __del__(self):
		self.file.close()
		del self.file

# class Word(str):
# 	"""Class for words, defining comparison on word length"""

# 	def __new__(cls, word):
# 		#need to use __new__ because str is an immutable type.  
# 		#...Need to Init at the creation
	
class Meter(object):
	"""descriptor for a meter"""

	def __init__(self, value=0.0):
		self.value = float(value)
	def __get__(self, instance, owner):
		return self.value
	def __set__(self, instance, value):
		self.value = float(value)

class Foot(object):
	"""Descriptor for a foot"""

	def __get__(self, instance, owner):
		return instance.meter * 3.2808
	def __set__(self, instance, value):
		instance.meter = float(value) / 3.2808

class Distance(object):
	"""Class to represent distance holding two values for feet 
	and meters"""
	meters = Meter()
	foot = Foot()


#Pickle?! 

import pickle

data = {'foo': [1,2,3],
		'bar': ('Hello', 'World'), 
		'baz': True}

# jar = open('data.pkl', 'rb') #Open picked data
# data = pickle.load(pkl_file) #Load it to a var
# print data
# pkl_file.close()


# pkl_file = open('data.pkl', 'rb') #Connect to data
# data = pickle.load(pkl_file) #load into a var
# print data
# pkl_file.close()











