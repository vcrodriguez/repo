import astropy.coordinates as coord
from astropy.io import fits
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
g=open("circle.txt","rb")
tabla=g.read()
tabla=tabla.split("\n")
g.close()
tablita=[]
y=[]
x=[]
contador=-1
for i in tabla:
    contador+=1
    if contador>5:
        i=i.split("\t")
        for j in i:
            j=j.split(",")
            y.append(j[1])
            for k in j:
                k=k.split("(")
                if k[0]=="circle":
                    x.append(k[1])
ls=[]
for i in range(len(x)):
    lista=[]
    if x[i].find(".") != -1:
        d=x[i].find(".")
        s=x[i][:d]
        lista.append(s)
    else:
        lista.append(x[i])
    if y[i].find(".") != -1:
        e=y[i].find(".")
        a=y[i][:e]
        lista.append(a)
    else:
        lista.append(y[i])
    ls.append(lista)
ir=fits.open("r.fits")
datr=ir[0].data
ir.close()
ig=fits.open("g.fits")
datg=ig[0].data
ig.close()
valueg=[]
valuer=[]
contador=0
d=[]
# cielo
for j in range(500):
    h=min(datr[j])
    d.append(h)
cielo=np.mean(d)
# value_r
for i in range(len(ls)):
    a=ls[i][0]
    b=ls[i][1]
    valuer.append(datr[b,a])
for i in range(len(ls)):
    a=ls[i][0]
    b=ls[i][1]
    valueg.append(datg[b,a])
gr=[]
contador=0
# g-r
for i in range(len(ls)):
    a=ls[i][0]
    b=ls[i][1]
    c=float(datg[b,a])-float(datr[b,a])
    gr.append(c)
print gr
mg=2.5*np.log10(valueg-cielo)+25
mr=2.5*np.log10(valuer-cielo)+25
gr=mg-mr
'''
plt.scatter(gr,mr)
plt.title("Diagrama H-R 1 pixel")
plt.xlabel("green-red")
plt.ylabel("red")
plt.gca().invert_yaxis()
plt.show()
'''
#valores de ambas imagenes y cielo
# sumar cuentas
# value_r 3x3
cuentasr3=[]
cuentasg3=[]
'''
for i in range(len(ls)):
    a=ls[i][0]
    b=ls[i][1]
    c=int(a)+1
    d=int(a)-1
    e=int(b)-1
    f=int(b)+1
    sumar=0
    sumar+=float(datr[b,a])+float(datr[f,c])+float(datr[e,d])
    sumar+=float(datr[e,a])+float(datr[e,c])+float(datr[b,d])
    sumar+=float(datr[b,c])+float(datr[f,a])+float(datr[f,d])
    cuentasr3.append(sumar)
    sumag=0
    sumag+=float(datg[b,a])+float(datg[f,c])+float(datg[e,d])
    sumag+=float(datg[e,a])+float(datg[e,c])+float(datg[b,d])
    sumag+=float(datg[b,c])+float(datg[f,a])+float(datg[f,d])
    cuentasg3.append(sumag)
'''
n=[0,1]
for i in range(len(ls)):
    x=ls[i][1]
    y=ls[i][0]
    sumar=0
    sumag=0
    for j in n:
        for k in n:
            m=int(x)+int(j)
            l=int(y)+int(k)
            if m>500 or l>500 or m<0 or l<0:
                a="ja"
            else:
                sumar+=float(datr[m,l])
                sumag+=float(datg[m,l])
    cuentasg3.append(sumag)
    cuentasr3.append(sumar)
mg3=2.5*np.log10(cuentasg3-cielo)+25
mr3=2.5*np.log10(cuentasr3-cielo)+25
gr=mg3-mr3
'''
plt.scatter(gr,mr3)
plt.title("Diagrama H-R 3x3")
plt.xlabel("green-red")
plt.ylabel("red")
plt.gca().invert_yaxis()
plt.show()
'''
cuentasg5=[]
cuentasr5=[]
n=[0,1,2]
for i in range(len(ls)):
    x=ls[i][1]
    y=ls[i][0]
    sumar=0
    sumag=0
    for j in n:
        for k in n:
            m=int(x)+int(j)
            l=int(y)+int(k)
            if m>500 or l>500 or m<0 or l<0:
                a="ja"
            else:
                sumar+=float(datr[m,l])
                sumag+=float(datg[m,l])
    cuentasg5.append(sumag)
    cuentasr5.append(sumar)
mg5=2.5*np.log10(cuentasg5-cielo)+25
mr5=2.5*np.log10(cuentasr5-cielo)+25
gr=mg5-mr5
'''
plt.plot(gr,mr5,"ro")
plt.title("Diagrama H-R 5x5")
plt.xlabel("green-red")
plt.ylabel("red")
plt.gca().invert_yaxis()
plt.show()
'''
n=[0,1,2,3]
cuentasr7=[]
cuentasg7=[]
for i in range(len(ls)):
    x=ls[i][1]
    y=ls[i][0]
    sumar=0
    sumag=0
    for j in n:
        for k in n:
            m=int(x)+int(j)
            l=int(y)+int(k)
            if m>500 or l>500 or m<0 or l<0:
                a="ja"
            else:
                sumar+=float(datr[m,l])
                sumag+=float(datg[m,l])
    cuentasg7.append(sumag)
    cuentasr7.append(sumar)
mg7=2.5*np.log10(cuentasg7-cielo)+25
mr7=2.5*np.log10(cuentasr7-cielo)+25
gr=mg7-mr7
'''
plt.scatter(gr,mr7)
plt.title("Diagrama H-R 7x7")
plt.xlabel("green-red")
plt.ylabel("red")
plt.gca().invert_yaxis()
plt.show()
'''
ta=open("nuevo.txt","w")
ta.write(" x\t y\t\tvalue_r\t\tvalue_g\t\t\tm_r5\t\tm_g5\n")
#ta.write(" x\t y\tvalue_r\tvalue_g\tm_r\tm_g\tm_r3\tm_g3\tm_r5\tm_g5\tm_r7\tm_g7\n")
for i in range(len(ls)):
    #ta.write()
    ta.write(str(ls[i][0])+"\t"+str(ls[i][1])+"\t\t"+str(valuer[i])+"\t\t"+str(valueg[i])+"\t\t"+str(mg5[i])+"\t\t"+str(mr5[i])+"\n")
ta.write("cielo: "+str(cielo))
ta.close
