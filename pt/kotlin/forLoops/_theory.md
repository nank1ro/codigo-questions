> A palavra-chave `for` executa um bloco de codigo para cada valor em uma sequencia.

O loop `for` itera por qualquer coisa que forneça um iterador.

A sintaxe do `for` é a seguinte:
```kotlin
for (item in collection) print(item)
```

O corpo do `for` também pode ser um bloco
```kotlin
for (item in collection) {
    print(item)
}
```

A cada passagem pelo loop, `item` recebe o próximo elemento dos valores.

Aqui está um loop `for` repetindo uma ação um número fixo de vezes:

```kotlin
for (i in 1..3) {
    println(i)
}
// imprime 1, 2, 3
```

A saída mostra o índice `i` recebendo cada valor no intervalo de _1_ a _3_.

---

Um _intervalo_ é um conjunto de valores definido por um par de extremidades.
Existem duas formas básicas de definir intervalos:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ usando a sintaxe `..` inclui ambos os limites no intervalo resultante.
- __[2]__ `until` exclui o final. A saída mostra que _3_ não faz parte do intervalo.

---

Você pode iterar sobre um intervalo em ordem reversa.

Você provavelmente espera que `3..1` funcione, infelizmente, a equipe do Kotlin decidiu importar essa funcionalidade de uma forma diferente.

Na verdade, se você tentar executar este trecho de código:
```kotlin
for (i in 3..1) println(i)
```

Você verá que nada é impresso.
Para fazê-lo funcionar, precisamos usar a palavra-chave `downTo`:

```kotlin
for (i in 3 downTo 1) println(i)
// imprime 3, 2, 1
```

`downTo` produz um intervalo decrescente.

---

O _passo_ padrão de um intervalo é __1__, mas você pode definir explicitamente outro valor.

Você pode definir o __passo__ do seu loop `for` usando a palavra-chave `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// imprime 1, 3, 5, 7, 9
```

Como você pode ver, o bloco de código é executado com um passo de _2_ em vez de _1_, mudando completamente a nossa saída.

---

Você também pode produzir um intervalo de _caracteres_.
```kotlin
for (char in 'a'..'z') print(char)
// imprime abcdefghijklmnopqrstuvwxyz
```

---

Você pode iterar sobre uma __String__.
```kotlin
for (char in 'abc') print(char + 1)
// imprime bdc
```

No exemplo acima, imprimimos cada caractere + 1, então `'a'` se torna `'b'`, `'b'` se torna `'c'` e assim por diante.

Isso é possível porque os caracteres são armazenados como números correspondentes aos seus [Códigos ASCII](https://en.wikipedia.org/wiki/ASCII).

Portanto, adicionar um inteiro a um caractere produz um novo caractere correspondente ao novo valor do código.

---

Caso você simplesmente precise repetir um bloco de código `n` vezes, pode usar a função `repeat(times: Int)`.

```kotlin
repeat(3) {
    println("repeat")
}
// imprime repeat 3 vezes
```

Você pode até acessar o índice com
```kotlin
repeat(3) { index ->
    println(index)
}
// imprime 0, 1, 2
```

---

Em Kotlin podemos usar o `for-in` também para coleções iteráveis, chamando o closure fornecido em cada elemento:
```kotlin
// isso é uma lista, veremos sobre isso em breve
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// imprime (2, 4, 6, 8, 10)
```

---

Em Kotlin também temos o loop `forEach`.
Ele chama o closure fornecido em cada elemento da sequência na mesma ordem que um loop `for-in`:

```kotlin
// isso é uma lista, veremos sobre isso em breve
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

Usar o método `forEach` é diferente de um loop `for-in` de duas maneiras importantes:
1. As instruções `break` ou `continue` não podem ser usadas para sair da chamada atual do closure ou para pular chamadas subsequentes. (_Na verdade, é possível com anotações, mas é um tópico um pouco mais complexo que não veremos agora._)
2. Usar a instrução `return` no closure do corpo apenas sairá do closure e não do escopo externo, e não pulará chamadas subsequentes.
