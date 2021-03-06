"""
Contains all logic for the load keyword which is used to
load a predefined and trained model from a .mlsql file
"""

from pyparsing import Keyword, Word
from ...util.grammar import *

def define_load():
	'''
	Defition of Load Keyword
	:returns pyparsing object
	'''
	filename = Word(everything).setResultsName("fileName")

    #define so that there can be multiple verisions of LOAD
	loadKeyword = Keyword("load", caseless = True).setResultsName("load")

    #Combine to create parsing for load keyword
	load = loadKeyword + filename
	return load
