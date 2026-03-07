Kotlin posiada podstawowy typ Boolean, zwany `Boolean`.
Wartości boolowskie są nazywane logicznymi, ponieważ mogą być tylko prawdziwe lub fałszywe.
Możesz ocenić dowolne wyrażenie w Kotlin i uzyskać jedną z dwóch odpowiedzi: `true` lub `false`.

---

Możemy przechowywać wartość boolowską `true` w zmiennej, tak jak liczbę lub ciąg znaków.

---

Przeciwna wartość `true` to `false`

---

Wartości boolowskie można też negować, używając `!` przed nimi, np.:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

Możemy również tworzyć wyrażenia boolowskie przy użyciu `&&` (_i_) oraz `||` (_lub_):

- `&&` (_i_): daje true tylko wtedy, gdy wyrażenie boolowskie po lewej stronie operatora i to po prawej są oba prawdziwe.
- `||` (_lub_): daje true, jeśli wyrażenie po lewej lub prawej stronie operatora jest prawdziwe, albo oba są prawdziwe.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
