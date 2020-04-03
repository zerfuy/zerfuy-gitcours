
# -*- coding: utf-8 -*-
# Juin 2019
# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...
# Quelques codes d'échappement (tous ne sont pas utilisés)
import sys
import random
import math
import time
import os
import multiprocessing as mp
from multiprocessing import Process

CLEARSCR = "\x1B[2J\x1B[;H"  # Clear SCReen
CLEAREOS = "\x1B[J"  # Clear End Of Screen
CLEARELN = "\x1B[2K"  # Clear Entire LiNe
CLEARCUP = "\x1B[1J"  # Clear Curseur UP
GOTOYX = "\x1B[%.2d;%.2dH"  # ('H' ou 'f') : Goto at (y,x), voir le code
DELAFCURSOR = "\x1B[K"  # effacer après la position du curseur
CRLF = "\r\n"  # Retour à la ligne
# VT100 : Actions sur le curseur
CURSON = "\x1B[?25h"  # Curseur visible
CURSOFF = "\x1B[?25l"  # Curseur invisible
# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"  # Normal
BOLD = "\x1B[1m"  # Gras
UNDERLINE = "\x1B[4m"  # Souligné
# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK = "\033[22;30m"  # Noir. NE PAS UTILISER. On verra rien !!
CL_RED = "\033[22;31m"  # Rouge
CL_GREEN = "\033[22;32m"  # Vert
CL_BROWN = "\033[22;33m"  # Brun
CL_BLUE = "\033[22;34m"  # Bleu
CL_MAGENTA = "\033[22;35m"  # Magenta
CL_CYAN = "\033[22;36m"  # Cyan
CL_GRAY = "\033[22;37m"  # Gris
# "01" pour quoi ? (bold ?)
CL_DARKGRAY = "\033[01;30m"  # Gris foncé
CL_LIGHTRED = "\033[01;31m"  # Rouge clair
CL_LIGHTGREEN = "\033[01;32m"  # Vert clair
CL_YELLOW = "\033[01;33m"  # Jaune
CL_LIGHTBLU = "\033[01;34m"  # Bleu clair
CL_LIGHTMAGENTA = "\033[01;35m"  # Magenta clair
CL_LIGHTCYAN = "\033[01;36m"  # Cyan clair
CL_WHITE = "\033[01;37m"  # Blanc
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
keep_running = True  # Fin de la course ?
# Une liste de couleurs à affecter aléatoirement aux chevaux

LONGUEUR_COURSE=20
mutex = mp.Semaphore(1)
semarbitre = mp.Semaphore(1)
Nb_process=20
mes_process=[0 for i in range(Nb_process)]
cols = mp.Array('i', Nb_process)

lyst_colors = [CL_WHITE, CL_RED, CL_GREEN, CL_BROWN, CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN, CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]


def effacer_ecran(): print(CLEARSCR, end='')


def erase_line_from_beg_to_curs(): print("\033[1K", end='')


def curseur_invisible(): print(CURSOFF, end='')


def curseur_visible(): print(CURSON, end='')


def move_to(lig, col): print("\033[" + str(lig) + ";" + str(col) + "f", end='')


def en_couleur(Coul): print(Coul, end='')


def en_rouge(): print(CL_RED, end='')  # Un exemple, La tache d'un cheval

def un_arbitre():
    #TODO change to stop when max col 
    while 1:
        mutex.acquire()
        en_couleur(CL_WHITE)
        #semarbitre.release()
        #erase_line_from_beg_to_curs()
        move_to(Nb_process+2, 0)  # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        max = 0
        min = LONGUEUR_COURSE
        maxindex = 0
        mindex = Nb_process
        i = 0
        for val in cols:
            if val > max:
                max = val
                maxindex = i-1
            if val < min:
                min = val
                minindex = i-1
            i += 1
        print("First is " + chr(ord('A') + maxindex + 1) + "---- Ligne " + str(maxindex+1) + "---- position : " + str(max) + "----")
        print("Last is " + chr(ord('A') + minindex + 1) + "---- Ligne " + str(minindex+1) + "---- position : " + str(min) + "----")

        if max >= LONGUEUR_COURSE-1:
            move_to(Nb_process+2, 0)
            print("EPIC WIN " + chr(ord('A') + maxindex+1) + ", en ligne " + str(maxindex+1) + " in position : " + str(max) + "----------")
            print("EPIC LOOSE " + chr(ord('A') + mindex+1) + ", en ligne " + str(mindex+1) + " in position : " + str(min) + "----------")
            mutex.release()
            break
        mutex.release()
        time.sleep(0.1)

def un_cheval(ma_ligne: int, triche=False):  # ma_ligne commence à 0
    col = 1
    while col < LONGUEUR_COURSE and keep_running:
        #semarbitre.acquire()
        mutex.acquire()
        # ajout pour l'arbitre : nu mde ligne = num de process, val = col
        if triche:
            col += 2
        else:
            col += 1
        cols[ma_ligne] = col
        move_to(ma_ligne+1, col)  # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne % len(lyst_colors)])
        print(chr(ord('A') + ma_ligne) + "(=\".\"=)")
        mutex.release()
        time.sleep(0.1 * random.randint(1, 5))

"""
> Exercices
Travail à réaliser  # 15
# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# La partie principale :
"""
if __name__ == "__main__":
    text = input("> pssst donne la lettre du panda qui doit gagner\n>")
    if text.lower() == "Non je refuse cette pratique non etique".lower():
        print("> :'(\n")
        time.sleep(10)
        exit()
    else:
        if len(text) != 1:
            text = "?"
            print("Course honnete alors\n")
            time.sleep(2)
        arbitre = Process(target=un_arbitre,)
        effacer_ecran()
        curseur_invisible()
        arbitre.start()
        for i in range(Nb_process):  # Lancer Nb_process processus
            if ord('A') + i == ord(text):
                mes_process[i]=Process(target=un_cheval, args=(i, True, ))
            else:
                mes_process[i]=Process(target=un_cheval, args=(i, ))
            mes_process[i].start()
            move_to(Nb_process + 4, 20)
            print("tous lancés")
        for i in range(Nb_process): mes_process[i].join()
        arbitre.join()
        move_to(Nb_process + 4, 40)
        curseur_visible()
        print("Fini")
