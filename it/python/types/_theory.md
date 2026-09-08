Ogni valore in Python ha un **tipo** che indica che tipo di dato è e cosa puoi farci.
I tipi di base integrati sono:
- `int`, un numero intero come `42` o `-3`
- `float`, un numero con una parte decimale come `3.5`
- `str`, un pezzo di testo come `"hello"`
- `bool`, uno dei due valori `True` e `False`
- `NoneType`, il tipo del valore speciale `None`, che significa "nessun valore"

La funzione integrata `type()` restituisce il tipo di un valore. Stampandolo si vede il nome della classe:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
Non scriverai mai `NoneType` tu stesso: `type(None)` lo restituisce, ma il nome non è un built-in come gli altri quattro.

---

`type()` restituisce la classe di un valore, quindi puoi confrontarla con il nome di una classe usando `is`:
```python
age = 30
print(type(age) is int)  # True
```
Il più delle volte, però, vuoi solo sapere **se** un valore è di un certo tipo. È il compito di `isinstance(value, cls)`, che restituisce `True` o `False`:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
Il secondo argomento può anche essere una **tupla** di classi: il risultato è `True` se il valore appartiene a una di esse:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python è **a tipizzazione dinamica**: il tipo appartiene al **valore**, non alla variabile.
Una variabile è solo un nome collegato a un valore, e puoi collegarlo a un valore di un tipo diverso in qualsiasi momento:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
Non serve né una dichiarazione né una conversione: il vecchio valore viene semplicemente dimenticato.
È comodo, ma significa anche che il tipo di una variabile è noto solo quando il programma è in esecuzione, quindi mescolare i tipi per errore si manifesta come un errore in fase di esecuzione, non prima.

---

Conosci già gli operatori aritmetici. Quello che conta qui è il **tipo del risultato**.
Combinare un `int` con un `float` dà un `float`, anche quando la parte decimale è zero:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
La **divisione vera** `/` restituisce sempre un `float`, anche quando i numeri si dividono esattamente:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
La **divisione intera** `//` arrotonda il risultato verso il basso al numero intero più vicino (quindi `-7 // 2` è `-4`) e restituisce un `int` quando entrambi gli operandi sono interi. Insieme al resto `%` scompatta una quantità in parti intere:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

I valori non cambiano tipo da soli: per trasformare un valore in un altro tipo chiami il nome del tipo come una funzione. Questo si chiama **conversione** (o *casting*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` e `float()` leggono numeri scritti come testo, che è ciò che ottieni dall'input dell'utente o dai file. `str()` trasforma qualsiasi cosa in testo, così può essere unita con `+` ad altre stringhe.
Nota che `int(3.9)` non arrotonda: scarta la parte decimale.

---

Una conversione può fallire. `int("abc")` non può produrre un numero, quindi solleva un `ValueError` e il programma si ferma:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Per far continuare il programma puoi intercettare l'errore con `try` / `except`: il codice nel blocco `try` viene eseguito, e se solleva l'errore indicato viene eseguito invece il blocco `except`:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Quando la conversione riesce il blocco `except` viene saltato.

---

Ogni valore può essere interpretato come un booleano. `bool()` converte un valore in `True` o `False`, e la stessa regola viene applicata quando un valore è usato direttamente in un `if`.
I valori che contano come **falsi** sono quelli "vuoti":
- il numero `0` (e `0.0`)
- la stringa vuota `""`
- le collezioni vuote come `[]`, `{}`, `()` e `set()`
- `None`

Qualsiasi valore non vuoto è **vero**, inclusi i numeri negativi e le stringhe che sembrano solo vuote, come `"0"` o `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
Ecco perché `if name:` è un modo comune per controllare che una stringa non sia vuota.

---

`bool` è una **sottoclasse** di `int`: `True` si comporta come `1` e `False` come `0` ovunque sia atteso un numero:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` somma gli elementi di una lista, quindi sommare una lista di booleani **conta** quanti sono `True`:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
A causa della relazione di sottoclasse, `isinstance(True, int)` restituisce `True`, mentre `type(True)` resta `bool`.

---

`None` è un valore a sé che significa "qui non c'è niente". È ciò che una funzione restituisce quando non ha un'istruzione `return`, ed è un segnaposto comune per un valore non ancora noto.
Siccome esiste un solo `None`, controllalo con `is`, non con `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Ogni tipo ha un attributo `__name__` con il suo nome come stringa, comodo per i messaggi:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Stampare un `float` mostra tutte le cifre necessarie a rappresentarlo esattamente, che spesso sono troppe:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Dentro una f-string puoi aggiungere una **specificazione di formato** dopo due punti. `.2f` significa "numero a virgola fissa con 2 decimali":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
Il valore viene arrotondato al numero di decimali richiesto, e vengono aggiunti zeri quando serve: `f"{2.5:.2f}"` dà `2.50`.

---

La formattazione cambia solo il modo in cui un numero viene visualizzato. Per ottenere un **valore** arrotondato usa la funzione integrata `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Con un solo argomento `round()` arrotonda al numero intero più vicino e restituisce un `int`; con un numero di decimali restituisce un `float`:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Nota che i valori esattamente a metà strada tra due numeri vengono arrotondati a quello **pari**: `round(2.5)` è `2` e `round(3.5)` è `4`.

---

Un `float` è memorizzato in binario con un numero fisso di bit, quindi la maggior parte dei numeri decimali può essere solo **approssimata**. L'errore è minuscolo ma si manifesta nell'aritmetica:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Per questo motivo non dovresti confrontare i float per uguaglianza esatta. Arrotonda entrambi i lati, oppure usa `math.isclose()`, che controlla che due numeri siano uguali entro una piccola tolleranza:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Gli interi non hanno questo problema: `1 + 2 == 3` è sempre `True`.

---

A differenza di molti linguaggi, gli interi di Python **non hanno una dimensione massima**: un `int` cresce per contenere tutte le cifre necessarie, quindi i grandi calcoli restano esatti:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
Un `float`, invece, conserva solo circa 15 cifre significative, quindi la stessa potenza come float perde precisione:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Siccome `str()` funziona su qualsiasi `int`, un modo rapido per contare le cifre di un numero è misurare la lunghezza del suo testo.

---

Puoi scrivere il tipo atteso di una variabile, di un parametro o del valore restituito come **type hint**: due punti dopo il nome per variabili e parametri, una freccia `->` prima dei due punti per il valore restituito:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
I type hint sono **documentazione** per le persone e per strumenti come gli editor: Python **non** li controlla. Questo codice viene eseguito senza protestare e stampa `hello`:
```python
count: int = "hello"
print(count)
```
I type hint rendono chiari i tipi previsti, ma è sempre il valore a decidere il tipo reale.

---

Le conversioni possono essere combinate. `int("3.7")` fallisce, ma `float("3.7")` funziona, e `int()` di un `float` scarta la parte decimale:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` segue le regole di verità: `bool("")` è `False`, e nota che `bool("False")` è `True`, perché è una stringa non vuota.

---

Il testo che arriva dall'esterno è sempre una `str`, e spetta al tuo programma capire quale tipo contiene davvero.
Un approccio comune è provare prima la conversione **più rigorosa**, e ripiegare sulla successiva quando solleva un `ValueError`:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Annidare un secondo `try` dentro il blocco `except` ti permette di ripiegare ancora una volta, ad esempio per mantenere il testo com'è.
