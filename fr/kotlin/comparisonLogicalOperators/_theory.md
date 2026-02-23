Commençons par l'opérateur de comparaison d'**égalité** `==`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

Continuons avec l'opérateur de comparaison de **différence** `!=`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si deux expressions ne sont **PAS** égales, par exemple :
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
C'est exactement l'opposé de l'opérateur d'*égalité*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

Continuons avec l'opérateur de comparaison **inférieur ou égal à** `<=`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

Voyons maintenant les opérateurs **logiques**, commençons par le premier appelé __ET__ `&&`.
Il renvoie le premier opérande qui évalue à *false* ou le dernier si tous sont *true*.
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il renvoie le premier opérande qui évalue à *true* ou le dernier si tous sont *false*.
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

Terminons avec l'opérateur logique **non** `!`.
Il renvoie un booléen qui est l'inverse de l'état logique d'une expression.
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
