# coding: utf-8

## Libraries

## Class definitions
# Board
#
# Our game board

class Board():
	# Constructor
	def __init__(self, size):
		"""Instantiates a square

		Keywords arguments:
		size -- an integer representing the board size. The board is a square for now.
		"""
		# Properties
		self.turn = None
		self.squaresList = []
		self.size = size
		print("DEBUG: Board created!")