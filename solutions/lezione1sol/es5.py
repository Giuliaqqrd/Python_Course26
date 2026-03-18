numeri = [1, 2, 3, 4, 5]

terzo_elemento = numeri[2]
print(terzo_elemento)

del numeri[3]

numeri.sort(reverse=True)

nuovi_numeri = numeri + [6, 7, 8, 3, 5]
print(nuovi_numeri)

#oppure
# numeri.extend([6, 7, 8])
# print(numeri)

#trova duplicati nella lista
for i in range(len(nuovi_numeri)):
    for j in range(i + 1, len(nuovi_numeri)):
        if nuovi_numeri[i] == nuovi_numeri[j]:
            print(f"Il numero {nuovi_numeri[i]} è duplicato.")

#Versione alternativa con set

visti = set()

for n in nuovi_numeri:
    if n in visti:
        print(f"Il numero {n} è duplicato.")
    else:
        visti.add(n)


# rovesciare la lista con lo slicing
lista_rovesciata = nuovi_numeri[::-1]
print(lista_rovesciata)

# con reverse
nuovi_numeri.reverse()
print(nuovi_numeri)
