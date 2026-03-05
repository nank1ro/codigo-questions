Les variables sont des conteneurs pour stocker des valeurs.
Chaque variable en Swift est un objet.
Pour créer une variable, nous devons lui donner un **nom** en gardant à l'esprit qu'il ne doit pas contenir d'espaces.
Une variable est créée au moment où vous lui assignez une valeur pour la première fois.
En Swift, vous déclarez des constantes avec le mot-clé `let` et des variables avec le mot-clé `var`.
La valeur d'une constante ne peut pas être modifiée une fois qu'elle est définie, tandis qu'une variable peut être définie à une valeur différente à l'avenir.
Un exemple de création d'une variable nommée `x` est :
```swift
var x = 1
```
De cette façon, nous avons assigné la valeur `1` à la variable nommée `x`.
Si nous affichons la variable `x`, nous obtenons le nombre `1` :
```swift
print(x) // prints 1
```

---

Les variables sont appelées de cette façon parce que la valeur qu'elles stockent peut changer.
Nous pouvons mettre à jour `x` en utilisant `=` et en lui donnant une nouvelle valeur.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

Nous pouvons aussi donner aux variables les valeurs d'autres variables. Ici, nous pouvons donner à la variable `y` la valeur de `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

Quand nous mettons à jour une variable, elle oublie sa valeur précédente. Ici, nous pouvons afficher la variable `x` deux fois et voir comment sa valeur se met à jour.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

En Swift, les variables de chaîne peuvent être déclarées uniquement en utilisant des guillemets doubles :
```swift
let x = "May"
```

---

Si nous voulons un nom de variable avec plusieurs mots, nous utilisons **camelCase**.
C'est la pratique d'écrire des phrases de sorte que chaque mot au milieu de la phrase commence par une lettre majuscule
