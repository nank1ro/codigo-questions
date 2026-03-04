Comencemos con el operador de comparación **igual** `==`.
Devuelve un **booleano** (`true` o `false`) indicando si dos expresiones son iguales, por ejemplo:
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Continuemos con el operador de comparación **no igual** `!=`.
Devuelve un **booleano** (`true` o `false`) indicando si dos expresiones **NO** son iguales, por ejemplo:
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
Es exactamente lo opuesto al operador *igual*

---

Continuemos con el operador de comparación **mayor que** `>`.
Devuelve un **booleano** (`true` o `false`) indicando si una expresión es mayor que la otra, por ejemplo:
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Continuemos con el operador de comparación **menor que** `<`.
Devuelve un **booleano** (`true` o `false`) indicando si una expresión es menor que la otra, por ejemplo:
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Continuemos con el operador de comparación **mayor que o igual a** `>=`.
Devuelve un **booleano** (`true` o `false`) indicando si una expresión es mayor que o igual a la otra, por ejemplo:
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Continuemos con el operador de comparación **menor que o igual a** `<=`.
Devuelve un **booleano** (`true` o `false`) indicando si una expresión es menor que o igual a la otra, por ejemplo:
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Ahora veamos los operadores **lógicos**, comencemos con el primero llamado __Y__ `&&`.
Devuelve el primer operando que se evalúa como *false* o el último si todos son *true*.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Continuemos con el operador lógico **o** `||`.
Devuelve el primer operando que se evalúa como *true* o el último si todos son *false*.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Terminemos con el operador lógico **no** `!`.
Devuelve un booleano que es el inverso del estado lógico de una expresión.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
