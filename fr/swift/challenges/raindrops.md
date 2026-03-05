---
language: swift
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne contenant des sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui divise exactement un autre nombre, sans reste.
Le moyen le plus simple de tester si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont que si un nombre donné :

- a 3 comme facteur, ajoutez 'Pling' au résultat.
- a 5 comme facteur, ajoutez 'Plang' au résultat.
- a 7 comme facteur, ajoutez 'Plong' au résultat.
- n'a pas 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas factorisé par 3, 5 ou 7, donc le résultat serait `"34"`.

> ASTUCE : omettez l'étiquette d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(raindrops(28))
// prints "Plong"
```

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Le son pour 1 est "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

Le son pour 3 est "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

Le son pour 5 est "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

Le son pour 7 est "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

Le son pour 6 est "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

Le son pour 8 est "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

Le son pour 9 est "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

Le son pour 10 est "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

Le son pour 14 est "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

Le son pour 15 est "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

Le son pour 21 est "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

Le son pour 25 est "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

Le son pour 27 est "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

Le son pour 35 est "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

Le son pour 49 est "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

Le son pour 52 est "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

Le son pour 105 est "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

Le son pour 3125 est "Plang"

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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


