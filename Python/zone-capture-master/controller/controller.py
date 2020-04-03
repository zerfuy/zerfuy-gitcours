#!/usr/bin/python3
# coding: utf-8

import pygame
import pygame.draw
import pygame.gfxdraw

# import os
# import sys
# if os.path.join("..", "model") not in sys.path:
#     sys.path.append(os.path.join("..", "model"))
# if os.path.join("..", "view") not in sys.path:
#     sys.path.append(os.path.join("..", "view"))
# import square, board, player, boardView
from model.ButtonColor import ButtonColor, ButtonText
from model.player import Player
from view.boardView import BoardView

liste_ligne = []
liste_colonne = []
nbSquares = 10
xx = 600  # todo : decider si seulement des carrés ou non
currplayer = 1
scorep1 = 0
scorep3 = 0
color1 = [255, 255, 0]
color3 = [0, 255, 255]
colorb = [255, 255, 255]
gwidth = 5
screen = 0
cheeseburger = 1


def text_objects_white(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def refreshScore(player1, player2):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    if player1.score + player2.score >= 100:
        TextSurf, TextRect = text_objects_white("P1 : " + str(player1.score) + ", P2 : " + str(player2.score) + ". Fin !",
                                                largeText)
    else:
        TextSurf, TextRect = text_objects_white("P1 : " + str(player1.score) + ", P2 : " + str(player2.score),
                                            largeText)
    TextRect.center = ((xx / 2), (xx) + (xx / nbSquares / 2))
    pygame.draw.rect(screen, (0, 0, 0), (0, xx + 2, xx, 60), 0)
    screen.blit(TextSurf, TextRect)


def configure():
    # init
    c1 = button(200, 400, 100, 50, "p1")
    c3 = button(500, 400, 100, 50, "p2")
    cb = button(350, 200, 100, 50, "board")
    ctxt = button(350, 400, 100, 50, "width")
    pygame.init()

    player1 = Player(1)
    player2 = Player(2)

    display_width = 800
    display_height = 600

    white = (255, 255, 255)

    block_color = (53, 115, 255)

    car_width = 73

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    """
    pygame.display.set_caption('A bit Racey')

    """

    intro = True
    playing = False
    configuring = True

    while configuring:
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                configuring = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (c1.isOver(event.dict['pos'])):
                    global color1
                    color1 = list(ButtonColor().c.chosen)
                    color1.pop()
                if (c3.isOver(event.dict['pos'])):
                    global color3
                    color3 = list(ButtonColor().c.chosen)
                    color3.pop()
                if (cb.isOver(event.dict['pos'])):
                    global colorb
                    colorb = list(ButtonColor().c.chosen)
                    colorb.pop()
                if (ctxt.isOver(event.dict['pos'])):
                    global gwidth
                    gwidth = list(ButtonText().c.chosen)
                    gwidth = int("".join(gwidth))
                    print("gwidth = " + str(gwidth))

        gameDisplay.fill(white)
        c1.draw(gameDisplay)
        c3.draw(gameDisplay)
        cb.draw(gameDisplay)
        ctxt.draw(gameDisplay)
        pygame.display.update()


def main(player1, player2):
    pygame.init()
    size = [xx, xx + 60]
    global screen
    screen = pygame.display.set_mode(size)
    global liste_ligne
    global liste_colonne
    liste_ligne = []
    liste_colonne = []
    setCurrPlayer(1)
    player1.score = 49
    player2.score = 49
    max_vsize = xx
    max_hsize = xx
    length = (int)(max_vsize / nbSquares)
    height = (int)(max_hsize / nbSquares)
    screen.fill(colorb)

    board = BoardView(screen, max_hsize, max_vsize, length, height)
    refreshScore(player1, player2)

    #########################
    # BOUCLE DES ÉVÈNEMENTS
    #########################
    done = False
    clock = pygame.time.Clock()
    clock.tick(15)

    pygame.display.update()
    pygame.display.flip()
    while not done:
        for event in pygame.event.get():

            if event.type == pygame.QUIT: done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Dans le cas d'un clic souris,
                # event.dict['pos'] contient les coordonnées
                # event.dict['button'] contient le numéro
                # du bouton souris
                clic(screen, event.dict['pos'], event.dict['button'], player1, player2)

    #################################
    # FIN DE LA BOUCLE DES ÉVÈNEMENTS
    #################################
    global playing
    playing = False
    # quit()

    #################################
    # FIN DE LA BOUCLE DES ÉVÈNEMENTS
    #################################


def clic(screen, coord, b, player1, player2):
    """ Procédure appelée en cas de clic
        à la souris. Elle a pour effet d'afficher
        un point de couleur (la couleur dépend du
        bouton souris utilisé) à l'endroit cliqué
        """
    global currplayer
    if b != currplayer:
        return
    print("Clic en ", coord[0], coord[1])
    print("Bouton ", b)
    pos1 = coord[0] % int(xx / nbSquares)  # modulo 100 pour savoir s'il s'agit d'une ligne ou d'une colonne
    pos2 = coord[1] % int(xx / nbSquares)
    res1 = int((coord[0] + int(xx / (nbSquares * nbSquares))) / int(
        xx / nbSquares))  # divise par 100 puis on tronque grace a int à l'entier pour savoir de quelle ligne/colonne il s'agit
    res2 = int((coord[1] + int(xx / (nbSquares * nbSquares))) / int(xx / nbSquares))
    test = str(res1) + str(res2)

    if ((int(xx / (nbSquares * nbSquares)) > pos1 > -int(xx / (nbSquares * nbSquares))) or (
            int(xx / nbSquares) + int(xx / (nbSquares * nbSquares)) > pos1 > int(xx / nbSquares) - int(
            xx / (nbSquares * nbSquares)))):
        print("c'est une colonne : " + test)
        if test in liste_colonne:
            print("la colonne existe déjà")
        else:
            liste_colonne.append(test)
            print(liste_colonne)
            coordx = round(coord[0] / int(xx / nbSquares)) * int(xx / nbSquares)
            coordy = res2 * int(xx / nbSquares)
            if (b == 1):
                pygame.draw.line(screen, color1, (coordx, coordy), (coordx, (coordy + int(xx / nbSquares))), gwidth)
            else:
                pygame.draw.line(screen, color1, (coordx, coordy), (coordx, (coordy + int(xx / nbSquares))), gwidth)
            res = check_colonne(test)
            if (res['color'] is not None):
                if (res['color'] == 1):
                    tmpcolor = color1
                else:
                    tmpcolor = color3
                if (res['arg1'] == 1):
                    pygame.draw.rect(screen,
                                     tmpcolor,
                                     [coordx,
                                      coordy,
                                      xx / nbSquares,
                                      xx / nbSquares])
                    if b == 1:
                        player1.score += 1
                    elif b == 3:
                        player2.score += 1
                if res['arg2'] == 1:
                    pygame.draw.rect(screen,
                                     tmpcolor,
                                     [coordx - (xx / nbSquares),
                                      coordy,
                                      xx / nbSquares,
                                      xx / nbSquares])
                    if b == 1:
                        player1.score += 1
                    elif b == 3:
                        player2.score += 1

    elif ((int(xx / (nbSquares * nbSquares)) > pos2 > -int(xx / (nbSquares * nbSquares))) or (
            int(xx / nbSquares) + int(xx / (nbSquares * nbSquares)) > pos2 > int(xx / nbSquares) - int(
            xx / (nbSquares * nbSquares)))):
        print("C'est une ligne : " + test)
        if test in liste_ligne:
            print("la ligne existe déjà")
        else:
            liste_ligne.append(test)
            print(liste_ligne)
            coordx = res1 * int(xx / nbSquares)
            coordy = round(coord[1] / int(xx / nbSquares)) * int(xx / nbSquares)
            if (b == 1):
                pygame.draw.line(screen, color1, (coordx, coordy), (coordx + int(xx / nbSquares), coordy), gwidth)
            else:
                pygame.draw.line(screen, color3, (coordx, coordy), (coordx + int(xx / nbSquares), coordy), gwidth)
            res = check_ligne(test)
            if (res['color'] is not None):
                if (res['color'] == 1):
                    tmpcolor = color1
                else:
                    tmpcolor = color3
                if (res['arg1'] == 1):
                    pygame.draw.rect(screen,
                                     tmpcolor,
                                     [coordx,
                                      coordy,
                                      xx / nbSquares,
                                      xx / nbSquares])
                    if b == 1:
                        player1.score += 1
                    elif b == 3:
                        player2.score += 1
                if (res['arg2'] == 1):
                    pygame.draw.rect(screen,
                                     tmpcolor,
                                     [coordx,
                                      coordy - (xx / nbSquares),
                                      xx / nbSquares,
                                      xx / nbSquares])
                    if b == 1:
                        player1.score += 1
                    elif b == 3:
                        player2.score += 1

    print("player1: " + str(player1.score) + " player2: " + str(player2.score))
    refreshScore(player1, player2)
    pygame.display.flip()


def setCurrPlayer(c):
    global currplayer
    currplayer = c


def check_ligne(ligne):
    ligne = int(ligne)
    print(ligne)
    # les colonnes sont les dizaines, les lignes sont les unites

    # case du dessous
    numcolonne = ligne % int(xx / (nbSquares * nbSquares))
    numligne = ligne // int(xx / (nbSquares * nbSquares))

    res = {}
    res['arg1'] = res['arg2'] = res['color'] = None

    if str(ligne + 1) in liste_ligne:
        if (str(ligne) in liste_colonne) and (str(ligne + nbSquares) in liste_colonne):
            print(" c'est un carré")
            res['arg1'] = 1
    # case du dessus
    if str(ligne - 1) in liste_ligne:
        if (str(ligne - 1) in liste_colonne) and (str(ligne + nbSquares - 1) in liste_colonne):
            print(" c'est un carré")
            res['arg2'] = 1
    res['color'] = getCurrPlayer()

    if res['arg1'] == res['arg2'] is None:
        c = 1 if (getCurrPlayer() == 3) else 3
        setCurrPlayer(c)
    return res


def getCurrPlayer():
    global currplayer
    return currplayer


def check_colonne(ligne):
    ligne = int(ligne)
    print(ligne)
    numcolonne = ligne // nbSquares
    numligne = ligne % (nbSquares)
    # case de droite
    res = {}
    res['arg1'] = res['arg2'] = res['color'] = None
    if str(ligne + nbSquares) in liste_colonne:
        if (str(ligne) in liste_ligne) and (str(ligne + 1) in liste_ligne):
            print(" c'est un carré")
            res['arg1'] = 1
    # case de gauche
    if str(ligne - nbSquares) in liste_colonne:
        if (str(ligne - nbSquares) in liste_ligne) and (str(ligne - nbSquares + 1) in liste_ligne):
            print(" c'est un carré")
            res['arg2'] = 1

    res['color'] = getCurrPlayer()

    if res['arg1'] == res['arg2'] == None:
        c = 1 if (getCurrPlayer() == 3) else 3
        setCurrPlayer(c)
    return res


class button():
    def __init__(self, x, y, width, height, text=''):
        self.color = (255, 255, 0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


if __name__ == '__main__': main()
