Uma **struct** (abreviação de *structure*) é um tipo que você mesmo projeta para manter valores relacionados juntos. Em vez de malabarizar com um `title` separado e um `pages` separado, você descreve um `Book` uma única vez e o usa em qualquer lugar.

Você declara uma com a palavra-chave `struct`, e as variáveis escritas dentro dela são suas **propriedades armazenadas**:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` agora é um tipo, exatamente como `Int` ou `String`. Você acessa uma propriedade de uma instância com um ponto:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Você nunca escreveu o código que constrói um `Book`, ainda assim `Book(title: "Swift", pages: 120)` funcionou. O Swift o escreve para você: toda struct recebe de graça um **inicializador membro a membro**, um inicializador cujos parâmetros são suas propriedades armazenadas, na ordem em que são declaradas, cada um usando o nome da propriedade como seu rótulo de argumento:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Classes não recebem isso de graça, o que é uma das razões pelas quais structs são a forma mais rápida de modelar um valor.

---

Uma propriedade armazenada pode receber um **valor padrão** bem onde ela é declarada. O Swift infere seu tipo a partir desse valor, então você pode omitir a anotação de tipo:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
O inicializador membro a membro transforma cada propriedade com valor padrão em um argumento opcional: passe-o para sobrescrever o padrão, omita-o para mantê-lo.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Uma struct também pode conter **métodos**: funções escritas dentro das chaves que trabalham sobre a instância na qual são chamadas. Dentro de um método você usa os nomes das propriedades diretamente, sem nenhum prefixo:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
Se um parâmetro do método sombrear o nome de uma propriedade, escreva `self.width` para se referir à propriedade da instância.

---

Uma **propriedade computada** parece uma propriedade, mas se comporta como um método: ela não armazena nada, calcula seu valor toda vez que você a lê. Você escreve o tipo e, em seguida, um bloco de código que retorna o valor:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, no parentheses
```
Propriedades computadas não fazem parte do inicializador membro a membro, já que não há nada a armazenar. Use uma quando o valor for derivado dos outros, e um método quando o trabalho precisar de parâmetros.
