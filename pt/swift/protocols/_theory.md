Um **protocolo** descreve o que um tipo deve ter, sem dizer como. É uma lista de requisitos — propriedades e métodos — que qualquer tipo que o adota promete fornecer.

Você declara um com a palavra-chave `protocol`. Um requisito de propriedade é escrito com seu tipo seguido de um bloco que diz como ele pode ser acessado: `{ get }` significa que o tipo deve pelo menos permitir que você o leia.
```swift
protocol Named {
    var name: String { get }
}
```
Um tipo **conforma-se** ao protocolo escrevendo o nome do protocolo depois de dois-pontos e fornecendo tudo o que ele pede:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Um protocolo não guarda dados próprios: é um contrato. Todo tipo que o satisfaz pode ser tratado da mesma forma pelo restante do seu código.

---

Um protocolo também pode exigir **métodos**. Você escreve a assinatura — nome, parâmetros e tipo de retorno — e para por aí, sem corpo:
```swift
protocol Greeter {
    func greet() -> String
}
```
O tipo em conformidade deve declarar um método com exatamente essa assinatura, e ele fornece o corpo:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Se algo diferir — o nome, um tipo de parâmetro, o tipo de retorno — o tipo não está em conformidade, e o compilador lhe diz qual requisito está faltando.

---

Um requisito de propriedade sempre indica como a propriedade pode ser usada. `{ get }` pede apenas que o valor possa ser lido; `{ get set }` pede que ele possa ser lido **e** atribuído:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Um tipo em conformidade pode sempre dar mais do que o contrato pede: uma propriedade armazenada `var` satisfaz `{ get }` perfeitamente bem. Ele nunca pode dar menos — uma constante `let`, ou uma propriedade computada somente leitura, não pode satisfazer `{ get set }`.

---

Protocolos não se limitam a structs. Uma **classe** conforma-se exatamente da mesma forma, listando o protocolo depois de dois-pontos:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
Se a classe também herdar de outra classe, a superclasse vem primeiro na lista e os protocolos a seguem. Um tipo pode adotar vários protocolos de uma vez, separados por vírgulas.

---

Um **enum** também pode se conformar. Ele não tem propriedades armazenadas, então um requisito de propriedade geralmente é atendido com uma propriedade computada que faz switch sobre os casos:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Structs, classes e enums: todos os três adotam protocolos da mesma forma, e código escrito contra o protocolo funciona com todos eles.

---

Um protocolo geralmente reúne mais de um requisito, e um tipo em conformidade deve satisfazer todos eles:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
A ordem dos requisitos dentro das chaves não importa, nem a ordem em que o tipo em conformidade os fornece: o compilador só verifica que nada está faltando.

---

Uma struct é um tipo de valor, então um método que altera uma de suas propriedades armazenadas deve ser marcado como `mutating`. Quando esse método é um requisito de protocolo, o protocolo também precisa dizê-lo:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Sem `mutating` no protocolo, uma struct nunca poderia satisfazer o requisito. Classes são tipos de referência e nunca precisam da palavra-chave: uma classe atende a um requisito `mutating` com um método comum. Chamar um método mutating precisa de um `var` — em um `let` é um erro de compilação.

---

A conformidade não precisa ser declarada ao lado do tipo. Uma **extension** pode adicioná-la depois, o que mantém a declaração do próprio tipo focada em seus dados:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
Isso também funciona para tipos que você não escreveu: você pode fazer um tipo da biblioteca padrão conformar-se a um dos seus protocolos sem tocar em seu código-fonte.

---

Uma extension de um **protocolo** é uma ferramenta diferente: ela adiciona membros a todo tipo em conformidade, presente e futuro. É assim que você dá a um requisito uma **implementação padrão**:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` nunca escreve `greet()` e ainda assim se conforma. Dentro da extension do protocolo você pode usar cada requisito do protocolo — aqui `name` — porque qualquer tipo em conformidade tem a garantia de tê-lo.

---

Uma extension de protocolo também pode adicionar membros que o protocolo nunca listou como requisitos. São conveniências extras, disponíveis em todo tipo em conformidade:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` não é um requisito, então um tipo em conformidade não precisa fornecê-lo — ele simplesmente o recebe.

---

Um protocolo pode se basear em outro. Escrever o nome de um protocolo depois de dois-pontos faz o novo protocolo **herdar** cada requisito do antigo:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Um tipo em conformidade com `Aged` deve fornecer `age` *e* `name`, e conta como um tipo `Named` em todos os lugares. Um protocolo pode herdar de vários protocolos de uma vez, separados por vírgulas.

---

Uma implementação padrão é um fallback, não uma regra. Se um tipo em conformidade fornece sua própria versão de um requisito, a versão dele é a que roda:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, not 0
```
O padrão apenas preenche as lacunas que o tipo deixa em aberto.

---

A biblioteca padrão é construída a partir de protocolos, e seus próprios tipos podem adotá-los.

`Equatable` dá a um tipo o operador `==`. Para uma struct cujas propriedades armazenadas são todas `Equatable`, declarar a conformidade é suficiente — o Swift escreve `==` para você:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` herda de `Equatable` e adiciona ordenação. Você implementa um único operador, `<`, escrito como uma `static func` que recebe os dois valores, e ganha de graça `>`, `<=`, `>=`, além de `sorted()`, `min()` e `max()` nas coleções:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` decide o que o `print` mostra para o seu tipo. Seu único requisito é uma propriedade `description`:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Sem a conformidade, imprimir uma struct cai em um dump padrão como `Coin(value: 25)`, e uma propriedade `description` sozinha não muda nada — o `print` procura pelo protocolo. A interpolação de strings também usa `description`.

---

Um nome de protocolo sozinho não é um tipo, é uma restrição, então o Swift pede que você diga qual de duas coisas você quer dizer.

`some Shape` significa *um tipo em conformidade específico*, fixo em tempo de compilação. Quem chama nunca descobre qual é, mas é sempre o mesmo:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` significa *uma caixa que pode conter qualquer tipo em conformidade*, e dois valores desse tipo podem conter tipos diferentes. Você precisa dele sempre que o tipo concreto puder variar, como dentro de um array misto:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Ambos permitem chamar os requisitos do protocolo. Prefira `some` quando um único tipo for suficiente, porque não custa nada em tempo de execução; recorra a `any` quando realmente precisar misturar tipos.
