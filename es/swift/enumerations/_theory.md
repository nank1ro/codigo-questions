Una `enumeration` define un tipo común para un grupo de valores relacionados y le permite trabajar con esos valores de forma segura dentro de su código.
Declaramos enumeraciones usando la palabra clave `enum`:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
Los valores definidos en una enumeración (como `blue`, `red` y `green`) son sus _enumeration cases_.
Usamos la palabra clave `case` para introducir nuevos enumeration cases.

---

Múltiples casos pueden aparecer en una sola línea, separados por comas:
```swift
enum Colors {
    case blue, red, green
}
```

---

Podemos coincidir con valores de enumeración individuales con una declaración `switch`:
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
Tenga en cuenta que si no necesita proporcionar un `case` para cada caso de enumeración, puede proporcionar un caso `default` para cubrir cualquier caso que no se trate explícitamente

---

Para algunas enumeraciones, es útil tener una colección de todos los casos de esa enumeración.
Lo habilitas escribiendo `: CaseIterable` después del nombre de la enumeración.
Swift expone una colección de todos los casos como una propiedad `allCases` del tipo de enumeración:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```

---

Para algunas enumeraciones, es útil tener una colección de todos los casos de esa enumeración.
Lo habilitas escribiendo `: CaseIterable` después del nombre de la enumeración.
Swift expone una colección de todos los casos como una propiedad `allCases` del tipo de enumeración:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// imprime blue, red, green
```
