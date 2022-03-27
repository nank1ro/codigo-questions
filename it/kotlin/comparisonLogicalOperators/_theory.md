Iniziamo con l'operatore di comparazione **uguale** `==`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni sono uguali, ad esempio:
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Continuiamo con l'operatore di comparazione **non uguale** `!=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni **NON** sono uguali, ad esempio:
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
E' esattamente l'opposto dell'operatore *uguale*

---

Continuiamo con l'operatore di comparazione **maggiore di** `>`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore dell'altra, per esempio:
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Continuiamo con l'operatore di comparazione **minore di** `<`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore dell'altra, per esempio:
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Continuiamo con l'operatore di comparazione **maggiore di o uguale a** `>=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore o uguale all'altra, per esempio:
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Continuiamo con l'operatore di comparazione **minore di o uguale a** `<=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore o uguale all'altra, per esempio:
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Ora vediamo gli operatori **logici**, iniziamo con il primo chiamato __AND__ `&&`.
L'operatore restituisce il primo operando che e' uguale a *false* o l'ultimo se tutti sono *true*.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Continuiamo con l'operatore logico **or** `||`.
L'operatore restituisce il primo operando che e' uguale a *true* o l'ultimo se tutti sono *false*.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Concludiamo con l'operatore logico **not** `!`.
L'operatore restituisce un valore booleano che e' il contrario dello stato logico di un'espressione.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
