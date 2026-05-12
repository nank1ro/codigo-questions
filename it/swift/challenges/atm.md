---
language: swift
exerciseType: 1
difficulty: 1
title: ATM
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

> SUGGERIMENTO: ometti il nome degli argomenti con l'underscore `_`

Esempio di chiamata della funzione:
```swift
print(saldoConto(10, 20))
// stampa 9,5
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func saldoConto() -> Double {
    return
}
```

# --asserts--

Esegui una transazione con successo

```swift
do {
    let expected: Double = 69.50
    tryCatch(saldoConto(50, 120.00) == expected)
}
```

Fondi insufficienti

```swift
do {
    let expected: Double = 120.00
    tryCatch(saldoConto(200, 120.00) == expected)
}
```

Transazione rifiutata, importo non valido

```swift
do {
    let expected: Double = 120.00
    tryCatch(saldoConto(22, 120.00) == expected)
}
```

Preleva tutti i soldi con successo

```swift
do {
    let expected: Double = 0.00
    tryCatch(saldoConto(95, 95.50) == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func saldoConto(_ prelievo: Double,_ bilancio: Double) -> Double {
    let multiploDi5 = prelievo.truncatingRemainder(dividingBy: 5) == 0;
    let importoDisponibile = bilancio >= (prelievo + 0.50)
    if multiploDi5 && importoDisponibile {
        return bilancio - prelievo - 0.50
    }
    return bilancio
}
```
