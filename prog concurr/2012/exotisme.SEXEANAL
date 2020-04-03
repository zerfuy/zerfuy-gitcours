# Dec 2019

"""
 effacer ecran
 dessiner un cadre 
 * Tache screen :
    - lire val température
    - lire val pression
    - afficher les états
    
* Tache capteur temp : ...
* Tache capteur pression :
* Tache ctrl : 
    - lire val température
    - lire val pression
    - Si Temp > Consigne : déclancher Chauffage sinon eteindre
    - Si pression > Consigne : déclancher Pompe sinon eteindre
    
 ------------------------------
 |                            |
 |  * Température :           |
 |   - consigne : 21          |
 |   - actuelle : 20          |
 |                            |
 |  * Pression :              |
 |   - consigne : 2           |
 |   - actuelle : 20          |
 |                            |
 |  * Etat Chauffage : on     |
 |  * Etat Pompe : off        |
 |  * Relation T / P :        |
 |                            |
 ------------------------------ 
 """
# VT100 : Couleurs


CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"         

CLEARSCR="\x1B[2J\x1B[;H"        #  Clear SCReen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"
CRLF  = "\r\n"                  #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


#-------------------------------------------------------
import os, time,math, random, sys
from array import array  # Attention : différent des 'Array' des Process
import os
from multiprocessing import Process, Semaphore, Value
from threading import Thread

keep_running=True # Fin de la course ?
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY, CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN, \
             CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]


def effacer_ecran() : print(CLEARSCR,end='')
    # for n in range(0, 64, 1): print("\r\n",end='')

def erase_line_from_beg_to_curs() :
    print("\033[1K",end='')

def erase_current_line():
    print(CLEARELN, end='')

def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')

def move_to(lig, col) : # No work print("\033[%i;%if"%(lig, col)) # print(GOTOYX%(x,y))
    print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='')


#============ Constantes d'affichage ====
x_coin_H_G_cadre, y_coin_H_G_cadre= 5, 10
x_coin_B_G_cadre, y_coin_B_G_cadre= 22, 10
x_coin_H_G_Temperature, y_coin_H_G_Temperature= 7, 12
x_coin_H_G_Pression, y_coin_H_G_Pression= 12, 12
x_coin_H_G_Chauffage, y_coin_H_G_Chauffage= 17, 12
x_coin_H_G_Pompe, y_coin_H_G_Pompe= 18, 12
x_coin_H_G_relation_T_P, y_coin_H_G_relation_T_P= 20, 12


# Partie trace et messages :
# 'Nom tache' : [ligne_mess, col_mess]
dict_messages_des_taches={'tache_controleur_central : Pompe' : [25,1], 
                          'tache_controleur_central : Chauffage' : [26,1],
                          'tache_capteur_temperature' : [26,1]
                          #'tache_capteur_pression' : [27,1],
                          #'tache_screen' :[28,1]
                          }

ligne_prompt_systeme, col_prompt_systeme= 30,1
relation_entre_T_et_P_courte="P.V = n.8,3.T"
relation_entre_T_et_P_longue="Pression_en_Pa * Volume_en_m3 = nb_molécules * 8.31441 * Temp_en_C"
# avec R = 8,31441 [J/mol.K ] , T en [K] , V en [m3] , p en [Pa], n en [mol]

nb_traits=35
ligne_traits="-"*nb_traits
une_ligne_vid_avec_barres="|"+(" "*(nb_traits-2))+"|"

# Les constantes 
max_temperature_possible=40.0
min_temperature_possible=-10.0
max_pression_possible=200.0
min_pression_possible=50.0 

Temp_init=18.0
Pression_init=120.0
chauffage_init_on=False
Pompe_init_on=False
Cste_Consigne_Temperature=22.0
Cste_Consigne_Pression=117.0

Cste_Alpha=0.345642         # 0.02 # On a P = T * Alpha et T=P/alpha

import multiprocessing as mp
import random, time,math

def ecrire_um_message(nom_tache, mess) :
    ligne_messages, col_messages=dict_messages_des_taches[nom_tache]
    move_to(ligne_messages, col_messages) 
    erase_current_line()
    move_to(ligne_messages, col_messages) 
    print("Tache ", nom_tache, " : ", mess)    
    
def placer_le_cadre() :
    effacer_ecran()
    move_to(x_coin_H_G_cadre, y_coin_H_G_cadre) 
    print(ligne_traits)
    for i in range(17) :
        move_to(x_coin_H_G_cadre+i+1, y_coin_H_G_cadre) 
        print(une_ligne_vid_avec_barres)
    move_to(x_coin_B_G_cadre, y_coin_B_G_cadre) 
    print(ligne_traits)    
    
def ecrire_donnees_temp(val_consigne = 21.0, val_actuelle = 0.0):
    move_to(x_coin_H_G_Temperature, y_coin_H_G_Temperature) 
    print("* Température ")
    move_to(x_coin_H_G_Temperature+1, y_coin_H_G_Temperature+3) 
    print("-Consigne : ", round(val_consigne,2))
    move_to(x_coin_H_G_Temperature+2, y_coin_H_G_Temperature+3) 
    print("-Actuel : ", round(val_actuelle,2))

def ecrire_donnees_pression(val_consigne = 2.0, val_actuelle = 0.0):
    move_to(x_coin_H_G_Pression, y_coin_H_G_Pression)
    print("* Pression ")
    move_to(x_coin_H_G_Pression+1, y_coin_H_G_Pression+3) 
    print("-Consigne : ", val_consigne)
    move_to(x_coin_H_G_Pression+2, y_coin_H_G_Pression+3) 
    print("-Actuel : ", round(val_actuelle,2))
  
