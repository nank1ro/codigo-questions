Una **stringa** è un pezzo di testo: una sequenza di caratteri racchiusa tra virgolette.
Python accetta sia le virgolette singole `'...'` che quelle doppie `"..."`, e funzionano esattamente allo stesso modo:
```python
name = 'Ada'
language = "Python"
```
La scelta conta quando il testo stesso contiene una virgoletta.
Un apostrofo dentro virgolette singole terminerebbe la stringa troppo presto, quindi racchiudi quel testo tra virgolette doppie:
```python
print("It's sunny")  # It's sunny
```

---

La funzione integrata `len()` restituisce la **lunghezza** di una stringa, cioè quanti caratteri contiene.
Anche spazi e punteggiatura contano come caratteri:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Ogni carattere di una stringa ha una posizione chiamata **indice**.
Gli indici iniziano da `0`, non da `1`: il primo carattere è all'indice `0`, il secondo all'indice `1`, e così via.
Scrivi l'indice tra parentesi quadre dopo la stringa per leggere un singolo carattere:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Richiedere un indice che non esiste, come `word[6]`, genera un `IndexError`.

---

Gli indici possono anche essere **negativi**: contano a partire dalla fine della stringa.
`-1` è l'ultimo carattere, `-2` quello prima, e così via:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
Questo è comodo perché non serve conoscere la lunghezza della stringa per raggiungerne la fine.

---

Una **slice** estrae una parte di una stringa.
Scrivi `[start:end]` tra parentesi quadre: il carattere in posizione `start` è incluso, quello in posizione `end` è **escluso**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Puoi omettere `start` per tagliare dall'inizio, oppure `end` per tagliare fino alla fine:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Lo slicing non genera mai un errore: un `end` più grande della lunghezza si ferma semplicemente all'ultimo carattere.

---

Sai già che `+` unisce due stringhe (**concatenazione**).
L'operatore `*` **ripete** una stringa un determinato numero di volte:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
La ripetizione è un modo rapido per disegnare separatori e semplici motivi.

---

L'operatore `in` verifica se una stringa ne **contiene** un'altra.
Restituisce `True` o `False`, quindi si inserisce naturalmente in un `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` esegue il controllo opposto.

---

Le stringhe hanno molti **metodi** integrati: funzioni chiamate con un punto dopo la stringa.
`upper()` restituisce il testo in maiuscolo, `lower()` in minuscolo:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Nota che i metodi **restituiscono una nuova stringa**: la `word` originale non viene modificata.
`lower()` è spesso usato per confrontare testi ignorando maiuscole e minuscole: `"Yes".lower() == "yes"`.

---

Le stringhe sono **immutabili**: una volta create, i loro caratteri non possono essere modificati.
Assegnare a un indice genera un `TypeError`:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Per "cambiare" una stringa ne costruisci una nuova, per esempio con slice e concatenazione, e la salvi nella variabile:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

Il testo digitato dagli utenti ha spesso spazi in più intorno.
Il metodo `strip()` restituisce una copia della stringa **senza spazi bianchi iniziali e finali** (spazi, tabulazioni e a capo):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Gli spazi al centro del testo vengono mantenuti.
`lstrip()` rimuove solo il lato sinistro e `rstrip()` solo quello destro.

---

`split()` suddivide una stringa in una **lista** di pezzi.
Senza argomenti divide sugli spazi bianchi; con un argomento divide su quel separatore:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` fa il contrario: incolla gli elementi di una lista in un'unica stringa.
Si chiama sul **separatore**, e la lista è l'argomento:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` restituisce una copia della stringa in cui **ogni** occorrenza di `old` è sostituita da `new`:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Dato che le stringhe sono immutabili, ricordati di salvare il risultato se vuoi conservarlo.

---

`find(sub)` restituisce l'**indice** della prima occorrenza di `sub`, o `-1` se non viene trovata:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` restituisce **quante volte** `sub` compare:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` ed `endswith(suffix)` restituiscono `True` o `False` a seconda di come inizia o finisce la stringa:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
Sono il modo abituale per controllare estensioni di file, protocolli o prefissi.

---

Alcuni caratteri non possono essere digitati direttamente dentro una stringa.
Una **sequenza di escape** è un backslash `\` seguito da una lettera o un simbolo che rappresenta un carattere speciale:

- `\n` un a capo
- `\t` una tabulazione
- `\"` una virgoletta doppia dentro una stringa tra virgolette doppie
- `\'` una virgoletta singola dentro una stringa tra virgolette singole
- `\\` un backslash letterale

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
stampa:
```
Line 1
Line 2
She said "hi"
```
Ogni sequenza di escape conta come **un solo** carattere, anche se ne digiti due.

---

Una stringa che si estende su **più righe** può essere scritta con le **virgolette triple** `"""..."""` (o `'''...'''`).
Ogni a capo dentro le virgolette diventa parte della stringa, quindi non serve `\n`:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
stampa:
```
Roses are red,
Violets are blue
```
Le stringhe con virgolette triple possono anche contenere liberamente virgolette singole e doppie.

---

Dato che ogni metodo delle stringhe restituisce una nuova stringa, puoi **concatenare** i metodi uno dopo l'altro.
Ogni chiamata lavora sul risultato della precedente:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Una slice accetta anche un terzo valore, il **passo** (step).
Il passo `-1` percorre la stringa all'indietro, il trucco classico per invertirla:
```python
print("abc"[::-1])  # cba
```

---

Uno **slug** è una versione di un titolo adatta agli URL: minuscola, senza spazi intorno, e con le parole separate da trattini, come `hello-world`.
Costruirne uno è solo una concatenazione dei metodi che hai già imparato: `strip()`, `lower()` e `replace()`.
