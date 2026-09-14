---
language: kotlin
exerciseType: 1
difficulty: 2
title: Ordenação por bolha
---

# --description--

A ordenação por bolha é um dos algoritmos de ordenação mais simples. Ela percorre uma lista e compara cada par de elementos adjacentes, trocando-os sempre que estão na ordem errada. Depois de cada passagem completa, o maior valor restante "borbulhou" até a sua posição final, e a lista está ordenada assim que uma passagem termina sem uma única troca.

# --instructions--

Escreva uma função chamada `bubbleSort` que receba uma `List<Int>` e devolva uma **nova** lista com os mesmos valores ordenados em ordem crescente. A lista passada não deve ser modificada.

Você deve implementar o algoritmo de ordenação por bolha por conta própria, comparando e trocando elementos adjacentes. Não use uma função de ordenação da biblioteca padrão.

A sua função também deve funcionar com um array vazio, um array com um único elemento, um array já ordenado, valores repetidos e números negativos.

Exemplo de chamada de função:
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// prints [1, 2, 3]
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

Um array vazio deve devolver um array vazio

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Um array com um único elemento deve permanecer igual

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Um array já ordenado deve manter a mesma ordem

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Um array ordenado ao contrário deve ser colocado em ordem crescente

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Todos os valores repetidos devem ser mantidos

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Os números negativos devem ser ordenados antes dos positivos

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Um array misto mais longo deve ser ordenado em ordem crescente

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
