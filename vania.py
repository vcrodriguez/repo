from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import math

im=fits.open("spDR2-008.fit")
data=im[0].data
im.close()
g=open("filtroG.txt")
r=open("filtroR.txt")
tabla=g.read()
tabla=tabla.split("\n")
g.close()
tablaR=r.read()
tablaR=tablaR.split("\n")
r.close()
tablita=[]
contador=-1
for i in tabla:
    contador+=1
    if contador>5:
        i=i.split("\t")
        for j in i:
            j=j.split()
            tablita.append(j)
x=[]
y=[]
for i in range(len(tablita)-1):
    x.append(tablita[i][0])
    h=float(tablita[i][1])*700
    y.append(h)
tr=[]
contador=-1
for i in tablaR:
    contador+=1
    if contador>5:
        i=i.split("\t")
        for j in i:
            j=j.split()
            tr.append(j)
w=[]
z=[]
for i in range(len(tr)-1):
    w.append(tr[i][0])
    h=float(tr[i][1])*500
    z.append(h)
#curvas de transmision g y r
'''
plt.plot(x,y)
plt.plot(w,z)
#estrella similar al sol
plt.plot(np.arange(4000,4000+data[0].size), data[0])
plt.show()
'''
#Cuerpo Negro, ley de planck
h=constants.value("Planck constant in eV s")
#print "constante de planck: "+str(h)
c=constants.value("speed of light in vacuum") #metros/segundos
#print "speed of light in vacuum: "+str(c)
#k=constants.value("Boltzmann constant in eV/K")
k=8.6173324E-15
#print "Boltzmann constant: "+str(k)
T=5000
l=np.linspace(1000,13000,1000)
densidad=((8*np.pi*h*c**2)/(l**5))/(np.exp((h*c)/(l*k*T))-1)
plt.plot(l,densidad)


plt.title("Spectrum of black body 5000 K")
plt.xlabel("Wanvelength")
plt.ylabel("Spectral energy density")
plt.show()
'''
l=np.linspace(300,7000,1000)
c=3e14 # speed of light
h=6.626e-22 # Planck constant
k=1.38e-11 # Boltzmann constant
# Planck curves
#p1=1e-6*2*h*c**2/(l**5*(np.exp(h*c/(l*k*3000))-1))
#p2=1e-6*2*h*c**2/(l**5*(np.exp(h*c/(l*k*4000))-1))
p3=1e-6*2*h*c**2/(l**5*(np.exp(h*c/(l*k*T))-1))
#p4=1e-6*2*h*c**2/(l**5*(np.exp(h*c/(l*k*6000))-1))
#plt.plot(l,p1)
#plt.plot(l,p2)
plt.plot(l,p3)
#plt.plot(l,p4)
plt.xlabel("Wanvelength")
plt.ylabel("Spectral energy density")
plt.title("Spectrum of black body 5000 K")
plt.show()
# FALTAN LAS UNIDADES EN EL GRAFICO

#Comparacion
#plt.plot(x,y)
#plt.plot(w,z)
l=np.linspace(500,8000,1000)
#p3=1e-6*2*h*c**2/(l**5*(np.exp(h*c/(l*k*5000))-1))
p=8*np.pi*h*c**2/(l**5*(np.exp(h*c/(l*k*5000))-1))
plt.plot(l,p*500)
plt.plot(np.arange(4000,4000+data[0].size), data[0]/50)
plt.show()
'''
