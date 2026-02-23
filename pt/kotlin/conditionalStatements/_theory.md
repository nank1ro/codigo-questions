A tomada de decisão é necessária quando queremos executar código apenas se uma certa condição for satisfeita.
Vamos supor que queremos brincar fora apenas se o tempo estiver bom.
Na programação, podemos salvar uma variável booleana `niceWeather` e realizar a ação de brincar fora `if` esta variável for `true`, como:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

Vamos continuar com o exemplo anterior.
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
Vimos que a declaração `if` executa o bloco de código apenas se a condição for `true`.
Outra coisa importante a considerar é representada pelas **chaves** `{}` que indicam um bloco de código.

---

Acabamos de ver como executar um bloco de código se uma condição ocorre, agora vamos ver como executar outro bloco de código se a primeira condição falhar.
Vamos brincar fora se o tempo estiver bom; caso contrário, ficamos em casa.
Em Kotlin podemos usar a declaração `else`, como:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
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
Então vamos passar para a segunda declaração e verificar se `num` é igual a 3, sendo verdadeiro executamos o seguinte bloco de código imprimindo `the number is 3`

---

Podemos adicionar quantas declarações `else if` quisermos, não há limites
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

Também podemos aninhar uma declaração condicional (`if`, `else if` ou `else`) dentro de outra declaração condicional, para criar uma estrutura mais complexa.
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

O _operador elvis_ `a ?: b` desempacota um opcional `a` se ele contiver um valor, ou retorna um valor padrão `b` se `a` for `null`.
A expressão `a` é sempre de um tipo opcional.
A expressão `b` deve corresponder ao tipo que está armazenado em a.
O operador elvis é uma abreviação para o código abaixo:
```kotlin
if (a != null) a else b
```
