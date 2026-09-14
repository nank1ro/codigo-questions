---
language: kotlin
exerciseType: 1
difficulty: 2
title: Busca binária
---

# --description--

A busca binária encontra um valor dentro de uma coleção **ordenada** dividindo o intervalo de busca pela metade repetidamente: olhe o elemento no meio e, se não for o que você procura, continue na metade esquerda quando o alvo for menor ou na metade direita quando o alvo for maior.

Como cada etapa descarta metade dos elementos restantes, a busca binária chega à resposta em poucas comparações, mesmo em coleções muito grandes, enquanto verificar os elementos um por um custaria tantos passos quanto o número de elementos.

# --instructions--

Escreva uma função `binarySearch` que recebe um array de inteiros ordenado em ordem crescente e um inteiro alvo, e retorna o índice do alvo dentro do array, ou `-1` quando o alvo não está presente.

O array nunca contém duplicatas, então o índice é sempre único. O array também pode estar vazio. Sua função deve usar busca binária, dividindo o intervalo de busca pela metade a cada passo, e não uma varredura linear.

Exemplo de chamada da função:
```kotlin
println(binarySearch(intArrayOf(1, 3, 5, 7), 5))
// prints 2
```

# --seed--

```kotlin
fun binarySearch() {

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

A busca em um array vazio deve retornar -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

A busca por 5 em `[5]` deve retornar 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

A busca por 9 em `[5]` deve retornar -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

O primeiro elemento -9 do array de 12 elementos deve ser encontrado no índice 0

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

O último elemento 78 do array de 12 elementos deve ser encontrado no índice 11

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

O elemento 15 deve ser encontrado no índice 6

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

O elemento 22 deve ser encontrado no índice 7

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

O valor 12, que está entre 11 e 15, deve retornar -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

Um alvo menor que todos os elementos deve retornar -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

Um alvo maior que todos os elementos deve retornar -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 100) == -1)
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
fun binarySearch(arr: IntArray, target: Int): Int {
    var low = 0
    var high = arr.size - 1
    while (low <= high) {
        val mid = low + (high - low) / 2
        if (arr[mid] == target) {
            return mid
        }
        if (arr[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
```
