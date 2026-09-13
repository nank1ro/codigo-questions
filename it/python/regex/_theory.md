Un'**espressione regolare** (regex) è un piccolo linguaggio di pattern che descrive il testo. Python la fornisce nel modulo standard `re`:
```python
import re
```

`re.search(pattern, text)` cerca il pattern in un punto qualsiasi del testo. Restituisce un **oggetto match** quando trova qualcosa, e `None` quando non trova nulla. `match.group()` restituisce la porzione di testo che ha trovato il pattern:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Due parti del pattern fanno il lavoro qui. `\d` significa *una qualsiasi cifra*, e `+` significa *una o più ripetizioni dell'elemento precedente*, quindi `\d+` si legge come "una o più cifre". Altre abbreviazioni utili sono `\w` (una lettera, una cifra o un underscore) e `\s` (uno spazio, una tabulazione o un a capo).

I pattern si scrivono come **raw string**, con una `r` prima delle virgolette. In una normale stringa Python il backslash inizia una sequenza di escape, quindi `"\d"` è un problema in attesa di accadere e `"\n"` diventerebbe un vero a capo invece dei due caratteri che il motore delle regex si aspetta. Il prefisso `r` restituisce al backslash il ruolo di carattere ordinario, così `r"\d"` è esattamente ciò che il motore riceve. Usa sempre `r"..."` per i pattern.

---

`re.search` scorre tutto il testo, ma `re.match` prova il pattern soltanto **all'inizio**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Entrambe restituiscono `None` quando non trovano nulla, e un oggetto match è sempre truthy, quindi il modo abituale per chiedersi "c'è stata una corrispondenza?" è un semplice `if`:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Quando serve un vero `True` o `False`, confronta con `is not None` o avvolgi la chiamata in `bool(...)`.

---

Esiste un terzo punto di ingresso, `re.fullmatch`, che ha successo solo quando il pattern copre il testo **per intero**, dal primo carattere all'ultimo. È lo strumento giusto per la validazione:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Le tre funzioni differiscono quindi solo nel punto in cui il pattern può trovarsi: `re.match` all'inizio del testo, `re.search` in un punto qualsiasi del testo, e `re.fullmatch` sull'intero testo.

---

Un oggetto match trasporta più del testo trovato. Oltre a `.group()` offre la posizione della corrispondenza all'interno della stringa originale:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` è l'indice del primo carattere trovato, `.end()` è l'indice subito dopo l'ultimo, e `.span()` li restituisce entrambi come tupla. Ciò significa che `text[match.start():match.end()]` è sempre uguale a `match.group()`.

Poiché `re.search` può restituire `None`, leggere `.group()` subito dopo solleva un `AttributeError` quando non c'è stata corrispondenza; controlla prima il risultato.

---

Le parentesi tonde all'interno di un pattern creano un **gruppo di cattura**: una parte della corrispondenza che può essere letta da sola. I gruppi sono numerati da sinistra a destra, a partire da `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` è l'intera corrispondenza, esattamente come `match.group()`, e `match.groups()` restituisce tutti i gruppi come tupla. Chiedere un numero di gruppo che non esiste solleva un `IndexError`.

---

Contare le parentesi per trovare il gruppo `3` stanca in fretta. A un gruppo si può dare un nome con `(?P<name>...)` e poi leggerlo con `match.group("name")`:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` restituisce tutti i gruppi con nome in un dizionario. I gruppi con nome mantengono anche il loro numero, quindi `match.group(1)` continua a funzionare.

L'esempio usa anche un **quantificatore** con le graffe: `\d{2}` significa esattamente due cifre, `\d{2,4}` significa da due a quattro, e `\d{2,}` significa due o più. Sono la versione precisa di `+` (una o più), `*` (zero o più) e `?` (zero o una).

---

Le parentesi quadre definiscono una **classe di caratteri**: un insieme di caratteri di cui viene accettato uno qualsiasi in quella posizione. `[aeiou]` corrisponde a una vocale, `[0-9]` a una cifra e `[a-z]` a una lettera minuscola. Una `^` subito dopo la parentesi aperta ne ribalta il significato, quindi `[^0-9]` corrisponde a tutto ciò che *non* è una cifra.

Fuori da una classe, `^` e `$` sono **ancore**: `^` lega il pattern all'inizio del testo e `$` alla fine. Con `re.fullmatch` le ancore sono implicite, ed è per questo che la validazione si legge meglio con esso:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` si ferma alla prima corrispondenza. `re.findall(pattern, text)` raccoglie invece **tutte** le corrispondenze, e le restituisce come lista di stringhe:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
La lista è vuota quando non c'è nessuna corrispondenza, quindi non c'è alcun `None` da controllare: si può scorrere con un ciclo o misurare con `len(...)` direttamente. Nota che `findall` restituisce stringhe semplici, non oggetti match, quindi le posizioni non sono disponibili.

