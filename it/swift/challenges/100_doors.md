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

# --seed--

```swift
func calcolaPorteAperte(_ numPorte: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Date 100 porte, restituire l'elenco corretto delle porte aperte

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(calcolaPorteAperte(100), solution, "--err-t1--")
    }
```

Date 10 porte, restituire l'elenco corretto delle porte aperte

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(calcolaPorteAperte(16), solution, "--err-t2--")
    }
```

Date 950 porte, restituire l'elenco corretto delle porte aperte

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(calcolaPorteAperte(950), solution, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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
