import easygui

from model.square import Square
from model.board import Board
from model.player import Player
from model.Button import Button
import controller.controller
import pygame
import pygame.draw
import pygame.gfxdraw

chosen = ""

class ButtonColor():
    def __init__(self):
        chosen = ""
        size = width, height = 400, 400
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("monospace", 20)
        black = 0, 0, 0
        running = True
        all_rects = []
        NAME_TO_RGBA = pygame.color.THECOLORS
        RGBA_TO_NAME = {}
        for name, rgb in NAME_TO_RGBA.items():
            if rgb in RGBA_TO_NAME:
                RGBA_TO_NAME[rgb].append(name)
            else:
                RGBA_TO_NAME[rgb] = [name]

        # defs
        def DrawWindow():
            pygame.display.flip()
            screen.fill(black)

        class Rect():
            def __init__(self, name, color, x, y):
                self.rect = pygame.Rect(10, 10, 10, 10)
                self.rect.x = x
                self.rect.y = y
                self.name = name
                self.color = color
                all_rects.append(self)

            def Draw(self):
                pygame.draw.rect(screen, (self.color), self.rect)

        class ColorPicker():
            def __init__(self):
                self.colors = RGBA_TO_NAME
                self.gridX = 25
                self.MakeGrid()

            def MakeGrid(self):
                x, y = 75, 100
                i = 0
                for col, name in self.colors.items():

                    rect = Rect(name, col, x, y)
                    x += 10
                    i += 1
                    if i == 25:
                        i = 0
                        y += 10
                        x = 75

        self.c = ColorPicker()
        print
        len(RGBA_TO_NAME)
        name_label = font.render("", 1, (255, 255, 255))
        color_label = font.render("", 1, (255, 255, 255))
        while running:
            clock.tick(60)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        pos = pygame.mouse.get_pos()
                        for rect in all_rects:
                            if rect.rect.collidepoint(pos):
                                name_label = font.render(str(rect.name), 1, (255, 255, 255))
                                color_label = font.render(str(rect.color), 1, (255, 255, 255))
                                self.c.chosen = rect.color
            screen.blit(name_label, (100, 20))
            screen.blit(color_label, (100, 40))
            for rect in all_rects:
                rect.Draw()
            DrawWindow()
        return None

class ButtonText():
    def __init__(self):
        chosen = ""
        size = width, height = 0, 0
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("monospace", 20)
        black = 0, 0, 0
        running = True
        all_rects = []
        import tkinter


        # defs
        def DrawWindow():
            pygame.display.flip()
            screen.fill(black)

        class Rect():
            def __init__(self, name, color, x, y):
                self.rect = pygame.Rect(10, 10, 10, 10)
                self.rect.x = x
                self.rect.y = y
                self.name = name
                self.color = color
                all_rects.append(self)

            def Draw(self):
                pygame.draw.rect(screen, (self.color), self.rect)

        class ColorPicker():
            def __init__(self):
                self.colors = ""


        self.c = ColorPicker()


        name_label = font.render("", 1, (255, 255, 255))
        color_label = font.render("", 1, (255, 255, 255))
        while running:
            clock.tick(60)
            self.c.chosen = easygui.enterbox("please choose a width ?","width",1)
            if self.c.chosen == "" or self.c.chosen is None:
                self.c.chosen = ["1"]
            running = False

            for rect in all_rects:
                rect.Draw()
            DrawWindow()
        return None
