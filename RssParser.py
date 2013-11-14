#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from Lexic import Lexic
from FileMan import FileMan

class RssParser:
	""""""
	def __init__( self ):
		self.lx = Lexic( )
		self.fm = FileMan( )


	def run( self ):
		"""Main method for rss parser.
		"""
		fData = self.fm.loadTxtFile( "test.rss" )
		self.lx.tokenize( fData )

app = RssParser( )
app.run( )
		
