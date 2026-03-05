Você já deve ter considerado a situação em que gostaria de reutilizar um trecho de código, apenas com alguns valores diferentes.
Em vez de reescrever todo o código, é muito mais limpo definir uma função, que pode ser usada repetidamente.
Em Swift, usamos a palavra-chave `func` seguida pelo nome da função:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Os parênteses na __definição da função__ não precisam estar vazios se quisermos especificar parâmetros

---

Às vezes queremos que uma função __retorne__ um valor.
Bem, existe a palavra-chave `return`.

---

Funções podem ter múltiplos parâmetros de entrada, que são escritos dentro dos parênteses da função, separados por vírgulas.
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

Você pode usar um tipo tupla como tipo de retorno de uma função para retornar múltiplos valores como parte de um único valor de retorno composto.

---

Se você não quiser um rótulo de argumento para um parâmetro, escreva um sublinhado `_` em vez de um rótulo de argumento explícito para esse parâmetro

---

Você pode definir um valor _padrão_ para qualquer parâmetro em uma função atribuindo um valor ao parâmetro após o tipo desse parâmetro.
Se um valor padrão for definido, você pode omitir esse parâmetro ao chamar a função
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

Um _parâmetro variádico_ aceita zero ou mais valores de um tipo especificado.
Você usa um parâmetro variádico para especificar que o parâmetro pode receber um número variável de valores de entrada quando a função é chamada.
Escreva parâmetros variádicos inserindo três caracteres de ponto `...` após o nome do tipo do parâmetro.
Os valores passados para um parâmetro variádico são disponibilizados dentro do corpo da função como um array do tipo apropriado.
Por exemplo, um parâmetro variádico com o nome `numbers` e o tipo `Double...` é disponibilizado dentro do corpo da função como um array constante chamado numbers do tipo `[Double]`

---

Em funções, podemos adicionar um _comentário opcional_ que explica o que a função faz:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
Podemos usar `///` para um comentário de linha única e `/** */` para um comentário de múltiplas linhas
