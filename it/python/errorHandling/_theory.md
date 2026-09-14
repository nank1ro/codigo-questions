Un'**eccezione** è il modo in cui Python dice che un'istruzione non può essere eseguita. Dividere per zero, convertire `"abc"` in un intero o leggere una chiave mancante di un dizionario la sollevano tutte. Quando nessuna la gestisce, il programma si ferma subito lì e stampa un **traceback**:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
Il traceback elenca le righe che erano in esecuzione, e l'ultima riga indica il **tipo di eccezione** (`ZeroDivisionError`) e il suo messaggio (`division by zero`). Quell'ultima riga è la prima da leggere.

Per mantenere in vita il programma, metti l'istruzione rischiosa in un blocco `try` e descrivi il recupero in un blocco `except`:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python esegue il blocco `try`; se l'eccezione nominata viene sollevata salta direttamente al blocco `except` corrispondente e prosegue con il resto del programma.

---

Il blocco `try` si ferma alla **prima** istruzione che solleva un'eccezione; le righe successive vengono saltate e il controllo passa al blocco `except`. Nulla di ciò che è stato fatto nel blocco `try` viene annullato, quindi tienilo il più corto possibile:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
Un `return` dentro `except` funziona come qualsiasi altro `return`, il che rende `try`/`except` un modo naturale per restituire un valore di ripiego invece di andare in crash.

---

Un'eccezione che nessun blocco `except` intercetta continua a viaggiare verso l'esterno: fuori dalla riga, fuori dalla funzione che l'ha eseguita, fuori dal suo chiamante, e così via. Se nulla la cattura prima della cima del programma, Python stampa il traceback e il processo termina con uno stato di uscita diverso da zero. Le righe successive all'istruzione che ha fallito non vengono mai eseguite.

---

Una clausola `except` cattura solo il tipo che nomina, e le sue sottoclassi. È proprio questo il punto: tutto il resto continua a viaggiare verso l'esterno, così un bug che non ti aspettavi si presenta comunque come un traceback invece di essere inghiottito.

`int(text)` solleva **`ValueError`** quando il testo non descrive un numero intero, quindi è quello il tipo da nominare quando leggi l'input dell'utente:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Nominare `ValueError` qui è una decisione, non una formalità: `int(None)` solleva `TypeError`, che questa funzione deliberatamente **non** cattura, perché passare `None` è un errore di programmazione e deve essere visibile.

---

Scegliere il tipo più ristretto che copre il fallimento che ti aspetti è ciò che rende affidabile la gestione degli errori. Una funzione che legge del testo dovrebbe riprendersi da un testo sbagliato (`ValueError`) ma non deve nascondere di essere stata chiamata con il tipo di argomento sbagliato (`TypeError`) — quell'errore appartiene al chiamante, quindi lascialo passare.

---

Un solo blocco `try` può essere seguito da **più** clausole `except`, ognuna delle quali gestisce un fallimento diverso con un recupero diverso. Python confronta l'eccezione sollevata con esse dall'alto verso il basso ed esegue la **prima** che corrisponde; le altre vengono saltate:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Poiché vince la prima corrispondenza, l'ordine conta quando i tipi sono imparentati: una clausola per un tipo generale posta sopra una clausola per un tipo più specifico vincerebbe sempre, rendendo irraggiungibile la clausola specifica.

---

Quando più fallimenti meritano lo **stesso** recupero, elencarli come una tupla in una sola clausola è più breve che ripetere il blocco:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Le parentesi sono obbligatorie: `except ValueError, ZeroDivisionError:` è un errore di sintassi in Python 3. Una tupla resta comunque un elenco esplicito di tipi.

---

`except:` senza alcun tipo dopo è un **except nudo**. Corrisponde a tutto, comprese eccezioni che non hanno nulla a che fare con l'operazione che stavi proteggendo, quindi la regola è semplice: nomina sempre i tipi dai quali puoi davvero riprenderti.

---

Un'eccezione è un oggetto, e `as` la lega a un nome così che il gestore possa esaminarla:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — che è ciò che usano `print(e)` e uno slot di f-string — dà il messaggio con cui l'eccezione è stata costruita, e `type(e).__name__` dà il nome della classe come testo. Il nome legato da `as` esiste solo dentro il blocco `except`; Python lo elimina quando il blocco termina.

---

Un blocco `try` può essere seguito da un blocco `else`, che viene eseguito **solo quando il blocco `try` è terminato senza sollevare eccezioni**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Mettere `print(number * 2)` dentro il blocco `try` funzionerebbe anche, ma allora un `ValueError` sollevato dalla stampa stessa verrebbe scambiato per un fallimento di conversione. `else` mantiene il blocco `try` ridotto alla singola istruzione protetta, e contiene tutto ciò che deve accadere in caso di successo.

---

Un blocco `finally` viene eseguito **qualunque cosa accada**: dopo un blocco `try` andato a buon fine, dopo un blocco `except`, anche mentre un'eccezione che nessuno ha catturato viaggia verso l'esterno, e anche quando il blocco `try` o `except` esegue un `return`:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Entrambi i percorsi stampano `done` prima che il valore esca dalla funzione. Quella garanzia è lo scopo di `finally`: chiudere un file, rilasciare un lock, ripristinare un'impostazione. La forma completa è `try` / `except` / `else` / `finally`; un `try` ha bisogno di almeno un `except` o di un `finally`, e `else` funziona solo insieme a un `except`.

---

Anche il tuo codice può sollevare eccezioni, con l'istruzione `raise` seguita da un oggetto eccezione:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` ferma immediatamente la funzione, esattamente come farebbe un fallimento integrato. Restituire invece un valore di errore — `-1`, `None`, `False` — è facile da dimenticare per chi chiama; un'eccezione non può essere ignorata per sbaglio.

Scegli il tipo che descrive il problema: `ValueError` quando l'argomento ha il tipo giusto ma un valore impossibile, `TypeError` quando ha proprio il tipo sbagliato. Il testo passato all'eccezione è il suo messaggio.

---

Una manciata di eccezioni integrate copre la maggior parte dei fallimenti quotidiani:

| Eccezione | Sollevata quando | Esempio |
|---|---|---|
| `ValueError` | il tipo è giusto ma il valore è impossibile | `int("abc")` |
| `TypeError` | il tipo stesso è sbagliato | `"x" + 1` |
| `ZeroDivisionError` | una divisione o un modulo ha divisore zero | `1 / 0` |
| `KeyError` | un dizionario non ha quella chiave | `{"a": 1}["b"]` |
| `IndexError` | un indice di sequenza è fuori intervallo | `[1, 2][5]` |

Ricorrere a una di queste invece di inventare un tipo nuovo mantiene i tuoi errori leggibili per chiunque conosca Python.
