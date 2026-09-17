Une **chaîne formatée** est un morceau de texte dont certaines parties sont remplies avec des valeurs à l'exécution : un prix, un nom, un score. Swift te donne deux outils pour cela.

La première est l'**interpolation de chaîne**, que tu connais déjà : tout ce qui est écrit à l'intérieur de `\( )` est évalué et inséré dans le texte. Cela n'a pas besoin d'être une variable, cela peut être n'importe quelle expression :
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
L'interpolation est le moyen le plus rapide de construire une chaîne, mais elle affiche les nombres exactement comme Swift les stocke : `3.5` reste `3.5`, jamais `3.50`. Pour un contrôle total sur les chiffres, la largeur et le remplissage, nous utiliserons `String(format:)`, présenté dans le prochain exercice.

---

Le second outil est `String(format:)`, qui vient du framework **Foundation**, donc le fichier doit commencer par `import Foundation`.

Il prend une **chaîne de format** suivie des valeurs à insérer. À l'intérieur de la chaîne de format, un **spécificateur** commençant par `%` marque où va chaque valeur et comment elle est écrite. Le spécificateur pour un entier est `%d` :
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` renvoie une `String` normale, donc tu peux l'afficher, la stocker ou la renvoyer depuis une fonction.

---

Pour les nombres décimaux (`Double`), le spécificateur est `%f`. À lui seul, il affiche toujours six chiffres après le point décimal :
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Pour choisir le nombre de décimales que tu veux, écris un point et un nombre entre `%` et `f`. C'est la **précision**, et la valeur est arrondie en conséquence :
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` est le choix habituel pour les prix, car il affiche toujours exactement deux décimales.

---

Un nombre entre `%` et la lettre définit la **largeur minimale** du champ. Si la valeur est plus courte, des espaces sont ajoutés à gauche pour qu'elle soit **alignée à droite** ; si elle est plus longue, rien n'est coupé :
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
La largeur et la précision se combinent : `%8.2f` signifie "au moins 8 caractères de large, avec 2 décimales" :
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Ce sont les largeurs fixes qui alignent les colonnes d'un tableau.

---

Par défaut, le remplissage se fait à gauche. Un signe moins juste après `%` met le remplissage à droite, si bien que la valeur est **alignée à gauche** :
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
Le signe moins est un **drapeau** : il change la façon dont le champ est rempli sans changer la largeur.

---

Un autre drapeau est `0` : au lieu d'espaces, le champ est rempli de zéros à gauche. C'est ainsi que tu obtiens des nombres comme `007` ou `00042` :
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Comme avec les espaces, une valeur plus longue que la largeur n'est jamais coupée.

---

Une chaîne de format peut contenir autant de spécificateurs que tu veux. Les valeurs suivent dans le même ordre, séparées par des virgules, et chacune doit correspondre au type de son spécificateur : `%d` pour un `Int`, `%f` pour un `Double` :
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Passer un `Double` à `%d` (ou un `Int` à `%f`) compile, mais affiche un nombre sans signification, donc vérifie toujours que les spécificateurs et les valeurs correspondent.

---

Les entiers peuvent aussi s'écrire dans d'autres bases. `%x` affiche la valeur en **hexadécimal** avec des lettres minuscules, `%X` avec des lettres majuscules, et `%o` en octal :
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
La largeur et le drapeau `0` fonctionnent ici aussi : `%02x` est la façon classique d'écrire un octet d'une couleur, comme dans `#ff8000`.

---

Pour insérer une `String` dans une chaîne de format, utilise le spécificateur `%@` :
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` accepte directement une `String` Swift. N'utilise pas `%s` avec une chaîne Swift : ce spécificateur attend une chaîne C et affiche n'importe quoi ou plante.

---

Puisque `%` commence un spécificateur, un signe pourcentage littéral doit s'écrire `%%`. C'est ainsi que tu formates un pourcentage :
```swift
let ratio = 0.4567
print(String(format: "%.1f%%", ratio * 100)) // 45.7%
```
Multiplie d'abord le rapport par `100`, puis choisis la précision : `%.0f%%` pour `46%`, `%.1f%%` pour `45.7%`.

---

Les drapeaux de largeur ne fonctionnent qu'à l'intérieur de `String(format:)`. Pour compléter toi-même une chaîne simple, construis les espaces avec `String(repeating:count:)` et joins-les au texte :
```swift
let text = "7"
let spaces = String(repeating: " ", count: 4 - text.count)
print(spaces + text + "|") //    7|
```
Si le texte est déjà plus long que la largeur, `4 - text.count` devient négatif et `String(repeating:count:)` plante. Protège-le avec `max(0, ...)`, pour que le compte ne descende jamais en dessous de zéro et que le texte long reste tel quel.

---

Foundation possède aussi une fonction utilitaire toute faite pour le remplissage à droite : `padding(toLength:withPad:startingAt:)`. Elle étend la chaîne jusqu'à la longueur donnée en répétant le texte de remplissage, et la coupe si elle est plus longue :
```swift
import Foundation

let name = "Ada"
print(name.padding(toLength: 8, withPad: " ", startingAt: 0) + "|") // Ada     |
print("Tea".padding(toLength: 6, withPad: ".", startingAt: 0))     // Tea...
```
`startingAt` est l'indice à l'intérieur du texte de remplissage où la répétition commence ; avec un texte de remplissage d'un seul caractère, c'est toujours `0`.

---

Combine les deux outils pour afficher un tableau : `padding` aligne le texte de chaque ligne à gauche, `String(format:)` aligne les nombres à droite avec une largeur et une précision fixes :
```swift
import Foundation

let items = [("Tea", 2.5), ("Cake", 12.0)]
for (name, price) in items {
    let label = name.padding(toLength: 6, withPad: ".", startingAt: 0)
    print(label + String(format: "%6.2f", price))
}
// Tea...  2.50
// Cake.. 12.00
```
Comme chaque ligne a la même largeur, les points décimaux se retrouvent dans la même colonne.
