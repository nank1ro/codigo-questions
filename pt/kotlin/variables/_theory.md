Variáveis são contêineres para armazenar valores de dados.
Cada variável em Kotlin é um objeto.
Para criar uma variável, precisamos dar a ela um __nome__ lembrando que não deve conter espaços.
Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.
Em Kotlin, você declara constantes com a palavra-chave `val` (abreviação de _value_) e variáveis com a palavra-chave `var` (abreviação de _variable_).
O valor de uma constante não pode ser alterado depois de definido, enquanto uma variável pode receber um valor diferente no futuro.
Um exemplo de criação de variável chamada `x` é:
```kotlin
var x = 1
```
Dessa forma, atribuímos o valor `1` à variável chamada `x`.
Se imprimirmos a variável `x`, obtemos o número `1`:
```kotlin
println(x) // prints 1
```

---

Variáveis são chamadas assim porque o valor que armazenam pode mudar.
Podemos atualizar `x` usando `=` e atribuindo um novo valor.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

Também podemos atribuir a variáveis os valores de outras variáveis. Aqui, podemos atribuir à variável `y` o valor de `x`
```kotlin
var x = 5
var y = x
println(y) // prints 5
```

---

Quando atualizamos uma variável, ela esquece seu valor anterior. Aqui podemos exibir a variável `x` duas vezes e ver como seu valor é atualizado.
```kotlin
var x = 5
println(x) // prints 5
x = 10
println(x) // prints 10
```

---

Em Kotlin, variáveis do tipo string podem ser declaradas apenas usando aspas duplas:
```kotlin
val x = "May"
```

---

Se quisermos um nome de variável com várias palavras, usamos **camelCase**.
É a prática de escrever frases de modo que cada palavra no meio da frase comece com uma letra maiúscula
