> Computadores são ideais para tarefas repetitivas.

A forma mais básica de repetição usa a palavra-chave `while`.
Isso repete um bloco enquanto a _expressão booleana_ de controle for true:

```kotlin
while (Boolean-expression) {
  // Código a ser repetido
}
```
A expressão booleana é avaliada uma vez no início do loop e
novamente antes de cada iteração seguinte pelo bloco.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Aqui criamos uma variável `x`, atribuindo a ela o valor inicial de __3__.

Depois usamos a instrução `while` que executará o bloco de código até que a condição `x > 0` seja `true`.

Dentro do bloco de código, **NÃO** devemos esquecer de adicionar a linha `x--`.
Ela decrementa o valor de `x`, caso contrário, nosso loop será infinito.

---

Vamos analisar este trecho de código.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Inicializamos a variável `counter` com __0__.
- __[2]__: A expressão condicional do _while_ diz: "repita as instruções no corpo enquanto counter for menor que _100_".
- __[3]__: O operador `+=` adiciona _10_ ao `counter` e atribui o resultado ao `counter` em uma única operação.

A saída do código acima é _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Existe uma segunda maneira de usar o _while_, em conjunto com a palavra-chave `do`.
```kotlin
do {
  // Código a ser repetido
} while (Boolean-expression)
```
Como você pode ver, o `do-while` é bastante semelhante ao loop `while`, exceto por uma diferença importante:
> o corpo do loop é executado uma vez antes que a condição seja avaliada.

Em outras palavras, o corpo do `do-while` sempre executa pelo menos uma vez, mesmo que a expressão condicional inicialmente produza `false`.

Em contraste, o corpo de um loop `while` nunca será executado se a condição produzir `false` na primeira vez.

---

O loop _while_ suporta três expressões de salto estrutural:
- `break` encerra o loop mais próximo.
- `continue` avança para o próximo passo do loop mais próximo.
- `return` por padrão retorna da função ou função anônima mais próxima (_veremos isso mais tarde quando falarmos sobre funções_).

Aqui está um exemplo do uso de `continue` dentro de um loop _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// imprime 1, 3
```

Como você pode ver em __[1]__ quando `i` é igual a _2_, pulamos e _continuamos_ para o próximo passo. Na verdade, o número 2 nunca é impresso.

---

Aqui está um exemplo do uso de `break` dentro de um loop _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// imprime 1
```

Como você pode ver em __[1]__ quando `i` é igual a _2_, _interrompemos_ o loop. Na verdade, os números 2 e 3 nunca são impressos.
