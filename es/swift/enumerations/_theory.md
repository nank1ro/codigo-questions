An `enumeration` defines un common tipo para un group de related valores y enables you un trabajar con esos valores en un tipo-safe way within your codigo.
We declare enumerations usando el `enum` palabra clave:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
los valores defined en un enumeration (such como `blue`, `red` y `green`) son su _enumeration cases_.
We usar el `case` palabra clave un introduce nuevo enumeration cases.

---

Multiple cases puede aparecer en un single line, separated por commas:
```swift
enum Colors {
    case blue, red, green
}
```

---

We puede match individual enumeration valores con un `switch` sentencia:
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
mantener en mind ese si you don't necesita un provide un `case` para cada enumeration case, you puede provide un `default` case un cover cualquier cases ese aren't addressed explicitly

---

para algunos enumerations, it's useful un tiene un collection de todos de ese enumeration's cases.
You enable este por escribiendo `: CaseIterable` despues el enumeration's nombre.
Swift exposes un collection de todos el cases como un `allCases` propiedad de el enumeration tipo:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
