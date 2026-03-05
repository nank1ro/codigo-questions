---
language: kotlin
exerciseType: 1
difficulty: 1
title: "Gotas de Chuva"
---

# --description--

Sua tarefa é converter um número em uma string que contenha sons de gotas de chuva correspondentes a certos fatores potenciais.
Um fator é um número que divide outro número de forma exata, sem deixar resto.
A maneira mais simples de testar se um número é um fator de outro é usar a operação módulo.
As regras das gotas de chuva são que, se um determinado número:

- tem 3 como fator, adicione 'Pling' ao resultado.
- tem 5 como fator, adicione 'Plang' ao resultado.
- tem 7 como fator, adicione 'Plong' ao resultado.
- não tem 3, 5 ou 7 como fator, o resultado deve ser os dígitos do número.

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

- 28 tem 7 como fator, mas não 3 ou 5, então o resultado seria `"Plong"`.
- 30 tem tanto 3 quanto 5 como fatores, mas não 7, então o resultado seria `"PlingPlang"`.
- 34 não é divisível por 3, 5 ou 7, então o resultado seria `"34"`.

Exemplo de chamada da função:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

O som para 1 é "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

O som para 3 é "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

O som para 5 é "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

O som para 7 é "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

O som para 6 é "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

O som para 8 é "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

O som para 9 é "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

O som para 10 é "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

O som para 14 é "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

O som para 15 é "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

O som para 21 é "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

O som para 25 é "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

O som para 27 é "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

O som para 35 é "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

O som para 49 é "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

O som para 52 é "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

O som para 105 é "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

O som para 3125 é "Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
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
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
