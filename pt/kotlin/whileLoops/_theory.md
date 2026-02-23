> Computadores so ideais para tarefas repetitivas.

A forma mais bsica de repetio usa a palavra-chave `while`.
Isso repete um bloco enquanto a _expresso booleana_ de controle for verdadeira:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
A expresso booleana  avaliada uma vez no incio do loop e
novamente antes de cada iterao adicional atravs do bloco.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Aqui criamos uma varivel `x`, atribuindo a ela o valor inicial de __3__.

Ento usamos a declarao `while` que executar o bloco de cdigo at que a condio `x > 0` seja `true`.

Dentro do bloco de cdigo, no devemos esquecer de adicionar a linha `x--`.
Isso decrementa o valor de `x`, caso contrrio, nosso loop ser infinito.

---

Let's analyze this snippet of code.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: We initialize the `counter` variable to __0__.
- __[2]__: The conditional expression for the _while_ says: "repeat the statements in the body as long as counter is less than _100_".
- __[3]__: The `+=` operator adds _10_ to `counter` and assigns the result to `counter` in a single operation.

The output of the code above is _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

There's a second way to use _while_, in conjuction with the `do` keyword.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
As you can see the `do-while` is pretty similar to the `while` loop, except for one important difference:
> the body of the loop is executed once before the condition is evaluated.

In other words, the body of the `do-while` always executes at least once, even if the condition expression initially produces `false`.

In constrast, the body of a `while` loop will never run if the condition produces `false` the first time.

---

The _while_ loop supports the three structural jump expression:
- `break` terminates the nearest enclosing loop.
- `continue` proceeds to the next step of the nearest enclosing loop.
- `return` by default returns from the nearest enclosing function or anonymous function (_we will see it later when we talk about functions_).

Here is an example of the use of `continue` within a _while_ loop:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

As you can see at __[1]__ when `i`  igual a _2_, we skip and _continue_ to the next step. In fact the number 2 is never printed.

---

Here is an example of the use of `break` within a _while_ loop:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

As you can see at __[1]__ when `i`  igual a _2_, we _break_ the loop. In fact the numbers 2 and 3 are never printed.
