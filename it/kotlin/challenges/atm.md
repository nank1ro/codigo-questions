---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James vorrebbe prelevare N euro da un bancomat.
Il bancomat accetterà la transazione solo se N è un multiplo di 5 e il conto di James ha abbastanza contante per eseguire il prelievo (incluse le commissioni bancarie).
Per ogni prelievo effettuato con successo, la banca addebita 0.50€.
Calcola il saldo del conto di James dopo un tentativo di transazione.
Gli input sono nell'ordine seguente:
1. la quantità di contanti che James desidera prelevare è nel seguente intervallo: `0 < N <= 2000`.
2. Il saldo iniziale di James viene fornito con due cifre decimali ed è nel seguente intervallo: `0 < B <= 2000`.

# --instructions--

Restituisci il saldo del conto, con due cifre decimali, dopo il tentativo di transazione.
Se non c'è abbastanza denaro nel conto per completare l'operazione, restituire il saldo bancario corrente.

Esempio di chiamata:
```kotlin
println(saldoConto(10, 20.00))
// stampa 9.5
```

# --seed--

```kotlin
fun saldoConto(): Double {
    return
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Esegui una transazione con successo

```kotlin
    tryCatch(saldoConto(50, 120.00) == 69.50)
```

Fondi insufficienti

```kotlin
    tryCatch(saldoConto(200, 120.00) == 120.00)
```

Transazione rifiutata, importo non valido

```kotlin
    tryCatch(saldoConto(22, 120.00) == 120.00)
```

Preleva tutti i soldi con successo

```kotlin
    tryCatch(saldoConto(95, 95.50) == 0.00)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun saldoConto(prelievo: Int, bilancio: Double): Double {
    val multiploDi5 = prelievo.rem(5) == 0;
    val importoDisponibile = bilancio >= (prelievo + 0.50)
    if (multiploDi5 && importoDisponibile) {
        return bilancio - prelievo - 0.50
    }
    return bilancio
}
```
