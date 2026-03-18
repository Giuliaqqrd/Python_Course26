utente = {"nome": "Mario", "cognome": "Rossi", "età": 30}

email = input("Inserisci la tua email: ").lower()

if email not in utente:
    utente["email"] = email
    print("Email aggiunta al dizionario.")
    print(utente)

key_list = list(utente.keys())
print(key_list)
value_list = list(utente.values())
print(value_list)

numero_chiavi = len(key_list)
print(f"Il numero di chiavi nel dizionario è: {numero_chiavi}")
numero_valori = len(value_list)
print(f"Il numero di valori nel dizionario è: {numero_valori}")

#check se chiavi e valori corrispondono
if numero_chiavi == numero_valori:
    print("Il numero di chiavi e valori corrisponde.")
else:    
    print("Il numero di chiavi e valori non corrisponde.")







