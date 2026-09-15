Kotlin a un type Boolean basique, appelé `Boolean`.
Les valeurs Boolean sont appelées logiques, car elles ne peuvent être que vrai ou faux.
Vous pouvez évaluer n'importe quelle expression en Kotlin, et obtenir l'une de deux réponses, `true` ou `false`.

---

Nous pouvons stocker la valeur booléenne `true` dans une variable tout comme un nombre ou une chaîne de caractères.

---

La valeur opposée de `true` est `false`

---

Les valeurs booléennes peuvent également être niées en utilisant le `!` avant elles, par exemple :
```kotlin
println(!true) // affiche false
println(!false) // affiche true
```

---

Nous pouvons également créer des expressions booléennes en utilisant le `&&` (_and_) et le `||` (_or_) :

- `&&` (_and_) : produit vrai seulement si l'expression Boolean à gauche de l'opérateur et celle à droite sont toutes deux vraies.
- `||` (_or_) : Produit vrai si l'expression à gauche ou à droite de l'opérateur est vraie, ou si les deux sont vraies.

```kotlin
println(true && true) // affiche true
println(true && false) // affiche false
println(false && false) // affiche false
println(true || true) // affiche true
println(true || false) // affiche true
println(false || false) // affiche false
```
