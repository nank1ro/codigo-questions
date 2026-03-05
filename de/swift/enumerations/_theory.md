Eine `Enumeration` definiert einen gemeinsamen Typ für eine Gruppe verwandter Werte und ermöglicht es dir, mit diesen Werten auf typsichere Weise in deinem Code zu arbeiten.
Wir deklarieren Enumerationen mit dem `enum` Schlüsselwort:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
Die in einer Enumeration definierten Werte (wie `blue`, `red` und `green`) sind ihre _Enumerationsfälle_.
Wir verwenden das `case` Schlüsselwort, um neue Enumerationsfälle einzuführen.

---

Mehrere Fälle können in einer einzigen Zeile erscheinen, getrennt durch Kommas:
```swift
enum Colors {
    case blue, red, green
}
```

---

Wir können einzelne Enumerationswerte mit einer `switch` Anweisung abgleichen:
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
Denke daran, dass wenn du kein `case` für jeden Enumerationsfall bereitstellen musst, du einen `default` Fall bereitstellen kannst, um alle Fälle abzudecken, die nicht explizit behandelt werden

---

Bei einigen Enumerationen ist es nützlich, eine Sammlung aller Fälle dieser Enumeration zu haben.
Du aktivierst dies, indem du `: CaseIterable` nach dem Namen der Enumeration schreibst.
Swift stellt eine Sammlung aller Fälle als `allCases` Eigenschaft des Enumerationstyps bereit:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
