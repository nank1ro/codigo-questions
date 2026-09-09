Uma **função de ordem superior** é uma função que recebe outra função como argumento, retorna uma, ou ambos. Você já conheceu `map`, `filter`, `reduce` e `sorted(by:)`: elas recebem uma closure e a aplicam aos elementos de uma coleção. O Swift tem muitas outras, e conhecê-las permite substituir loops longos por uma única linha legível.
`compactMap` funciona como `map`, mas a closure retorna um opcional e os resultados `nil` são descartados:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` é `nil`, então esse elemento desaparece e o resultado é um `[Int]`, não um `[Int?]`.

---

`flatMap` é para closures que retornam um **array**: em vez de construir um array de arrays, ela junta todos os arrays retornados em um único resultado plano:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
A closure também pode transformar cada array interno antes de ele ser achatado, por exemplo `teams.flatMap { $0.reversed() }` dá `["Bob", "Ann", "Cid"]`.

---

As três variantes de `map` diferem apenas no que a closure retorna:
- `map`: qualquer valor, um resultado por elemento
- `compactMap`: um opcional, os resultados `nil` são descartados
- `flatMap`: um array, todos os resultados são unidos em um único array

A closure passada para `flatMap` pode ela mesma chamar `map` no array interno, aninhando uma transformação dentro da outra:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` constrói um novo valor acumulado a cada passo, o que é desperdício quando o resultado é um array ou um dicionário. `reduce(into:)` entrega à closure o acumulador como um parâmetro `inout`, de modo que ele possa ser modificado no lugar, sem `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` cria um dicionário vazio, e `result[word, default: 0]` lê a contagem atual ou `0` quando a chave está ausente.

---

Algumas funções de ordem superior respondem a uma pergunta sobre a coleção em vez de transformá-la. Todas elas recebem uma closure que retorna um `Bool`:
- `first(where:)` retorna o primeiro elemento que satisfaz a closure, ou `nil` se não houver nenhum
- `contains(where:)` retorna `true` se pelo menos um elemento a satisfaz
- `allSatisfy` retorna `true` se todos os elementos a satisfazem

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
Ao contrário de `filter`, `first(where:)` para na primeira correspondência e não constrói um novo array.

---

`contains(where:)` e `allSatisfy` substituem o padrão comum de um loop com uma variável de sinalização. Ambas param assim que a resposta é conhecida: `contains(where:)` na primeira correspondência, `allSatisfy` no primeiro elemento que falha.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` é a forma de trailing closure de `contains(where:)`, para não confundir com `contains(_:)`, que procura por um valor específico.

---

Funções de ordem superior funcionam em qualquer array, incluindo arrays de suas próprias structs. Encadear `filter` e depois `map` é a forma usual de selecionar alguns elementos e extrair um valor de cada um:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Fazer na ordem oposta, `map` e depois `filter`, perderia a propriedade `pages` antes que a verificação pudesse usá-la.

---

Quando uma closure apenas lê uma propriedade, você pode passar um **key path** em vez disso: `\.name` significa "a propriedade `name` do elemento", e `map(\.name)` é o mesmo que `map { $0.name }`.
Para ordenar por uma propriedade usa-se a closure usual de dois argumentos, comparando essa propriedade nos dois elementos:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Para ordenar por **mais de um critério**, compare a primeira propriedade e recorra à segunda apenas quando os primeiros valores forem iguais:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Aqui as pessoas são ordenadas por idade, e pessoas com a mesma idade são ordenadas por nome. A closure deve retornar `true` apenas quando o primeiro elemento deve vir antes do segundo, de modo que o caso de igualdade passe para a próxima comparação.

---

`enumerated()` transforma um array em uma sequência de pares `(offset, element)`, de modo que uma closure possa usar a posição de cada elemento junto com seu valor:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Como cada par é uma tupla, a closure também pode desconstruí-lo: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` emparelha os elementos de duas sequências posição por posição, produzindo uma sequência de tuplas. Ela para no fim da mais curta:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Dentro da closure `$0` é o elemento da primeira sequência e `$1` o da segunda. `zip` é uma função livre, não um método: você escreve `zip(a, b)`, não `a.zip(b)`.

---

`forEach` é o gêmeo de ordem superior do loop `for-in`: ele chama a closure uma vez por elemento, em ordem. A diferença está em como você sai do loop. Em um `for-in` você pode usar `break` ou `continue`; dentro de uma closure `forEach`, `break` e `continue` não são permitidos, e `return` apenas encerra a **chamada atual** da closure, depois o próximo elemento é processado como de costume:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Use `forEach` para um efeito colateral curto em cada elemento, e `for-in` quando precisar parar mais cedo.

---

`Dictionary(grouping:by:)` divide uma coleção em um dicionário de arrays. A closure calcula a **chave** de cada elemento, e todos os elementos com a mesma chave acabam no mesmo array:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` transforma cada valor de um dicionário mantendo as chaves, então é o próximo passo natural após o agrupamento:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` toma elementos do início **enquanto** a closure retorna `true`, e para no primeiro elemento que falha, mesmo que elementos posteriores passassem de novo. `drop(while:)` é seu complemento: ele pula essa mesma sequência inicial e retorna todo o resto:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Ambos retornam um `ArraySlice`, uma visão do array original que é impressa como um array e pode ser convertida em um com `Array(...)`.

---

Você pode escrever suas próprias funções de ordem superior. Uma função que recebe uma closure e **retorna uma nova closure** construída a partir dela é um padrão comum: a closure retornada captura a original, então o parâmetro deve ser `@escaping`.
Por exemplo, `negate` transforma um predicado em seu oposto, pronto para ser passado a `filter`:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Note que `filter(negate(isEven))` passa a closure como um argumento normal, sem a sintaxe de trailing closure.

---

`map` e `filter` em um array são **eager**: cada um processa o array inteiro e constrói um novo antes que o próximo passo seja executado. Em uma coleção grande, ou quando você só precisa do primeiro resultado, isso é trabalho desperdiçado.
A propriedade `lazy` retorna uma visão cujas operações rodam apenas quando um elemento é realmente solicitado, um elemento por vez através de toda a cadeia:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Aqui apenas `1, 2, ..., 8` são elevados ao quadrado: `first(where:)` pede elementos até que um satisfaça a condição, e a cadeia para aí. Sem `lazy`, `map` elevaria todos os 1000 números ao quadrado primeiro.
