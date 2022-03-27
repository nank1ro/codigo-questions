Una Stringa _templata_ è 
A String _template_ è un modo programmatico per generare una stringa.
In Kotlin possiamo usare il segno `+` (concatenazione) per mostrare 2 o più stringhe assieme, ad esempio:
```kotlin
println("Ciao " + "Kotlin!")
// prints "Ciao Kotlin!"
```

---

Ma utilizzare il segno `+` per aggiungere un numero come `10` alla stringa `"amici"` produce un errore in quanto i valori sono di tipo diverso

---

L'interpolazione delle stringhe ci permette di mostrare espressioni come l'aggiunta di un numero ad una stringa, senza alcun errore
Mettendo un'espressione dentro `${}` la si valuta.
Il valore di ritorno viene convertito in una stringa e inserito nella stringa risultante

---

Se si mette il `$` (dollaro) prima del nome di un identificatore, il modello di stringa inserirà il contenuto di quell'identificatore nella stringa

---

Se ciò che segue il segno `$` non è riconoscibile come un identificatore di programma, non succede nulla di speciale

---

Possiamo anche inserire delle variabili dopo il simbolo del dollaro per mostrare il loro valore

---

Possiamo usare le parentesi graffe per inserire valori tutte le volte che vogliamo all'interno dei modelli di stringa

---

All'interno delle `${}` possiamo anche inserire delle condizioni, per esempio:
```kotlin
println("${if (true) "Corretto" else "Errato"}")
// stampa Corretto
```

---

Le interpolazione di stringhe vengono usate al meglio nelle istruzioni di `print`, ma possiamo anche salvarla in variabili come normali stringhe
