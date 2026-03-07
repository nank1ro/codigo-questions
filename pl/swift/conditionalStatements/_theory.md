Podejmowanie decyzji jest wymagane, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `niceWeather` i wykonać czynność zabawy na zewnątrz `if` ta zmienna jest `true`, tak jak:
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Kontynuujmy poprzedni przykład.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
Widzieliśmy, że instrukcja `if` wykonuje blok kodu tylko wtedy, gdy warunek jest `true`.
Kolejną ważną rzeczą do rozważenia są **nawiasy klamrowe** `{}`, które oznaczają blok kodu.

---

Właśnie widzieliśmy, jak wykonać blok kodu, gdy wystąpi warunek — teraz zobaczmy, jak wykonać inny blok kodu, gdy pierwszy warunek nie jest spełniony.
Wychodzimy bawić się na zewnątrz, gdy pogoda jest ładna; w przeciwnym razie zostajemy w domu.
W Swift możemy użyć instrukcji `else`, tak jak:
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Załóżmy, że mamy kolejny warunek do sprawdzenia, jak w tym przykładzie:
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
a wynikiem tego kodu jest `the number is 3`.
Najpierw sprawdzamy, czy liczba jest równa 2 — jest to fałsz.
Przejdźmy więc do drugiej instrukcji i sprawdźmy, czy `num` jest równe 3 — ponieważ jest to prawda, wykonujemy następujący blok kodu, drukując `the number is 3`

---

Możemy dodać tyle instrukcji `else if`, ile chcemy — nie ma żadnych ograniczeń
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
a wynikiem tego kodu jest `the number is 4`.

---

Możemy również zagnieżdżać instrukcję warunkową (`if`, `else if` lub `else`) wewnątrz innej instrukcji warunkowej, aby tworzyć bardziej złożoną strukturę.
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
a wynikiem tego kodu jest `the number is 4`.

---

Trójkowy operator warunkowy to specjalny operator składający się z trzech części, który przyjmuje postać `pytanie ? odpowiedź1 : odpowiedź2`.
Jest to skrót do oceniania jednego z dwóch wyrażeń w zależności od tego, czy `pytanie` jest prawdziwe czy fałszywe.
Jeśli `pytanie` jest prawdziwe, ocenia `odpowiedź1` i zwraca jej wartość; w przeciwnym razie ocenia `odpowiedź2` i zwraca jej wartość.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
Skrócony kod dla powyższego kodu to:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` jest ustawione równe `a`, ponieważ warunek `a < b` był prawdziwy

---

Operator _nil-coalescing_ `a ?? b` rozpakowuje opcjonalne `a`, jeśli zawiera wartość, lub zwraca domyślną wartość `b`, jeśli `a` jest `nil`.
Wyrażenie `a` jest zawsze typu opcjonalnego.
Wyrażenie `b` musi odpowiadać typowi przechowywanego w a.
Operator nil-coalescing jest skrótem dla poniższego kodu:
```swift
a != nil ? a! : b
```
