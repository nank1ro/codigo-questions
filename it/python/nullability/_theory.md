A volte una variabile **non ha** ancora un valore da contenere: un utente che non ha effettuato l'accesso, una ricerca che non ha trovato nulla, un'impostazione mai scelta. Python rappresenta questa situazione con il valore speciale `None`.
`None` è un valore come gli altri: puoi assegnarlo, stamparlo e passarlo alle funzioni. Il suo tipo è `NoneType`, e nell'intero programma esiste esattamente **un solo** `None`, quindi ogni `None` che scrivi si riferisce allo stesso oggetto:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` non è `0`, non è una stringa vuota e non è `False`: è un valore a parte che significa "qui non c'è nulla".

---

Ogni chiamata di funzione produce un valore, anche quando la funzione non sembra restituire nulla. Una funzione **senza** istruzione `return`, o con un `return` nudo, restituisce `None`:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
Per questo chiamare `print(my_list.append(3))` mostra `None`: `append` modifica la lista sul posto e non restituisce nulla.
Una funzione che esegue solo un'azione (stampare, salvare, modificare una lista) di solito restituisce `None`, mentre una funzione che calcola qualcosa deve restituirla esplicitamente con `return`.

---

Per controllare se una variabile contiene `None`, usa `is` e `is not`, mai `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` chiede "questi valori sono *uguali*?", e qualsiasi classe può rispondere a quella domanda a suo modo definendo il metodo `__eq__`. `is` chiede "questi sono lo *stesso oggetto*?", e nulla può cambiare la risposta.
Poiché esiste un solo `None`, `is None` è sempre corretto e leggermente più veloce, mentre `== None` può dare una risposta sorprendente per oggetti con un `__eq__` personalizzato.

---

`None` vale come **falso** in una condizione, quindi `if not value:` è `True` quando `value` è `None`. È allettante usarlo come controllo per `None`, ma lo stesso test è `True` anche per `0`, `""`, `[]` e ogni altro valore vuoto:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Quando "nessun valore" e "valore vuoto" vanno trattati in modo diverso, controlla prima `is None`, poi la veridicità:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Usa `if not value:` solo quando vuoi davvero trattare `None` e i valori vuoti allo stesso modo.

---

Un parametro può avere un **valore predefinito**, usato quando chi chiama omette l'argomento. `None` è il valore predefinito usuale per "non fornito":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Questo conta per liste e dizionari. Un valore predefinito viene valutato **una sola volta**, quando la funzione è definita, quindi `def add(item, items=[])` condivide la stessa lista in ogni chiamata che omette `items`, e gli elementi si accumulano. La soluzione è usare `None` come predefinito e creare una lista nuova all'interno della funzione:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Leggere una chiave mancante da un dizionario con `[]` solleva un `KeyError`. Il metodo `get` è l'alternativa sicura: restituisce il valore quando la chiave esiste e `None` quando non esiste:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` accetta un secondo argomento, il valore da restituire **al posto di** `None` quando la chiave manca:
```python
print(ages.get("Grace", 0))  # 0
```
Questo è il modo più comune in cui `None` compare nel codice di tutti i giorni: una ricerca che non ha trovato nulla.

---

Una funzione che restituisce un numero **o** `None` dovrebbe dirlo nella sua firma. Un **type hint** è un'annotazione che documenta il tipo atteso: `name: str` per un parametro e `-> int` per il valore restituito. Python non impone i type hint, ma editor e lettori vi si affidano:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` si legge "un `int` oppure `None`". La grafia più vecchia `Optional[int]` del modulo `typing` significa esattamente la stessa cosa, e la incontrerai ancora nel codice esistente.
Ogni volta che vedi `| None` in una firma, ricorda di controllare il risultato prima di usarlo.

---

Le funzioni che possono ricevere `None` spesso iniziano con una **guardia**: un `if` che restituisce presto quando non c'è nulla su cui lavorare. Il resto della funzione può così presupporre che il valore sia presente, senza annidare tutto dentro un `else`:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Le guardie vengono prime, nell'ordine in cui i controlli devono avvenire: non puoi chiamare `text.split()` prima di sapere che `text` non è `None`.

---

L'operatore `or` non restituisce `True` o `False`: restituisce il suo operando di **sinistra** quando è vero, e quello di **destra** altrimenti. Questo offre un modo su una riga per fornire un fallback:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
Il problema è che `or` guarda la veridicità, non `None`: anche `0`, `""` e `[]` vengono sostituiti dal fallback. Usa `x or fallback` solo quando ogni valore vuoto deve diventare anch'esso il fallback.

---

Quando `0` o `""` devono essere conservati e solo `None` sostituito, il fallback richiede un controllo esplicito `is None`. La forma compatta è l'**espressione condizionale**, `a if condition else b`, che vale `a` quando la condizione è vera e `b` altrimenti:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Una lista può contenere `None` accanto a valori reali, per esempio letture fallite o risposte saltate. La maggior parte delle operazioni non lo accetta: `sum([8, None])` solleva un `TypeError`.
Elimina i valori `None` con una list comprehension la cui condizione è `is not None`:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Usare `if r` al suo posto eliminerebbe anche ogni `0`, quindi sii esplicito quando zero è una lettura valida.

---

Una ricerca seguita da un controllo su `None` di solito richiede due righe: una per salvare il risultato, una per testarlo. L'operatore di **espressione di assegnazione** `:=`, soprannominato *walrus*, assegna un valore **dentro** un'espressione, così entrambi i passi stanno nell'`if`:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Le parentesi sono obbligatorie: senza di esse, `:=` tenterebbe di assegnare l'intero confronto. Dopo l'`if`, `age` resta disponibile come qualsiasi altra variabile.

---

Non ogni "non trovato" viene segnalato con `None`. Alcune funzioni più vecchie restituiscono invece un valore **sentinella**, un valore normale a cui viene dato un significato speciale. Il metodo delle stringhe `find` restituisce l'indice di una sottostringa, oppure `-1` quando è assente:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
La funzione `re.match(pattern, text)` del modulo `re` controlla se `text` inizia con `pattern`, e restituisce un oggetto match, oppure `None` quando non c'è corrispondenza.
`None` è la convenzione più sicura: `-1` è un indice valido, quindi `text[text.find("x")]` restituisce silenziosamente l'ultimo carattere invece di fallire, mentre usare `None` come indice solleva subito un errore.

---

`None` non può essere ordinato: `None < 1` solleva un `TypeError`, perché Python non ha idea se "nulla" sia più piccolo o più grande di un numero.
Questo conta quando `None` è usato come valore iniziale di una ricerca, come "il miglior valore visto finora, se presente". Ogni confronto deve essere protetto da un controllo `is None` messo **prima**, così che `or` cortocircuiti e il confronto venga saltato quando non c'è ancora nulla da confrontare:
```python
if best is None or value > best:
    best = value
```
Scritto al contrario, `value > best or best is None` confronterebbe con `None` alla prima iterazione e andrebbe in crash.
