Uma **expressão regular** (regex) é um pequeno padrão que descreve uma forma de texto: "uma sequência de dígitos", "uma palavra seguida por um sinal de igual", "três letras maiúsculas". Em vez de escrever loops sobre caracteres, você descreve a forma uma vez e deixa o Swift encontrá-la.

O Swift escreve uma regex entre `#/` e `/#`:
```swift
let digits = #/\d+/#
```
Dentro do padrão, `\d` significa "qualquer dígito" e `+` significa "um ou mais do elemento anterior", então `\d+` significa "uma sequência de um ou mais dígitos".

A pergunta mais simples que você pode fazer é se um texto contém uma correspondência. `contains(_:)` recebe uma regex e retorna um `Bool`:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Sempre use a forma `#/ ... /#` mostrada aqui: a grafia mais curta `/ ... /` confunde o compilador quando o padrão é escrito diretamente dentro de uma chamada de método.

---

Alguns atalhos cobrem a maioria dos padrões. Cada um corresponde a exatamente **um** caractere:
- `\d` é um dígito
- `\w` é uma letra, um dígito ou um underscore
- `\s` é um espaço, uma tabulação ou uma quebra de linha
- `.` é qualquer caractere único

Para corresponder a mais de um caractere, adicione um **quantificador** logo após o padrão:
- `+` significa um ou mais
- `*` significa zero ou mais
- `?` significa zero ou um

Então `\w+` é uma palavra, `\s*` é um espaçamento opcional, e `\d?` é um dígito opcional:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Um caractere sem significado especial simplesmente corresponde a si mesmo, então `#/cat/#` corresponde às três letras `cat`.

---

Por padrão, um padrão pode corresponder em qualquer lugar dentro do texto. **Âncoras** o vinculam a uma posição em vez disso:
- `^` significa "o início do texto"
- `$` significa "o fim do texto"

```swift
print("swift".contains(#/^sw/#))  // true, the text starts with sw
print("myswift".contains(#/^sw/#)) // false, sw is not at the start
print("swift".contains(#/ft$/#))  // true, the text ends with ft
```
Âncoras correspondem a uma posição, não a um caractere, então elas não acrescentam nada ao conteúdo da correspondência.

---

Quando nenhum dos atalhos serve, liste entre colchetes os caracteres que você aceita. `[abc]` corresponde a um `a`, a um `b` ou a um `c`, e um traço escreve um intervalo:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Um número entre chaves diz exatamente quantas vezes o padrão anterior se repete: `{3}` significa três vezes, `{2,4}` significa entre duas e quatro vezes:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Envolver um padrão em `^` e `$` com uma contagem é a maneira usual de verificar que um texto inteiro tem uma determinada forma.

---

`contains(_:)` apenas diz sim ou não. Para obter o texto correspondido, use `firstMatch(of:)`. Ele retorna uma **correspondência opcional**: `nil` quando nada correspondeu, então ele combina naturalmente com `if let`.

O texto correspondido é armazenado na propriedade `0` da correspondência, escrita `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` para na primeira correspondência, mesmo quando o texto contém mais.

---

`m.0` não é uma `String`, mas uma `Substring`: uma visão sobre o texto original, não uma cópia. Ela é exibida exatamente como uma string, mas onde uma `String` é exigida você precisa convertê-la:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Os inicializadores de números aceitam uma `Substring` diretamente, então `Int(m.0)` funciona sem o desvio.

---

`matches(of:)` retorna **todas** as correspondências em vez da primeira, como um array. O array nunca é `nil`: quando nada corresponde ele é simplesmente vazio, então ele pode ser percorrido ou transformado imediatamente:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Cada elemento é uma correspondência, então `$0.0` dentro de um `map` é o texto correspondido:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Como `Int(_:)` aceita uma `Substring`, transformar o texto encontrado em números é um único passo. `compactMap` é útil aqui: ele descarta os valores que retornam `nil`:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Use `map` quando todos os elementos convertem, `compactMap` quando alguns podem falhar.

---

Parênteses em volta de uma parte do padrão criam um **grupo de captura**: a correspondência inteira continua sendo `m.0`, e a parte dentro dos parênteses se torna `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
É assim que você mantém a parte interessante e descarta o texto em volta. Sem parênteses não existe `m.1` algum, e o código não compila.

---

Um padrão pode conter vários grupos. Eles são numerados da esquerda para a direita pelo parêntese de abertura, então o segundo é `m.2`, o terceiro `m.3`, e assim por diante:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` continua sendo sempre a correspondência inteira, não importa o número de grupos.

---

Contar parênteses fica frágil assim que um padrão cresce. Em vez disso, dê ao grupo um **nome**, escrevendo `?<name>` logo após o parêntese de abertura, e leia-o como uma propriedade da correspondência:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Grupos nomeados continuam numerados, então `m.1` segue funcionando, mas `m.key` diz o que ele contém e sobrevive a uma mudança no padrão.

---

`replacing(_:with:)` troca cada correspondência por um texto fixo e retorna uma nova `String`, deixando o original intacto:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Observe que `\d+` substitui uma sequência inteira de dígitos por um único `#`, enquanto `\d` substituiria um dígito por vez. O padrão decide quanto desaparece.

---

`split(separator:)` também aceita uma regex, o que permite que uma única chamada trate separadores que nem sempre são escritos da mesma maneira:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[;,]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
O padrão `[;,]\s*` significa "uma vírgula ou um ponto e vírgula, seguidos por qualquer quantidade de espaçamento", então cada separador é consumido por inteiro e nenhum campo vazio é produzido. O resultado é um array de `Substring`.

---

Validar um texto inteiro com `^` e `$` funciona, mas `wholeMatch(of:)` diz isso diretamente: ele retorna uma correspondência somente quando o padrão cobre o texto do primeiro ao último caractere, e `nil` caso contrário:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Use `firstMatch(of:)` para encontrar algo dentro de um texto, e `wholeMatch(of:)` para verificar que um texto tem uma forma exata.

---

Um literal `#/ ... /#` é fixo quando você compila. Quando o padrão só se torna conhecido em tempo de execução, por exemplo porque um usuário o digitou, construa-o com `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Esse inicializador **lança um erro**: um padrão inválido como `"["` só é descoberto enquanto o programa roda, então a chamada precisa de `try`, e o erro deve ser tratado com `do`/`catch` (ou `try?`) ou propagado marcando a função envolvente como `throws`, como este exercício faz. Uma regex construída dessa forma não tem propriedades numeradas conhecidas em tempo de compilação, mas `contains`, `matches(of:)` e `replacing` funcionam exatamente como antes.
