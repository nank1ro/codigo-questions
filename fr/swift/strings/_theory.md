Une **string** est un morceau de texte. En Swift, tu écris un littéral de string entre guillemets doubles, et son type est `String` :
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Comme pour toute autre valeur, `let` crée une constante qui ne peut pas être modifiée et `var` crée une variable qui le peut.
Swift déduit le type `String` à partir du littéral, donc l'annotation de type est facultative.

---

L'**interpolation de chaîne** insère la valeur d'une expression à l'intérieur d'un littéral de chaîne. Enveloppe l'expression dans `\()` :
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
N'importe quel type peut être interpolé : les nombres, les booléens et les autres chaînes sont tous automatiquement convertis en texte.

---

Deux chaînes peuvent être jointes avec l'opérateur `+`, qui produit une nouvelle chaîne :
```swift
let full = "Hello" + " " + "world" // Hello world
```
Pour ajouter du texte à la fin d'une variable de chaîne existante, utilise `+=`. La variable doit être déclarée avec `var`, car sa valeur change :
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

La propriété `count` renvoie le nombre de caractères d'une chaîne, et `isEmpty` vaut `true` quand la chaîne ne contient aucun caractère :
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Chaque caractère est compté, y compris les espaces et la ponctuation.

---

Une `String` est une collection de valeurs `Character`. Un `Character` est une seule lettre, un chiffre, un symbole ou un espace, et il s'écrit avec les mêmes guillemets doubles qu'une chaîne, donc tu as besoin d'une annotation de type pour en obtenir un :
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Vérifier `isEmpty` est préférable à comparer `count` à `0` : c'est plus lisible et cela n'a pas besoin de compter chaque caractère.

---

Un **littéral de string multiligne** commence et se termine par trois guillemets doubles `"""`, chacun sur sa propre ligne. Chaque ligne entre les deux fait partie de la chaîne, et les sauts de ligne sont conservés :
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
Cela affiche les deux lignes exactement telles qu'elles sont écrites. Les guillemets de fermeture `"""` déterminent aussi l'indentation : tout espace blanc avant eux est retiré du début de chaque ligne.

---

Puisqu'une chaîne est une collection de caractères, tu peux itérer dessus avec une boucle `for`-`in`. Chaque itération te donne un `Character` :
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
Un `Character` peut être comparé avec `==` à un littéral de caractère, donc compter combien de fois un caractère apparaît n'est qu'une boucle avec un compteur.

---

Contrairement aux tableaux, les chaînes ne peuvent pas être indexées avec un entier comme `text[2]` : certains caractères occupent plus de mémoire que d'autres, donc Swift utilise un type dédié `String.Index` pour désigner une position.
`startIndex` est la position du premier caractère et `endIndex` est la position *après* le dernier. Pour te déplacer à partir d'un index, utilise `index(_:offsetBy:)`, puis indexe la chaîne avec le résultat :
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Se déplacer au-delà de la fin de la chaîne plante à l'exécution, donc le décalage doit rester dans les limites de `count`.

---

Travailler avec des index est verbeux, donc Swift propose des raccourcis pour les cas les plus courants :
- `first` et `last` renvoient le premier et le dernier caractère sous forme de `Character?` optionnel (`nil` pour une chaîne vide)
- `prefix(n)` renvoie les `n` premiers caractères et `suffix(n)` les `n` derniers
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` et `suffix` renvoient une `Substring`, une vue sur le texte d'origine. Pour la stocker comme un vrai `String`, enveloppe-la dans `String(...)`. Si `n` est plus grand que `count`, tu obtiens simplement la chaîne entière.

---

Trois méthodes répondent aux questions les plus courantes sur le contenu d'une chaîne, et chacune renvoie un `Bool` :
- `contains(_:)` vaut `true` quand la chaîne contient le texte donné (ou le caractère) n'importe où
- `hasPrefix(_:)` vaut `true` quand la chaîne commence par le texte donné
- `hasSuffix(_:)` vaut `true` quand la chaîne se termine par le texte donné
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Les trois sont sensibles à la casse : `"Swift".hasPrefix("s")` vaut `false`.

---

Comme `contains`, `hasPrefix` et `hasSuffix` renvoient des booléens, ils se combinent naturellement avec `||` et `&&` pour construire des vérifications plus complexes.

---

`uppercased()` et `lowercased()` renvoient une **nouvelle** chaîne avec chaque lettre convertie en majuscule ou en minuscule. La chaîne d'origine n'est pas modifiée :
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Ce sont toutes les deux des méthodes, donc n'oublie pas les parenthèses.

---

Convertir en minuscules est la façon habituelle de comparer du texte en ignorant la casse : deux chaînes qui ne diffèrent que par la casse deviennent égales une fois que les deux sont converties en minuscules.

---

`split(separator:)` découpe une chaîne en un tableau de morceaux à chaque endroit où apparaît le caractère séparateur. `joined(separator:)` fait l'inverse : elle recolle les éléments d'un tableau en une seule chaîne, en plaçant le séparateur entre eux :
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Comme `prefix`, `split` renvoie des valeurs `Substring` ; enveloppe-en une dans `String(...)` si tu as besoin de la stocker comme un `String`.

---

Diviser sur un espace est la façon la plus simple de décomposer une phrase en mots, et joindre est la façon de reconstruire du texte à partir d'un tableau.

---

Le framework Foundation ajoute de nombreuses méthodes de chaîne supplémentaires. L'une des plus utiles est `replacingOccurrences(of:with:)`, qui renvoie une nouvelle chaîne où chaque occurrence du premier texte est remplacée par le second :
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
N'oublie pas de faire `import Foundation` en haut du fichier, sinon la méthode n'est pas disponible. Les appels de méthode peuvent être chaînés, donc `text.lowercased().replacingOccurrences(of: " ", with: "_")` est valide.

---

Les chaînes peuvent être comparées avec les mêmes opérateurs que les nombres. `==` vérifie que deux chaînes ont exactement les mêmes caractères, tandis que `<` et `>` les comparent par ordre alphabétique, caractère par caractère :
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
La comparaison est sensible à la casse, et chaque lettre majuscule vient **avant** chaque lettre minuscule, donc `"B" < "a"` vaut `true`.

---

Un `Character` n'est pas une `String`, donc il ne peut pas être joint directement à une chaîne avec `+`. Convertis-le d'abord avec `String(...)` :
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Combiner cela avec une boucle `for`-`in` te permet de reconstruire une chaîne caractère par caractère, par exemple en plaçant chaque nouveau caractère devant ceux déjà rassemblés.
