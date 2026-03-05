A tomada de decisao e necessaria quando queremos executar codigo apenas se uma determinada condicao for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o clima estiver bom.
Na programacao, podemos salvar uma variavel booleana `niceWeather` e executar a acao de brincar ao ar livre `if` (se) essa variavel for `true`, assim:
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
Vimos que a instrucao `if` executa o bloco de codigo apenas se a condicao for `true`.
Outra coisa importante a considerar sao as **chaves** `{}` que indicam um bloco de codigo.

---

Acabamos de ver como executar um bloco de codigo se uma condicao ocorrer, agora vamos ver como executar outro bloco de codigo se a primeira condicao falhar.
Vamos brincar ao ar livre se o clima estiver bom; caso contrario, ficamos em casa.
Em Kotlin podemos usar a instrucao `else`, assim:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Vamos supor que temos outra condicao para verificar, como neste exemplo:
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
e a saida deste codigo e `the number is 3`.
Primeiro, vamos verificar se o numero e igual a 2, isso e falso.
Entao vamos para a segunda instrucao e verificamos se `num` e igual a 3, sendo verdadeiro executamos o bloco de codigo seguinte imprimindo `the number is 3`

---

Podemos adicionar quantas instrucoes `else if` quisermos, nao ha limites
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
e a saida deste codigo e `the number is 4`.

---

Tambem podemos aninhar uma instrucao condicional (`if`, `else if` ou `else`) dentro de outra instrucao condicional, para criar uma estrutura mais complexa.
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
e a saida deste codigo e `the number is 4`.

---

O _operador elvis_ `a ?: b` desembrulha um opcional `a` se ele contiver um valor, ou retorna um valor padrao `b` se `a` for `null`.
A expressao `a` e sempre de um tipo opcional.
A expressao `b` deve corresponder ao tipo que esta armazenado dentro de a.
O operador elvis e uma abreviacao para o codigo abaixo:
```kotlin
if (a != null) a else b
```
