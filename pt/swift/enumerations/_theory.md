Uma `enumeration` (enumeração) define um tipo comum para um grupo de valores relacionados e permite que você trabalhe com esses valores de forma segura em termos de tipos no seu código.
Declaramos enumerações usando a palavra-chave `enum`:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
Os valores definidos em uma enumeração (como `blue`, `red` e `green`) são seus _casos de enumeração_.
Usamos a palavra-chave `case` para introduzir novos casos de enumeração.

---

Múltiplos casos podem aparecer em uma única linha, separados por vírgulas:
```swift
enum Colors {
    case blue, red, green
}
```

---

Podemos corresponder valores individuais de enumeração com uma instrução `switch`:
```swift
let color = Colors.red
switch color {
    case .blue:
        print("Blue")
    case .red:
        print("Red")
    case .green:
        print("Green")
}
// prints "Red"
```
Lembre-se de que, se você não precisar fornecer um `case` para cada caso da enumeração, pode fornecer um caso `default` para cobrir quaisquer casos que não sejam tratados explicitamente

---

Para algumas enumerações, é útil ter uma coleção de todos os casos dessa enumeração.
Você habilita isso escrevendo `: CaseIterable` após o nome da enumeração.
O Swift expõe uma coleção de todos os casos como uma propriedade `allCases` do tipo de enumeração:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
