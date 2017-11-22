import glob, os
import scipy.misc
from PIL import Image
import tensorflow as tf

grados=[45,90,135,180,225,270,315]
scale=256

def tamImagen(imagen):
    im = Image.open(imagen)
    pix = im.load()
    x=0
    y=0
    print ("Tamanio:",im.size)
    #print (pix[x,y])
    return im.size

def rotarImagen(imagen,grado):
    ima = Image.open(imagen)
    ima = ima.rotate(grado)
    ima.save(imagen[:-4]+"_"+str(grado)+".jpg")

def recortarImagen(imagen):
    size = 150,150
    for infile in glob.glob(imagen):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(file + "_n.jpg")

def aumentoData(imagen):
    for g in grados:
        rotarImagen(imagen,g)

def normalizacion_contraste_global(imagen):
    im = Image.open(imagen).convert('L')
    pix = im.load()
    w = im.size[0]
    h = im.size[1]
    print("Tamanio:", w, h)
    m = 0
    for i in range(w):
        for j in range(h):
            if (pix[i, j] > 0):
                m = (m + pix[i, j])
    m=int(m/(w*h))
    print('Media: ',m)

    for i in range(w):
        for j in range(h):
            pix[i,j]= pix[i, j]-m

    im.save(imagen[:-4]+"_GCN"+".jpg")

def vecinos_gaussian(imagen,size,i,j):
    im = Image.open(imagen).convert('L')
    pix = im.load()
    sum=0
    propiedad=1/size
    for p in range(size):
        for q in range(size):
            sum = sum + (propiedad*pix[p+i, q+j])

    return sum
def normalizacion_contraste_local(imagen,gauss,size):
    im = Image.open(imagen).convert('L')
    pix = im.load()

    w = im.size[0]
    h = im.size[1]
    for i in range(10):
        for j in range(10):
           pix[i,j] = pix[i, j]- int(vecinos_gaussian(imagen,size,i,j))
    im.save(imagen[:-4]+"_V"+".jpg")




imagen="DB_breast/p1.jpg"
#global_contrast_normalization(imagen)
#gcn(imagen, 1, 10, 0.000000001)
#recortarImagen(imagen)
aumentoData(imagen)
normalizacion_contraste_global(imagen)
#normalizacion_contraste_local(imagen[:-4]+"_GCN"+".jpg","",5)
#print(media(imagen))
#print (media("DB_breast/Patient_1_n.jpg"))