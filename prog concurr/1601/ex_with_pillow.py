from PIL import Image # Importation de la librairie d'image PIL
from math import sqrt # Importation de la fonction sqrt de la librairie math
import multiprocessing as mp
from threading import Thread
 
image_ = None     # sera chargée dans la partie Mian (ici,  on la 'pré-déclare')
width, height = None,  None # respectivement,  la largeur et la hauteur de l'image 

def GetPixel(x, y):  
    global matrice_pixels
    return matrice_pixels[x, y]
    
def PutPixel(x, y, r, g, b): 
    global matrice_pixels    
    matrice_pixels[x, y]= int(r),  int(g),  int(b) # Il faut des ints !
    
def PutRegion(x, y, width, height, triplet_color):
    for i in range(x,   x+width):
        for j in range(y,  y+height):
            PutPixel(i, j, triplet_color[0], triplet_color[1], triplet_color[2])

def Average(corner_x,  corner_y, region_w, region_h):  
    sum_red,  sum_green,  sum_blue = 0, 0, 0    #Initialisation des compteurs   
    area = region_w*region_h       #Calcul de la superficie de la région
    
    for i in range(corner_x,  corner_x+region_w):
        for j in range(corner_y,  corner_y+region_h):
            r, g, b = GetPixel(i, j)# Nous lisons les données r, v, b d'un pixel
            sum_red += r       # somme de chaque composant
            sum_green += g
            sum_blue += b 
    #Normalisation            
    sum_red/=area
    sum_green/=area
    sum_blue/=area
    
    return(sum_red,  sum_green, sum_blue)   #Retour des valeurs r, g, b moyennes


def Mesures_Std_et_Mu(corner_x,  corner_y,  region_w,  region_h):    
    av_red,  av_blue,  av_green = Average(corner_x, corner_y, region_w, region_h)    
    sum_red2, sum_green2, sum_blue2 = 0.0,  0.0,  0.0

    for i in range(corner_x,  corner_x+region_w):
        for j in range(corner_y,  corner_y+region_h):             
            red, green, blue = GetPixel(i, j)
            sum_red2  += (red**2)
            sum_green2 += (green**2)
            sum_blue2 += (blue**2)

    area=region_w*region_h*1.0
    r, g, b=0, 0, 0 
    r = sqrt(abs(sum_red2 / area - av_red**2))
    g= sqrt(abs(sum_green2 / area - av_green**2))
    b = sqrt(abs(sum_blue2 / area - av_blue**2))
    return ((av_red,  av_blue,  av_green),  (r+b+g)/3.0)


def Decouper_en4(x, y, width, height, threshold_alpha, mutex, procCount):
    if height * width < 4:  return   # rien à découper

    # Cas de région uniforme : une couleur uniforme est affectée à la partition 
    color, rm = Mesures_Std_et_Mu(x,  y,  width,  height)
    if rm < threshold_alpha:  # Affectation de la couleur moyenne à la partition      
        PutRegion(x, y, width, height, color)
    else: #Dans le cas contraire,  la partition non-uniforme est coupée en 4 (récursivement)
        mesprocs = []
        if procCount.value < 6:
            mesprocs.append(Thread(target=Decouper_en4, args=(x, y, width//2, height//2, threshold_alpha, mutex, procCount, )))
            procCount.value += 1
        else:
            Decouper_en4(x, y, width//2, height//2, threshold_alpha, mutex, procCount)
        if procCount.value < 6:
            mesprocs.append(Thread(target=Decouper_en4, args=(x + width//2,  y,  width//2,  height//2, threshold_alpha, mutex, procCount, )))
            procCount.value += 1
        else:
            Decouper_en4(x + width//2,  y,  width//2,  height//2, threshold_alpha, mutex, procCount)
        if procCount.value < 6:
            mesprocs.append(Thread(target=Decouper_en4, args=(x,  y + height//2,  width//2,  height//2, threshold_alpha, mutex, procCount, )))
            procCount.value += 1
        else:
            Decouper_en4(x,  y + height//2,  width//2,  height//2, threshold_alpha, mutex, procCount)
        
        Decouper_en4(x+width//2,  y+height//2,  width//2, height//2, threshold_alpha, mutex, procCount)
        
        for i in mesprocs:
            i.start()

        for i in mesprocs:
            i.join()



def code_projet_image() :
    # nom_fic_image="Image_Lyon.bmp"
    dir_image="Images"
    nom_fic_image="steve.png"
    nom_fic_image="Elena.png"
    nom_fic_in=dir_image+'/'+nom_fic_image
    try : 
        image_ = Image.open(nom_fic_in).convert("RGB") #  nécessaire pour une image "png"
    except :
        print("Problème avec le fichier ",nom_fic_in)
        quit(1)
        
    global matrice_pixels
    width, height=image_.size
    matrice_pixels = mp.Array('i', width*height)
    matrice_pixels = image_.load()

    #image_.show()   # Montrez l'image originale
    mutex = mp.Semaphore(1)
    procCount = mp.Value('i', 0)

    Decouper_en4(0, 0, width, height, 15, mutex, procCount) # tester avec les seuils différents 3,  10,  15,  20,  ...

    image_.show()
   
    # On sauvegarde le résultat
    nom_fic_out=dir_image+'/'+"out_"+nom_fic_image   # On construit le nom de l'image sauvegardée
    image_.save(nom_fic_out)

#=======================
# tests

if __name__ == '__main__' :
    code_projet_image()