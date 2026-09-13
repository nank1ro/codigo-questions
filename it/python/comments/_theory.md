Un **commento** è una nota scritta dentro il codice sorgente per le persone che lo leggono. Python ignora completamente i commenti, quindi non cambiano mai ciò che il programma fa.

L'unico tipo di commento che Python possiede è il **commento su singola riga**: inizia con `#` e prosegue fino alla fine della riga.
```python
# Greets the user
print("Hello")
```
Usa i commenti per spiegare a cosa serve un pezzo di codice, o perché è stato scritto in quel modo.

---

Un commento non ha bisogno di una riga tutta per sé: può seguire il codice sulla stessa riga. Questo è un **commento in linea**, ed è un buon posto per una breve nota su quella specifica istruzione:
```python
retries = 3  # give up after three attempts
```
Tutto ciò che va da `#` alla fine della riga viene ignorato, mentre il codice prima di esso viene eseguito come al solito.

La guida di stile di Python, **PEP 8**, chiede un po' di spaziatura qui: almeno **due spazi** tra il codice e il `#`, e **uno spazio** dopo il `#`. Un commento su una riga propria ha bisogno solo dello spazio dopo il `#`.

---

Poiché Python scarta i commenti completamente, aggiungere o eliminare un commento non cambia mai ciò che un programma fa. Viene eseguito solo il codice che **non** è commentato.

Questo fa di `#` un modo rapido per disattivare una riga di codice senza eliminarla. Si chiama **commentare il codice** (commenting out):
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
La seconda riga ora è un commento, quindi `total` resta `10`. Togliendo il `#` la riga torna in vita.

Commentare il codice è comodo mentre fai esperimenti, ma ricorda di fare pulizia: del codice che resta commentato per molto tempo confonde solo chi lo leggerà dopo.

---

Molti linguaggi hanno un secondo tipo di commento, un **commento a blocco** che si estende su più righe, come `/* ... */`. Python non ha una simile sintassi: `#` è tutto ciò che c'è.

Quando una spiegazione ha bisogno di più di una riga, metti un `#` davanti a ogni riga:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
Lo stesso trucco commenta più righe di codice in una volta: un `#` per riga. Qualsiasi editor sa aggiungere o rimuovere quei `#` per un'intera selezione con una singola scorciatoia, quindi costa meno di quanto sembri.

---

Spesso si vede una **stringa con triple virgolette** usata come se fosse un commento a blocco:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Una stringa tra `"""` e `"""` può estendersi su più righe, e una stringa scritta da sola è un'istruzione valida: Python la costruisce, non ci fa nulla e la butta via. Non viene stampato nulla, quindi il risultato sembra un commento.

Non lo è. È una stringa letterale, quindi le regole delle virgolette valgono ancora: una virgoletta non bilanciata o una `"""` smarrita al suo interno rompono il programma, mentre dentro un commento `#` può passare di tutto. Può anche diventare una docstring per sbaglio, se finisce per essere la prima istruzione di un file, di una classe o di una funzione. In ogni altro posto semplicemente non va da nessuna parte: CPython butta via l'intera istruzione durante la compilazione.

Quindi, per disattivare del codice, usa `#`. La stringa con triple virgolette ha un suo compito, che inizia nel prossimo esercizio.

---

Quando una stringa è la **prima istruzione** dentro una funzione, Python la tratta come la documentazione di quella funzione. Si chiama **docstring**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Per convenzione una docstring si scrive tra triple virgolette doppie, `"""`, anche quando sta su una riga, così può crescere in seguito senza dover cambiare le virgolette.

Scrivi il riassunto in terza persona, come se descrivessi la funzione: "Restituisce...", "Somma...", "Controlla...". La docstring deve venire prima di qualsiasi altra istruzione nel corpo, altrimenti è solo una stringa ordinaria.

---

Una docstring non viene gettata via: Python la memorizza nell'attributo `__doc__` della funzione, così il programma può leggere la propria documentazione mentre è in esecuzione:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Quando una funzione non ha una docstring, `__doc__` è `None`. Questo è ciò che stampa `help(greet)`, e ciò che mostra un editor quando passi con il mouse sopra il nome.

---

