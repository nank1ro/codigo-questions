Une **expression régulière** (regex) est un petit motif qui décrit une forme de texte : « une suite de chiffres », « un mot suivi d'un signe égal », « trois lettres majuscules ». Au lieu d'écrire des boucles sur les caractères, tu décris la forme une seule fois et tu laisses Swift la trouver.

Swift écrit une expression régulière entre `#/` et `/#` :
```swift
let digits = #/\d+/#
```
À l'intérieur du motif, `\d` signifie « n'importe quel chiffre » et `+` signifie « une ou plusieurs fois l'élément précédent », donc `\d+` signifie « une suite d'un ou plusieurs chiffres ».

La question la plus simple que tu peux poser est de savoir si un texte contient une correspondance. `contains(_:)` prend une expression régulière et renvoie un `Bool` :
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Utilise toujours la forme `#/ ... /#` montrée ici : l'écriture plus courte `/ ... /` embrouille le compilateur quand le motif est écrit directement dans un appel de méthode.

---

Quelques raccourcis couvrent la plupart des motifs. Chacun correspond à exactement **un** caractère :
- `\d` est un chiffre
- `\w` est une lettre, un chiffre ou un underscore
- `\s` est un espace, une tabulation ou un retour à la ligne
- `.` est n'importe quel caractère unique

Pour correspondre à plus d'un caractère, ajoute un **quantificateur** juste après le motif :
- `+` signifie une ou plusieurs fois
- `*` signifie zéro ou plusieurs fois
- `?` signifie zéro ou une fois

Ainsi `\w+` est un mot, `\s*` est une espacement facultatif et `\d?` est un chiffre facultatif :
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Un caractère sans signification spéciale correspond simplement à lui-même, donc `#/cat/#` correspond aux trois lettres `cat`.

---

Par défaut, un motif peut correspondre n'importe où dans le texte. Les **ancres** le lient plutôt à une position :
- `^` signifie « le début du texte »
- `$` signifie « la fin du texte »

```swift
print("swift".contains(#/^sw/#))  // true, the text starts with sw
print("myswift".contains(#/^sw/#)) // false, sw is not at the start
print("swift".contains(#/ft$/#))  // true, the text ends with ft
```
Les ancres correspondent à une position, pas à un caractère, donc elles n'ajoutent rien au contenu de la correspondance.

---

Quand aucun des raccourcis ne convient, liste les caractères que tu acceptes entre crochets. `[abc]` correspond à un `a`, un `b` ou un `c`, et un tiret écrit un intervalle :
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Un nombre entre accolades dit exactement combien de fois le motif précédent se répète : `{3}` signifie trois fois, `{2,4}` signifie entre deux et quatre fois :
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Envelopper un motif dans `^` et `$` avec un compteur est la façon habituelle de vérifier qu'un texte entier a une forme donnée.

---

`contains(_:)` ne dit que oui ou non. Pour obtenir le texte correspondant, utilise `firstMatch(of:)`. Elle renvoie une **correspondance optionnelle** : `nil` quand rien ne correspond, donc elle se marie naturellement avec `if let`.

Le texte correspondant est stocké dans la propriété `0` de la correspondance, écrite `m.0` :
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` s'arrête à la première correspondance, même quand le texte en contient d'autres.

---

`m.0` n'est pas une `String` mais une `Substring` : une vue sur le texte original, pas une copie. Elle s'affiche exactement comme une chaîne, mais là où une `String` est exigée tu dois la convertir :
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Les initialiseurs de nombres acceptent une `Substring` directement, donc `Int(m.0)` fonctionne sans le détour.

---

`matches(of:)` renvoie **toutes** les correspondances au lieu de la première, sous forme de tableau. Le tableau n'est jamais `nil` : quand rien ne correspond il est simplement vide, donc tu peux le parcourir ou le transformer directement :
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Chaque élément est une correspondance, donc `$0.0` dans un `map` est le texte correspondant :
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Comme `Int(_:)` accepte une `Substring`, transformer du texte trouvé en nombres se fait en une étape. `compactMap` est pratique ici : elle écarte les valeurs qui reviennent `nil` :
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Utilise `map` quand chaque élément se convertit, `compactMap` quand certains peuvent échouer.

---

Des parenthèses autour d'une partie du motif créent un **groupe de capture** : la correspondance entière reste `m.0`, et la partie entre parenthèses devient `m.1` :
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
C'est ainsi que tu gardes le morceau intéressant et jettes le texte autour. Sans parenthèses il n'y a pas de `m.1` du tout, et le code ne compile pas.

---

Un motif peut contenir plusieurs groupes. Ils sont numérotés de gauche à droite selon leur parenthèse ouvrante, donc le deuxième est `m.2`, le troisième `m.3`, et ainsi de suite :
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` reste toujours la correspondance entière, quel que soit le nombre de groupes.

---

Compter les parenthèses devient fragile dès qu'un motif grandit. Donne plutôt un **nom** à un groupe, en écrivant `?<nom>` juste après sa parenthèse ouvrante, et lis-le comme une propriété de la correspondance :
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Les groupes nommés restent numérotés, donc `m.1` continue de fonctionner, mais `m.key` dit ce qu'il contient et survit à un changement dans le motif.

---

`replacing(_:with:)` remplace chaque correspondance par un texte fixe et renvoie une nouvelle `String`, en laissant l'original intact :
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Note que `\d+` remplace une suite entière de chiffres par un seul `#`, tandis que `\d` remplacerait un chiffre à la fois. C'est le motif qui décide de la quantité qui disparaît.

---

`split(separator:)` accepte aussi une expression régulière, ce qui permet à un seul appel de gérer des séparateurs qui ne sont pas toujours écrits de la même façon :
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
Le motif `[,;]\s*` signifie « une virgule ou un point-virgule, suivi d'une quantité quelconque d'espacement », donc chaque séparateur est consommé en entier et aucun champ vide n'est produit. Le résultat est un tableau de `Substring`.

---

Valider un texte entier avec `^` et `$` fonctionne, mais `wholeMatch(of:)` le dit directement : elle renvoie une correspondance seulement quand le motif couvre le texte du premier au dernier caractère, et `nil` sinon :
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Utilise `firstMatch(of:)` pour trouver quelque chose dans un texte, et `wholeMatch(of:)` pour vérifier qu'un texte a une forme exacte.

---

Un littéral `#/ ... /#` est figé à la compilation. Quand le motif ne devient connu qu'à l'exécution, par exemple parce qu'un utilisateur l'a tapé, construis-le avec `Regex(_:)` :
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Cet initialiseur **lève** une erreur : un motif invalide comme `"["` n'est découvert que pendant l'exécution du programme, donc l'appel a besoin de `try`, et l'erreur doit soit être gérée avec `do`/`catch` (ou `try?`), soit être propagée en marquant la fonction englobante `throws`, comme le fait cet exercice. Une expression régulière construite de cette façon n'a pas de propriétés numérotées connues à la compilation, mais `contains`, `matches(of:)` et `replacing` fonctionnent exactement comme avant.
