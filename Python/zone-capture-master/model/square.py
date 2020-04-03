# coding: utf-8

## Libraries
import pygame

## Class definitions
# Square
#
# A square on our board

class Square():
	# Constructor
	def __init__(self):
		"""Instantiates a square

		Keywords arguments:
		"""
		# Properties
		self.up = None
		self.down = None
		self.left = None
		self.right = None
		self.captured = False
		print("DEBUG: Square created!")

	def check_captured(self, player):
		"""Check if drawing a side captures the square or not

		Keywords arguments:
		player -- the player that will, or not, own the square
		"""
		if self.up is not None and self.down is not None and self.left is not None and self.right is not None: # I'm sorry
			return False
		else:
			self.captured = player
			player.score += 1
			return True

	def own(self, side, player):
		"""Changes the ownership of a side.
		The idea is that whenever a player clicks on a side, that function is called.
		Keep in mind that a side is often common to several squares! (ie. the left
		side is the right side of the adjascent square)
		So when we click on a side, we invoke the "check captured" function for
		both squares, giving either square.side in parameters as well as the
		Player (*an instance of the player*).

		Keywords arguments:
		side -- the side of the square to own
		player -- the player that owns the side
		"""

		# TODO: test this. the idea is that we give a reference to side, but
		# i'm not sure it works that way in Python
		if side is None:
			side = player
			if self.check_captured(self, player):
				print("TODO: colorier la case")
			else:
				pass
			return True
		else:
			print("ERROR: Side already taken!")
			return False