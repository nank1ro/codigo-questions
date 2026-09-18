A tomada de decisão é necessária quando queremos executar código apenas se uma determinada condição for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o clima estiver bom.
Na programação, podemos salvar uma variável booleana `niceWeather` e executar a ação de brincar ao ar livre `if` (se) essa variável for `true`, assim:
```kotlin
var niceWeather = true
if (niceWeather) {
    // brincar lá fora
}
```

---

Vamos continuar com o exemplo anterior.
```kotlin
var niceWeather = true
if (niceWeather) {
    // brincar lá fora
}
```
Vimos que a instrução `if` executa o bloco de código apenas se a condição for `true`.
Outra coisa importante a considerar são as **chaves** `{}` que indicam um bloco de código.

---

Acabamos de ver como executar um bloco de código se uma condição ocorrer, agora vamos ver como executar outro bloco de código se a primeira condição falhar.
Vamos brincar ao ar livre se o clima estiver bom; caso contrário, ficamos em casa.
Em Kotlin podemos usar a instrução `else`, assim:
```kotlin
var niceWeather = true
if (niceWeather) {
    // brincar lá fora
} else {
    // ficar em casa
}
```

---

Vamos supor que temos outra condição para verificar, como neste exemplo:
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
e a saída deste código é `the number is 3`.
Primeiro, vamos verificar se o número é igual a 2, isso é falso.
Então vamos para a segunda instrução e verificamos se `num` é igual a 3, sendo verdadeiro executamos o bloco de código seguinte imprimindo `the number is 3`

---

Podemos adicionar quantas instruções `else if` quisermos, não há limites
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
e a saída deste código é `the number is 4`.

---

Também podemos aninhar uma instrução condicional (`if`, `else if` ou `else`) dentro de outra instrução condicional, para criar uma estrutura mais complexa.
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
e a saída deste código é `the number is 4`.

---

O _operador elvis_ `a ?: b` desembrulha um opcional `a` se ele contiver um valor, ou retorna um valor padrão `b` se `a` for `null`.
A expressão `a` é sempre de um tipo opcional.
A expressão `b` deve corresponder ao tipo que está armazenado dentro de a.
O operador elvis é uma abreviação para o código abaixo:
```kotlin
if (a != null) a else b
```
