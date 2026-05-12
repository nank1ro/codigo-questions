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
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --asserts--

Dadas 100 portas, retorne a lista correta de portas abertas

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

Dadas 10 portas, retorne a lista correta de portas abertas

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

Dadas 950 portas, retorne a lista correta de portas abertas

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    tryCatch(getFinalOpenedDoors(950) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
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
