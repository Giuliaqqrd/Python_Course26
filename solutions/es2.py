elementi = [5, 10, 15, 20]

user_input = int(input("Inserisci un numero: "))
if user_input in elementi:
    indice = elementi.index(user_input)
    print(f"{user_input} è presente nella lista all'indice {indice}.")
else:    
    print(f"{user_input} non è presente nella lista.")