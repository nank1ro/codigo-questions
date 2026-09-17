Uma **closure** é um bloco de código que você pode passar adiante e chamar mais tarde, como uma função sem nome.
A sintaxe completa da expressão de closure coloca os parâmetros e o tipo de retorno entre chaves, seguidos da palavra-chave `in` e do corpo:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Como qualquer outro valor, uma closure pode ser armazenada em uma constante e depois chamada usando o nome da constante:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Escrever todos os tipos dentro da closure geralmente é desnecessário. Quando a constante tem um **tipo de função** explícito, o Swift infere os tipos dos parâmetros e do retorno, então você só precisa listar os nomes dos parâmetros antes do `in`:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
O tipo `(Int) -> Int` se lê como "uma função que recebe um `Int` e retorna um `Int`".
Quando o corpo é uma única expressão, a palavra-chave `return` também pode ser omitida, isso é chamado de **retorno implícito**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

O Swift vai um passo além: dentro de uma closure você pode se referir aos argumentos usando os **nomes abreviados de argumento** `$0`, `$1`, `$2` e assim por diante, sem declarar nenhum parâmetro ou a palavra-chave `in`.
`$0` é o primeiro argumento, `$1` o segundo:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
Os tipos ainda vêm da anotação `(Int, Int) -> Int`.

---

Como closures são valores, uma função pode aceitar uma como parâmetro. O tipo do parâmetro é apenas o tipo de função:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
A função `apply` não sabe o que `operation` faz, ela só sabe que recebe um `Int` e retorna um `Int`, e a chama como qualquer outra função.

---

Quando uma closure é o **último** argumento de uma função, você pode escrevê-la depois do parêntese de fechamento da chamada. Essa é a sintaxe de **trailing closure**:
```swift
print(apply(5) { $0 + 1 }) // 6
```
Se a closure for o único argumento, os parênteses podem ser omitidos completamente:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
As duas formas chamam exatamente a mesma função, a sintaxe trailing só é mais fácil de ler quando a closure é longa.

---

As closures brilham com os métodos de array que recebem uma como argumento. `map` chama a closure em cada elemento e retorna um novo array com os resultados:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
O array original não é alterado. Como `map` recebe uma única closure como argumento, a sintaxe de trailing closure é a forma usual de chamá-lo.

---

`filter` mantém apenas os elementos para os quais a closure retorna `true`. A closure recebe um elemento e deve retornar um `Bool`:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Os elementos mantêm sua ordem original, e o resultado é um novo array do mesmo tipo de elemento.

---

`reduce` combina todos os elementos em um único valor. Ele recebe um valor inicial e uma closure com dois argumentos: o valor acumulado até agora e o elemento atual. A closure retorna o novo valor acumulado:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Aqui `$0` começa como `1`, depois se torna `1 * 1`, `1 * 2`, `2 * 3` e finalmente `6 * 4`.
Como `map`, `filter` e `reduce` retornam valores, eles podem ser encadeados: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` retorna um novo array ordenado. A closure recebe dois elementos e retorna `true` quando o primeiro deve vir **antes** do segundo:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
A closure pode comparar qualquer coisa, por exemplo `words.sorted { $0.count < $1.count }` ordena strings da mais curta para a mais longa.

---

Uma closure pode usar variáveis declaradas fora do seu corpo. Ela as **captura**: a variável continua existindo enquanto a closure existir, mesmo depois que a função que a declarou tiver retornado.
Isso permite que uma função construa uma closure com seu próprio estado privado:
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int` é o tipo de uma closure sem parâmetros que retorna um `Int`. Cada chamada à closure retornada incrementa o mesmo `count` capturado:
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

Retornar uma closure é uma forma prática de construir funções personalizadas. Os parâmetros da função externa são capturados pela closure que ela retorna:
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
O tipo de retorno `(Int) -> Int` descreve a closure, e a abreviação `$0` se refere ao argumento dessa closure, não de `makeAdder`.

---

Uma closure armazenada em uma constante pode ser passada sempre que uma closure for esperada como argumento, usando o rótulo de argumento do parâmetro:
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

Cada chamada a uma função que retorna uma closure cria uma **nova** variável capturada. Duas closures construídas por chamadas separadas não compartilham seu estado:
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
O estado é compartilhado somente entre chamadas da mesma closure.

---

Por padrão, uma closure passada para uma função só pode ser usada enquanto essa função estiver em execução. Se a função armazenar a closure ou retornar outra closure que a use, a closure **escapa** da função, e seu parâmetro precisa ser marcado com `@escaping`:
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
Sem `@escaping` o compilador reporta um erro, porque a closure retornada usaria `task` depois que `twice` já tivesse terminado.

---

Closures podem ser armazenadas em arrays como qualquer outro valor. O tipo do elemento é o tipo de função:
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
Percorrer um array assim e chamar cada closure em sequência constrói um pequeno **pipeline** de transformações.
