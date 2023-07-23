> La parola chiave `for` esegue un blocco di codice per ogni valore in una sequenza.

Il ciclo `for` itera attraverso qualsiasi cosa che fornisca un iteratore.

La sintassi del ciclo `for` è la seguente:
```kotlin
for (elemento in collezione) print(elemento)
```

Il corpo di un ciclo `for` può anche essere un blocck
```kotlin
for (elemento in collezione) {
    print(elemento)
}
```

A ogni ciclo, la variabile `elemento` riceve il prossimo elemento presente nei valori di `collezione`.

Ecco un ciclo `for` che ripete un'azione un numero fisso di volte:

```kotlin
for (i in 1..3) {
    println(i)
}
// stampa 1, 2, 3
```

L'output mostra l'indice `i` che riceve ogni valore nell'intervallo compreso tra _1_ e _3_.

---

Un _range_ è un intervallo di valori definito da una coppia di punti finali (_endpoint_).
Esistono due modi fondamentali per definire gli intervalli:

```kotlin
var primoRange = 1..3           // [1]
var secondoRange = 1 until 3     // [2]
println(primoRange)
println(secondoRange)

/* stampa
1..3
1..2
*/
```

- __[1]__ utilizzando la sintassi `..` si includono entrambi i limiti dell'intervallo risultante.
- __[2]__ `until` esclude la fine. L'output mostra che _3_ non fa parte dell'intervallo.

---

È possibile iterare su un intervallo in ordine inverso.

Probabilmente vi aspetterete che `3..1` funzioni, ma purtroppo il team di Kotlin ha deciso di importare questa funzionalità in modo diverso.

Infatti, se si prova a eseguire questo frammento di codice:
``kotlin
for (i in 3..1) println(i)
```

Vedrete che non viene stampato nulla.
Per farlo funzionare dobbiamo usare la parola chiave `downTo`:

``kotlin
per (i in 3 downTo 1) println(i)
// stampa 3, 2, 1
```

`downTo` produce un intervallo decrescente.

---

Il _passo_ predefinito di un intervallo è __1__, ma è possibile impostare esplicitamente un altro valore.

È possibile definire il __passo__ del ciclo `for` utilizzando la parola chiave `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// stampa 1, 3, 5, 7, 9
```

Come si può vedere, il blocco di codice viene eseguito con un passo di _2_ invece che di _1_, cambiando completamente il nostro output.

---

Puoi anche produrre un range di _caratteri_.
```kotlin
for (char in 'a'..'z') print(char)
// stampa abcdefghijklmnopqrstuvwxyz
```

---

È possibile iterare su una __Stringa__.
```kotlin
for (char in 'abc') print(char + 1)
// stampa bdc
```

Nell'esempio precedente abbiamo stampato ogni carattere + 1, quindi `'a'` è diventato `'b'`, `'b'` è diventato `'c'` e così via.

Questo è possibile perché i caratteri sono memorizzati come numeri corrispondenti ai loro [Codici ASCII](https://it.wikipedia.org/wiki/ASCII).

Quindi l'aggiunta di un numero intero a un carattere produce un nuovo carattere corrispondente al nuovo valore del codice.

---

Nel caso in cui si debba semplicemente ripetere un blocco di codice `n` volte, si può usare la funzione `repeat(times: Int)`.

```kotlin
repeat(3) {
    println("ripeti")
}
// stampa ripeti 3 volte
```

Si può anche accedere all'indice con
```kotlin
repeat(3) { indice ->
    println(indice)
}
// stampa 0, 1, 2
```

---

In Kotlin possiamo usare il ciclo `for-in` anche per collezioni iterabili, richiamando la [closure](https://it.wikipedia.org/wiki/Chiusura_(informatica)) fornita su ogni elemento:
```kotlin
// questa è una lista, la vedremo presto
val numeri = listOf(2, 4, 6, 8, 10) 
for (num in numeri) {
    println(num)
}
// stampa (2, 4, 6, 8, 10)
```

---

In Kotlin abbiamo anche il ciclo `forEach`.
Esso richiama la chiusura (_closure_) fornita su ogni elemento della sequenza nello stesso ordine di un ciclo `for-in`:

```kotlin
// questa è una lista, la vedremo presto
val numeri = listOf(1, 3, 5, 7, 9) 
numeri.forEach {
    println(it)
}
```

L'uso del metodo `forEach` si distingue da un ciclo `for-in` per due aspetti importanti:
1. Le istruzioni `break` o `continue` non possono essere usate per uscire dalla chiamata corrente della chiusura del corpo o per saltare le chiamate successive. (_In realtà è possibile con le annotazioni, ma è un argomento un po' più complesso che non vedremo ora).
2. L'uso dell'istruzione `return` nel corpo della chiusura farà uscire solo dalla chiusura e non l'ambito esterno, e non salterà le chiamate successive.
