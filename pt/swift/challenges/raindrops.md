---
language: swift
exerciseType: 1
difficulty: 1
title: "Gotas de chuva"
---

# --description--

Sua tarefa é converter um número em uma string que contenha sons de gotas de chuva correspondentes a certos fatores potenciais.
Um fator é um número que divide outro número de forma exata, sem deixar resto.
A maneira mais simples de testar se um número é fator de outro é usar a operação módulo.
As regras das gotas de chuva são que, se um determinado número:

- tem 3 como fator, adicione 'Pling' ao resultado.
- tem 5 como fator, adicione 'Plang' ao resultado.
- tem 7 como fator, adicione 'Plong' ao resultado.
- não tem nenhum dos fatores 3, 5 ou 7, o resultado deve ser os dígitos do número.

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

- 28 tem 7 como fator, mas não 3 ou 5, então o resultado seria `"Plong"`.
- 30 tem tanto 3 quanto 5 como fatores, mas não 7, então o resultado seria `"PlingPlang"`.
- 34 não é divisível por 3, 5 ou 7, então o resultado seria `"34"`.

> DICA: omita o rótulo do argumento com o `_` (underscore)

Exemplo de chamada da função:
```swift
print(raindrops(28))
// prints "Plong"
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
func raindrops() {
    
}
```

# --asserts--

O som para 1 é "1"

```swift
tryCatch("1" == raindrops(1))
```

O som para 3 é "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

O som para 5 é "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

O som para 7 é "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

O som para 6 é "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

O som para 8 é "8"

```swift
tryCatch("8" == raindrops(8))
```

O som para 9 é "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

O som para 10 é "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

O som para 14 é "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

O som para 15 é "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

O som para 21 é "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

O som para 25 é "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

O som para 27 é "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

O som para 35 é "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

O som para 49 é "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

O som para 52 é "52"

```swift
tryCatch("52" == raindrops(52))
```

O som para 105 é "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

O som para 3125 é "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


