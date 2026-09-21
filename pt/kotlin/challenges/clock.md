---
language: kotlin
exerciseType: 1
difficulty: 2
title: Relógio
---

# --description--

Um relógio de 24 horas mostra a hora do dia como `HH:MM`, começando em `00:00` logo após a meia-noite e terminando em `23:59`, um minuto antes da próxima meia-noite. Ambas as partes são sempre escritas com dois dígitos, então nove minutos após onze da manhã lê-se `11:09`.

Um dia inteiro dura 1440 minutos. Quando o relógio passa de `23:59`, ele volta para `00:00` e começa o dia novamente, e girá-lo para trás além de `00:00` cai em `23:59`.

# --instructions--

Escreva uma função `clockTime` que recebe dois números inteiros, `hours` e `minutes`, e retorna a leitura de um relógio de 24 horas como a string `"HH:MM"`, com ambas as partes preenchidas com dois dígitos.

Exemplos:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Qualquer um dos números pode ser negativo, ou maior do que um relógio real permite.
- Calcule o número total de minutos como `hours * 60 + minutes` e depois encaixe esse total na faixa de `0` a `1439` para que o relógio faça a volta em ambas as direções.
- `clockTime(24, 0)` é exatamente um dia, então lê-se `"00:00"`.

# --seed--

```kotlin
fun clockTime(hours: Int, minutes: Int): String {
    
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

Oito da manhã lê-se `08:00`

```kotlin
    tryCatch(clockTime(8, 0) == "08:00")
```

Números de um dígito são preenchidos com dois, então nove minutos após onze lê-se `11:09`

```kotlin
    tryCatch(clockTime(11, 9) == "11:09")
```

Exatamente um dia inteiro de horas faz a volta para `00:00`

```kotlin
    tryCatch(clockTime(24, 0) == "00:00")
```

Minutos acima de 60 são transportados para as horas

```kotlin
    tryCatch(clockTime(25, 160) == "03:40")
```

Uma hora negativa gira o relógio para trás além da meia-noite

```kotlin
    tryCatch(clockTime(-1, 15) == "23:15")
```

Uma contagem de minutos negativa também gira o relógio para trás

```kotlin
    tryCatch(clockTime(0, -90) == "22:30")
```

Mais de um dia inteiro para trás continua fazendo a volta

```kotlin
    tryCatch(clockTime(-25, 0) == "23:00")
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
fun clockTime(hours: Int, minutes: Int): String {
    // O % mantém o sinal do operando à esquerda, mas mod() sempre volta
    // para a faixa 0..1439.
    val total = (hours * 60 + minutes).mod(1440)

    return "%02d:%02d".format(total / 60, total % 60)
}
```
