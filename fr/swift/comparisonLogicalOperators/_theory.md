Commençons par l'opérateur de comparaison **égal** `==`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Continuons avec l'opérateur de comparaison **non égal** `!=`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si deux expressions ne sont **pas** égales, par exemple :
```swift
print(2 != 2) // false
print(2 != 3) // true
```
C'est exactement le contraire de l'opérateur *égal*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Continuons avec l'opérateur de comparaison **inférieur ou égal à** `<=`.
Il retourne une **valeur booléenne** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Maintenant, voyons les opérateurs **logiques**, commençons par le premier appelé **ET** `&&`.
Il retourne le premier opérande qui s'évalue à *false* ou le dernier si tous sont *true*.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il retourne le premier opérande qui s'évalue à *true* ou le dernier si tous sont *false*.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Terminons par l'opérateur logique **non** `!`.
Il retourne une valeur booléenne qui est l'inverse de l'état logique d'une expression.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
