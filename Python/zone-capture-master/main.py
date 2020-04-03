#!/usr/bin/python3
# coding: utf-8

# Main file for zone-capture, a game made at CPE Lyon

## Imports
# Libraries
import pygame

# DEBUG ONLY
from pprint import pprint

# Classes
from model.square import Square
from model.board import Board
from model.player import Player
import controller.controller
import pygame
import pygame.draw
import pygame.gfxdraw

## Functions

def main(player1, player2) :
	controller.controller.main(player1, player2)

def configure() :
	controller.controller.configure()

class button():
	def __init__(self, x,y,width,height, text=''):
		self.color = (255,255,0)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self,win,outline=None):
		#Call this method to draw the button on the screen
		if outline:
			pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
			
		pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
		
		if self.text != '':
			font = pygame.font.SysFont('comicsans', 60)
			text = font.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self, pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
			
		return False


pygame.quit()

def text_objects_white(text, font):
	textSurface = font.render(text, True, (255,255,255))
	return textSurface, textSurface.get_rect()

def text_objects_black(text, font):
	textSurface = font.render(text, True, (0,0,0))
	return textSurface, textSurface.get_rect()

if __name__=='__main__' : #main()
	pygame.init()

	player1 = Player(1)
	player2 = Player(2)
	 
	display_width = 800
	display_height = 600
	 
	black = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	 
	block_color = (53,115,255)
	 
	car_width = 73
	
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	clock = pygame.time.Clock()
	"""
	pygame.display.set_caption('A bit Racey')
	
	"""
	
	buttonPlay = button(200, 400, 100, 50, "Jouer")
	buttonConfigure = button(500, 400, 100, 50, "Options")

	intro = True
	playing = False
	configuring = False

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:				
				if(buttonPlay.isOver(event.dict['pos'])):
					playing = True
				if(buttonConfigure.isOver(event.dict['pos'])):
					configuring = True
				
				
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects_black("Zone Capture", largeText)
		TextRect.center = ((display_width/2),(display_height/3))
		gameDisplay.blit(TextSurf, TextRect)
		buttonPlay.draw(gameDisplay)
		buttonConfigure.draw(gameDisplay)
		pygame.display.update()
		clock.tick(15)

		if playing : 
			main(player1, player2)
			playing = False
			gameDisplay = pygame.display.set_mode((display_width,display_height))
			clock = pygame.time.Clock()

		if configuring : 
			configure()
			configuring = False
			gameDisplay = pygame.display.set_mode((display_width,display_height))
			clock = pygame.time.Clock()