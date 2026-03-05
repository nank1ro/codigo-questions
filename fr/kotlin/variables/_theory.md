Les variables sont des conteneurs pour stocker les valeurs de données.
Chaque variable en Kotlin est un objet.
Pour créer une variable, nous devons lui donner un __nom__ en gardant à l'esprit qu'il ne doit pas contenir d'espaces.
Une variable est créée au moment où vous assignez une valeur pour la première fois.
En Kotlin, vous déclarez des constantes avec le mot-clé `val` (abréviation de _value_) et des variables avec le mot-clé `var` (abréviation de _variable_).
La valeur d'une constante ne peut pas être modifiée une fois qu'elle est définie, tandis qu'une variable peut être définie à une valeur différente à l'avenir.
Un exemple de création d'une variable nommée `x` est :
```kotlin
var x = 1
```
De cette façon, nous avons assigné la valeur `1` à la variable nommée `x`.
Si nous affichons la variable `x`, nous obtenons le nombre `1` :
```kotlin
println(x) // affiche 1
```

---

Les variables sont appelées de cette manière car la valeur qu'elles stockent peut changer.
We can update `x` by using `=` and giving it a new value.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

Nous pouvons également donner aux variables les valeurs d'autres variables. Ici, nous pouvons donner à la variable `y` la valeur de `x`
```kotlin
var x = 5
var y = x
println(y) // prints 5
```

---

Quand nous mettons à jour une variable, elle oublie sa valeur précédente. Ici, nous pouvons afficher la variable `x` deux fois et voir comment sa valeur se met à jour.
```kotlin
var x = 5
println(x) // prints 5
x = 10
println(x) // prints 10
```

---

En Kotlin, les variables de chaîne ne peuvent être déclarées qu'en utilisant des guillemets doubles :
```kotlin
val x = "May"
```

---

Si nous voulons un nom de variable avec plusieurs mots, nous utilisons **camelCase**.
C'est la pratique d'écrire des phrases de telle sorte que chaque mot au milieu de la phrase commence par une majuscule
