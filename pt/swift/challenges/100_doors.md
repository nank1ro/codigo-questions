---
language: swift
exerciseType: 1
difficulty: 1
title: 100 portas
---

# --description--

Existem 100 portas em uma fileira que estão todas inicialmente fechadas.
Você faz 100 passagens pelas portas.
Na primeira vez, visite cada porta e 'alterne' a porta (se a porta estiver fechada, abra-a; se estiver aberta, feche-a).
Na segunda vez, visite apenas cada 2ª porta (ou seja, porta #2, #4, #6, ...) e alterne-a.
Na terceira vez, visite cada 3ª porta (ou seja, porta #3, #6, #9, ...), etc., até que você visite apenas a 100ª porta.

# --instructions--

Implemente uma função para determinar o estado das portas após a última passagem.
Retorne o resultado final em um array, com apenas o número da porta incluído no array se ela estiver aberta.
> O método deve ser capaz de funcionar com um número variável de portas.

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Dadas 100 portas, retorne a lista correta de portas abertas

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

Dadas 10 portas, retorne a lista correta de portas abertas

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

Dadas 950 portas, retorne a lista correta de portas abertas

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
