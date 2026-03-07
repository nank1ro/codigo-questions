`Wyliczenie` definiuje wspólny typ dla grupy powiązanych wartości i umożliwia pracę z tymi wartościami w sposób bezpieczny pod względem typów w kodzie.
Wyliczenia deklarujemy za pomocą słowa kluczowego `enum`:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
Wartości zdefiniowane w wyliczeniu (takie jak `blue`, `red` i `green`) to jego _przypadki wyliczenia_.
Używamy słowa kluczowego `case`, aby wprowadzić nowe przypadki wyliczenia.

---

Wiele przypadków może pojawić się w jednej linii, oddzielonych przecinkami:
```swift
enum Colors {
    case blue, red, green
}
```

---

Możemy dopasowywać poszczególne wartości wyliczenia za pomocą instrukcji `switch`:
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
Pamiętaj, że jeśli nie musisz podawać `case` dla każdego przypadku wyliczenia, możesz podać przypadek `default`, który obejmuje wszystkie przypadki nieadresowane wprost

---

W przypadku niektórych wyliczeń przydatne jest posiadanie kolekcji wszystkich przypadków tego wyliczenia.
Umożliwia to napisanie `: CaseIterable` po nazwie wyliczenia.
Swift udostępnia kolekcję wszystkich przypadków jako właściwość `allCases` typu wyliczenia:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
