---
language: kotlin
exerciseType: 1
difficulty: 3
title: "Ano bissexto"
---

# --description--

Em um ano civil existem exatamente 365,25 dias. Mas, eventualmente, isso levará a confusão porque os humanos normalmente contam pela divisibilidade exata de 1 e não com casas decimais. Então, para evitar isso, foi decidido acumular todos os 0,25 dias a cada ciclo de quatro anos e dar a esse ano 366 dias (incluindo 29 de fevereiro como dia intercalar) e chamá-lo de __ano bissexto__. Os outros três anos no ciclo de quatro anos conteriam apenas 365 dias e __não seriam anos bissextos__.

# --instructions--

Neste desafio, levaremos a um novo nível, onde você deve determinar se é um ano bissexto ou não sem o uso da classe `Date`, instruções `switch`, __blocos if__, __blocos if-else__ ou __operação ternária__ (`x ? a : b`) nem os operadores lógicos __AND__ (`&&`) e __OR__ (`||`) com a exceção do operador __NOT__ (`!`).

Retorne `true` se for um ano bissexto, `false` caso contrário.

Exemplo de chamada da função:
```kotlin
println(leapYear(2000))
// prints true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
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

O uso de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` não é permitido.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

O ano `2016` é um ano bissexto.

```kotlin
    tryCatch(leapYear(2016) == true)
```

O ano `1996` é um ano bissexto.

```kotlin
    tryCatch(leapYear(1996) == true)
```

O ano `1600` é um ano bissexto.

```kotlin
    tryCatch(leapYear(1600) == true)
```

O ano `2020` é um ano bissexto.

```kotlin
    tryCatch(leapYear(2020) == true)
```

O ano `2000` é um ano bissexto.

```kotlin
    tryCatch(leapYear(2000) == true)
```

O ano `2008` é um ano bissexto.

```kotlin
    tryCatch(leapYear(2008) == true)
```

O ano `1521` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(1521) == false)
```

O ano `1800` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(1800) == false)
```

O ano `2007` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(2007) == false)
```

O ano `2002` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(2002) == false)
```

O ano `1979` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(1979) == false)
```

O ano `2006` não é um ano bissexto.

```kotlin
    tryCatch(leapYear(2006) == false)
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
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
