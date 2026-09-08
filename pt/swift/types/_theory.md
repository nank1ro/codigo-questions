Todo valor em Swift tem um **tipo**, que informa ao compilador que tipo de dado ele é e o que você pode fazer com ele.
Os tipos básicos são:
- `Int`: um número inteiro, como `42` ou `-7`
- `Double`: um número com parte decimal, como `3.14`
- `String`: um texto, como `"Hello"`
- `Character`: um único caractere, como `"a"`
- `Bool`: `true` ou `false`

Você pode indicar o tipo de uma constante ou variável com uma **anotação de tipo**: dois-pontos e o nome do tipo depois do nome:
```swift
let age: Int = 36
let name: String = "Ada"
```
Um valor de um tipo não pode ser armazenado em uma constante de outro tipo: `let age: Int = "36"` é um erro de compilação.

---

Na maioria das vezes você não escreve a anotação de tipo: o Swift **infere** o tipo a partir do valor que você atribui, seguindo algumas regras de literais:
- um número sem ponto decimal, como `42`, é um `Int`
- um número com ponto decimal, como `3.14`, é um `Double`
- texto entre aspas duplas é uma `String`
- `true` e `false` são `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
O Swift também tem o `Float`, um número decimal que usa metade da memória de um `Double` mas é menos preciso, então um literal decimal nunca é inferido como `Float`: você precisa solicitá-lo com uma anotação.
Da mesma forma, `"a"` é inferido como uma `String`, então um `Character` sempre precisa de uma anotação.

---

A função `type(of:)` retorna o tipo de um valor, o que é útil para verificar o que o Swift inferiu:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Quando você quer um tipo diferente do inferido, adicione uma anotação. Um literal de número inteiro pode ser armazenado em uma constante `Double` ou `Float`, e um literal de um caractere em uma constante `Character`:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

O Swift nunca converte entre tipos numéricos por conta própria: somar um `Int` a um `Double` é um erro de compilação, mesmo que ambos sejam números.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Para combiná-los, você cria um novo valor do tipo necessário, passando o valor para o inicializador do tipo:
```swift
let total = Double(apples) * price // 4.5
```
O mesmo funciona no sentido contrário: `Int(4.5)` produz um `Int`, mantendo apenas a parte inteira do número.

---

`Int(x)` não arredonda: ele **trunca**, simplesmente descartando a parte decimal, então `Int(3.99)` é `3` e `Int(-3.99)` é `-3`.
Para arredondar para o número inteiro mais próximo, chame `rounded()` no `Double` primeiro e depois converta:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Valores intermediários como `2.5` são arredondados para longe do zero: `2.5` se torna `3.0` e `-2.5` se torna `-3.0`.

---

O tipo dos operandos decide como a divisão funciona. Quando ambos são `Int`, o operador `/` realiza a **divisão inteira**: o resultado é um `Int` e o resto é descartado.
Quando pelo menos um operando é um `Double`, o `/` realiza a divisão de ponto flutuante e mantém a parte decimal:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Então, para obter um resultado decimal a partir de dois valores `Int`, você precisa converter pelo menos um deles para `Double` **antes** de dividir: `Double(7 / 2)` é `3.0`, porque a divisão inteira já aconteceu.

---

Quando uma função precisa retornar um resultado decimal calculado a partir de números inteiros, converta os operandos para `Double` antes de dividir e declare o tipo de retorno como `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Lembre-se de que o `count` de um array também é um `Int`, então ele precisa da mesma conversão.

---

Números e strings são convertidos com a mesma sintaxe de inicializador. `String(42)` transforma um número no texto `"42"`, exatamente como interpolá-lo com `"\(42)"`.
A direção oposta pode falhar, porque nem todo texto é um número, então `Int("42")` retorna um `Int?` **opcional**: ele contém `42` aqui, mas `Int("hello")` é `nil`.
Como você aprendeu nas lições de opcionais, você pode fornecer um valor padrão com `??` ou desempacotá-lo com `if let`:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` tem sucesso apenas quando o texto inteiro é um número inteiro válido, com um sinal opcional:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Para texto decimal use `Double(text)`, que retorna um `Double?` da mesma forma: `Double("3.5")` é `Optional(3.5)`.

---

Um **alias de tipo** dá a um tipo existente um novo nome, com a palavra-chave `typealias`:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` e `Int` são o mesmo tipo, então eles se combinam livremente. Um alias não adiciona nenhuma segurança: ele apenas torna o código mais legível quando um tipo comum tem um significado específico no seu programa.

---

Um `Int` usa 64 bits, então ele só pode representar números em um intervalo fixo. O maior e o menor valor estão disponíveis como `Int.max` e `Int.min`:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Ultrapassar esses limites é chamado de **estouro** (overflow). Diferente de muitas outras linguagens, o Swift não volta silenciosamente ao outro extremo do intervalo: uma operação com estouro é um **erro em tempo de execução** que interrompe o programa.

---

`Int.max` e `Int.min` são úteis como valores iniciais quando você procura um extremo: qualquer número é menor que `Int.max`, então ele é um valor inicial seguro para "o menor visto até agora":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Como você viu nas lições de strings, iterar sobre uma `String` fornece um `Character` por vez. Um `Character` não é uma `String`, então para usá-lo como texto você o converte com `String(c)`.
Quando o caractere é um dígito, a propriedade `wholeNumberValue` fornece seu valor numérico como um `Int?`: ele é `nil` para caracteres que não são dígitos.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Como `Int(text)` e `Double(text)` retornam `nil` em caso de falha, comparar o resultado com `nil` informa se um texto é um número desse tipo:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Note a última linha: todo texto aceito pelo `Int` também é aceito pelo `Double`, então verifique primeiro o `Int` quando quiser distingui-los.

---

Às vezes você precisa armazenar valores de tipos diferentes juntos. O tipo especial `Any` pode conter um valor de **qualquer** tipo, então um array declarado como `[Any]` pode misturar números, strings e booleanos:
```swift
let items: [Any] = [1, "two", true]
```
Cada elemento ainda lembra seu tipo real, que o `type(of:)` revela. Para trabalhar com o valor como seu tipo real, você usa uma **conversão condicional** com `as?`, que retorna um opcional: ele contém o valor quando o tipo corresponde e `nil` caso contrário:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` é um último recurso: um array de um único tipo concreto é mais seguro e mais fácil de usar, então prefira-o sempre que puder.

---

Conversões condicionais se encadeiam naturalmente com `else if` para tratar vários tipos possíveis, convertendo cada um para o tipo de que você precisa para o resultado:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
Um `Int` armazenado em `Any` ainda é um `Int`: `as? Double` sobre ele retorna `nil`, porque `as?` verifica o tipo, ele não converte números.
