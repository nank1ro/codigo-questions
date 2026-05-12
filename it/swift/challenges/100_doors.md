---
language: swift
exerciseType: 1
difficulty: 1
title: 100 porte
---

# --description--

Ci sono 100 porte in fila che inizialmente sono tutte chiuse.
Fai 100 passaggi davanti alle porte.
La prima volta che passi, visita ogni porta e "alterna" la porta (se la porta è chiusa, aprila; se è aperta, chiudila).
La seconda volta, visita solo ogni 2a porta (cioè la porta #2, #4, #6, ...) e modificala.
La terza volta, visita ogni 3a porta (cioè la porta #3, #6, #9, ...), etc., fino a visitare solo la 100esima porta.

# --instructions--

Implementa una funzione per determinare lo stato delle porte dopo l'ultimo passaggio.
Restituire il risultato finale in un array, con solo il numero delle porte aperte.
> Il metodo deve essere in grado di funzionare con un numero variabile di porte.

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
func calcolaPorteAperte(_ numPorte: Int) -> Array<Int> {
    
}
```

# --asserts--

Date 100 porte, restituire l'elenco corretto delle porte aperte

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(calcolaPorteAperte(100) == solution)
}
```

Date 10 porte, restituire l'elenco corretto delle porte aperte

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(calcolaPorteAperte(10) == solution)
}
```

Date 950 porte, restituire l'elenco corretto delle porte aperte

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    tryCatch(calcolaPorteAperte(950) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func alQuadrato(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func calcolaPorteAperte(_ numPorte: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (alQuadrato(i) <= numPorte) {
        openDoors.append(alQuadrato(i))
        i += 1
    }
    return openDoors
}
```
