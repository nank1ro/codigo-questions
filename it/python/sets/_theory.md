Un **set** è una collezione di elementi **unici**: lo stesso valore può comparire una sola volta, indipendentemente da quante volte lo scrivi.
Un set è anche **non ordinato**: non esiste un primo o un ultimo elemento, quindi non puoi leggere un elemento tramite indice.
I set sono ideali quando ti interessa solo *quali* valori sono presenti, non quante volte o in quale posizione.
Crei un set scrivendo i suoi elementi tra parentesi graffe `{...}`:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
Il duplicato `"red"` viene scartato, quindi `len()` conta solo gli elementi distinti.

---

La funzione predefinita `set()` costruisce un set a partire da qualsiasi collezione, ad esempio una lista o una stringa.
Poiché un set conserva ogni valore una sola volta, questo è il modo classico per **rimuovere i duplicati**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Per verificare se un valore è presente usa l'operatore `in`, che restituisce `True` o `False`:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
I controlli di appartenenza su un set sono molto veloci, anche con migliaia di elementi.

---

C'è una trappola quando si crea un **set vuoto**.
Le parentesi graffe sono anche la sintassi dei dizionari, quindi `{}` crea un **dizionario** vuoto, non un set:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Per ottenere un set vuoto devi chiamare `set()` senza argomenti:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

I set sono **mutabili**: puoi aggiungere e rimuovere elementi dopo averli creati.
`add(value)` inserisce un valore; aggiungerne uno già presente non cambia nulla:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Ci sono due modi per rimuovere un elemento:
- `remove(value)` lo elimina, ma solleva un `KeyError` se il valore non è nel set
- `discard(value)` lo elimina se presente e **non fa nulla** altrimenti, senza errori
```python
letters.remove("a")
letters.discard("z")  # "z" non c'è, ma nessun errore
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` rimuove **un elemento arbitrario** dal set e lo restituisce.
Poiché un set non ha un ordine, non puoi scegliere quale elemento viene rimosso; chiamare `pop()` su un set vuoto solleva un `KeyError`:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` rimuove **tutti** gli elementi, lasciando un set vuoto:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Puoi scorrere un set con `for`, esattamente come una lista:
```python
for color in {"red", "blue"}:
    print(color)
```
Poiché un set non è ordinato, gli elementi possono uscire in **qualsiasi ordine**, e quest'ordine può persino cambiare tra un'esecuzione e l'altra.
Quando hai bisogno di un ordine prevedibile, passa il set a `sorted()`, che restituisce una **lista** ordinata dei suoi elementi:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

L'**unione** di due set è un nuovo set con gli elementi di **entrambi**, senza duplicati.
Usa l'operatore `|` o il metodo `union()`:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Né `a` né `b` viene modificato: le operazioni sui set restituiscono sempre un nuovo set.

---

L'**intersezione** di due set contiene solo gli elementi presenti in **entrambi**.
Usa l'operatore `&` o il metodo `intersection()`:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Se i set non hanno nulla in comune, il risultato è un set vuoto.

---

La **differenza** `a - b` contiene gli elementi di `a` che **non** sono in `b`.
L'ordine conta: `a - b` e `b - a` sono di solito diversi:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
La **differenza simmetrica** `a ^ b` contiene gli elementi presenti in **esattamente uno** dei due set:
```python
print(a ^ b)  # {1, 4}
```
Le forme metodo sono `difference()` e `symmetric_difference()`.

---

Gli operatori e i metodi non sono perfettamente equivalenti.
Gli operatori `|`, `&`, `-` e `^` funzionano solo quando **entrambi** gli operandi sono set.
I metodi `union()`, `intersection()`, `difference()` e `symmetric_difference()` accettano **qualsiasi iterabile**, come una lista o una stringa:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

I set possono anche essere **confrontati** tra loro.
`a.issubset(b)`, oppure `a <= b`, è `True` quando ogni elemento di `a` è anche in `b`.
`a.issuperset(b)`, oppure `a >= b`, è `True` quando `a` contiene ogni elemento di `b`.
`a.isdisjoint(b)` è `True` quando i due set non hanno **nessun** elemento in comune:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Un set può contenere solo elementi **hashabili**, cioè valori che non possono cambiare: numeri, stringhe, `True`/`False` e **tuple**.
Provare ad aggiungere una lista, un dizionario o un altro set solleva un `TypeError`:
```python
points = set()
points.add((1, 2))  # ok, una tupla
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
I set di tuple sono comodi per tenere traccia di coppie uniche, come coordinate o record (nome, età):
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

Un **frozenset** è un set **immutabile**: una volta creato, non puoi aggiungere o rimuovere elementi.
Crealo con `frozenset()` a partire da qualsiasi collezione:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Stampare un frozenset mostra il suo tipo attorno agli elementi, come `frozenset({'sat', 'sun'})`.
Poiché non può cambiare, un frozenset è hashabile: a differenza di un set normale, può essere un elemento di un altro set o una chiave di dizionario.
Tutte le operazioni di sola lettura (`in`, `len()`, `|`, `&`, `-`, `^`, confronti) funzionano come al solito.

---

Una **set comprehension** costruisce un set in un'unica espressione, con la stessa sintassi di una list comprehension ma con le parentesi graffe:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Un `if` opzionale filtra gli elementi, e i duplicati prodotti dall'espressione vengono scartati automaticamente:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Le operazioni sui set possono anche modificare un set **sul posto** invece di restituirne uno nuovo.
`update(iterable)` aggiunge ogni elemento di qualsiasi collezione, come `add()` ma per più valori insieme:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Gli operatori aumentati funzionano anche sul posto: `|=` aggiunge gli elementi di un altro set, `&=` mantiene solo quelli comuni, `-=` rimuove gli elementi di un altro set:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Due set sono **uguali** quando contengono gli stessi elementi, indipendentemente dall'ordine in cui sono stati scritti:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Confrontare la lunghezza di una collezione con la lunghezza del suo set è un modo rapido per rilevare i duplicati: se il set è **più piccolo**, qualche valore è comparso più di una volta:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
Il metodo delle liste `count(value)` indica quante volte un valore compare, il che aiuta a trovare *quali* valori sono duplicati.
