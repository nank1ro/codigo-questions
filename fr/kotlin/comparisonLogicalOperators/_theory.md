Commençons par l'opérateur de comparaison **égal** `==`.
Il retourne un **boolean** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Continuons avec l'opérateur de comparaison **pas égal** `!=`.
Il retourne un **boolean** (`true` ou `false`) indiquant si deux expressions ne sont **PAS** égales, par exemple :
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
C'est exactement l'opposé de l'opérateur *égal*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il retourne un **boolean** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il retourne un **boolean** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il retourne un **boolean** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Continuons avec l'opérateur de comparaison **inférieur ou égal à** `<=`.
Il retourne un **boolean** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Maintenant, voyons les opérateurs **logiques**, commençons par le premier appelé __ET__ `&&`.
Il retourne le premier opérande qui s'évalue à *false* ou le dernier s'ils sont tous *true*.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il retourne le premier opérande qui s'évalue à *true* ou le dernier s'ils sont tous *false*.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Terminons avec l'opérateur logique **non** `!`.
Il retourne un boolean qui est l'inverse de l'état logique d'une expression.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
