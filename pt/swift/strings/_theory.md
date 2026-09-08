Uma **string** é um trecho de texto. Em Swift você escreve um literal de string entre aspas duplas, e seu tipo é `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Como com qualquer outro valor, `let` cria uma constante que não pode ser alterada e `var` cria uma variável que pode.
O Swift infere o tipo `String` a partir do literal, então a anotação de tipo é opcional.

---

A **interpolação de strings** insere o valor de uma expressão dentro de um literal de string. Envolva a expressão em `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Qualquer tipo pode ser interpolado: números, booleanos e outras strings são todos convertidos em texto automaticamente.

---

Duas strings podem ser unidas com o operador `+`, que produz uma nova string:
```swift
let full = "Hello" + " " + "world" // Hello world
```
Para adicionar texto ao final de uma variável de string existente, use `+=`. A variável deve ser declarada com `var`, porque seu valor muda:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

A propriedade `count` retorna o número de caracteres em uma string, e `isEmpty` é `true` quando a string não tem nenhum caractere:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Todo caractere é contado, incluindo espaços e pontuação.

---

Uma `String` é uma coleção de valores `Character`. Um `Character` é uma única letra, dígito, símbolo ou espaço, e é escrito com as mesmas aspas duplas de uma string, então você precisa de uma anotação de tipo para obter um:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Verificar `isEmpty` é preferível a comparar `count` com `0`: fica mais claro e não precisa contar todos os caracteres.

---

Um **literal de string multilinha** começa e termina com três aspas duplas `"""`, cada uma em sua própria linha. Toda linha entre elas se torna parte da string, e as quebras de linha são preservadas:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
Isso imprime as duas linhas exatamente como foram escritas. O `"""` de fechamento também define o recuo: qualquer espaço em branco antes dele é removido do início de cada linha.

---

Como uma string é uma coleção de caracteres, você pode iterar sobre ela com um laço `for`-`in`. Cada iteração fornece um `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
Um `Character` pode ser comparado com `==` a um literal de caractere, então contar quantas vezes um caractere aparece é apenas um laço e um contador.

---

Diferente dos arrays, strings não podem ser indexadas com um inteiro como `text[2]`: alguns caracteres ocupam mais memória que outros, então o Swift usa um tipo dedicado `String.Index` para apontar para uma posição.
`startIndex` é a posição do primeiro caractere e `endIndex` é a posição *depois* do último. Para se mover a partir de um índice, use `index(_:offsetBy:)`, depois indexe a string com o resultado:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Mover-se além do final da string causa uma falha em tempo de execução, então o deslocamento deve permanecer dentro de `count`.

---

Trabalhar com índices é verboso, então o Swift oferece atalhos para os casos mais comuns:
- `first` e `last` retornam o primeiro e o último caractere como um `Character?` opcional (`nil` para uma string vazia)
- `prefix(n)` retorna os primeiros `n` caracteres e `suffix(n)` os últimos `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` e `suffix` retornam uma `Substring`, uma visão sobre o texto original. Para armazená-la como uma `String` de verdade, envolva-a em `String(...)`. Se `n` for maior que `count`, você simplesmente obtém a string inteira.

---

Três métodos respondem às perguntas mais comuns sobre o conteúdo de uma string, e cada um retorna um `Bool`:
- `contains(_:)` é `true` quando a string inclui o texto (ou caractere) informado em qualquer lugar
- `hasPrefix(_:)` é `true` quando a string começa com o texto informado
- `hasSuffix(_:)` é `true` quando a string termina com o texto informado
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Os três diferenciam maiúsculas de minúsculas: `"Swift".hasPrefix("s")` é `false`.

---

Como `contains`, `hasPrefix` e `hasSuffix` retornam booleanos, eles se combinam naturalmente com `||` e `&&` para construir verificações mais complexas.

---

`uppercased()` e `lowercased()` retornam uma **nova** string com cada letra convertida para maiúscula ou minúscula. A string original não é modificada:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Ambos são métodos, então não se esqueça dos parênteses.

---

Converter para minúsculas é a maneira usual de comparar texto ignorando maiúsculas e minúsculas: duas strings que diferem apenas na capitalização se tornam iguais assim que ambas são convertidas para minúsculas.

---

`split(separator:)` divide uma string em um array de pedaços onde quer que o caractere separador apareça. `joined(separator:)` faz o oposto: cola os elementos de um array em uma única string, colocando o separador entre eles:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Assim como `prefix`, `split` retorna valores `Substring`; envolva um em `String(...)` se precisar armazená-lo como uma `String`.

---

Dividir por um espaço é a maneira mais simples de quebrar uma frase em palavras, e unir é como você reconstrói o texto a partir de um array.

---

O framework Foundation adiciona muitos métodos extras para strings. Um dos mais úteis é `replacingOccurrences(of:with:)`, que retorna uma nova string onde toda ocorrência do primeiro texto é substituída pelo segundo:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Lembre-se de fazer `import Foundation` no topo do arquivo, caso contrário o método não estará disponível. Chamadas de método podem ser encadeadas, então `text.lowercased().replacingOccurrences(of: " ", with: "_")` é válido.

---

Strings podem ser comparadas com os mesmos operadores usados em números. `==` verifica se duas strings têm exatamente os mesmos caracteres, enquanto `<` e `>` as comparam em ordem alfabética, caractere por caractere:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
A comparação diferencia maiúsculas de minúsculas, e toda letra maiúscula vem **antes** de toda letra minúscula, então `"B" < "a"` é `true`.

---

Um `Character` não é uma `String`, então não pode ser unido a uma string com `+` diretamente. Converta-o primeiro com `String(...)`:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Combinar isso com um laço `for`-`in` permite reconstruir uma string um caractere de cada vez, por exemplo colocando cada novo caractere na frente dos já coletados até então.
