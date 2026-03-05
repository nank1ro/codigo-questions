> Computadores sao ideais para tarefas repetitivas.

A forma mais basica de repeticao usa a palavra-chave `while`.
Isso repete um bloco enquanto a _expressao booleana_ de controle for true:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
A expressao booleana e avaliada uma vez no inicio do loop e
novamente antes de cada iteracao seguinte pelo bloco.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Aqui criamos uma variavel `x`, atribuindo a ela o valor inicial de __3__.

Depois usamos a instrucao `while` que executara o bloco de codigo ate que a condicao `x > 0` seja `true`.

Dentro do bloco de codigo, **NAO** devemos esquecer de adicionar a linha `x--`.
Ela decrementa o valor de `x`, caso contrario, nosso loop sera infinito.

---

Vamos analisar este trecho de codigo.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Inicializamos a variavel `counter` com __0__.
- __[2]__: A expressao condicional do _while_ diz: "repita as instrucoes no corpo enquanto counter for menor que _100_".
- __[3]__: O operador `+=` adiciona _10_ ao `counter` e atribui o resultado ao `counter` em uma unica operacao.

A saida do codigo acima e _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Existe uma segunda maneira de usar o _while_, em conjunto com a palavra-chave `do`.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
Como voce pode ver, o `do-while` e bastante semelhante ao loop `while`, exceto por uma diferenca importante:
> o corpo do loop e executado uma vez antes que a condicao seja avaliada.

Em outras palavras, o corpo do `do-while` sempre executa pelo menos uma vez, mesmo que a expressao condicional inicialmente produza `false`.

Em contraste, o corpo de um loop `while` nunca sera executado se a condicao produzir `false` na primeira vez.

---

O loop _while_ suporta tres expressoes de salto estrutural:
- `break` encerra o loop mais proximo.
- `continue` avanca para o proximo passo do loop mais proximo.
- `return` por padrao retorna da funcao ou funcao anonima mais proxima (_veremos isso mais tarde quando falarmos sobre funcoes_).

Aqui esta um exemplo do uso de `continue` dentro de um loop _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

Como voce pode ver em __[1]__ quando `i` e igual a _2_, pulamos e _continuamos_ para o proximo passo. Na verdade, o numero 2 nunca e impresso.

---

Aqui esta um exemplo do uso de `break` dentro de um loop _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

Como voce pode ver em __[1]__ quando `i` e igual a _2_, _interrompemos_ o loop. Na verdade, os numeros 2 e 3 nunca sao impressos.
