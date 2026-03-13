# Esercizi Python

## Esercizio 1

Scrivi un programma che chieda due numeri all'utente tramite la funzione `input` e mostri il più grande tra i due utilizzando la funzione `print`.

Per quanto Python disponga di una funzione `max()`, siete invitati ad utilizzare le istruzioni `if`, `elif` ed `else` per la scrittura dell'algoritmo.

---

## Esercizio 2

Scrivi un programma che, a partire da un elemento e una lista di elementi, dica in output se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo `index()`.

---

## Esercizio 3

Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la **frequenza di comparsa** di ciascun carattere della stringa.

Esempio:

Data la stringa ababcc il risultato dovrà essere {"a": 2, "b": 2, "c": 2}


---

## Esercizio 4

1. Creare una tupla con i seguenti elementi: `"mela"`, `"banana"`, `"kiwi"`.
2. Accedere all'elemento `"banana"` della tupla precedente.
3. Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.
4. Verificare se l'elemento `"ananas"` è presente nella tupla precedente.
5. Creare una nuova tupla concatenando la tupla precedente con la tupla `("pesca", "arancia")`.

### Note: Slice (Slicing) in Python

Lo **slicing** permette di estrarre una parte di una sequenza (lista, tupla, stringa).

La sintassi generale è:

`sequenza[start:end:step]`


- `start` → indice di partenza (incluso)
- `end` → indice finale (**escluso**)
- `step` → passo di spostamento (può essere anche negativo)
Questo significa che Python prende gli elementi **da `start` fino a `end - 1`**.

Esempio:

```
lista = [10, 20, 30, 40, 50]

lista[1:3]   # [20, 30]
lista[:3]    # [10, 20, 30]  (dall'inizio)
lista[2:]    # [30, 40, 50]  (fino alla fine)
lista[-1]    # 50 (ultimo elemento)
```
---

## Esercizio 5

1. Creare una lista di numeri e assegnarla ad una variabile
2. Accedere al terzo elemento della lista
3. Rimuovere il quarto elemento della lista (usare `del`)
4. Ordinare la lista in ordine decrescente (usare `sort`)
5. Concatenare una nuova lista di numeri alla lista precedente
6. Trovare numeri duplicati nella lista finale
7. Usare lo slicing per rovesciare la lista. Esempio: [3,5,6] diventa [6,5,3] 

### Note
Per inserire variabili o espressioni direttamente dentro una stringa si usa `f"... {var}..."` che rappresenta una f-string

## Esercizio 6

1. Creare un dizionario che contiene nome, cognome e età di un utente
2. Da input da tastiera chiedere l'email all'utente
3. Aggiungere l'email al dizionario
4. Creare una lista che contenga solo le chiavi del dizionario e stamparla
5. Creare una lista che contenga solo i valori del dizionario e stamparla
6. Contare gli elementi delle due liste e fare un check per vedere se 

## Esercizio 7
Scrivere un programma che gestisca un insieme di punti nel piano cartesiano e li assegni al centroide più vicino (simulazione del clustering).

Dato un elenco di punti e due centroidi definiti, il programma deve:
1. Calcolare la distanza di ogni punto dai due centroidi
2. Assegnare ogni punto al centro più vicino
3. Mostrare i gruppi finali

### Indicazioni
Requisiti: installare matplotlib (pip install matplotlib)

Il programma va organizzato usando le seguenti funzioni
1. `math.dist(p1,p2)` è la funzione che restituisce la distanza euclidea fra due punti (N.B: importare il modulo math)
2. `assegna_punto(punto, centroide1, centroide2)` restituisce a quale centroide appartiene il punto
3. `crea_cluster(punti, centroide1, centroide2)` costituisce i cluster
4. `visualizza_cluster(cluster1, cluster2)` installare matplotlib e importarlo 
5. `main()` definisce i dati iniziali e chiama le funzioni. Il main raccoglie la logica del programma! `__main__` è un nomew speciale che Python usa per il modulo da cui parte l'esecuzione

come definire il main:

```
def main()
    dati
    chiamata alle funzioni

if __name__ == "__main__":    
    main()
    
```



## Dati da usare

```python
punti = [(1, 2), (2, 1), (6, 5), (7, 8), (1, 0), (8, 7)]
centroide1 = (0, 0)
centroide2 = (7, 7)
```

### funzione per visualizzare i cluster
```
def visualizza_cluster(cluster1, cluster2, centroide1, centroide2):
    """Visualizza i due cluster."""
    x1, y1 = zip(*cluster1)
    x2, y2 = zip(*cluster2)
    plt.scatter(x1, y1, color='blue', label='Cluster 1')
    plt.scatter(x2, y2, color='red', label='Cluster 2')
    plt.scatter(*centroide1, color='cyan', marker='X', s=200, label='Centroide 1')
    plt.scatter(*centroide2, color='magenta', marker='X', s=200, label='Centroide 2')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Visualizzazione dei Cluster')
    plt.legend()
    plt.grid()
    plt.show()
```

