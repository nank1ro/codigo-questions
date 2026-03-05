Frequentemente em programacao, precisamos repetir um bloco de codigo, por exemplo:
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Isso produz a seguinte saida:
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instrucoes longas gastariamos muito tempo escrevendo o codigo, mas felizmente, podemos usar lacos de repeticao.
Vamos aprender o laco `while`, obtendo a mesma saida acima.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
Entao criamos uma variavel `count` atribuindo `2`, o valor inicial.
Depois usamos a instrucao `while` que executara o bloco de codigo ate que a condicao `count <= 5` seja `true`.
Dentro do bloco de codigo, **NAO** devemos esquecer de adicionar a linha `count += 1`.
Ela incrementa o valor de `count`, caso contrario, nosso laco sera infinito

---

Para controlar quantas vezes um laco `while` se repete, comecamos com uma variavel definida como um numero.
Chamamos essa variavel de variavel contadora

---

Em seguida, usamos uma comparacao na condicao para comparar a variavel `counter` com um numero.

---

Dentro do bloco de codigo, para parar o laco `while`, incrementamos a variavel `counter`.

---

A ordem em que voce escreve o codigo afeta a saida.

---

Em Swift tambem temos a variacao **repeat-while** do laco `while`.
Ela executa uma unica passagem pelo bloco do laco primeiro, _antes_ de considerar a condicao do laco.
Depois continua repetindo o laco ate que a condicao seja `false`.
O laco __repeat-while__ em Swift e analogo ao laco __do-while__ em outras linguagens