def ecrire_etats_T_P_et_rel_TP(chauffage_is_on=False, pompe_is_on=False) :
    move_to(x_coin_H_G_Chauffage, y_coin_H_G_Chauffage) 
    print("* Etat Chauffage :", "True " if chauffage_is_on else "False") 
    move_to(x_coin_H_G_Pompe, y_coin_H_G_Pompe) 
    print("* Etat Pompe :", "True " if pompe_is_on else "False")   
    move_to(x_coin_H_G_relation_T_P, y_coin_H_G_relation_T_P) 
    print("* Relation T/P :", relation_entre_T_et_P_courte) 
 
#------------- Les taches / processus -------------------------
def tache_capteur_pression(semPress, val_temperature, val_pression, chauffage_is_on, pompe_is_on):  
    while(True):
        # La pression
        time.sleep(0.05)
        if (not pompe_is_on.value) : # on augmente la température de 10% par unité de temps   
            semPress.acquire()
            val_pression.value -=1 # KPa
            semPress.release()
        else :
            semPress.acquire()
            val_pression.value*=1.1 # On suppose que la pression augmente de 10% par unité de temps. Vol=Cste
            semPress.release()
    
def tache_capteur_temperature(semTemp, val_temperature, val_pression, chauffage_is_on, pompe_is_on):  
    while(True):
        delta=0.0            
        if (not chauffage_is_on.value): # on baisse la température de 0.1 par seconde
            delta=0.5-random.random()
            if delta > 0:
                delta=-0.3            
        else :
            delta=0.2
        semTemp.acquire()
        val_temperature.value+=delta
        time.sleep(0.05)
        semTemp.release()

        ecrire_um_message("tache_capteur_temperature", "Chauffage allumé" if chauffage_is_on.value else "Chauffage eteint")      


def tache_screen(val_temperature, val_pression, chauffage_is_on, pompe_is_on):
    while(True):
        ecrire_donnees_temp(Cste_Consigne_Temperature, val_temperature.value)
        ecrire_donnees_pression(Cste_Consigne_Pression, val_pression.value)
        ecrire_etats_T_P_et_rel_TP(chauffage_is_on.value, pompe_is_on.value) 


def tache_controleur_central(semchauffe, sempompe, semPress, semTemp, val_temperature, val_pression, chauffage_is_on, pompe_is_on):  
    while(True):
        semTemp.acquire()
        if (Cste_Consigne_Temperature > val_temperature.value):
            semchauffe.acquire()
            chauffage_is_on.value=1
            semchauffe.release()
        else:
            semchauffe.acquire()
            chauffage_is_on.value=0 
            semchauffe.release()
        semTemp.release()
        semPress.acquire()
        if (Cste_Consigne_Pression > val_pression.value):
            sempompe.acquire()
            pompe_is_on.value=1
            sempompe.release()
        else:
            sempompe.acquire()
            pompe_is_on.value=0
            sempompe.release()
        semPress.release()
        semTemp.acquire()
        if (val_temperature.value >= max_temperature_possible) :
            val_temperature.value = max_temperature_possible
            semchauffe.acquire()
            chauffage_is_on.value=0
            semchauffe.release()
        if (val_temperature.value < min_temperature_possible) :
            val_temperature.value = min_temperature_possible
            semchauffe.acquire()
            chauffage_is_on.value=1
            semchauffe.release()
        semTemp.release()
        semPress.acquire()
        if (val_pression.value >= max_pression_possible) :
            val_pression.value = max_pression_possible
            sempompe.acquire()
            pompe_is_on.value=0
            sempompe.release()
        if (val_pression.value < min_pression_possible) :
            val_pression.value = min_pression_possible
            sempompe.acquire()
            pompe_is_on.value=1
            sempompe.release()
        semPress.release()
    
        #===================================================
        # Lien T et P    
        semPress.acquire()
        semTemp.acquire()
        val_pression.value = (val_temperature.value + 273.15) * Cste_Alpha
        semTemp.release()
        semPress.release()
        #===================================================
       
        ecrire_um_message("tache_controleur_central : Chauffage" , " --> j'allume" if pompe_is_on.value else "--> j'teints")
        ecrire_um_message("tache_controleur_central : Pompe", " --> j'allume" if pompe_is_on.value else "--> j'teints")
    
    
    
if __name__ == "__main__" :
    semTemp = Semaphore(1)
    semPress = Semaphore(1)
    semchauff = Semaphore(1)
    sempompe = Semaphore(1)
    val_temperature = Value('d', Temp_init)
    val_pression = Value('d', Pression_init)
    chauffage_is_on = Value('b', chauffage_init_on)
    pompe_is_on = Value('b', Pompe_init_on)

    placer_le_cadre()

    liste_process = []

    liste_process.append(Process(target=tache_capteur_temperature, args=(semTemp, val_temperature, val_pression, chauffage_is_on, pompe_is_on,)))
    liste_process.append(Process(target=tache_capteur_pression, args=(semPress, val_temperature, val_pression, chauffage_is_on, pompe_is_on,)))
    liste_process.append(Process(target=tache_controleur_central, args=(semchauff, sempompe, semPress, semTemp, val_temperature, val_pression, chauffage_is_on, pompe_is_on,)))
    liste_process.append(Process(target=tache_screen, args=(val_temperature, val_pression, chauffage_is_on, pompe_is_on,)))

    for th in liste_process:
        th.start()

    curseur_invisible()

    for th in liste_process:
        th.join()

    curseur_visible()

    # Fin
    move_to(ligne_prompt_systeme, col_prompt_systeme)
    os.system("tset;reset")    
    
