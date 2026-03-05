La prise de décision est nécessaire lorsque nous voulons exécuter du code seulement si une certaine condition est satisfaite.
Supposons que nous voulons jouer dehors seulement si le temps est beau.
En programmation, nous pouvons sauvegarder une variable booléenne `niceWeather` et effectuer l'action de jouer dehors `if` cette variable est `true`, comme :
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

Continuons avec l'exemple précédent.
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
Nous avons vu que la déclaration `if` exécute le bloc de code seulement si la condition est `true`.
Une autre chose importante à considérer est représentée par les **accolades** `{}` qui indiquent un bloc de code.

---

Nous venons de voir comment exécuter un bloc de code si une condition se produit, maintenant voyons comment exécuter un autre bloc de code si la première condition échoue.
Nous jouons dehors si le temps est beau ; sinon, nous restons à la maison.
En Kotlin, nous pouvons utiliser la déclaration `else`, comme :
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Supposons que nous ayons une autre condition à vérifier, comme dans cet exemple :
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
et la sortie de ce code est `the number is 3`.
D'abord, vérifions si le nombre est égal à 2, c'est faux.
Passons ensuite à la deuxième déclaration et vérifions si `num` est égal à 3, étant vrai, nous exécutons le bloc de code suivant en imprimant `the number is 3`

---

Nous pouvons ajouter autant de déclarations `else if` que nous voulons, il n'y a pas de limites
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
et la sortie de ce code est `the number is 4`.

---

On peut aussi imbriquer une instruction conditionnelle (`if`, `else if` ou `else`) à l'intérieur d'une autre instruction conditionnelle, pour créer une structure plus complexe.
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
et la sortie de ce code est `the number is 4`.

---

L'_opérateur elvis_ `a ?: b` déballe un optionnel `a` s'il contient une valeur, ou renvoie une valeur par défaut `b` si `a` est `null`.
L'expression `a` est toujours d'un type optionnel.
L'expression `b` doit correspondre au type stocké dans a.
L'opérateur elvis est un raccourci pour le code ci-dessous :
```kotlin
if (a != null) a else b
```
