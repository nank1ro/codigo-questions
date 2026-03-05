> Les ordinateurs sont idéaux pour les tâches répétitives.

La forme la plus basique de répétition utilise le mot-clé `while`.
Cela répète un bloc tant que l'expression _booléenne_ de contrôle est vraie:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
L'expression booléenne est évaluée une fois au début de la boucle et
à nouveau avant chaque itération supplémentaire à travers le bloc.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Ici, nous avons créé une variable `x`, en lui attribuant la valeur initiale de __3__.

Ensuite, nous avons utilisé l'instruction `while` qui exécutera le bloc de code jusqu'à ce que la condition `x > 0` soit `true`.

À l'intérieur du bloc de code, nous ne devons **PAS** oublier d'ajouter la ligne `x--`.
Elle décrémente la valeur de `x`, sinon, notre boucle sera infinie.

---

Analysons cet extrait de code.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Nous initialisons la variable `counter` à __0__.
- __[2]__: L'expression conditionnelle pour _while_ dit: "répétez les instructions du corps tant que le compteur est inférieur à _100_".
- __[3]__: L'opérateur `+=` ajoute _10_ à `counter` et assigne le résultat à `counter` en une seule opération.

La sortie du code ci-dessus est _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Il existe une deuxième façon d'utiliser _while_, en conjonction avec le mot-clé `do`.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
Comme vous pouvez le voir, la boucle `do-while` est très similaire à la boucle `while`, sauf pour une différence importante:
> le corps de la boucle est exécuté une fois avant l'évaluation de la condition.

En d'autres termes, le corps de la boucle `do-while` s'exécute toujours au moins une fois, même si l'expression de condition produit initialement `false`.

En revanche, le corps d'une boucle `while` ne s'exécutera jamais si la condition produit `false` la première fois.

---

La boucle _while_ supporte les trois expressions de saut structurel:
- `break` termine la boucle englobante la plus proche.
- `continue` passe à l'étape suivante de la boucle englobante la plus proche.
- `return` retourne par défaut de la fonction englobante la plus proche ou de la fonction anonyme (_nous verrons cela plus tard quand nous parlerons de fonctions_).

Voici un exemple d'utilisation de `continue` dans une boucle _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

Comme vous pouvez le voir au __[1]__ quand `i` est égal à _2_, nous sautons et _continuons_ à l'étape suivante. En fait, le nombre 2 ne s'imprime jamais.

---

Voici un exemple d'utilisation de `break` dans une boucle _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

Comme vous pouvez le voir au __[1]__ quand `i` est égal à _2_, nous _romperions_ la boucle. En fait, les nombres 2 et 3 ne s'impriment jamais.
