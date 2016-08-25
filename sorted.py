g=open("nuevo.txt","rb")
tabla=g.read()
tabla=tabla.split("\n")
g.close()
print tabla
t=sorted(tabla)
a=open("sorted.txt","w")
for i in range(len(tabla)):
    print t[i]
    a.write(str(t[i])+"\n")
a.close()
