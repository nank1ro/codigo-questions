Um **comentário** é uma nota escrita dentro do código-fonte para as pessoas que o leem. O compilador ignora completamente os comentários, então eles nunca mudam o que o programa faz.

O comentário mais simples é o **comentário de linha única**: ele começa com `//` e vai até o fim da linha.
```swift
// Greets the user
print("Hello")
```
Use comentários para explicar para que serve um trecho de código, ou por que ele foi escrito daquela forma.

---

Um comentário não precisa de uma linha própria: ele pode vir depois do código na mesma linha. Esse é um **comentário de fim de linha**, e é um bom lugar para uma nota curta sobre aquela instrução específica:
```swift
let retries = 3 // give up after three attempts
```
Tudo, do `//` até o fim da linha, é ignorado, enquanto o código antes dele é executado normalmente.

---

Como o compilador remove os comentários completamente, adicionar ou excluir um comentário nunca muda o que um programa faz. Apenas o código que **não** está comentado é executado.

Isso faz do `//` uma forma rápida de desligar uma linha de código sem excluí-la. Isso é chamado de **comentar o código**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
A segunda linha agora é um comentário, então `total` permanece `10`. Remover o `//` traz a linha de volta à vida.

Comentar o código é útil enquanto você experimenta, mas lembre-se de limpar depois: código que fica comentado por muito tempo apenas confunde quem o ler em seguida.

---

Quando um comentário precisa de mais de uma linha, o Swift oferece o **comentário de várias linhas** (também chamado de comentário em bloco): ele começa com `/*` e termina com `*/`, e tudo entre eles é ignorado, incluindo quebras de linha.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Um comentário em bloco também pode ser curto e ficar em uma única linha: `/* like this */`.

---

Diferente do `//`, que para no fim da linha, um comentário `/*` só para no `*/`. Se você esquecer de fechá-lo, o compilador trata todo o código seguinte como parte do comentário e reporta um erro:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Tanto `//` quanto `/* */` funcionam como comentários de fim de linha, mas com `/*` sempre certifique-se de que o `*/` está lá.

---

Em muitas linguagens, comentários em bloco não podem conter outros comentários em bloco, mas no Swift eles **podem ser aninhados**: cada `/*` deve ter o seu próprio `*/`, e o comentário só termina quando o mais externo é fechado.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Aqui `still a comment */` faz parte do comentário externo, então apenas `done` é exibido. É isso que permite comentar um bloco inteiro de código mesmo quando esse bloco já contém um comentário `/* */`.

---

Para comentar várias linhas de uma vez, envolva-as em um único comentário em bloco em vez de adicionar `//` a cada linha:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Graças ao aninhamento, isso funciona mesmo quando uma dessas linhas já contém um comentário `/* */`.

---

Um uso comum dos comentários em bloco é o **comentário de cabeçalho**: um pequeno bloco colocado diretamente acima de uma função que diz o que ela faz e o que seus parâmetros significam.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Quem chama `toSeconds` agora pode ler o cabeçalho em vez do corpo. Mantenha o cabeçalho junto à função para que sejam atualizados juntos.

---

O Swift tem um terceiro tipo de comentário, o **comentário de documentação**: um comentário de linha única que começa com `///` (três barras) colocado diretamente acima de uma função, um tipo ou uma propriedade.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Para o compilador é apenas um comentário, mas ferramentas como o Xcode o leem e o exibem como texto de ajuda para `greet`. Comentários de documentação suportam **Markdown**, então você pode usar crases para código, `**negrito**` e listas.

---

A primeira linha de um comentário de documentação é o **resumo**: uma frase curta que diz o que a função faz. Escreva-a na terceira pessoa, como se estivesse descrevendo a função: "Retorna...", "Soma...", "Verifica...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
O comentário deve ficar logo acima da declaração, sem linha em branco entre eles, caso contrário o Xcode não o vincula à função.

---

Comentários de documentação também existem em forma de bloco: `/**` o abre e `*/` o fecha, exatamente como um comentário de várias linhas, mas com um segundo asterisco no início.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` e `/** text */` significam a mesma coisa para as ferramentas; `///` é a escolha mais comum no código Swift, enquanto `/** */` é útil para descrições longas. Um comentário comum `/* */` ou `//` **não** é documentação, mesmo quando colocado acima de uma função.

---

Depois do resumo, um comentário de documentação pode descrever os parâmetros e o valor de retorno com itens de lista Markdown especiais que o Xcode reconhece:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
A ordem é sempre a mesma: primeiro o resumo, depois `- Parameter name:` para cada parâmetro e, por fim, `- Returns:`.

---

Alguns comentários seguem uma convenção que os editores entendem. No Swift, os **marcadores** mais comuns são:
- `// MARK: - Title` rotula uma seção do arquivo, para que ela apareça no menu de navegação do Xcode
- `// TODO: ...` sinaliza algo que ainda precisa ser escrito
- `// FIXME: ...` sinaliza código que se sabe estar errado e deve ser corrigido

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Para o compilador, eles são comentários comuns; o Xcode os lista para que o trabalho pendente seja fácil de encontrar. Quando o trabalho estiver concluído, exclua o marcador: um `TODO` desatualizado é enganoso.

---

Um `TODO` geralmente fica ao lado de um marcador de posição que mantém o código compilando até que a implementação real seja escrita. Quando você conclui o trabalho, substitua o marcador de posição e remova o marcador na mesma alteração, para que o comentário nunca minta sobre o estado do código.

---

Um `FIXME` é diferente de um `TODO`: o código já existe, mas se sabe que está errado. Um bom `FIXME` diz qual é o bug e, quando possível, dá um exemplo que o demonstra, para que a próxima pessoa possa corrigi-lo rapidamente. Assim como no `TODO`, exclua o marcador assim que o bug for corrigido, mas mantenha o comentário de documentação, que continua verdadeiro.

---

Um bom comentário explica **por que** o código faz algo, não **o que** ele faz. O código já mostra o que acontece; repeti-lo em palavras apenas adiciona ruído e fica desatualizado assim que o código muda:
```swift
// set timeout to 30
let timeout = 30
```
O motivo por trás do número é o que o leitor não consegue adivinhar:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Se um comentário apenas repete a linha abaixo dele, exclua-o ou substitua-o pelo motivo.
