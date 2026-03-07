Zacznijmy od operatora porównania **równości** `==`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są równe, na przykład:
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Przejdźmy do operatora porównania **nierówności** `!=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są **RÓŻNE**, na przykład:
```swift
print(2 != 2) // false
print(2 != 3) // true
```
Jest to dokładne przeciwieństwo operatora *równości*

---

Przejdźmy do operatora porównania **większy niż** `>`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe od drugiego, na przykład:
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Przejdźmy do operatora porównania **mniejszy niż** `<`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Przejdźmy do operatora porównania **większy lub równy** `>=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Przejdźmy do operatora porównania **mniejszy lub równy** `<=`.
Zwraca on wartość **logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Teraz poznajmy operatory **logiczne** — zacznijmy od pierwszego o nazwie __AND__ `&&`.
Zwraca on pierwszy operand, który przyjmuje wartość *false*, lub ostatni, jeśli wszystkie mają wartość *true*.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Przejdźmy do operatora logicznego **lub** `||`.
Zwraca on pierwszy operand, który przyjmuje wartość *true*, lub ostatni, jeśli wszystkie mają wartość *false*.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Zakończmy operatorem logicznym **negacji** `!`.
Zwraca on wartość logiczną będącą odwrotnością stanu logicznego wyrażenia.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
