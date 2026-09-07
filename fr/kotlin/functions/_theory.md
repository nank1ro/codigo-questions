Une fonction est un bloc de code qui effectue une tâche spécifique et peut être réutilisé dans tout votre programme.
En Kotlin, on définit une fonction avec le mot-clé `fun`, suivi du nom de la fonction et de parenthèses :
```kotlin
fun greet() {
    println("Hello!")
}
```
Pour appeler (exécuter) une fonction, utilisez son nom suivi de parenthèses :
```kotlin
greet() // prints Hello!
```
Une fonction qui ne retourne pas de valeur retourne implicitement `Unit`.

---

Les fonctions peuvent retourner une valeur. On spécifie le type de retour après les parenthèses avec deux-points :
```kotlin
fun getNumber(): Int {
    return 42
}
```
Le mot-clé `return` renvoie une valeur à l'appelant :
```kotlin
var result = getNumber()
println(result) // prints 42
```
Le type de retour doit correspondre au type de la valeur retournée.

---

Les fonctions peuvent accepter des paramètres, qui sont des entrées que vous passez lors de l'appel de la fonction.
Les paramètres sont déclarés à l'intérieur des parenthèses avec un nom et un type :
```kotlin
fun greet(name: String) {
    println("Hello, \$name!")
}
```
Vous passez des arguments lors de l'appel de la fonction :
```kotlin
greet("Alice") // prints Hello, Alice!
```
Les paramètres permettent d'écrire du code réutilisable qui fonctionne avec différentes valeurs.

---

Kotlin prend en charge les valeurs de paramètres par défaut. Si un appelant ne fournit pas d'argument, la valeur par défaut est utilisée :
```kotlin
fun greet(name: String = "World") {
    println("Hello, \$name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Les valeurs par défaut rendent les paramètres optionnels, réduisant le besoin de fonctions surchargées.

---

Lorsque le corps d'une fonction consiste en une seule expression, vous pouvez utiliser la syntaxe à expression unique avec `=` :
```kotlin
fun square(n: Int): Int = n * n
```
C'est plus concis que la forme à corps de bloc. Kotlin peut souvent inférer le type de retour, vous pouvez donc aussi écrire :
```kotlin
fun square(n: Int) = n * n
```
Les fonctions à expression unique sont un idiome Kotlin courant pour les calculs simples.

---

Les fonctions peuvent retourner des valeurs `Boolean`, ce qui est utile pour vérifier des conditions :
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Une fonction `Boolean` retourne soit `true` soit `false`.

---

Les fonctions peuvent avoir plusieurs paramètres de types différents :
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is \$name and I am \$age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Les arguments nommés vous permettent de passer des valeurs dans n'importe quel ordre en utilisant le nom du paramètre :
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Une fonction de base en Kotlin utilise le mot-clé `fun` suivi d'un nom et de parenthèses :
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Pour déclarer un type de retour pour une fonction, ajoutez deux-points et le type après les parenthèses :
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Un paramètre de fonction est déclaré avec un nom, deux-points et un type :
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Une fonction à expression unique utilise `=` au lieu d'un corps de bloc :
```kotlin
fun triple(n: Int) = n * 3
```
C'est l'abréviation de :
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
