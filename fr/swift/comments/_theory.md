Un **commentaire** est une note écrite dans le code source pour les personnes qui le lisent. Le compilateur ignore complètement les commentaires, ils ne changent donc jamais ce que fait le programme.

Le commentaire le plus simple est le **commentaire sur une seule ligne** : il commence par `//` et s'étend jusqu'à la fin de la ligne.
```swift
// Greets the user
print("Hello")
```
Utilise les commentaires pour expliquer à quoi sert un morceau de code, ou pourquoi il a été écrit de cette façon.

---

Un commentaire n'a pas besoin de sa propre ligne : il peut suivre le code sur la même ligne. C'est un **commentaire en fin de ligne**, et c'est un bon endroit pour une courte note à propos de cette instruction précise :
```swift
let retries = 3 // give up after three attempts
```
Tout ce qui va de `//` jusqu'à la fin de la ligne est ignoré, tandis que le code qui le précède s'exécute normalement.

---

Comme le compilateur supprime complètement les commentaires, ajouter ou supprimer un commentaire ne change jamais ce que fait un programme. Seul le code qui n'est **pas** commenté s'exécute.

Cela fait de `//` un moyen rapide de désactiver une ligne de code sans la supprimer. Cela s'appelle **mettre en commentaire** :
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
La deuxième ligne est maintenant un commentaire, donc `total` reste `10`. Enlever le `//` redonne vie à la ligne.

Mettre en commentaire est pratique quand tu fais des essais, mais pense à nettoyer : du code qui reste en commentaire longtemps ne fait qu'embrouiller celui qui le lira ensuite.

---

Quand un commentaire a besoin de plusieurs lignes, Swift propose le **commentaire multiligne** (aussi appelé commentaire de bloc) : il commence par `/*` et se termine par `*/`, et tout ce qui se trouve entre les deux est ignoré, y compris les sauts de ligne.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Un commentaire de bloc peut aussi être court et tenir sur une seule ligne : `/* like this */`.

---

Contrairement à `//`, qui s'arrête à la fin de la ligne, un commentaire `/*` ne s'arrête qu'au `*/`. Si tu oublies de le fermer, le compilateur traite tout le code qui suit comme faisant partie du commentaire et signale une erreur :
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
`//` et `/* */` fonctionnent tous les deux comme commentaires en fin de ligne, mais avec `/*` assure-toi toujours que le `*/` est bien là.

---

Dans beaucoup de langages, les commentaires de bloc ne peuvent pas contenir d'autres commentaires de bloc, mais en Swift ils **peuvent être imbriqués** : chaque `/*` doit être refermé par son propre `*/`, et le commentaire ne se termine que lorsque le plus extérieur est fermé.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Ici `still a comment */` fait partie du commentaire extérieur, donc seul `done` est affiché. C'est ce qui permet de mettre en commentaire tout un bloc de code même quand ce bloc contient déjà un commentaire `/* */`.

---

Pour mettre plusieurs lignes en commentaire d'un coup, enveloppe-les dans un seul commentaire de bloc au lieu d'ajouter `//` à chaque ligne :
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Grâce à l'imbrication, cela fonctionne même quand l'une de ces lignes contient déjà un commentaire `/* */`.

---

Un usage courant des commentaires de bloc est le **commentaire d'en-tête** : un court bloc placé directement au-dessus d'une fonction qui dit ce qu'elle fait et ce que signifient ses paramètres.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Celui qui appelle `toSeconds` peut maintenant lire l'en-tête au lieu du corps. Garde l'en-tête à côté de la fonction pour qu'ils soient mis à jour ensemble.

---

Swift possède un troisième type de commentaire, le **commentaire de documentation** : un commentaire sur une seule ligne qui commence par `///` (trois barres obliques) et qui est placé directement au-dessus d'une fonction, d'un type ou d'une propriété.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Pour le compilateur ce n'est qu'un commentaire, mais des outils comme Xcode le lisent et l'affichent comme texte d'aide pour `greet`. Les commentaires de documentation prennent en charge **Markdown**, tu peux donc utiliser des accents graves pour le code, `**bold**` et les listes.

---

La première ligne d'un commentaire de documentation est le **résumé** : une courte phrase qui dit ce que fait la fonction. Écris-la à la troisième personne, comme si tu décrivais la fonction : « Returns... », « Adds... », « Checks... ».
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
Le commentaire doit se trouver juste au-dessus de la déclaration, sans ligne vide entre les deux, sinon Xcode ne l'attache pas à la fonction.

---

Les commentaires de documentation existent aussi sous forme de bloc : `/**` l'ouvre et `*/` le ferme, exactement comme un commentaire multiligne mais avec un deuxième astérisque au début.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` et `/** text */` signifient la même chose pour les outils ; `///` est le choix le plus courant dans le code Swift, tandis que `/** */` est pratique pour les longues descriptions. Un simple commentaire `/* */` ou `//` n'est **pas** de la documentation, même placé au-dessus d'une fonction.

---

Après le résumé, un commentaire de documentation peut décrire les paramètres et la valeur de retour avec des éléments de liste Markdown spéciaux que Xcode reconnaît :
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
L'ordre est toujours le même : le résumé d'abord, puis `- Parameter name:` pour chaque paramètre, puis `- Returns:`.

---

Certains commentaires suivent une convention que les éditeurs comprennent. En Swift les **marqueurs** les plus courants sont :
- `// MARK: - Title` étiquette une section du fichier, elle apparaît donc dans le menu de navigation de Xcode
- `// TODO: ...` signale quelque chose qui reste encore à écrire
- `// FIXME: ...` signale du code connu pour être faux et qui doit être corrigé

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Pour le compilateur ce sont des commentaires ordinaires ; Xcode les liste pour que le travail en attente soit facile à trouver. Une fois le travail fait, supprime le marqueur : un `TODO` périmé est trompeur.

---

Un `TODO` se trouve généralement à côté d'un placeholder qui garde le code compilable jusqu'à ce que la vraie implémentation soit écrite. Quand tu termines le travail, remplace le placeholder et supprime le marqueur dans la même modification, pour que le commentaire ne mente jamais sur l'état du code.

---

Un `FIXME` est différent d'un `TODO` : le code existe déjà, mais il est connu pour être faux. Un bon `FIXME` dit quel est le bug et, quand c'est possible, donne un exemple qui le montre, pour que la personne suivante puisse le corriger rapidement. Comme pour `TODO`, supprime le marqueur une fois le bug corrigé, mais garde le commentaire de documentation, qui reste vrai.

---

Un bon commentaire explique **pourquoi** le code fait quelque chose, pas **ce** qu'il fait. Le code montre déjà ce qui se passe ; le redire avec des mots ajoute du bruit et devient obsolète dès que le code change :
```swift
// set timeout to 30
let timeout = 30
```
La raison derrière le nombre est ce qu'un lecteur ne peut pas deviner :
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Si un commentaire ne fait que répéter la ligne en dessous, supprime-le ou remplace-le par la raison.
