Variáveis são recipientes para armazenar valores de dados.
Cada variável em Swift é um objeto.
Para criar uma variável, precisamos dar a ela um **nome** lembrando que ele não deve conter espaços.
Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.
Em Swift você declara constantes com a palavra-chave `let` e variáveis com a palavra-chave `var`.
O valor de uma constante não pode ser alterado depois de definido, enquanto uma variável pode receber um valor diferente no futuro.
Um exemplo de criação de uma variável chamada `x` é:
```swift
var x = 1
```
Dessa forma, atribuímos o valor `1` à variável chamada `x`.
Se imprimirmos a variável `x`, obtemos o número `1`:
```swift
print(x) // prints 1
```

---

Variáveis são chamadas assim porque o valor que armazenam pode mudar.
Podemos atualizar `x` usando `=` e atribuindo um novo valor.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

Também podemos atribuir a variáveis os valores de outras variáveis. Aqui, podemos atribuir à variável `y` o valor de `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

Quando atualizamos uma variável, ela esquece seu valor anterior. Aqui podemos exibir a variável `x` duas vezes e ver como seu valor é atualizado.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

Em Swift, variáveis do tipo string podem ser declaradas apenas usando aspas duplas:
```swift
let x = "May"
```

---

Se quisermos um nome de variável com múltiplas palavras, usamos **camelCase**.
É a prática de escrever frases de modo que cada palavra no meio da frase comece com uma letra maiúscula
