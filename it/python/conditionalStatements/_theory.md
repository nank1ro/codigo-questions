Il processo decisionale e' necessario quando vogliamo eseguire il codice solo se una certa condizione viene soddisfatta.
Supponiamo di voler giocare all'aperto solo se il tempo e' bello.
In programmazione, possiamo salvare una variabile booleana `bel_tempo` ed eseguire l'azione di giocare fuori **solo** se (`if`) questa variabile e' `True`, come:
```python
bel_tempo = True
if (bel_tempo):
    # gioca fuori
```

---

Continuiamo con l'esempio precedente.
```python
bel_tempo = True
if (bel_tempo):
    # gioca fuori
```
Abbiamo visto che l'istruzione `if` esegue il blocco di codice solo se la condizione e' `True`.
Un'altra cosa importante da considerare e' rappresentata dai **due punti** `:` e dall'**indentazione**, che indicano l'inizio di un blocco di codice.
L'indentazione si riferisce agli spazi all'inizio di una riga di codice.
Mentre in altri linguaggi di programmazione l'indentazione del codice e' a fini di leggibilità, in Python e' essenziale.
Potete usare il vostro numero di spazi preferito (2, 4, 6, 8), notando che il piu' utilizzato e' 4.
Qui nell'app, suggeriamo di usare il tasto **TAB** per indentare correttamente le linee di codice

---

Abbiamo appena visto come eseguire un blocco di codice se si verifica una condizione, ora vediamo come eseguire un altro blocco di codice se la prima condizione fallisce.
Andiamo a giocare fuori se il tempo e' bello, altrimenti restiamo a casa.
In Python possiamo usare l'istruzione `else`, come:
```python
bel_tempo = True
if (bel_tempo):
    # gioca fuori
else:
    # resta a casa
```

---

Supponiamo di avere un'altra condizione da verificare, come in questo esempio:
```python
num = 3
if (num == 2):
    print("il numero e' 2")
elif (num == 3):
    print("il numero e' 3")
else:
    print("fai qualcos'altro")
```
e l'output di questo codice e' `il numero e' 3`.
Prima di tutto, verifichiamo se il numero e' uguale a 2, questo e' falso.
Passiamo quindi alla seconda istruzione e verifichiamo se `num` e' uguale a 3, essendo vero eseguiamo il seguente blocco di codice stampando `il numero e' 3`.

---

Possiamo aggiungere tutte le istruzioni `elif` che vogliamo, non ci sono limiti
```python
num = 4
if (num == 2):
    print("il numero e' 2")
elif (num == 3):
    print("il numero e' 3")
elif (num == 4):
    print("il numero e' 4")
elif (num == 5):
    print("il numero e' 5")
elif (num == 6):
    print("il numero e' 6")
```
e l'output del codice e' `il numero e' 4`.

---

Possiamo anche nidificare un'istruzione condizionale (`if`, `elif` o `else`) all'interno di un'altra istruzione condizionale, per creare una struttura piu' complessa.
```python
num = 4
if (num < 3):
    print("il numero e' minore di 3")
else:
    if (num == 3):
        print("il numero e' 3")
    elif (num == 4):
        print("il numero e' 4")
    else:
        print("il numero e' maggiore di 4")
```
e l'output del codice e' `il numero e' 4`.
