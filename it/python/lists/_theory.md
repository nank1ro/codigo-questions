Le liste sono un tipo di dati che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
Una lista memorizza valori multipli di qualsiasi tipo e utilizza gli **indici** per distinguere questi valori.
E' possibile assegnare gli elementi ad una lista con un'espressione della forma:
```python
nome_lista = [item1, item2]
```

---

E' possibile accedere ad un singolo valore della lista tramite il suo indice.
Un indice e' come un indirizzo che identifica il posto dell'elemento nella lista.
L'indice si inserisce direttamente dopo il nome della lista, tra le parentesi quadre, in questo modo:
```python
nome_lista[indice]
```
Gli indici delle liste iniziano con `0`, **non** `1`! Per ottenere il primo valore della lista usiamo: `nome_lista[0]`.
Il secondo elemento della lista si trova all'indice 1: `nome_lista[1]`.

---

L'indice di una lista si comporta come qualsiasi altro nome di variabile!
Può essere usato per ottenere e assegnare valori.
Abbiamo visto come accedere ad una valore di una lista:
```python
nomi = ["Jeremiah", "Barney", "Ivan", "Noel"]
nomi[0] # Ottieni il valore "Jeremiah"
```
Ecco come funziona l'assegnazione:
```python
nomi = ["Jeremiah", "Barney", "Ivan", "Noel"]
nomi[0] = "Jordan"
nomi[0] # Ottieni il valore "Jordan"
```

---

Proprio come le stringhe, le liste hanno una lunghezza.
La lunghezza di una lista e' il numero di elementi che contiene

---

Una lista non deve avere una lunghezza fissa.
Puoi aggiungere elementi alla fine di una lista quando vuoi!
Per aggiungere un elemento ad una lista usiamo la parola chiave `append`:
```python
>>> lettere = ["a", "b"]
>>> lettere.append("c")
>>> print(lettere)
['a', 'b', 'c']
```

---

A volte si vuole accedere solo a una parte di una lista.
Considera il seguente codice:
```python
>>> numeri = [1, 2, 3, 4]
>>> fetta = numeri[1:3]
>>> print(fetta)
[2, 3]
```
Per prima cosa, creiamo una lista chiamata `numeri`.
Poi, prendiamo una sottosezione della lista e la memorizziamo nella nuova lista `fetta`.
Lo facciamo definendo gli indici che vogliamo includere dopo il nome: `numeri[1:3]`.
In Python, quando specifichiamo una porzione di una lista in questo modo, includiamo l'elemento con il primo indice, `1`, ma escludiamo l'elemento con il secondo indice, `3`.

---

Si può tagliare una stringa esattamente come una lista! Infatti, si può pensare alle stringhe come a liste di caratteri: ogni carattere e' un elemento sequenziale nella lista, a partire dall'indice `0`.
```python
nome_lista[:2]
# Ottieni i primi due elementi
nome_lista[3:]
# Ottieni dal quarto fino all'ultimo elemento
```
Se la tua fetta comprende il primo o l'ultimo elemento di una lista (o una stringa), l'indice non deve essere incluso

---

Gli elementi della lista possono essere di qualsiasi tipo:
```python
nome_lista = ["uno", 2, True]
```
Difatti, sopra abbiamo, in quest'ordine, una stringa, un intero e un booleano.
Ma possiamo anche avere una lista di liste, e così via!

---

A volte e' necessario cercare un elemento in una lista.
In Python possiamo usare il metodo `index()`:
```python
>>> nomi = ["Trevor", "Zac", "Glenn"]
>>> print(nomi.index("Zac"))
1
```
Il codice qui sopra stampa il primo indice che contiene la stringa `"Zac"`, `1` in questo caso.
Possiamo anche inserire elementi in una lista in un indice specifico, usando il metodo `insert()`:
```python
>>> nomi.insert(1, "Ali")
>>> print(nomi)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
Il codice qui sopra inserisce `"Ali"` all'indice `1`, e incrementa l'indice di 1 a tutti gli elementi che lo seguono

---

In Python possiamo far scorrere una lista in un ciclo in un modo molto semplice usando le parole chiave `for..in`:
```python
>>> numeri = [1, 2, 3]
>>> for num in numeri:
>>> 	print(num)
1
2
3
```
Un nome di variabile segue la parola chiave `for`, ad essa verrà assegnato il valore di ogni elemento della lista a turno.

---

Le **tuple** sono come le liste, ma sono molto piu' veloci.
Tuttavia, i valori delle tuple non possono essere modificat.
Tendiamo ad usare le tuple per i dati **di sola lettura** che rimangono costanti mentre il programma e' in esecuzione.
Per creare una tupla usiamo le parentesi tonde `()`.

---

Ci possono essere momenti in cui vogliamo modificare la nostra tupla in una lista.
Per fare ciò, possiamo usare la funzione `list()`

---

Allo stesso modo, possiamo convertire una lista in una tupla
