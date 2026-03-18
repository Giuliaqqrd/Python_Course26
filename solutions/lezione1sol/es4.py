frutta = ("mela", "banana", "kiwi")

elemento = frutta[1]
print(elemento)

frutta_new = frutta[0:2]
print(frutta_new)

# verificare se ananas è presente nella tupla
if "ananas" in frutta:
    print("Ananas è presente nella tupla.")
else:    
    print("Ananas non è presente nella tupla.")

nuova_frutta = frutta + ("pesca", "arancia")
print(nuova_frutta)


