import pygame
import pygame.draw
import pygame.gfxdraw

liste_ligne = []
liste_colonne = []

def clic(screen, coord,b) :
    """ Procédure appelée en cas de clic
        à la souris. Elle a pour effet d'afficher
        un point de couleur (la couleur dépend du
        bouton souris utilisé) à l'endroit cliqué
        """
    print("Clic en ",coord[0],coord[1])
    print("Bouton ",b)
#    if b==1   : c=[255,255,0]
#    elif b==2 : c=[255,0,255]
#    else      : c=[0,255,255]
#    pygame.draw.circle(screen,c,coord,5,0)
#    if()
#    pygame.display.flip()
#    check_square(coord)
    pos1 = coord[0] % 100  #modulo 100 pour savoir s'il s'agit d'une ligne ou d'une colonne
    pos2 = coord[1] % 100
    res1 = int(coord[0] / 100) #divise par 100 puis on tronque grace a int à l'entier pour savoir de quelle ligne/colonne il s'agit
    res2 = int(coord[1] / 100)
    print("valeur res1:",res1,"valeur res2:",res2)
    test = str(res1)+str(res2)
    #   print(pos1)
    if ( (pos1 < 12 and pos1 > -12) or ( pos1 < 112 and pos1 > 88 ) ):
        print("c'est une colonne")
        if test in liste_colonne:
            print("la colonne existe déjà")
        else:
            liste_colonne.append(test)
            print(liste_colonne)
            coordx = round(coord[0] / 100) * 100
            coordy = res2 * 100
            pygame.gfxdraw.line(screen, coordx, coordy, coordx, (coordy+100), [255,255,0])
    elif ( (pos2 < 12 and pos2 > -12) or ( pos2 < 112 and pos2 > 88 ) ):
        print("C'est une ligne")
        if test in liste_ligne:
            print("la colonne existe déjà")
        else:
            liste_ligne.append(test)
            print(liste_ligne)
            coordx = res1 * 100
            coordy = round(coord[1] / 100) * 100
            pygame.gfxdraw.line(screen, coordx, coordy, coordx+100, coordy, [255,255,0])
            check_ligne(test)
    pygame.display.flip()

def jeu():
    joueur1 = 0
    joueur2 = 0
    joueur1couleur = [0,255,255]
    joueur2couleur = [255,255,0]

def check_ligne(ligne):
    ligne = int(ligne)
    print(ligne)
    print(ligne+10)
    if (ligne+10 in liste_ligne) and (ligne in liste_colonne) and (ligne+10 in liste_colonne):
        print(" c'est un carré")
        print("ligne : "+ligne)
    elif (ligne-10 in liste_ligne) and (ligne in liste_colonne) and (ligne+10 in liste_colonne):
        print(" c'est un carré")
        print("ligne : "+ligne)
    else:
        print("eh non")

#def check_colonne(colonne):

def main() :
    pygame.init()
    xx,yy=1000,1000
    size=[xx,yy]
    screen=pygame.display.set_mode(size)
    max_vsize = xx
    max_hsize = yy
    i = (int)(max_vsize/10)
    j = (int)(max_hsize/10)
    length = i
    height = j
    print(i,j)
    dico = {}
    ligne = {}
    number = 0
    while j < max_hsize:
        while i < max_vsize:
            pygame.gfxdraw.line(screen, i, 0, i, max_hsize, [100,100,100])
            ligne[number] = {"x0": i, "y0": 0, "x1": i, "y1": max_hsize}
            #dico[]
            number += 1
            i += length
        pygame.gfxdraw.line(screen, 0, j, max_vsize, j, [100,100,100])
        j += height
    pygame.display.flip()
    print(ligne)

    #    un côté est 2 coordonnées : le debut et la fin d'une ligne
#    ligne[] =


    #########################
    # BOUCLE DES ÉVÈNEMENTS
    #########################
    done=False
    while done==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: done=True
            if event.type == pygame.MOUSEBUTTONDOWN :
                # Dans le cas d'un clic souris,
                # event.dict['pos'] contient les coordonnées
                # event.dict['button'] contient le numéro
                # du bouton souris
                clic(screen, event.dict['pos'],event.dict['button'])

#################################
# FIN DE LA BOUCLE DES ÉVÈNEMENTS
#################################

pygame.quit()

if __name__=='__main__' : main()
