Voce pode ter considerado a situacao em que gostaria de reutilizar um pedaco de codigo, apenas com alguns valores diferentes.
Em vez de reescrever todo o codigo, e muito mais limpo definir uma funcao, que pode ser usada repetidamente.
Em Swift usamos a palavra-chave `func` seguida pelo nome da funcao:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Os parenteses na __definicao da funcao__ nao precisam estar vazios se quisermos especificar parametros

---

As vezes queremos que uma funcao __retorne__ um valor.
Bem, existe a palavra-chave `return`.

---

As funcoes podem ter varios parametros de entrada, que sao escritos dentro dos parenteses da funcao, separados por virgulas.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

Voce pode usar um tipo de tupla como o tipo de retorno de uma funcao para retornar varios valores como parte de um valor de retorno composto.

---

Se voce nao quiser um rotulo de argumento para um parametro, escreva um sublinhado `_` em vez de um rotulo de argumento explicito para esse parametro

---

Voce pode definir um valor _padrao_ para qualquer parametro em uma funcao atribuindo um valor ao parametro depois do tipo desse parametro.
Se um valor padrao for definido, voce pode omitir esse parametro ao chamar a funcao
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

Um _parametro variadico_ aceita zero ou mais valores de um tipo especificado.
Voce usa um parametro variadico para especificar que o parametro pode receber um numero variado de valores de entrada quando a funcao e chamada.
Escreva parametros variadicos inserindo tres caracteres de ponto `...` depois do nome do tipo do parametro.
Os valores passados para um parametro variadico sao disponibilizados dentro do corpo da funcao como um array do tipo apropriado.
Por exemplo, um parametro variadico com o nome de `numbers` e um tipo de `Double...` e disponibilizado dentro do corpo da funcao como um array constante chamado numbers do tipo `[Double]`

---

Em funcoes podemos adicionar um _comentario opcional_ que explica o que a funcao faz:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
Podemos usar `///` para um comentario de uma linha e `/** */` para um comentario de multiplas linhas
