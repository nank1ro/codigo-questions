Su Swift possiamo usare il segno `+` per mostrare two o più stringhe assieme, as esempio:
```swift
>>> print("Ciao " + "Swift!")
Ciao Swift!
```

---

Ma utilizzare il segno `+` per aggiungere un numero come `10` alla stringa `"amici"` produce un errore in quanto i valori sono di tipo diverso

---

L'interpolazione delle stringhe ci permette di mostrare espressioni come l'aggiunta di un numero ad una stringa, senza alcun errore

---

Ogni istruzione di interpolazione di stringa è costituita da due parti, la `\()` dove inseriamo il numero o la variabile, e la stringa normale

---

Successivamente, aggiungiamo il tipo diverso di valore tra le parentesi graffe in modo che venga mostrato come un'istruzione di print.
Come qui, con `\()`

---

L'inserimento di variabili come `amici` tra le parentesi tonde mostra anche il loro valore

---

Possiamo usare le parentesi tonde per inserire valore quanto spesso vogliamo all'interno della stringa

---

Le interpolazione di stringhe vengono usate al meglio nelle istruzioni di `print`, ma possiamo anche salvarla in variabili come normali stringhe
