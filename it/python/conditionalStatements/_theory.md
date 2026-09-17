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

---

Ogni istruzione condizionale ha bisogno della parola chiave `if` per introdurla. È quello che dice a Python che il blocco sottostante viene eseguito solo quando una condizione è verificata.

---

Una condizione non deve essere per forza un confronto — funziona anche un valore booleano come `True` da solo, e il blocco viene eseguito ogni volta che quel valore è `True`.

---

La stessa istruzione può saltare il proprio blocco semplicemente cambiando la condizione: ogni volta che questa vale `False`, Python salta direttamente il codice indentato.

---

Una riga `if` in Python è composta da tre parti: la parola chiave `if`, una condizione e i due punti che chiudono la riga. Tutto ciò che è indentato dopo quei due punti è il blocco.

---

Poiché qui la condizione è `True`, Python esegue la riga indentata sottostante e stampa `Hello!`.

---

Una condizione `False` significa che Python non entra mai nel blocco indentato, quindi non viene stampato nulla.

---

Il valore che decide se un blocco viene eseguito si chiama condizione, e deve sempre valutare a un booleano, `True` o `False`.

---

Il blocco sotto un `if` non può mai essere vuoto: Python solleva un `IndentationError` quando nessuna riga indentata segue i due punti. `pass` è il segnaposto abituale quando non c'è ancora nulla da eseguire.

---

I due punti appartengono alla riga `if` e non al blocco: segnano la fine della condizione e annunciano che le righe indentate sottostanti fanno parte dell'istruzione.

---

Quando una condizione è `False`, Python salta l'intero blocco indentato e prosegue dalla riga successiva che non è indentata sotto l'`if`.

---

Python non richiede le parentesi attorno a una condizione — `if True:` è già un'istruzione completa da sola. Qui le parentesi sono un normale raggruppamento, lo stesso usato nell'aritmetica, e lasciano il valore invariato.

---

Un blocco di codice può contenere più di una riga, e le righe vengono eseguite nell'ordine in cui sono scritte — un'istruzione aggiunta sopra una già esistente viene stampata per prima.

---

Una variabile booleana può essere usata come condizione da sola — non c'è bisogno di confrontarla prima con `True` o `False`.

---

Quando la condizione è una variabile, `if` legge qualunque valore quella variabile contenga in quel momento. Cambiare l'assegnazione sopra è sufficiente per disattivare il blocco, senza toccare affatto la riga `if`.

---

Le righe indentate che appartengono a un'istruzione condizionale si chiamano il suo blocco di codice — è l'indentazione a contrassegnarle come parte di esso.

---

Una riga che si trova al di fuori dell'indentazione dell'`if` viene eseguita indipendentemente dalla condizione, poiché non ha mai fatto parte di quel blocco.

---

Un blocco di codice non è limitato a una sola riga — può essere corto o lungo quanto richiede la logica, purché ogni riga rimanga indentata in modo coerente.

---

Con `online` impostato su `False`, la condizione non è mai verificata, quindi il blocco viene saltato e non viene stampato nulla.

---

Solo il `print` indentato subito dopo l'`if` appartiene al suo blocco; una riga scritta con la stessa indentazione dell'`if` stesso non ne fa parte.

---

Una riga posta dopo il blocco `if` ma senza alcuna indentazione aggiuntiva non ne fa più parte — viene eseguita ogni volta, qualunque sia la condizione.

---

Un blocco può contenere un numero qualsiasi di istruzioni. Vengono eseguite dall'alto verso il basso, e ognuna deve essere indentata allo stesso livello delle altre.

---

Assegnare `True` alla variabile fa sì che la condizione in cui viene usata sia verificata, quindi il blocco sottostante viene eseguito.

---

Assegnare invece `False` fa fallire la condizione, quindi il blocco sottostante viene saltato completamente.

---

La parola chiave `if` è ciò che avvia un'istruzione condizionale — insieme alla sua condizione, decide se il blocco sottostante viene eseguito.

---

`"False"` tra virgolette è una stringa, non un booleano, e una stringa non vuota conta sempre come vera. Solo il `False` nudo impedisce l'esecuzione di un blocco.
```python
print(bool("False"))  # True
```

---

Scegliere `True` qui esegue entrambe le righe del blocco, non solo la prima — tutto ciò che è indentato sotto l'`if` appartiene allo stesso blocco.

---

I due punti sono l'unico elemento di cui una riga `if` non può fare a meno: chiudono la condizione e aprono il blocco. Le parentesi attorno alla condizione sono opzionali in Python, quindi `if True:` e `if (True):` si comportano in modo identico.

---

Istruzioni come `if`, `elif` ed `else`, che eseguono o saltano il codice in base a un valore booleano, sono note collettivamente come istruzioni condizionali.

---

L'operatore `not` inverte un valore booleano: `not True` è `False`, e `not False` è `True`.
```python
is_online = False
print(not is_online)  # True
```

---

`not` costruisce un nuovo booleano invece di modificare quello che legge, quindi dopo `is_afternoon = not is_morning` la variabile `is_morning` mantiene ancora il suo valore originale.

---

Una condizione si trova sempre tra la parola chiave `if` e i due punti che la seguono, da nessun'altra parte nella riga.

---

Non c'è un limite rigido al numero di righe che un blocco `if` può contenere — ciò che conta è che ogni riga rimanga indentata allo stesso livello.

---

Un letterale booleano costituisce una condizione perfettamente valida: `if True:` esegue il suo blocco ogni volta. Scriverlo come `if (True):` è esattamente la stessa istruzione, poiché le parentesi attorno a una condizione sono opzionali in Python.

---

Il blocco di codice di un'istruzione `if` è il gruppo di righe indentate sottostanti, separato dal resto del programma proprio da quella indentazione.

---

Una condizione si riduce sempre a uno di due valori, `True` o `False` — è questo che la rende un booleano.
