---
language: kotlin
exerciseType: 1
difficulty: 2
title: Ricerca binaria
---

# --description--

La ricerca binaria trova un valore all'interno di una collezione **ordinata** dimezzando ripetutamente l'intervallo di ricerca: guarda l'elemento centrale e, se non è quello che cerchi, continua nella metà sinistra quando il valore cercato è più piccolo o nella metà destra quando è più grande.

Poiché ogni passo scarta metà degli elementi rimanenti, la ricerca binaria arriva alla risposta in poche comparazioni anche su collezioni molto grandi, mentre controllare gli elementi uno per uno costerebbe tanti passi quanti sono gli elementi.

# --instructions--

Scrivi una funzione `binarySearch` che riceve un array di numeri interi ordinato in modo crescente e un numero intero cercato, e restituisce l'indice del valore cercato all'interno dell'array, oppure `-1` quando il valore non è presente.

L'array non contiene mai duplicati, quindi l'indice è sempre unico. L'array può anche essere vuoto. La tua funzione deve usare la ricerca binaria, dimezzando l'intervallo di ricerca a ogni passo, non una scansione lineare.

Esempio di chiamata di funzione:
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

La ricerca in un array vuoto deve restituire -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

La ricerca di 5 in `[5]` deve restituire 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

La ricerca di 9 in `[5]` deve restituire -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

Il primo elemento -9 dell'array di 12 elementi deve essere trovato all'indice 0

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

L'ultimo elemento 78 dell'array di 12 elementi deve essere trovato all'indice 11

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

L'elemento 15 deve essere trovato all'indice 6

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

L'elemento 22 deve essere trovato all'indice 7

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

Il valore 12, che si trova tra 11 e 15, deve restituire -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

Un valore cercato più piccolo di ogni elemento deve restituire -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

Un valore cercato più grande di ogni elemento deve restituire -1

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
