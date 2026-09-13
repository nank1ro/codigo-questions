Un **commentaire** est une note écrite à l'intérieur du code source pour les personnes qui le lisent. Le compilateur ignore complètement les commentaires, ils ne changent donc jamais ce que fait le programme.

Le commentaire le plus simple est le **commentaire sur une seule ligne** : il commence par `//` et va jusqu'à la fin de la ligne.
```kotlin
// Greets the user
println("Hello")
```
Utilisez les commentaires pour expliquer à quoi sert un morceau de code, ou pourquoi il a été écrit de cette manière.

---

Un commentaire n'a pas besoin d'une ligne à lui : il peut suivre le code sur la même ligne. C'est un **commentaire de fin de ligne**, et c'est un bon endroit pour une courte note sur cette instruction précise :
```kotlin
val retries = 3 // give up after three attempts
```
Tout ce qui va de `//` jusqu'à la fin de la ligne est ignoré, tandis que le code qui le précède s'exécute normalement.

---

Comme le compilateur supprime complètement les commentaires, ajouter ou supprimer un commentaire ne change jamais ce que fait un programme. Seul le code qui n'est **pas** commenté s'exécute.

Cela fait de `//` un moyen rapide de désactiver une ligne de code sans la supprimer : on appelle cela **mettre en commentaire**.
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
La deuxième ligne est maintenant un commentaire, donc `total` reste `10`. Retirer le `//` la remet en vie.

Mettre du code en commentaire est pratique pendant que vous expérimentez, mais pensez à faire le ménage : du code qui reste en commentaire longtemps ne fait qu'embrouiller la personne qui le lira ensuite.

---

Quand un commentaire a besoin de plus d'une ligne, Kotlin propose le **commentaire multiligne** (aussi appelé commentaire de bloc) : il commence par `/*` et se termine par `*/`, et tout ce qui se trouve entre les deux est ignoré, y compris les retours à la ligne.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Un commentaire de bloc peut aussi être court et tenir sur une seule ligne : `/* like this */`.

---

Contrairement à `//`, qui s'arrête à la fin de la ligne, un commentaire `/*` ne s'arrête qu'au `*/`. Si vous oubliez de le fermer, le compilateur considère tout le code qui suit comme faisant partie du commentaire et signale une erreur :
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
`//` et `/* */` fonctionnent tous les deux comme commentaires de fin de ligne, mais avec `/*` assurez-vous toujours que le `*/` est bien là.

---

En Java un commentaire de bloc ne peut pas en contenir un autre, mais en Kotlin ils **peuvent être imbriqués** : chaque `/*` doit être fermé par son propre `*/`, et le commentaire ne se termine que lorsque le plus externe est fermé.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Ici `still a comment */` fait partie du commentaire externe, donc seul `done` est affiché. C'est ce qui permet de mettre en commentaire tout un bloc de code même quand ce bloc contient déjà un commentaire `/* */`.

---

Pour mettre plusieurs lignes en commentaire d'un coup, entourez-les d'un seul commentaire de bloc au lieu d'ajouter `//` à chaque ligne :
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
Grâce à l'imbrication, cela fonctionne même quand l'une de ces lignes contient déjà un commentaire `/* */`.

---

Une utilisation courante des commentaires de bloc est le **commentaire d'en-tête** : un court bloc placé juste au-dessus d'une fonction qui dit ce qu'elle fait et ce que signifient ses paramètres.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Celui qui appelle `toSeconds` peut maintenant lire l'en-tête au lieu du corps. Gardez l'en-tête à côté de la fonction pour qu'ils soient mis à jour ensemble.

---

Kotlin possède un troisième type de commentaire, le **commentaire de documentation**, écrit dans un format appelé **KDoc** : il commence par `/**` (une barre oblique et deux astérisques) et se termine par `*/`, et il se place juste au-dessus d'une fonction, d'une classe ou d'une propriété.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Pour le compilateur ce n'est qu'un commentaire, mais des outils comme IntelliJ IDEA le lisent et l'affichent comme texte d'aide pour `greet`. L'`*` au début des lignes internes n'est qu'une convention qui garde le bloc aligné. Dans KDoc vous pouvez utiliser du Markdown, et les crochets comme `[name]` deviennent des liens vers ce paramètre.

---

La première ligne d'un commentaire de documentation est le **résumé** : une courte phrase qui dit ce que fait la fonction. Écrivez-la à la troisième personne, comme si vous décriviez la fonction : "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
Le commentaire doit se trouver juste au-dessus de la déclaration, sans aucune autre instruction entre les deux, sinon les outils ne l'associent pas à la fonction.

---

Après le résumé, un commentaire de documentation peut décrire les paramètres et la valeur renvoyée avec les **balises KDoc**, qui commencent toujours par `@` :
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` est suivi du nom du paramètre puis de sa description ; il y a un `@param` par paramètre. `@return` décrit la valeur que la fonction renvoie. L'ordre est toujours le même : le résumé d'abord, puis les balises `@param`, puis `@return`.

---

Une fonction avec plus d'un paramètre reçoit une balise `@param` pour chacun d'eux, écrites dans le même ordre que les paramètres :
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Une balise n'est toujours qu'un commentaire : si vous renommez un paramètre et que vous oubliez la balise, rien ne casse, mais la documentation se met à mentir. Mettez à jour le KDoc en même temps que la signature.

---

Le compilateur ne cherche les commentaires que dans le code, jamais à l'intérieur d'une **chaîne de caractères**. Entre guillemets doubles, `//` et `/* */` sont des caractères ordinaires :
```kotlin
println("50 // 2") // prints 50 // 2
```
Le premier `//` fait partie du texte, le second commence un vrai commentaire. Cela surprend le plus souvent avec les adresses web, qui contiennent `//` juste après le protocole.

---

Certains commentaires suivent une convention que les éditeurs comprennent. Les **marqueurs** les plus courants sont :
- `// TODO: ...` signale quelque chose qui reste à écrire
- `// FIXME: ...` signale du code dont on sait qu'il est faux et qui doit être corrigé

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
Pour le compilateur ce sont des commentaires ordinaires ; IntelliJ IDEA les rassemble dans une fenêtre dédiée pour retrouver facilement le travail en attente. Un `TODO` se trouve souvent à côté d'un bouchon qui garde le code compilable jusqu'à ce que la vraie implémentation soit écrite. Quand vous terminez le travail, remplacez le bouchon et supprimez le marqueur dans le même changement, pour que le commentaire ne mente jamais sur l'état du code.

---

Un `FIXME` est différent d'un `TODO` : le code existe déjà, mais on sait qu'il est faux. Un bon `FIXME` dit quel est le bug et, si possible, donne un exemple qui le montre, pour que la personne suivante puisse le corriger vite. Comme pour `TODO`, supprimez le marqueur une fois le bug corrigé, mais gardez le commentaire de documentation, qui reste vrai.

---

Un bon commentaire explique **pourquoi** le code fait quelque chose, pas **ce qu'il** fait. Le code montre déjà ce qui se passe ; le répéter avec des mots ajoute du bruit et devient faux dès que le code change :
```kotlin
// set timeout to 30
val timeout = 30
```
La raison derrière ce nombre est ce qu'un lecteur ne peut pas deviner :
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
Si un commentaire ne fait que répéter la ligne en dessous, supprimez-le ou remplacez-le par la raison. Les meilleurs commentaires sont ceux qui disent quelque chose que le code ne peut pas dire.
