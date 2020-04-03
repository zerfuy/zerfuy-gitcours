# coding: utf-8

## Libraries
import pygame

## Class definitions
# Player
#
# A player

class Player():
	# Constructor
	def __init__(self, id):
		"""Instantiates a square

		Keywords arguments:
		id -- an integer representing the player ID
		"""
		# Properties
		self.score = 49
		self.color = ""
		self.idPlayer = id
		self.name = "Player " + str(self.idPlayer)
		print("DEBUG: Player " + self.name + " created!")