A volte serve una piccola funzione una sola volta, per esempio per raddoppiare un numero.
Scrivere un intero blocco `def` per questo sembra eccessivo.
Python offre una forma più breve: l'espressione **lambda**, una funzione _anonima_ scritta su una singola riga:
```python
lambda x: x * 2
```
La sintassi è `lambda parametri: espressione`.
Una lambda non ha un nome, ma puoi salvarla in una variabile e chiamarla come qualsiasi altra funzione:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Nota che il corpo della lambda non ha la parola chiave `return`.
Il corpo è una **singola espressione**, e il suo valore viene restituito automaticamente:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Una lambda può prendere **più di un parametro**.
Separali con virgole, esattamente come in una funzione `def`:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Poiché il corpo deve essere una singola espressione, una lambda **non può contenere istruzioni**.
Né `return`, né blocchi `if`, né cicli, né assegnazioni:
```python
# SyntaxError
increment = lambda x: return x + 1
```
Se ti serve qualcosa di tutto ciò, scrivi invece una normale funzione `def`.

---

I parametri di una lambda supportano anche i **valori predefiniti**:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Non devi nemmeno salvare una lambda: puoi **chiamarla immediatamente**.
Racchiudi la lambda tra parentesi, poi aggiungi gli argomenti:
```python
print((lambda x: x + 1)(4))  # 5
```

---

Le lambda danno il meglio di sé come **argomenti di altre funzioni**.
`sorted()` accetta un parametro `key`: una funzione chiamata su ogni elemento, il cui risultato decide l'ordine.
Una lambda è perfetta per questo:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

La lambda `key` può scegliere qualsiasi parte di un elemento.
Per una lista di liste, `lambda p: p[1]` ordina in base al secondo elemento di ogni lista interna.

---

`map()` applica una funzione a **ogni elemento** di una lista.
Restituisce un particolare _oggetto map_, quindi racchiudilo in `list()` per vedere i valori:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` mantiene solo gli elementi per cui la funzione restituisce `True`:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Stampare direttamente un oggetto `map` non ne mostra i valori: ottieni qualcosa come `<map object at 0x7f2b1c>`.
Solo `list()` (o un ciclo) lo trasforma nei valori che ti aspetti.

---

Le lambda non si limitano alle funzioni integrate: **le tue funzioni** possono prendere una funzione come parametro e chiamarla.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

Anche `max()` e `min()` accettano una funzione `key`, proprio come `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**Quando dovresti preferire `def`?**
Una lambda è ottima per una funzione breve e usa e getta passata come argomento.
Se la logica ha bisogno di un nome, di più righe, di una docstring, o viene riutilizzata in molti punti, una funzione `def` è più chiara.
Un ultimo trucco: `sorted()` accetta anche `reverse=True` per ottenere prima i valori più grandi:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
