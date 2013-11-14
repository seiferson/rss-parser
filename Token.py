#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

class Token:
	""""""
	def __init__( self, str_, type_ ):
		self.str_ = str_
		self.type_ = type_

	def getType( self ):
		return self.type_

	def __str__( self ):
		return self.str_
