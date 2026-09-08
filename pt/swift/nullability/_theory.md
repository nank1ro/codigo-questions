Às vezes um valor está simplesmente ausente: um usuário sem segundo nome, uma busca que não encontra nada, um texto que não pode ser convertido em número.
O Swift representa um valor ausente com `nil`, mas uma variável comum nunca pode conter esse valor:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Para permitir um valor ausente, você declara um tipo **opcional** adicionando um ponto de interrogação `?` depois do tipo.
Um `Int?` contém um `Int` ou `nil`:
```swift
var age: Int? = 30
age = nil // permitido
```
Uma variável opcional declarada sem um valor começa como `nil`.

---

Você pode comparar um opcional com `nil` usando `==` e `!=`, e também pode compará-lo diretamente com um valor comum do tipo envolvido:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Lembre-se de que `Int?` e `Int` são dois tipos diferentes: um `Int?` pode estar vazio, um `Int` nunca está.

---

Um opcional é como uma caixa: antes de usar o valor de dentro, você precisa abri-la, o que o Swift chama de **desempacotamento**.
A forma mais rápida é o **desempacotamento forçado** com um ponto de exclamação `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
O `!` diz ao Swift "tenho certeza de que há um valor aqui". Se você estiver errado e o opcional for `nil`, o programa para imediatamente com uma falha em tempo de execução:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
É por isso que o desempacotamento forçado é considerado perigoso: use-o apenas quando tiver certeza de que o valor existe.

---

O desempacotamento forçado só é seguro quando você já verificou que o opcional não é `nil`:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Verificar se é `nil` e depois fazer o desempacotamento forçado é verboso. O Swift oferece a **vinculação opcional** com `if let`, que desempacota o opcional e armazena o valor em uma nova constante em uma única etapa:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value é um Int, não um Int?
} else {
    print("No score")
}
```
O corpo do `if` só executa quando o opcional contém um valor; dentro dele `value` é um `Int` comum e não precisa de `!`.

---

Quando um valor ausente significa "pare aqui", `guard let` é mais claro do que `if let`.
Ele desempacota o opcional e, se isso falhar, executa o bloco `else`, que deve sair do escopo atual (com `return`, `break`, `continue` ou `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // name é uma String a partir daqui
}
```
Ao contrário do `if let`, a constante desempacotada continua disponível pelo resto da função, então o caminho principal não fica aninhado dentro de um `if`.

---

Um uso típico do `guard let` é validar a entrada de uma função logo no início e retornar um valor padrão quando ela está ausente:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Muitas vezes tudo o que você quer de um opcional é o seu valor ou um padrão.
O **operador de coalescência nula** `??` faz exatamente isso: ele desempacota o opcional se houver um valor, caso contrário retorna o valor à sua direita:
```swift
let score: Int? = nil
let points = score ?? 0 // points é um Int igual a 0
```
O valor padrão deve ter o mesmo tipo do valor envolvido.
Você pode encadear vários `??`: o primeiro valor que não for `nil` vence.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` é a forma mais curta de transformar um opcional em um valor comum quando existe um padrão razoável:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Ao encadear `??`, o Swift avalia da esquerda para a direita e para no primeiro valor que não é `nil`; o último padrão só é usado quando todos os opcionais anteriores são `nil`.

---

Acessar uma propriedade ou chamar um método em um opcional exigiria desempacotá-lo primeiro.
O **encadeamento opcional** com `?.` faz isso por você: se o opcional for `nil`, a expressão inteira se torna `nil`, caso contrário o acesso é feito normalmente:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? contendo "SWIFT"
```
O resultado é sempre um opcional, mesmo quando a própria propriedade não é.
As cadeias podem ser tão longas quanto necessário, e combinam bem com `??`:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

O encadeamento opcional brilha quando os dados podem estar ausentes em vários níveis: um objeto pode ser `nil`, e uma de suas propriedades também pode ser `nil`.
Uma única cadeia `?.` trata os dois casos sem nenhum `if`.

---

Um único `if let` ou `guard let` pode desempacotar vários opcionais de uma vez: basta separar as vinculações com vírgulas.
O corpo só executa se todos os opcionais tiverem um valor:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
Você também pode acrescentar uma condição booleana após as vinculações, como `if let n = number, n > 0`.

---

Vincular vários opcionais em um único `if let` mantém o código plano: um único bloco `else` cobre todos os valores ausentes.

---

Muitas operações podem falhar, e o Swift reporta a falha retornando um opcional.
Converter texto em número é o exemplo clássico: `Int("42")` retorna um `Int?` contendo `42`, enquanto `Int("abc")` retorna `nil`.
`Int("3.5")` também é `nil`, porque o texto não é um número inteiro; use `Double("3.5")` para decimais.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Outros exemplos são `array.first` (`nil` para um array vazio) e `dictionary[key]` (`nil` quando a chave está ausente).

---

Como uma conversão pode falhar, seu resultado é sempre um opcional e deve ser desempacotado antes de ser usado, mesmo quando você tem certeza de que o texto é um número válido.

---

Conversões que podem falhar combinam naturalmente com `guard let`: converta, saia se o resultado for `nil`, e depois trabalhe com o valor comum.

---

Às vezes você quer transformar o valor dentro de um opcional e manter o resultado opcional, sem desempacotar e reempacotar manualmente.
Os opcionais têm um método `map`: ele aplica a closure ao valor, se houver um, e retorna `nil` caso contrário.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? contendo 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Combinado com uma conversão que pode falhar, ele forma um pipeline compacto: `Int(text).map { $0 + 1 }`.
