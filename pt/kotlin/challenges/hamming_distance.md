---
language: kotlin
exerciseType: 1
difficulty: 1
title: Distância de Hamming
---

# --description--

O DNA é escrito como uma fita de nucleotídeos, cada um representado por uma única letra: `A`, `C`, `G` ou `T`. Quando duas fitas de mesmo comprimento são alinhadas lado a lado, algumas posições contêm o mesmo nucleotídeo e outras contêm nucleotídeos diferentes.

O número de posições em que as duas fitas diferem é chamado de distância de Hamming, e biólogos o usam para medir o quanto duas fitas se afastaram uma da outra. Alinhar `GAGCCTACTAACGGGAT` com `CATCGTAATGACGGCCT` resulta em 7 posições que diferem, de modo que a distância de Hamming entre elas é 7.

# --instructions--

Escreva uma função `hammingDistance` que recebe duas fitas de DNA de mesmo comprimento e retorna o número de posições em que elas diferem.

Exemplos:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- As duas fitas sempre têm o mesmo comprimento, então você nunca precisa lidar com fitas de comprimentos diferentes.
- Duas fitas vazias não diferem em nenhuma posição, então a distância entre elas é 0.

# --seed--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Duas fitas vazias não diferem em nenhuma posição

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

Duas fitas idênticas de um único nucleotídeo não têm nenhuma diferença

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

Duas fitas diferentes de um único nucleotídeo diferem em uma posição

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

Duas fitas curtas que diferem em todas as posições

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

Duas fitas curtas que diferem apenas na primeira posição

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

Um único nucleotídeo diferente no meio das fitas

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Os mesmos nucleotídeos em posições diferentes ainda contam como diferenças

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Um par de fitas mais longo com quatro diferenças

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Deslocar uma fita em uma posição faz quase todas as posições diferirem

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

As duas fitas da descrição têm uma distância de sete

```kotlin
    tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    var distance = 0

    for (i in left.indices) {
        if (left[i] != right[i]) {
            distance++
        }
    }

    return distance
}
```
