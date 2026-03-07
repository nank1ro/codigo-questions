Podejmowanie decyzji jest konieczne, gdy chcemy wykonać kod tylko wtedy, gdy spełniony jest określony warunek.
Załóżmy, że chcemy bawić się na zewnątrz tylko wtedy, gdy pogoda jest ładna.
W programowaniu możemy zapisać zmienną logiczną `niceWeather` i wykonać akcję zabawy na zewnątrz `if` ta zmienna ma wartość `true`, na przykład:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

Kontynuujmy poprzedni przykład.
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
Widzieliśmy, że instrukcja `if` wykonuje blok kodu tylko wtedy, gdy warunek ma wartość `true`.
Kolejną ważną rzeczą jest użycie **nawiasów klamrowych** `{}`, które wskazują blok kodu.

---

Właśnie zobaczyliśmy, jak wykonać blok kodu, gdy zaistnieje warunek. Teraz zobaczmy, jak wykonać inny blok kodu, gdy pierwszy warunek nie jest spełniony.
Idziemy bawić się na zewnątrz, jeśli pogoda jest ładna; w przeciwnym razie zostajemy w domu.
W Kotlin możemy użyć instrukcji `else`, na przykład:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Załóżmy, że mamy kolejny warunek do sprawdzenia, jak w tym przykładzie:
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
a wynik tego kodu to `the number is 3`.
Na początku sprawdzamy, czy liczba jest równa 2 – to jest fałsz.
Więc przechodzimy do drugiej instrukcji i sprawdzamy, czy `num` jest równe 3. Ponieważ to prawda, wykonujemy następujący blok kodu, wyświetlając `the number is 3`

---

Możemy dodać tyle instrukcji `else if`, ile chcemy – nie ma ograniczeń
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
a wynik tego kodu to `the number is 4`.

---

Możemy też zagnieżdżać instrukcje warunkowe (`if`, `else if` lub `else`) wewnątrz innej instrukcji warunkowej, tworząc bardziej złożoną strukturę.
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
a wynik tego kodu to `the number is 4`.

---

Operator _elvis_ `a ?: b` rozpakowuje opcjonalne `a`, jeśli zawiera wartość, lub zwraca wartość domyślną `b`, jeśli `a` jest `null`.
Wyrażenie `a` jest zawsze typu opcjonalnego.
Wyrażenie `b` musi być zgodne z typem przechowywanym wewnątrz a.
Operator Elvis jest skrótem dla poniższego kodu:
```kotlin
if (a != null) a else b
```
