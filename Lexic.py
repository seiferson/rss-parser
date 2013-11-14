#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from Token import Token
from re import split
import TokenTypes

class Lexic:
	""" Lexic analysis class, defines the first step in the
		rss parser. 
		It takes a raw text string, tokenizes and determine
		wich type it represents, it also check for lexic errors.
	"""
	def __init__( self ):
		#Status represents the last analysis result
		#True for ok and False for error
		self.status = True

		#Error contains the error string, if it exists
		self.error = ''

		#List for all of the processed tokens
		self.tokens = list( )

		#List for all unprocessed strings
		self.raw = list( )

	def getAnalysisStatus( self ):
		"""Returns the status of last processed analysis.
		"""
		return self.status

	def tokenize( self, rawText ):
		""" Digest raw text and prepare tokens for analysis,
			it uses as separators:
			--->  <
			--->  >
			--->  \\s	#Blank spaces
			--->  \\t	#Tabs
			--->  \\n   #EOL 
			Returns unprocessed tokens list. 
		"""
		lines = rawText.split( '\n' )
		for i in lines:
			for j in split( '(<)|(>)|(=)|(\")|\n|\t|\s', i ):
				if( j is not None and j != "" ):
					self.raw.append( j )
		return self.raw

	def analyze( self ):
		"""
		"""
		pass




