Un compito molto comune è costruire una nuova lista a partire da una esistente.
Con un ciclo `for` e `append()` servono alcune righe:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python offre una forma più breve per esattamente questo compito: la **list comprehension**, che costruisce l'intera lista in una singola espressione:
```python
doubled = [n * 2 for n in nums]
```
La sintassi è `[espressione for elemento in iterabile]`: la parte `for` scorre gli elementi, e l'espressione a sinistra viene valutata per ciascuno di essi.
Il risultato è una lista completamente nuova, esattamente uguale a quella costruita con il ciclo.

---

L'espressione a sinistra può essere qualsiasi cosa che produca un valore: un calcolo, una chiamata a funzione, una chiamata a metodo.
La variabile del ciclo può avere qualsiasi nome tu voglia, ed esiste solo all'interno delle parentesi quadre:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Una comprehension può anche **filtrare** gli elementi.
Aggiungi una condizione `if` dopo la parte `for`: solo gli elementi per cui la condizione è `True` finiscono nella nuova lista:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
Questo è lo stesso di un ciclo con un `if` al suo interno, e sostituisce `filter()` con una lambda in modo più leggibile.

---

La condizione di filtro può essere qualsiasi espressione che restituisca un booleano, incluse chiamate a funzione come `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

L'iterabile non deve per forza essere una lista: funziona qualsiasi cosa su cui puoi ciclare, e `range()` è un favorito.
È il modo più rapido per costruire una lista di numeri:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Ricorda che `range(start, stop)` esclude `stop`.

---

Le comprehension sono ottime per **trasformare le stringhe**.
Chiama un metodo stringa su ogni elemento, oppure costruisci una nuova stringa con una f-string:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

All'interno di una comprehension puoi usare qualsiasi variabile definita prima, per esempio come limite di un `range()`.

---

A volte non vuoi scartare elementi, ma scegliere **un valore diverso** per alcuni di essi.
Usa un'espressione condizionale `a if condizione else b` come espressione, a sinistra del `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Nota la posizione: l'`if-else` va **prima** del `for` e produce sempre un valore, mentre il filtro `if` va **dopo** il `for` e non ha `else`.

---

Le due condizioni possono essere combinate nella stessa comprehension: un `if-else` per scegliere il valore, e un filtro `if` alla fine per saltare alcuni elementi.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

Le due posizioni di `if` si confondono facilmente, quindi tienile distinte:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else prima del for: sceglie un valore, else obbligatorio
positives = [n for n in nums if n > 0]      # if dopo il for: filtra, else non consentito
```
Mettere un `else` dopo il filtro `if` è un errore di sintassi.

---

Una comprehension può avere **più di un `for`**.
Funzionano come cicli annidati: il primo `for` è il ciclo esterno, il secondo è quello interno.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

Il `for` interno può usare la variabile di quello esterno.
Questo è il modo classico per **appiattire** una lista di liste in un'unica lista:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
La funzione `sum()` poi somma tutti i numeri di una lista.

---

Puoi anche ciclare su un **dizionario**.
Con `.items()` la parte `for` scompatta ogni coppia in due variabili, una chiave e un valore:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

La stessa idea funziona per i dizionari: una **dict comprehension** usa le parentesi graffe e un'espressione `key: value`:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Le parentesi graffe **senza** la parte `key: value` danno una **set comprehension**.
Un set è una collezione non ordinata che mantiene solo valori unici, quindi i duplicati scompaiono automaticamente:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**Quando dovresti usare una comprehension?**
È perfetta quando il risultato è una lista (o un dict, o un set) e la logica sta in una riga leggibile: una trasformazione semplice, un filtro opzionale.
Se hai bisogno di più istruzioni, più di due `for` annidati, o la riga diventa difficile da leggere, scrivi invece un semplice ciclo `for`: il codice sarà più lungo, ma più chiaro.
Una comprehension sostituisce anche la maggior parte degli usi di `map()` e `filter()` con le lambda:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
