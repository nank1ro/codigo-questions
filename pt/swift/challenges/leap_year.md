---
language: swift
exerciseType: 1
difficulty: 3
title: "Ano bissexto"
---

# --description--

Em um ano civil existem exatamente 365,25 dias. Mas, eventualmente, isso levará a confusão porque os humanos normalmente contam pela divisibilidade exata de 1 e não com casas decimais. Então, para evitar isso, foi decidido somar todos os 0,25 dias a cada ciclo de quatro anos e dar a esse ano 366 dias (incluindo 29 de fevereiro como um dia intercalar) e chamá-lo de __ano bissexto__. Os outros três anos no ciclo de quatro anos conteriam apenas 365 dias e __não seriam anos bissextos__.

# --instructions--

Neste desafio, vamos levar a um novo nível, onde você deve determinar se é um ano bissexto ou não sem o uso da classe `Date`, instruções `switch`, blocos __if__, blocos __if-else__ ou __operação ternária__ (`x ? a : b`) nem os operadores lógicos __AND__ (`&&`) e __OR__ (`||`) com exceção do operador __NOT__ (`!`).

Retorne `true` se for um ano bissexto, `false` caso contrário.

Exemplo de chamada da função:
```swift
print(leapYear(2000))
// prints true
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

O uso de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` não é permitido.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

O ano `2016` é um ano bissexto.

```swift
tryCatch(leapYear(2016) == true)
```

O ano `1996` é um ano bissexto.

```swift
tryCatch(leapYear(1996) == true)
```

O ano `1600` é um ano bissexto.

```swift
tryCatch(leapYear(1600) == true)
```

O ano `2020` é um ano bissexto.

```swift
tryCatch(leapYear(2020) == true)
```

O ano `2000` é um ano bissexto.

```swift
tryCatch(leapYear(2000) == true)
```

O ano `2008` é um ano bissexto.

```swift
tryCatch(leapYear(2008) == true)
```

O ano `1521` não é um ano bissexto.

```swift
tryCatch(leapYear(1521) == false)
```

O ano `1800` não é um ano bissexto.

```swift
tryCatch(leapYear(1800) == false)
```

O ano `2007` não é um ano bissexto.

```swift
tryCatch(leapYear(2007) == false)
```

O ano `2002` não é um ano bissexto.

```swift
tryCatch(leapYear(2002) == false)
```

O ano `1979` não é um ano bissexto.

```swift
tryCatch(leapYear(1979) == false)
```

O ano `2006` não é um ano bissexto.

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
