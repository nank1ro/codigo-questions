Une `énumération` définit un type commun pour un groupe de valeurs connexes et vous permet de travailler avec ces valeurs de manière type-safe dans votre code.
Nous déclarons les énumérations en utilisant le mot-clé `enum` :
```swift
enum Colors {
    case blue
    case red
    case green
}
```
Les valeurs définies dans une énumération (telles que `blue`, `red` et `green`) sont ses _cas d'énumération_.
Nous utilisons le mot-clé `case` pour introduire de nouveaux cas d'énumération.

---

Multiple cases can appear on a single line, separated by commas:
```swift
enum Colors {
    case blue, red, green
}
```

---

Nous pouvons faire correspondre les valeurs d'énumération individuelles avec une instruction `switch` :
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
Gardez à l'esprit que si vous n'avez pas besoin de fournir un `case` pour chaque cas d'énumération, vous pouvez fournir un `default` case pour couvrir tous les cas qui ne sont pas explicitement traités

---

Pour certaines énumérations, il est utile d'avoir une collection de tous les cas de cette énumération.
You enable this by writing `: CaseIterable` after the enumeration's name.
Swift exposes a collection of all the cases as an `allCases` property of the enumeration type:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
