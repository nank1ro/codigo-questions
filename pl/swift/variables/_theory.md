Zmienne to kontenery do przechowywania wartości danych.
Każda zmienna w Swift jest obiektem.
Aby stworzyć zmienną, musimy nadać jej **nazwę**, pamiętając, że nie może zawierać spacji.
Zmienna jest tworzona w momencie pierwszego przypisania do niej wartości.
W Swift stałe deklaruje się za pomocą słowa kluczowego `let`, a zmienne za pomocą słowa kluczowego `var`.
Wartości stałej nie można zmienić po jej ustawieniu, natomiast zmienną można ustawić na inną wartość w przyszłości.
Przykład tworzenia zmiennej o nazwie `x`:
```swift
var x = 1
```
W ten sposób przypisaliśmy wartość `1` do zmiennej o nazwie `x`.
Jeśli wyświetlimy zmienną `x`, otrzymamy liczbę `1`:
```swift
print(x) // prints 1
```

---

Zmienne nazywane są w ten sposób, ponieważ wartość, którą przechowują, może się zmieniać.
Możemy zaktualizować `x` używając `=` i podając nową wartość.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

Możemy również przypisywać zmiennym wartości innych zmiennych. Tutaj możemy przypisać zmiennej `y` wartość `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

Kiedy aktualizujemy zmienną, zapomina ona poprzednią wartość. Tutaj możemy wyświetlić zmienną `x` dwa razy i zobaczyć, jak jej wartość się aktualizuje.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

W Swift zmienne tekstowe można deklarować tylko przy użyciu podwójnych cudzysłowów:
```swift
let x = "May"
```

---

Jeśli chcemy, aby nazwa zmiennej składała się z wielu słów, używamy **camelCase**.
Jest to praktyka pisania fraz w taki sposób, że każde słowo w środku frazy zaczyna się wielką literą
