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

Plusieurs cas peuvent apparaître sur une seule ligne, séparés par des virgules :
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
Vous activez cela en écrivant `: CaseIterable` après le nom de l'énumération.
Swift expose une collection de tous les cas en tant que propriété `allCases` du type d'énumération :
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