---

Quando servono la posizione o i gruppi di ogni corrispondenza, `re.finditer(pattern, text)` è la chiamata giusta: percorre il testo e produce un **oggetto match** per ogni corrispondenza, una alla volta:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produce un iteratore, non una lista, quindi può essere usato in un ciclo `for` o in una comprehension. Dove `findall` dà soltanto il testo, `finditer` dà tutto ciò che un oggetto match sa.

---

`findall` cambia comportamento quando il pattern contiene gruppi di cattura. Con esattamente un gruppo restituisce il contenuto di quel gruppo invece dell'intera corrispondenza, e con due o più restituisce una tupla di gruppi per ogni corrispondenza:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Vale la pena ricordarlo: aggiungere parentesi a un pattern solo per raggruppare cambia silenziosamente ciò che `findall` restituisce. `re.finditer` non si comporta mai così, perché un oggetto match conserva sempre sia la corrispondenza completa sia i gruppi.

---

`re.sub(pattern, replacement, text)` restituisce una nuova stringa in cui ogni corrispondenza è stata sostituita. Le stringhe sono immutabili, quindi il testo originale resta intatto:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

La sostituzione può riferirsi ai gruppi di cattura con `\1`, `\2`, ... (o `\g<name>` per un gruppo con nome), il che rende il riordino del testo una riga di codice sola. Anche la sostituzione è una raw string, per lo stesso motivo del backslash:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Un argomento `count` limita quante corrispondenze vengono sostituite: `re.sub(r"\d", "#", "1 2 3", count=1)` dà `# 2 3`.

---

La sostituzione data a `re.sub` può essere anche una **funzione**. Viene chiamata una volta per ogni corrispondenza, riceve l'oggetto match, e deve restituire la stringa da mettere al suo posto. È così che una sostituzione può dipendere da ciò che è stato trovato:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
La funzione viene passata per nome, senza parentesi: scrivere `shout(match)` la chiamerebbe subito invece di passarla a `re.sub`.

---

`str.split` può tagliare solo su un separatore fisso. `re.split(pattern, text)` taglia su qualsiasi cosa descriva il pattern, che è ciò che input disordinati di solito richiedono:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Scrivere il separatore come `[,;\s]+` fa sì che un'intera sequenza di virgole, punti e virgola e spazi conti come un solo taglio, invece di lasciare stringhe vuote tra loro.

Un argomento `maxsplit` si ferma dopo un dato numero di tagli, lasciando il resto del testo nell'ultimo elemento: `re.split(r"\s+", "a b c", maxsplit=1)` dà `['a', 'b c']`.

---

Ogni chiamata a `re.search` o `re.findall` deve prima cercare la stringa del pattern in una cache interna. `re.compile(pattern)` salta quella ricerca e restituisce un **oggetto pattern** che porta con sé gli stessi metodi:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
Il testo è l'unico argomento rimasto, perché il pattern è già incorporato nell'oggetto. Compilare ripaga quando lo stesso pattern viene usato molte volte, per esempio dentro un ciclo, e dà anche al pattern un nome che spiega cosa trova.

---

I **flag** cambiano il modo in cui un pattern viene applicato. Ogni funzione in `re` li accetta come argomento `flags`, e `re.compile` li memorizza nell'oggetto pattern:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
I due usati più spesso sono `re.IGNORECASE`, che fa corrispondere le lettere indipendentemente dalle maiuscole e minuscole, e `re.MULTILINE`, che fa corrispondere `^` e `$` all'inizio e alla fine di ogni riga invece che di tutto il testo. Più flag si combinano con `|`, come in `re.IGNORECASE | re.MULTILINE`.

Un flag cambia solo le regole di corrispondenza: il testo restituito è sempre il testo che c'era davvero, con le sue maiuscole e minuscole originali.
