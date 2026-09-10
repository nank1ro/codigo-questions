Uma **string formatada** é um trecho de texto em que algumas partes são preenchidas com valores em tempo de execução: um preço, um nome, uma pontuação. O Swift oferece duas ferramentas para isso.

A primeira é a **interpolação de string**, que você já conhece: tudo o que é escrito dentro de `\( )` é avaliado e inserido no texto. Não precisa ser uma variável, pode ser qualquer expressão:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
A interpolação é a maneira mais rápida de construir uma string, mas ela imprime os números exatamente como o Swift os armazena: `3.5` continua `3.5`, nunca `3.50`. Para controle total sobre dígitos, largura e preenchimento usaremos `String(format:)`, apresentado no próximo exercício.

---

A segunda ferramenta é a `String(format:)`, que vem do framework **Foundation**, então o arquivo deve começar com `import Foundation`.

Ela recebe uma **string de formato** seguida dos valores a inserir. Dentro da string de formato, um **especificador** que começa com `%` marca onde cada valor entra e como ele é escrito. O especificador para um inteiro é `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
A `String(format:)` retorna uma `String` normal, então você pode imprimi-la, armazená-la ou retorná-la de uma função.

---

Para números decimais (`Double`) o especificador é `%f`. Sozinho, ele sempre imprime seis dígitos depois do ponto:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Para escolher quantas casas decimais você quer, escreva um ponto e um número entre `%` e `f`. Isso é a **precisão**, e o valor é arredondado para se ajustar:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` é a escolha usual para preços, porque sempre mostra exatamente duas casas decimais.

---

Um número entre `%` e a letra define a **largura mínima** do campo. Se o valor for mais curto, espaços são adicionados à esquerda para que fique **alinhado à direita**; se for mais longo, nada é cortado:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Largura e precisão se combinam: `%8.2f` significa "pelo menos 8 caracteres de largura, com 2 casas decimais":
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Larguras fixas são o que alinham as colunas de uma tabela.

---

Por padrão, o preenchimento vai à esquerda. Um sinal de menos logo depois de `%` coloca o preenchimento à direita, de modo que o valor fica **alinhado à esquerda**:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
O sinal de menos é uma **flag**: ele muda como o campo é preenchido sem mudar a largura.

---

Outra flag é `0`: em vez de espaços, o campo é preenchido com zeros à esquerda. É assim que você obtém números como `007` ou `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Como com os espaços, um valor mais longo que a largura nunca é cortado.

---

Uma string de formato pode conter quantos especificadores você quiser. Os valores vêm na mesma ordem, separados por vírgulas, e cada um deve corresponder ao tipo do seu especificador: `%d` para um `Int`, `%f` para um `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Passar um `Double` para `%d` (ou um `Int` para `%f`) compila, mas imprime um número sem sentido, então sempre verifique se especificadores e valores correspondem.

---

Inteiros também podem ser escritos em outras bases. `%x` imprime o valor em **hexadecimal** com letras minúsculas, `%X` com letras maiúsculas, e `%o` em octal:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
A largura e a flag `0` funcionam aqui também: `%02x` é a maneira clássica de escrever um byte de uma cor, como em `#ff8000`.

---

Para inserir uma `String` em uma string de formato, use o especificador `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` aceita uma `String` do Swift diretamente. Não use `%s` com uma string do Swift: esse especificador espera uma string C e imprime lixo ou faz o programa travar.
