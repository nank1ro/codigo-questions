> A palavra-chave `for` executa um bloco de código para cada valor em uma sequência.

O loop `for` itera através de qualquer coisa que forneça um iterador.

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

Cada vez através do loop, `item` recebe o próximo elemento em valores.

Aqui está um loop `for` repetindo uma ação um número fixo de vezes:

```kotlin
for (i in 1..3) {
    println(i)
}
// imprime 1, 2, 3
```

A saída mostra o índice `i` recebendo cada valor no intervalo de _1_ a _3_.

---

Um _intervalo_ (range) é um intervalo de valores definido por um par de extremidades.
Existem duas formas básicas de definir intervalos:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* imprime
1..3
1..2
*/
```

- __[1]__ usando a sintaxe `..` inclui ambos os limites no intervalo resultante.
- __[2]__ `until` exclui o final. A saída mostra que _3_ não faz parte do intervalo.

---

Você pode iterar sobre um intervalo em ordem inversa.

Você provavelmente espera que `3..1` funcione, infelizmente, a equipe Kotlin decidiu importar esta funcionalidade de uma forma diferente.

De fato, se você tentar executar este trecho de código:
```kotlin
for (i in 3..1) println(i)
```

Você verá que nada é impresso.
Para fazer funcionar, temos que usar a palavra-chave `downTo`:

```kotlin
for (i in 3 downTo 1) println(i)
// imprime 3, 2, 1
```

`downTo` produz um intervalo decrescente.

---

O _passo_ (step) padrão de um intervalo é __1__, mas você pode definir explicitamente outro valor.

Você pode definir o __passo__ do seu loop `for` usando a palavra-chave `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// imprime 1, 3, 5, 7, 9
```

Como você pode ver, o bloco de código é executado com um passo de _2_ em vez de _1_, mudando completamente nossa saída.

---

Você também pode produzir um intervalo de _caracteres_.
```kotlin
for (char in 'a'..'z') print(char)
// imprime abcdefghijklmnopqrstuvwxyz
```

---

You can iterate over a __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

In the example above we've printed each character + 1, so `'a'` becomes `'b'`, `'b'` becomes `'c'` and so on.

This is possibile because characters are stored as numbers corresponding to their [ASCII Codes](https://en.wikipedia.org/wiki/ASCII).

So adding an integer to a character produces a new character corresponding to the new code value.

---

Caso você simplesmente precise repetir um bloco de código `n` vezes, você pode usar a função `repeat(times: Int)`.

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

In Kotlin we can use the `for-in` also for iterable collections calling the given closure on each element:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10) 
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```
