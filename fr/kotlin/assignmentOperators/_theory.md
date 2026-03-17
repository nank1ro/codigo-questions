Les opérateurs d'affectation sont utilisés pour affecter des valeurs aux variables.
L'opérateur d'affectation le plus basique est `=`, qui affecte la valeur à droite à la variable à gauche :
```kotlin
var x = 10
```
Ici, `10` est affecté à la variable `x`.
Vous pouvez également réaffecter une nouvelle valeur à une variable existante :
```kotlin
x = 20
```
Maintenant `x` contient la valeur `20`.

---

L'opérateur `+=` est un raccourci qui ajoute une valeur à une variable et réaffecte le résultat.
Au lieu d'écrire :
```kotlin
x = x + 5
```
Vous pouvez écrire :
```kotlin
x += 5
```
Les deux expressions font la même chose : elles augmentent la valeur de `x` de `5`.

---

L'opérateur `-=` soustrait une valeur d'une variable et réaffecte le résultat.
Au lieu d'écrire :
```kotlin
x = x - 3
```
Vous pouvez écrire :
```kotlin
x -= 3
```
Cela diminue la valeur de `x` de `3`.

---

L'opérateur `*=` multiplie une variable par une valeur et réaffecte le résultat.
Au lieu d'écrire :
```kotlin
x = x * 4
```
Vous pouvez écrire :
```kotlin
x *= 4
```
Cela multiplie `x` par `4` et stocke le résultat dans `x`.

---

L'opérateur `/=` divise une variable par une valeur et réaffecte le résultat.
Au lieu d'écrire :
```kotlin
x = x / 2
```
Vous pouvez écrire :
```kotlin
x /= 2
```
Remarque : lorsque les deux opérandes sont de type `Int`, Kotlin effectue une **division entière** (la partie fractionnaire est ignorée) :
```kotlin
var x = 7
x /= 2
// x vaut maintenant 3 (pas 3.5)
```
