Zacznijmy od operatora porównania **równości** `==`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia są równe, na przykład:
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Kontynuujmy z operatorem porównania **nierówności** `!=`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy dwa wyrażenia **NIE** są równe, na przykład:
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
Jest to dokładne przeciwieństwo operatora *równości*

---

Kontynuujmy z operatorem porównania **większy niż** `>`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe od drugiego, na przykład:
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Kontynuujmy z operatorem porównania **mniejszy niż** `<`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Kontynuujmy z operatorem porównania **większy lub równy** `>=`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Kontynuujmy z operatorem porównania **mniejszy lub równy** `<=`.
Zwraca on **wartość logiczną** (`true` lub `false`) określającą, czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Teraz poznajmy operatory **logiczne**, zacznijmy od pierwszego o nazwie __AND__ `&&`.
Zwraca on pierwszy operand, który ma wartość *false*, lub ostatni, jeśli wszystkie są *true*.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Kontynuujmy z logicznym operatorem **lub** `||`.
Zwraca on pierwszy operand, który ma wartość *true*, lub ostatni, jeśli wszystkie są *false*.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Zakończmy z logicznym operatorem **negacji** `!`.
Zwraca on wartość logiczną będącą odwróceniem stanu logicznego wyrażenia.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
