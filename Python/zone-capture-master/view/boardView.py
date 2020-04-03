#!/usr/bin/python3
# coding: utf-8

import pygame
import pygame.draw
import pygame.gfxdraw

class BoardView():
    def __init__(self, screen, max_hsize, max_vsize, length, height):
        self.screen = screen
        self.max_hsize = max_hsize
        self.max_vsize = max_vsize
        self.length = length
        self.height = height
        ligne = {}
        number = 0
        j = i = 0
        while j < max_hsize+1:
            while i < max_vsize:
                pygame.gfxdraw.line(screen, i, 0, i, max_hsize, [100, 100, 100])
                ligne[number] = {"x0": i, "y0": 0, "x1": i, "y1": max_hsize}
                number += 1
                i += length
            pygame.gfxdraw.line(screen, 0, j, max_vsize, j, [100, 100, 100])
            j += height
        pygame.display.flip()
        print(ligne)

    def refresh(self):
        j = i = 0
        ligne = {}
        number = 0
        while j < self.max_hsize:
            while i < self.max_vsize:
                pygame.gfxdraw.line(self.screen, i, 0, i, self.max_hsize, [100, 100, 100])
                ligne[number] = {"x0": i, "y0": 0, "x1": i, "y1": self.max_hsize}
                number += 1
                i += self.length
            pygame.gfxdraw.line(self.screen, 0, j,self. max_vsize, j, [100, 100, 100])
            j += self.height
        pygame.display.flip()
        print(ligne)
