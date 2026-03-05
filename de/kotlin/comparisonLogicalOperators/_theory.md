Beginnen wir mit dem **gleich**-Vergleichsoperator `==`.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke gleich sind, zum Beispiel:
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Fahren wir mit dem **nicht gleich**-Vergleichsoperator `!=` fort.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke **NICHT** gleich sind, zum Beispiel:
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
Es ist genau das Gegenteil des *gleich*-Operators

---

Fahren wir mit dem **größer als**-Vergleichsoperator `>` fort.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer als der andere ist, zum Beispiel:
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Fahren wir mit dem **kleiner als**-Vergleichsoperator `<` fort.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Fahren wir mit dem **größer als oder gleich**-Vergleichsoperator `>=` fort.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer als oder gleich dem anderen ist, zum Beispiel:
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Fahren wir mit dem **kleiner als oder gleich**-Vergleichsoperator `<=` fort.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als oder gleich dem anderen ist, zum Beispiel:
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Schauen wir uns jetzt die **logischen** Operatoren an, beginnen wir mit dem ersten, genannt __UND__ `&&`.
Er gibt den ersten Operanden zurück, der zu *false* ausgewertet wird, oder den letzten, wenn alle *true* sind.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Fahren wir mit dem **oder** `||` logischen Operator fort.
Er gibt den ersten Operanden zurück, der zu *true* ausgewertet wird, oder den letzten, wenn alle *false* sind.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Abschließend mit dem **nicht** `!` logischen Operator.
Er gibt einen booleschen Wert zurück, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
