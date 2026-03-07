Zmienne to kontenery do przechowywania wartości danych.
Każda zmienna w Kotlinie jest obiektem.
Aby utworzyć zmienną, musimy nadać jej __nazwę__, pamiętając, że nie może ona zawierać spacji.
Zmienna jest tworzona w momencie pierwszego przypisania wartości.
W Kotlinie stałe deklarujemy za pomocą słowa kluczowego `val` (skrót od _value_), a zmienne za pomocą `var` (skrót od _variable_).
Wartości stałej nie można zmienić po jej ustawieniu, natomiast zmienną można ustawić na inną wartość w przyszłości.
Przykład tworzenia zmiennej o nazwie `x`:
```kotlin
var x = 1
```
W ten sposób przypisaliśmy wartość `1` do zmiennej o nazwie `x`.
Jeśli wyświetlimy zmienną `x`, otrzymamy liczbę `1`:
```kotlin
println(x) // prints 1
```

---

Zmienne są tak nazwane, ponieważ przechowywana przez nie wartość może się zmieniać.
Możemy zaktualizować `x` używając `=` i nadając mu nową wartość.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

Możemy też przypisywać zmiennym wartości innych zmiennych. Tutaj możemy przypisać zmiennej `y` wartość `x`
```kotlin
var x = 5
var y = x
println(y) // prints 5
```

---

Gdy aktualizujemy zmienną, zapomina ona swojej poprzedniej wartości. Tutaj możemy wyświetlić zmienną `x` dwa razy i zobaczyć, jak jej wartość się zmienia.
```kotlin
var x = 5
println(x) // prints 5
x = 10
println(x) // prints 10
```

---

W Kotlinie zmienne tekstowe można deklarować tylko przy użyciu podwójnych cudzysłowów:
```kotlin
val x = "May"
```

---

Jeśli chcemy, aby nazwa zmiennej składała się z wielu słów, używamy **camelCase**.
Jest to praktyka pisania fraz w taki sposób, że każde słowo w środku frazy zaczyna się wielką literą
