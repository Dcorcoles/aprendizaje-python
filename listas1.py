miLista=[1,2,3,4,5,6,7,8,9,10]
print(miLista)

# miLista2 tiene los valores (2*elemento)siendo elemento los valores de la Lista miLista
miLista2=[2*elemento for elemento in miLista]
print(miLista2)

#Crear una lista solo con los elementos pares
listaPares=[elemento for elemento in miLista if elemento%2==0]
print(listaPares)

# A la menera tradicional seria:
listaPares2=[]
for i in miLista:
    if i%2==0:
        listaPares2.append(i)
print(listaPares2)

# anidar iteracciones dentro de la lista

a=["a","b","c"]
b=[1,2,3]
##Para cada elemento de a me recorre todos los elementos de b
c=[elemento1*elemento2 for elemento1 in a for elemento2 in b]
print(c)

##Puedo incluso poner alguna condicion
c=[elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(c)




