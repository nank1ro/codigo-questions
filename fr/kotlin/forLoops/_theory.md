> Le mot-clé `for` exécute un bloc de code pour chaque valeur dans une séquence.

La boucle `for` itère sur tout ce qui fournit un itérateur.

La syntaxe de `for` est la suivante :
```kotlin
for (item in collection) print(item)
```

Le corps de `for` peut aussi être un bloc
```kotlin
for (item in collection) {
    print(item)
}
```

À chaque passage de la boucle, `item` reçoit l'élément suivant dans les valeurs.

Voici une boucle `for` répétant une action un nombre fixe de fois :

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

La sortie montre l'index `i` recevant chaque valeur dans la plage de _1_ à _3_.

---

Une _plage_ est un intervalle de valeurs défini par une paire de points de terminaison.
Il y a deux façons de base de définir des plages :

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ l'utilisation de la syntaxe `..` inclut les deux limites dans la plage résultante.
- __[2]__ `until` exclut la fin. La sortie montre que _3_ n'est pas inclus dans la plage.

---

Vous pouvez parcourir une plage dans l'ordre inverse.

Vous vous attendrez probablement à ce que `3..1` fonctionne, malheureusement, l'équipe Kotlin a décidé d'importer cette fonctionnalité d'une manière différente.

En fait, si vous essayez d'exécuter cet extrait de code :
```kotlin
for (i in 3..1) println(i)
```

Vous verrez que rien n'est affiché.
Pour le faire fonctionner, nous devons utiliser le mot-clé `downTo` :

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` produit une plage décroissante.

---

Le _pas_ par défaut d'une plage est __1__, mais vous pouvez explicitement définir une autre valeur.

Vous pouvez définir le __pas__ de votre boucle `for` en utilisant le mot-clé `step`.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

Comme vous pouvez le voir, le bloc de code s'exécute avec un pas de _2_ au lieu de _1_, changeant complètement notre sortie.

---

Vous pouvez également produire une plage de _caractères_.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

You can iterate over a __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

In the example above we've printed each character + 1, so `'a'` becomes `'b'`, `'b'` becomes `'c'` and so on.

This is possibile because characters are stored as numbers corresponding to their [ASCII Codes](https://en.wikipedia.org/wiki/ASCII).

So adding an integer to a character produces a new character corresponding to the new code value.

---

In case you simply need to repeat a block of code `n` times, you can use the `repeat(times: Int)` function.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

You can even access the index with
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

In Kotlin we can use the `for-in` also for iterable collections calling the given closure on each element:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10) 
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

In Kotlin we have also the `forEach` loop.
It calls the given closure on each element in the sequence in the same order as a `for-in` loop:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9) 
numbers.forEach {
    println(it)
}
```

Using the `forEach` method is distinct from a `for-in` loop in two important ways:
1. The `break` or `continue` statement cannot be used to exit the current call of the body closure or to skip subsequent calls. (_Actually it is possible with annotations, but it's a bit more complex topic that we won't see now._)
2. Using the `return` statement in the body closure will only exit the closure and not the outer scope, and it won't skip subsequent calls.
