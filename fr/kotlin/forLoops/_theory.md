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

Vous pouvez itérer sur une __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

Dans l'exemple ci-dessus, nous avons affiché chaque caractère + 1, donc `'a'` devient `'b'`, `'b'` devient `'c'` et ainsi de suite.

Cela est possible car les caractères sont stockés sous forme de nombres correspondant à leurs [codes ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange).

Ainsi, ajouter un entier à un caractère produit un nouveau caractère correspondant à la nouvelle valeur de code.

---

Si vous avez simplement besoin de répéter un bloc de code `n` fois, vous pouvez utiliser la fonction `repeat(times: Int)`.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

Vous pouvez même accéder à l'index avec
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

En Kotlin, nous pouvons utiliser le `for-in` également pour les collections itérables en appelant la closure donnée sur chaque élément :
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

En Kotlin, nous avons aussi la boucle `forEach`.
Elle appelle la closure donnée sur chaque élément de la séquence dans le même ordre qu'une boucle `for-in` :

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

L'utilisation de la méthode `forEach` se distingue d'une boucle `for-in` de deux manières importantes :
1. L'instruction `break` ou `continue` ne peut pas être utilisée pour sortir de l'appel en cours de la closure du corps ou pour ignorer les appels suivants. (_En fait, c'est possible avec des annotations, mais c'est un sujet un peu plus complexe que nous ne verrons pas maintenant._)
2. L'utilisation de l'instruction `return` dans la closure du corps ne sortira que de la closure et non de la portée extérieure, et elle n'ignorera pas les appels suivants.
