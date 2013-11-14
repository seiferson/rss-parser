#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from Token import Token
from re import split
import TokenTypes

class Lexical:
	""" Lexical analysis class, defines the first step in the
		rss parser. 
		It takes a raw text string, tokenizes and determine
		wich type it represents, it also checks for lexical errors.
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
		"""Returns the status of the last processed analysis.
		"""
		return self.status

	def tokenize( self, rawText ):
		""" Digest raw text and prepare tokens for analysis,
			it uses as separators:
			--->  <
			--->  >
			--->  =
			--->  \\s	#Blank spaces
			--->  \\t	#Tabs
			--->  \\n   #EOL 
			Returns unprocessed tokens list. 
		"""
		#Cleaning the raw token list
		self.raw = list( ) 

		lines = rawText.split( '\n' )
		for i in lines:
			for j in split( '(<)|(>)|(\")|(=)|\n|\t|\s', i ):
				if( j != None and j != "" ):
					self.raw.append( j )
		return self.raw

	def analyze( self ):
		"""
		"""
		#Cleaning tokens list
		self.tokens = list( )

		for i in self.raw:
			token = i.strip( )

			#Reserved words and 1 char tokens identification
			if( token == 'rss' ):
				self.tokens.append( Token( token, 'RSS' ) )
			elif( token == '/rss' ):
				self.tokens.append( Token( token, 'RSS_CLOSURE' ) )
			elif( token == 'channel' ):
				self.tokens.append( Token( token, 'CHANNEL' ) )
			elif( token == '/channel' ):
				self.tokens.append( Token( token, 'CHANNEL_CLOSURE' ) )
			elif( token == 'title' ):
				self.tokens.append( Token( token, 'TITLE' ) )
			elif( token == '/title' ):
				self.tokens.append( Token( token, 'TITLE_CLOSURE' ) )
			elif( token == 'link' ):
				self.tokens.append( Token( token, 'LINK' ) )
			elif( token == '/link' ):
				self.tokens.append( Token( token, 'LINK_CLOSURE' ) )
			elif( token == 'description' ):
				self.tokens.append( Token( token, 'DESCRIPTION' ) )
			elif( token == '/description' ):
				self.tokens.append( Token( token, 'DESC_CLOSURE' ) )
			elif( token == 'item' ):
				self.tokens.append( Token( token, 'ITEM' ) )
			elif( token == '/item' ):
				self.tokens.append( Token( token, 'ITEM_CLOSURE' ) )
			elif( token == '<' ):
				self.tokens.append( Token( token, 'LEFT_CHEVRON' ) )
			elif( token == '>' ):
				self.tokens.append( Token( token, 'RIGHT_CHEVRON' ) )
			elif( token == '\"' ):
				self.tokens.append( Token( token, 'QUOTE' )	)
			elif( token == '=' ):
				self.tokens.append( Token( token, 'EQUAL' ) )
			else:
				self.tokens.append( Token( token, 'STRING' ) )
		return self.tokens




