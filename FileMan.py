#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores


class FileMan:
	""" File managment class, can be used for both
		text and binary files.
	"""
	def __init__( self ):
		#Buffer used for data reading and writing
		self.fBuffer = None
		
	def createTxtFile( self, filename ):
		""" Creates a txt file, if the file exists overwrite it,
			filename should be the path including file name.
		"""
		try:
			self.fBuffer = open( filename, 'w' )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: Creating file failed' )
			
	def createBinFile( self, filename ):
		""" Creates a bin file, if the file exists overwrite it,
			filename should be the path including file name.
		""" 
		try:
			self.fBuffer = open( filename, 'wb' )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def loadTxtFile( self, filename ):
		""" Opens and reads a txt file
		""" 
		data = ''
		try:
			self.fBuffer = open( filename, 'r' )
			data = self.fBuffer.read( )
			self.fBuffer.close( )
			return data
		except IOError:
			print( 'Error: ' )
			
	def loadBinFile( self, filename ):
		""" Not implemented yet.
		"""
		pass
		
	def writeTxtFile( self, filename, data ):
		"""
		"""
		try:
			self.fBuffer = open( filename, 'w' )
			self.fBuffer.write( data )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def writeBinFile( self, filename, data ):
		""" Not implemented yet.
		"""
		pass
		
	def appendTxtFile( self, filename, data ):
		"""
		"""		
		try:
			self.fBuffer = open( filename, 'a' )
			self.fBuffer.write( data )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def appendBinFile( self, filename, data ):
		""" Not implemented yet.
		"""
		pass
