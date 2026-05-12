---
language: swift
exerciseType: 1
difficulty: 1
title: "Função de Ackermann"
---

# --description--

A função de Ackermann é um exemplo clássico de uma função recursiva, notável especialmente porque não é uma função recursiva primitiva. Ela cresce muito rapidamente em valor, assim como o tamanho de sua árvore de chamadas.

A função de Ackermann é geralmente definida da seguinte forma:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Seus argumentos nunca são negativos e ela sempre termina

# --instructions--

Escreva uma função que retorne o valor da função de Ackermann.

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` deve retornar 1.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` deve retornar 3.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` deve retornar 13.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` deve retornar 61.

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