Anche un file può essere documentato. Una stringa scritta come **primissima istruzione del file**, prima di qualsiasi import o definizione, è la **docstring del modulo**: dice a cosa serve l'intero file.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Conta solo la prima istruzione. Un commento può trovarsi sopra, ma qualsiasi vero codice in mezzo riporta la stringa a essere una stringa ordinaria, inutile.

---

Le classi funzionano allo stesso modo: una stringa posta come prima istruzione del corpo di una classe è la docstring di quella classe, e viene memorizzata in `__doc__`:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Anche ogni metodo dentro la classe può avere la sua docstring, leggibile con `Point.__init__.__doc__`. Quindi i tre posti che accettano una docstring sono la cima di un modulo, la cima di una classe e la cima di una funzione.

---

Le docstring e i commenti `#` sembrano simili ma rispondono a domande diverse.

Una **docstring** è per chi **usa** il codice: cosa fa la funzione, cosa si aspetta e cosa restituisce. Sopravvive in `__doc__`, `help()` la legge, gli editor la mostrano e gli strumenti di documentazione la raccolgono.

Un **commento** è per chi **legge** il codice: perché questa riga è scritta in questo modo, cosa significa lo strano numero, quale bug aggira. Esiste solo nel file sorgente e sparisce una volta che il programma è in esecuzione.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
Quindi: la documentazione della funzione va nella docstring, le note sull'implementazione vanno nei commenti.

---

Quando una riga non basta, una docstring cresce fino a diventare un layout fisso, descritto nella **PEP 257**: un riassunto di una riga, una riga vuota, poi i dettagli, e le virgolette `"""` di chiusura su una riga a sé.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
La riga vuota è importante: gli strumenti mostrano la prima riga da sola, come breve descrizione, e conservano il resto per chi vuole leggere di più.

---

La docstring deve essere la **prima riga del corpo**, sopra ogni altra istruzione. Una stringa scritta dopo il `return`, o in qualsiasi altro punto del corpo, è solo una stringa: `__doc__` resta `None` e nessuno strumento la mostrerà mai.

---

Alcuni commenti seguono una convenzione che gli editor capiscono. I **marcatori** più comuni sono:
- `# TODO: ...` segnala qualcosa che deve ancora essere scritto
- `# FIXME: ...` segnala del codice notoriamente sbagliato che deve essere corretto

```python
limit = 10
# TODO: read the limit from the settings
```
Per Python sono commenti ordinari; gli editor li raccolgono in un pannello dedicato, così il lavoro in sospeso è facile da trovare. Un `TODO` di solito sta accanto a un segnaposto che mantiene il programma in esecuzione finché il vero codice non viene scritto.

Quando finisci il lavoro, sostituisci il segnaposto ed elimina il marcatore nella stessa modifica, così il commento non mente mai sullo stato del codice.

---

Un commento posto sopra una funzione per dire cosa fa la funzione si trova nel posto sbagliato. La docstring è il posto giusto per questo: è allegata alla funzione, `help()` la trova e gli editor la mostrano, mentre un commento `#` sopra il `def` è invisibile a tutti quanti.

```python
# adds a and b
def add(a, b):
    return a + b
```
Spostando la stessa frase di una riga più giù, tra triple virgolette, la si trasforma in vera documentazione:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python cerca `#` solo nel codice, mai dentro una **stringa**. Tra virgolette, `#` è un carattere ordinario:
```python
print("black is #000000")  # a hex colour
```
Il primo `#` fa parte del testo, il secondo invece avvia un vero commento. Lo stesso vale per `"""` dentro un commento `#`: lì sono solo tre caratteri virgoletta, e non avviano nulla.

---

Un buon commento spiega **perché** il codice fa qualcosa, non **cosa** fa. Il codice mostra già cosa succede; ripeterlo a parole aggiunge rumore e diventa superato appena il codice cambia:
```python
# set timeout to 30
timeout = 30
```
Il motivo dietro al numero è ciò che un lettore non può indovinare:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Se un commento si limita a ripetere la riga sotto di sé, eliminalo o sostituiscilo con il motivo. I migliori commenti sono quelli che dicono qualcosa che il codice non può dire.
