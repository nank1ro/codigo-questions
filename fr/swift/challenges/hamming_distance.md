---
language: swift
exerciseType: 1
difficulty: 1
title: Distance de Hamming
---

# --description--

L'ADN s'écrit sous la forme d'un brin de nucléotides, chacun étant une seule lettre : `A`, `C`, `G` ou `T`. Lorsque deux brins de même longueur sont alignés côte à côte, certaines positions portent le même nucléotide et d'autres un nucléotide différent.

Le nombre de positions où les deux brins diffèrent s'appelle la distance de Hamming, et les biologistes l'utilisent pour mesurer à quel point deux brins ont divergé. L'alignement de `GAGCCTACTAACGGGAT` avec `CATCGTAATGACGGCCT` donne 7 positions différentes, leur distance de Hamming est donc 7.

# --instructions--

Écrivez une fonction `hammingDistance` qui prend deux brins d'ADN de même longueur et retourne le nombre de positions où ils diffèrent.

Exemples :
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Les deux brins ont toujours la même longueur, vous n'avez donc jamais à gérer des brins de longueurs différentes.
- Deux brins vides ne diffèrent nulle part, leur distance est donc 0.

> ASTUCE : omettez les étiquettes d'arguments avec le `_` (trait de soulignement)

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
func hammingDistance(_ left: String, _ right: String) -> Int {
    
}
```

# --asserts--

Deux brins vides ne diffèrent nulle part

```swift
tryCatch(hammingDistance("", "") == 0)
```

Deux brins identiques d'un seul nucléotide n'ont aucune différence

```swift
tryCatch(hammingDistance("A", "A") == 0)
```

Deux brins d'un seul nucléotide différents diffèrent en une position

```swift
tryCatch(hammingDistance("A", "G") == 1)
```

Deux brins courts qui diffèrent à chaque position

```swift
tryCatch(hammingDistance("AG", "CT") == 2)
```

Deux brins courts qui ne diffèrent qu'à la première position

```swift
tryCatch(hammingDistance("AT", "CT") == 1)
```

Un seul nucléotide différent au milieu des brins

```swift
tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Les mêmes nucléotides à des positions différentes comptent quand même comme des différences

```swift
tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Une paire de brins plus longue avec quatre différences

```swift
tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Décaler un brin d'une position fait différer presque toutes les positions

```swift
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

Les deux brins de la description ont une distance de sept

```swift
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func hammingDistance(_ left: String, _ right: String) -> Int {
    var distance = 0

    for (leftNucleotide, rightNucleotide) in zip(left, right) {
        if leftNucleotide != rightNucleotide {
            distance += 1
        }
    }

    return distance
}
```
