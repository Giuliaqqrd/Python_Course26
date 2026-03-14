numero1 = input("Inserisci un numero: ").lower()
numero2 = input("Inserisci un altro numero: ").lower()
numero1 = int(numero1)
numero2 = int(numero2)

if numero1 > numero2:
    print(f"{numero1} è maggiore di {numero2}")
elif numero1 < numero2:
    print(f"{numero1} è minore di {numero2}")
else:
    print(f"{numero1} è uguale a {numero2}")