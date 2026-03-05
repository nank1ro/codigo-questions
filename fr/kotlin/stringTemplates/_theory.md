Un _modèle_ de chaîne est un moyen programmatique de générer une chaîne.
En Kotlin, nous pouvons utiliser le signe `+` (concaténation) pour afficher deux chaînes ou plus ensemble, comme :
```kotlin
println("Hello " + "Kotlin!")
// affiche "Hello Kotlin!"
```

---

Mais utiliser le signe `+` pour ajouter un nombre comme '10' à une chaîne comme ` "friends"` produit une erreur car ce sont des valeurs d'un type différent

---

Les modèles de chaînes nous permettent d'afficher des expressions comme l'ajout d'une chaîne à un nombre, sans aucune erreur.
La mise d'une expression à l'intérieur `${}` l'évalue.
La valeur de retour est convertie en chaîne et insérée dans la chaîne résultante

---

Si vous mettez un $ avant un nom d'identificateur, le modèle de chaîne insérera le contenu de cet identificateur dans la chaîne

---

Si ce qui suit le signe `$` n'est pas reconnaissable comme un identificateur de programme, rien de spécial ne se passe

---

Nous pouvons également insérer des variables après les signes dollar pour afficher leur valeur

---

Nous pouvons utiliser des accolades pour insérer des valeurs aussi souvent que nous le souhaitons dans les modèles de chaînes

---

À l'intérieur du `${}` nous pouvons également mettre des conditions, par exemple :
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// affiche Correct
```

---

Les modèles de chaînes sont mieux utilisés dans les instructions d'impression, mais nous pouvons également les stocker dans des variables comme des chaînes normales.
