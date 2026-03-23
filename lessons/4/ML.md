# Machine Learning basics
Un computer impara dall'*esperienza* **E** rispetto ad una classe di *tasks* **T** e ad una misura della *performance* **P**, se la sua performance su **T** misurata con **P**, migliora con l'esperienza **E**.

### ML vs Data Science
La Data Science studia come estrarre significato da grandi quantità di dati. Questa conoscenza viene sfruttata dal Machine Learning, che include tecniche per apprendere autonomamente dai dati e informare predizioni future. Le due discipline sono interconnesse, ma il campo della Data Science è più ampio e comprende tutto il **ciclo di vita** del dato.


## Terminologia e definizioni 
Il processo attraverso cui vengono usati algoritmi per costruire modelli a partire dai dati viene definito **apprendimento** o **training**. 

L'apprendimento può essere:
> Supervisionato: dati etichettati.

>Non supervisionato: dati non etichettati.

**Training data**: dati usati nella fase di addestramento

**Training example**: esempio di training. Una singola istanza di un set di dati.

**Training set**: insieme di tutti i dati usati per l'addestramento.

**Hypotesis**: modo alternativo per definire un modello appreso. Viene chiamato anche ipotesi perchè corrisponde alle regole sottostanti i dati che vengono apprese.

**Facts/Ground-truth**: regole sottostanti i dati.

> Una buona ipotesi deve essere in grado di approssimare il ground-truth su dati non ancora visti.
> **Goal:** apprendere un modello che sia in grado di **generalizzare** su dati mai visti.

### No Free Lunch Theorem
Informalmente: non esiste un algoritmo di Machine Learning che è universalmente migliore di un altro su tutti i problemi possibili.

In sostanza, dobbiamo trovare l'algoritmo che performa meglio per lo specifico problema in esame.

## Model selection and Evaluation
Uno degli obiettivi dell'addestramento è quello di minimizzare l'**errore di generalizzazione**. MA, mentre addestriamo non abbiamo accesso ai nuovi dati, di conseguenza stiamo approssimando la generalizzazione minimizzando l'errore sui dati di training.

**Overfitting:** situazione in cui il modello si adatta troppo ai dati di training. Il nostro modello performa benissimo sui dati già visti e male su quelli nuovi.

**Underfitting:** situazione opposta all'overfitting. Il modello è troppo semplice per catturare il significato dei dati.

***Come scegliamo il modello migliore per i dati che abbiamo a disposizione?*** Tramite l'Evaluation (valutazione).

**Test set**: percentuale di dati del training set che non verrà utilizzata durante l'addestramento. Viene utilizzato per valutare le performance del modello addestrato simulando la situazione in cui si presentano dati nuovi. Split ratio: scelta di "quanti" dati tenere per il test set. Solitamente è 80 training e 20 test, ma può dipendere dalla dimensione del dataset e dal problema.

Se il dataset è molto piccolo, spesso si ricorre alla **Cross Validation**: serve per mitigare problemi come l'overfitting o il bias di selezione. Consiste nel dividere l'intero dataset in sottoinsiemi (K) e iterativamente scegliere uno dei K come test set. Il modello viene addestrato su K-1 dati e testato sul rimanente; l'intero processo viene ripetuto K volte. Le performance finali saranno date da una media dei risultati ottenuti su tutti i sottoinsiemi. *Nota:* stiamo parlando della K-fold cross validation, ma esistono anche altri metodi.

**Validation set**: sottoinsieme del dataset usato per la validazione durante il training.






