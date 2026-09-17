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

---

Uma struct é um **value type**: atribuí-la a outra variável, ou passá-la a uma função, entrega uma *cópia*. Alterar a cópia deixa o original intacto.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Uma classe é um **reference type**: `b = a` faria ambos os nomes apontarem para a mesma instância, então `b.x = 99` também mudaria `a.x` para `99`.

Essa é a verdadeira diferença entre os dois, e a razão pela qual o Swift modela a maioria dos dados como structs: um valor que você possui não pode ser modificado pelas suas costas pelo código que o recebeu.

---

Como uma struct é um valor, um método não tem permissão para alterar suas propriedades, a menos que você indique isso com a palavra-chave `mutating`:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
Um método `mutating` só pode ser chamado em uma instância armazenada em um `var`. Em uma instância `let` o valor está congelado, então `c.increase(by: 5)` não compilaria.

---

Quando o inicializador membro a membro não é a forma como você quer que seu tipo seja construído, escreva seu próprio **inicializador**. Ele é declarado com `init`, recebe os parâmetros que você escolher e deve dar a cada propriedade armazenada um valor antes de terminar. Dentro dele, `self` é a instância que está sendo criada:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Escrever um `init` dentro das chaves da struct substitui o membro a membro, então de agora em diante `Square(side: 5)` não existe mais.

---

Alguns valores pertencem ao próprio tipo, e não a uma única instância: um código de moeda, um padrão compartilhado, uma fábrica que constrói um caso comum. Marque-os como `static` e leia-os através do nome do tipo:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Aqui `currency` é declarado com `let` porque nunca muda, então é uma constante compartilhada pelo programa inteiro. `Money.currency` funciona sem criar um único `Money`, enquanto `amount` precisa de uma instância.

---

Duas structs não podem ser comparadas com `==` até que o tipo diga que oferece esse suporte. Você faz isso conformando-se ao **protocolo** `Equatable`, escrito depois de dois-pontos na declaração:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
Você não precisa escrever `==` você mesmo: quando toda propriedade armazenada já é `Equatable`, o Swift o sintetiza para você, comparando as propriedades uma a uma. Duas instâncias são iguais quando todas as suas propriedades são iguais, que é exatamente o que se espera de um valor.

---

Uma struct é um tipo como qualquer outro, então pode ser armazenada em um array, um dicionário ou um conjunto, e toda ferramenta que você já conhece continua funcionando sobre ela:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Lembre-se de que o array contém *cópias*: ler `items[0]` em uma variável e alterá-la não afeta o array.
