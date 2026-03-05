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

# --seed--

```swift
func leapYear(_ year: Int) -> Bool {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
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
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

O ano `1996` é um ano bissexto.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

O ano `1600` é um ano bissexto.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

O ano `2020` é um ano bissexto.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

O ano `2000` é um ano bissexto.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

O ano `2008` é um ano bissexto.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

O ano `1521` não é um ano bissexto.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

O ano `1800` não é um ano bissexto.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

O ano `2007` não é um ano bissexto.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

O ano `2002` não é um ano bissexto.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

O ano `1979` não é um ano bissexto.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

O ano `2006` não é um ano bissexto.

```swift
    func test12() {
        XCTAssertEqual(leapYear(2006), false, "--err-t12--")
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
            ("test4", test4),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test11", test11),
            ("test12", test12), 
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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
