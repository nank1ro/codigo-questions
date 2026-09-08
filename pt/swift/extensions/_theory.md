Uma **extension** adiciona novas funcionalidades a um tipo existente: um tipo da biblioteca padrão como `Int` ou `String`, ou uma struct ou classe que você mesmo escreveu.
Você escreve a palavra-chave `extension` seguida do nome do tipo e coloca os novos membros entre chaves:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Dentro da extension, `self` é o valor no qual o método é chamado: em `4.squared()` é `4`. Uma vez que a extension existe, todo `Int` do programa tem o novo método, exatamente como se ele tivesse feito parte de `Int` desde o início.

---

Extensions funcionam com qualquer tipo, até mesmo com aqueles para os quais você não tem o código-fonte. `String` vem da biblioteca padrão, mas você ainda pode dar a ela novos métodos:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Dentro de uma extension você pode omitir `self.` ao chamar outros membros do tipo: `lowercased()` sozinho significa `self.lowercased()`.

---

Uma extension não cria um novo tipo e não copia o antigo: ela adiciona membros ao próprio tipo, então todo valor existente e futuro desse tipo os recebe.
É por isso que extensions são tão úteis com tipos que você não pode editar, como os da biblioteca padrão ou de um framework: você não pode abrir o arquivo onde `Int` é definido, mas pode estendê-lo a partir de qualquer arquivo do seu programa.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

Além de métodos, uma extension pode adicionar **propriedades computadas**: propriedades que não armazenam um valor, mas o calculam toda vez que são lidas.
Uma propriedade computada é declarada com `var`, uma anotação de tipo e um corpo entre chaves que retorna o valor:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Ela é lida como qualquer propriedade, sem parênteses: `7.isNegative`, e não `7.isNegative()`.

---

Propriedades computadas em extensions também são uma escolha natural para `String`. O método `reversed()` retorna os caracteres em ordem inversa, e `String(...)` os transforma de volta em uma string:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Assim como nos métodos, `reversed()` dentro da extension significa `self.reversed()`.

---

Extensions podem adicionar propriedades computadas, mas **não propriedades armazenadas**: isto não compila:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Uma propriedade armazenada precisa de espaço dentro de cada instância do tipo. Valores `Int` já existem por todo o seu programa, e até mesmo em código compilado muito antes da sua extension, então o layout de memória deles não pode mudar. Uma propriedade computada não precisa de espaço, porque é apenas código que executa quando a propriedade é lida.

---

`Int`, `String`, arrays e structs são **value types**: um método não pode alterar o valor no qual é chamado, a menos que esteja marcado como `mutating`. Extensions também podem adicionar métodos `mutating`:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
Dentro de um método `mutating` você pode atribuir a `self`. O valor deve ser armazenado em um `var`: chamar `increment()` em uma constante `let` é um erro de compilação.

---

Um método `mutating` pode receber parâmetros como qualquer outro método, e pode substituir `self` inteiramente em vez de atualizá-lo no lugar:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

Uma extension pode adicionar novos **inicializadores** a um tipo. Para uma struct este é o melhor lugar para colocá-los: um `init` escrito dentro do corpo da struct substitui o inicializador membro a membro automático, enquanto um adicionado em uma extension o mantém.
O novo inicializador geralmente delega a um existente com `self.init(...)`:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Extensions não são apenas para tipos de outras pessoas. Uma forma comum de organizar o seu próprio código é manter as propriedades armazenadas no corpo da struct ou classe e adicionar o comportamento em uma ou mais extensions, cada uma agrupando membros relacionados:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
Os membros adicionados em uma extension podem usar as propriedades armazenadas diretamente, exatamente como se tivessem sido escritos dentro do tipo.

---

Uma extension também pode fazer um tipo conformar a um **protocolo**, uma lista de requisitos que o tipo promete implementar. Escreva o nome do protocolo depois do nome do tipo, separado por dois pontos, e adicione os membros exigidos no corpo.
`CustomStringConvertible` é um protocolo padrão com um único requisito, uma propriedade computada `description` do tipo `String`, que o `print` usa para exibir o valor:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Manter cada conformidade a um protocolo em sua própria extension é a forma usual de organizar um tipo Swift.

---

`Array` é um tipo genérico: `[Int]` e `[String]` são ambos arrays, com um tipo **`Element`** diferente. Uma extension de `Array` se aplica a todos eles, o que é um problema quando o novo membro só faz sentido para alguns elementos: você não pode somar números que são strings.
Uma cláusula `where` restringe a extension aos arrays cujo `Element` é de um tipo dado:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` funciona, enquanto `["a", "b"].largest` é um erro de compilação: a propriedade não existe em `[String]`.

---

Extensions podem adicionar membros **estáticos**: propriedades e métodos que pertencem ao próprio tipo em vez de a um único valor, marcados com a palavra-chave `static` e acessados através do nome do tipo.
Um `static let` é permitido mesmo que armazene um valor, porque existe apenas uma cópia para o tipo inteiro, e não uma por instância:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
Um membro estático não tem valor `self` para trabalhar: `Int.answer` é lido no tipo, não em um número.

---

Métodos estáticos em extensions são um bom lugar para pequenas funções de fábrica que constroem um valor do tipo. `String(repeating:count:)` é o inicializador padrão que repete um pedaço de texto um número de vezes:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Extensions só podem **adicionar** membros, nunca substituir ou sobrescrever os existentes. `override` pertence a subclasses, que são um tipo diferente do seu pai; uma extension é o mesmo tipo, então declarar um método que já existe é um erro de redeclaração:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
Se você precisa de um comportamento diferente, adicione um método com um novo nome, ou escreva uma subclasse quando o tipo for uma classe.
