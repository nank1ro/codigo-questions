Gli operatori di confronto confrontano due valori e restituiscono un **booleano**, `True` o `False`: `==` uguale, `!=` diverso, `<` minore di, `>` maggiore di, `<=` minore o uguale, `>=` maggiore o uguale:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
Il risultato può essere memorizzato in una variabile o stampato direttamente. Un singolo `=` è un'assegnazione, non un confronto.

---

Gli operatori di confronto non sono limitati ai numeri. Le stringhe vengono confrontate carattere per carattere usando i loro code point, quindi `"apple" < "banana"` è `True` e, poiché ogni lettera maiuscola viene prima di quelle minuscole, anche `"Zoo" < "apple"` è `True`. Liste e tuple vengono confrontate elemento per elemento allo stesso modo:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Un confronto è un'espressione, quindi una funzione può fare `return a < b` direttamente invece di racchiuderlo in un `if`.

---

I confronti possono essere **concatenati**: `1 < x < 10` verifica che `x` sia maggiore di `1` **e** minore di `10`, esattamente come `1 < x and x < 10`, ma `x` viene valutato una sola volta:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Qualsiasi operatore di confronto può essere concatenato e ognuno si applica ai suoi due vicini: `a < b == c` significa `a < b and b == c`. Leggere una catena come un intervallo, `low < x < high`, è l'uso più comune.

---

Gli operatori logici combinano booleani. `and` è `True` solo quando entrambi i lati sono `True`, `or` quando almeno un lato lo è, e `not` inverte un singolo valore:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
I confronti hanno precedenza maggiore rispetto agli operatori logici, quindi `age >= 18 and member` non richiede parentesi. Le parentesi servono per raggruppare un `or` dentro un `and`: `a and (b or c)`.

---

Quando `not`, `and` e `or` compaiono in una stessa espressione, Python applica prima `not`, poi `and`, poi `or`. Quindi `a or b and c` significa `a or (b and c)`, e `not a == b` significa `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Quando si intende un raggruppamento diverso, aggiungi le parentesi; rendono anche l'espressione più leggibile.

---

Ogni valore ha un **valore di verità**. `bool(value)` restituisce `False` per `0`, `0.0`, `None`, la stringa vuota `""` e i contenitori vuoti come `[]`, `{}` e `set()`; ogni altro valore è vero, inclusi `"0"` e `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` e `not` usano questa regola, quindi `if items:` verifica che la lista non sia vuota e `not name` verifica che la stringa sia vuota; non serve scrivere `len(items) > 0` o `name == ""`.

---

Poiché `if value:` applica già il valore di verità, confrontare con `== True` o `== False` è inutile e può persino essere sbagliato: `2 == True` è `False`, eppure `2` è vero. Verifica il valore stesso:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` e `or` non restituiscono sempre `True` o `False`: restituiscono uno dei loro **operandi**. `a and b` restituisce `a` se è falso, altrimenti `b`; `a or b` restituisce `a` se è vero, altrimenti `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
Il risultato è vero o falso esattamente quando lo è l'intera espressione, ed è per questo che `if a and b:` funziona comunque. Un uso comune è il valore predefinito: `name = user_input or "guest"`.

---

Gli operatori logici sono a **corto circuito**: `and` si ferma appena un operando è falso e `or` appena uno è vero, perché il risultato è già noto. Gli operandi rimanenti non vengono mai valutati, quindi se sono chiamate di funzione non vengono eseguite:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` confronta i **valori**; `is` confronta l'**identità**, cioè se entrambi i nomi si riferiscono allo stesso identico oggetto. Due liste uguali costruite separatamente sono `==` ma non `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` è pensato per i singleton come `None`, `True` e `False`: scrivi `value is None` o `value is not None`, mai `value == None`, perché una classe può definire `==` in modo che restituisca qualsiasi cosa. Usare `is` con numeri o stringhe non è affidabile e Python lo segnala.

---

La valutazione a corto circuito è un modo sicuro per **proteggere** un'operazione che fallirebbe su alcuni valori. In `word is not None and len(word) < 4`, `len(word)` viene eseguito solo quando `word` non è `None`, quindi la chiamata non solleva mai un errore. La protezione deve venire per prima:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Tieni presente che `and` restituisce un operando: `word and len(word) < 4` dà `None` per `None` e `""` per la stringa vuota, non `False`. Proteggi con un confronto vero e proprio quando serve un booleano.

---

L'operatore `in` verifica l'**appartenenza**: se un elemento è in una lista, tupla o insieme, se una sottostringa è in una stringa, o se una chiave è in un dizionario. `not in` è la sua negazione:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Entrambi restituiscono un booleano e si leggono come l'inglese, il che li rende il modo preferito per verificare l'appartenenza invece di scrivere un ciclo.
