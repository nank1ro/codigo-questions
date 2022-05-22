---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 porte
---

# --description--

Ci sono 100 porte in fila che inizialmente sono tutte chiuse.
Fai 100 passaggi davanti alle porte.
La prima volta che passi, visita ogni porta e "alterna" la porta (se la porta è chiusa, aprila; se è aperta, chiudila).
La seconda volta, visita solo ogni 2a porta (cioè la porta #2, #4, #6, ...) e modificala.
La terza volta, visita ogni 3a porta (cioè la porta #3, #6, #9, ...), etc., fino a visitare solo la 100esima porta.

# --instructions--

Implementa una funzione per determinare lo stato delle porte dopo l'ultimo passaggio.
Restituire il risultato finale in un array, con solo il numero delle porte aperte.
> Il metodo deve essere in grado di funzionare con un numero variabile di porte.

# --seed--

```kotlin
fun calcolaPorteAperte(numDoors: Int): ArrayList<Int> {
    
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

Date 100 porte, restituire l'elenco corretto delle porte aperte

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(calcolaPorteAperte(100) == solution1)
```

Date 10 porte, restituire l'elenco corretto delle porte aperte

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(calcolaPorteAperte(10) == solution2)
```

Date 950 porte, restituire l'elenco corretto delle porte aperte

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(calcolaPorteAperte(950) == solution3)
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
fun quadrato(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun calcolaPorteAperte(numDoors: Int): ArrayList<Int> {
    val porteAperte = ArrayList<Int>()
    var i = 1
    while (quadrato(i) <= numDoors) {
        porteAperte.add(quadrato(i))
        i += 1
    }
    return porteAperte
}
```
