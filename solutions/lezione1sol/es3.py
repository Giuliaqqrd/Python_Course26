stringa = input("Inserisci una stringa: ").lower()
def restituisci_dict(stringa):
    dizionario = {}
    for elemento in stringa:
        if elemento in dizionario:
            dizionario[elemento] += 1 #se l'elemento è già presente, incrementa il contatore
        else:
            dizionario[elemento] = 1 #se l'elemento non è presente, aggiungilo al dizionario con contatore 1
    return dizionario

result = restituisci_dict(stringa)
print(result)