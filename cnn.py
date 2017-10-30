import glob, os
import numpy as np
import scipy
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
    size = 20, 20
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

'''
def global_contrast_normalization(filename):
    X = np.array(Image.open(filename))
    r, c, u = X.shape
    sum_x = 0

    for i in range(r):
        for j in range(c):
            for k in range(u):
                sum_x = sum_x + X[i][j][k]
    X_average = float(sum_x) / (r * c * u)

    for i in range(r):
        for j in range(c):
            for k in range(u):
                X[i][j][k] = (X[i][j][k]) - X_average

    scipy.misc.imsave('DB_breast/result.jpg', X)

def gcn(filename, s, lmda, epsilon):
    X = np.array(Image.open(filename).convert('L'))

    X_prime = X.astype(float)
    r,c,u=X.shape
    contrast =0
    su=0
    sum_x=0

    for i in range(r):
        for j in range(c):
            for k in range(u):

                sum_x=sum_x+X[i][j][k]
    X_average=float(sum_x)/(r*c*u)

    for i in range(r):
        for j in range(c):
            for k in range(u):

                su=su+((X[i][j][k])-X_average)**2
    contrast=np.sqrt(lmda+(float(su)/(r*c*u)))


    for i in range(r):
        for j in range(c):
            for k in range(u):

                X_prime[i][j][k] = s * (X[i][j][k] - X_average) / max(epsilon, contrast)
    Image.fromarray(X_prime).save("result.jpg")
'''

imagen="DB_breast/p1.jpg"
#global_contrast_normalization(imagen)
#gcn(imagen, 1, 10, 0.000000001)
aumentoData(imagen)
normalizacion_contraste_global(imagen)
#recortarImagen(imagen)
#print(media(imagen))
#print (media("DB_breast/Patient_1_n.jpg"))