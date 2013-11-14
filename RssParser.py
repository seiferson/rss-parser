#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from Lexical import Lexical
from FileMan import FileMan

class RssParser:
	""""""
	def __init__( self ):
		self.lx = Lexical( )
		self.fm = FileMan( )

	def run( self ):
		"""Main method for rss parser.
		"""
		fData = self.fm.loadTxtFile( "./rss/universal.rss" )
		self.lx.tokenize( fData )
		for i in self.lx.analyze( ):
			print( i.getType( ) )

app = RssParser( )
app.run( )
		
