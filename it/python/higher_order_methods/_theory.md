In Python una funzione è un **valore**, proprio come un numero o una stringa. Puoi salvarla in una variabile, metterla in una lista o passarla a un'altra funzione. Sono solo le parentesi a chiamarla: `shout` è la funzione stessa, `shout("hi")` è il suo risultato:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Una funzione che riceve un'altra funzione come parametro, o che ne restituisce una, è chiamata **funzione di ordine superiore**. Al suo interno, il parametro viene chiamato con le parentesi come qualsiasi altra funzione:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Passare una funzione come argomento permette a chi chiama di decidere **cosa** fare, mentre la funzione di ordine superiore decide **quante volte** o **su cosa**. Il parametro funzione può essere chiamato quante volte serve, e il suo risultato può essere reimmesso nella funzione:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Va bene qualsiasi callable: una funzione `def`, un built-in come `len` o una `lambda`.

---

Il built-in `map(func, iterable)` chiama `func` su ogni elemento e produce i risultati, uno per ogni elemento. Restituisce un *map object* pigro, quindi avvolgilo in `list()` per vedere i valori:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Puoi passare qualsiasi callable, non solo una lambda: un built-in come `len`, oppure un metodo preso dalla sua classe, come `str.upper`, che riceve la stringa come primo argomento:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

Il built-in `filter(func, iterable)` conserva solo gli elementi per cui `func` restituisce un valore vero. Come `map`, restituisce un oggetto pigro che deve essere trasformato in una lista:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
La funzione passata a `filter` è chiamata **predicato**: prende un elemento e risponde a una domanda sì/no su di esso. Passare `None` al posto di una funzione conserva gli elementi veri di per sé, scartando `0`, `""` e `None`.

---

`sorted(iterable, key=func)` ordina gli elementi in base al valore che `func` restituisce per ciascuno di essi, senza modificare gli elementi stessi. Aggiungi `reverse=True` per avere prima i più grandi:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
L'ordinamento è **stabile**: gli elementi con chiavi uguali mantengono il loro ordine originale. La funzione `key` viene chiamata una volta per elemento e i suoi risultati sono usati solo per confrontare, quindi l'output contiene ancora le parole originali, non le loro lunghezze.

---

La funzione `key` può scegliere **qualsiasi parte** di un elemento. Per una lista di tuple, `lambda s: s[1]` ordina in base al secondo elemento di ogni tupla; per una lista di dizionari, `lambda d: d["age"]` ordina in base a un valore:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` e `max` accettano lo stesso parametro `key`, quindi `max(pairs, key=lambda p: p[1])` restituisce `('a', 3)`: la tupla intera, non solo il numero.

---

Una funzione può anche **restituire** una funzione. Definisci una funzione interna con `def` e restituiscila senza chiamarla:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
La funzione interna continua a usare `greeting` anche dopo che `make_greeter` è terminata: **ricorda** le variabili dello scope in cui è stata creata. Una funzione del genere è chiamata **closure**. Ogni chiamata a `make_greeter` crea una nuova closure indipendente, con il suo `greeting`.

---

Una closure può leggere le variabili della funzione che la racchiude, ma assegnarne una crea una **nuova variabile locale**. Per aggiornare la variabile esterna, dichiarala con `nonlocal` all'interno della funzione interna:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` cercherebbe `count` a livello di modulo, dove non esiste. Con `nonlocal`, ogni chiamata alla funzione restituita aggiorna lo stesso `count`, così la closure porta con sé lo stato tra le chiamate, come un piccolo oggetto.

---

`reduce(func, iterable, initial)` del modulo `functools` ripiega una sequenza in un **singolo valore**. Chiama `func` con il risultato fin qui ottenuto e l'elemento successivo, partendo da `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
I passi sono `0 + 1`, poi `1 + 2`, poi `3 + 3`. Quando `initial` è omesso, il primo elemento viene usato come valore di partenza, ma in quel caso una sequenza vuota solleva un `TypeError`, quindi fornisci un valore iniziale ogni volta che la sequenza può essere vuota.

---

`partial(func, *fixed)` di `functools` costruisce una nuova funzione con alcuni argomenti **già riempiti**. Chiamare il risultato fornisce quelli rimanenti:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Gli argomenti posizionali dati a `partial` riempiono i primi parametri; gli argomenti per parola chiave fissano un parametro per nome e possono comunque essere sovrascritti alla chiamata. Un partial è un semplice callable, quindi può essere passato a `map`, `sorted` o a qualsiasi altra funzione di ordine superiore.

---

`partial` è comodo con i built-in che accettano opzioni. `int(text, base=16)` analizza una stringa esadecimale; fissare la base dà un convertitore a un solo argomento, adatto a `map`:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
L'oggetto partial ricorda cosa avvolge: `hex_to_int.func` è `int`, e `hex_to_int.keywords` è `{'base': 16}`.

---

Un **decoratore** è una funzione di ordine superiore che prende una funzione e ne restituisce una nuova che la avvolge, di solito per aggiungere un comportamento prima o dopo la chiamata originale:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` è il nome con cui la funzione è stata definita. Applicare il decoratore è semplicemente una chiamata: `greet = announce(greet)`. La sintassi `@` posta sulla riga **sopra** un `def` fa esattamente questo:
```python
@announce
def greet(name):
    return "Hello, " + name
```
Il decoratore deve essere definito prima di essere usato con `@`, perché la sostituzione avviene non appena viene eseguito il `def`.

---

Un decoratore che accetta un solo argomento è di poca utilità. Per avvolgere **qualsiasi** funzione, il wrapper raccoglie ogni argomento posizionale in `*args` e ogni argomento per parola chiave in `**kwargs`, e li inoltra invariati:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
All'interno del wrapper, `args` è una tupla e `kwargs` un dizionario; `*` e `**` nella chiamata li spacchettano di nuovo in argomenti separati.

---

`any(iterable)` restituisce `True` se **almeno un** elemento è vero, `all(iterable)` se **tutti** gli elementi lo sono. Si abbinano naturalmente a un'**espressione generatore**: una list comprehension scritta senza le parentesi quadre, che produce i valori uno alla volta invece di costruire una lista:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Poiché i valori sono prodotti pigramente, `any` si ferma al primo `True` e `all` al primo `False`, senza valutare il resto. Anche `sum` accetta un'espressione generatore: `sum(1 for age in ages if age >= 18)` conta gli adulti.
