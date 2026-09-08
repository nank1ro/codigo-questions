Chaque valeur en Swift possède un **type**, qui indique au compilateur de quelles données il s'agit et ce que tu peux en faire.
Les types de base sont :
- `Int` : un nombre entier, comme `42` ou `-7`
- `Double` : un nombre avec une partie décimale, comme `3.14`
- `String` : un morceau de texte, comme `"Hello"`
- `Character` : un seul caractère, comme `"a"`
- `Bool` : soit `true` soit `false`

Tu peux indiquer le type d'une constante ou d'une variable avec une **annotation de type** : un deux-points et le nom du type après le nom :
```swift
let age: Int = 36
let name: String = "Ada"
```
Une valeur d'un type ne peut pas être stockée dans une constante d'un autre type : `let age: Int = "36"` est une erreur de compilation.

---

La plupart du temps, tu n'écris pas l'annotation de type : Swift **déduit** le type à partir de la valeur que tu assignes, en suivant quelques règles sur les littéraux :
- un nombre sans point décimal, comme `42`, est un `Int`
- un nombre avec un point décimal, comme `3.14`, est un `Double`
- un texte entre guillemets doubles est une `String`
- `true` et `false` sont des `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift possède aussi `Float`, un nombre décimal qui utilise la moitié de la mémoire d'un `Double` mais qui est moins précis, donc un littéral décimal n'est jamais déduit comme `Float` : tu dois le demander avec une annotation.
De la même façon, `"a"` est déduit comme une `String`, donc un `Character` a toujours besoin d'une annotation.

---

La fonction `type(of:)` retourne le type d'une valeur, ce qui est pratique pour vérifier ce que Swift a déduit :
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Quand tu veux un type différent de celui déduit, ajoute une annotation. Un littéral entier peut être stocké dans une constante `Double` ou `Float`, et un littéral d'un seul caractère dans une constante `Character` :
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift n'effectue jamais de conversion entre types numériques de lui-même : additionner un `Int` à un `Double` est une erreur de compilation, même si les deux sont des nombres.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Pour les combiner, tu crées une nouvelle valeur du type dont tu as besoin, en passant la valeur à l'initialiseur du type :
```swift
let total = Double(apples) * price // 4.5
```
Cela fonctionne aussi dans l'autre sens : `Int(4.5)` produit un `Int`, en gardant seulement la partie entière du nombre.

---

`Int(x)` n'arrondit pas : il **tronque**, en supprimant simplement la partie décimale, donc `Int(3.99)` vaut `3` et `Int(-3.99)` vaut `-3`.
Pour arrondir au nombre entier le plus proche, appelle d'abord `rounded()` sur le `Double` puis convertis :
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Les valeurs à mi-chemin comme `2.5` sont arrondies en s'éloignant de zéro : `2.5` devient `3.0` et `-2.5` devient `-3.0`.

---

Le type des opérandes décide du fonctionnement de la division. Quand les deux sont des `Int`, l'opérateur `/` effectue une **division entière** : le résultat est un `Int` et le reste est jeté.
Quand au moins un opérande est un `Double`, `/` effectue une division à virgule flottante et garde la partie décimale :
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Donc, pour obtenir un résultat décimal à partir de deux valeurs `Int`, tu dois convertir au moins l'une des deux en `Double` **avant** de diviser : `Double(7 / 2)` vaut `3.0`, car la division entière a déjà eu lieu.

---

Quand une fonction doit renvoyer un résultat décimal calculé à partir de nombres entiers, convertis les opérandes en `Double` avant de diviser et déclare le type de retour comme `Double` :
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Souviens-toi que `count` d'un tableau est aussi un `Int`, donc il a besoin de la même conversion.

---

Les nombres et les chaînes se convertissent avec la même syntaxe d'initialiseur. `String(42)` transforme un nombre en le texte `"42"`, exactement comme son interpolation avec `"\(42)"`.
Le sens inverse peut échouer, car tout texte n'est pas un nombre, donc `Int("42")` retourne un `Int?` **optionnel** : il contient `42` ici, mais `Int("hello")` vaut `nil`.
Comme tu l'as appris dans les leçons sur les optionnels, tu peux fournir une valeur de secours avec `??` ou l'extraire avec `if let` :
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` réussit seulement quand tout le texte est un nombre entier valide, avec un signe optionnel :
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Pour un texte décimal, utilise `Double(text)`, qui retourne un `Double?` de la même façon : `Double("3.5")` vaut `Optional(3.5)`.

---

Un **alias de type** donne à un type existant un nouveau nom, avec le mot-clé `typealias` :
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` et `Int` sont le même type, donc ils se mélangent librement. Un alias n'ajoute aucune sécurité : il rend seulement le code plus lisible quand un type simple a une signification précise dans ton programme.

---

Un `Int` utilise 64 bits, donc il ne peut représenter que des nombres dans une plage fixe. La plus grande et la plus petite valeur sont disponibles sous la forme de `Int.max` et `Int.min` :
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Dépasser ces limites s'appelle un **débordement** (*overflow*). Contrairement à beaucoup d'autres langages, Swift ne repart pas silencieusement à l'autre bout de la plage : une opération qui déborde est une **erreur à l'exécution** qui arrête le programme.

---

`Int.max` et `Int.min` sont utiles comme valeurs de départ quand tu cherches un extremum : tout nombre réel est plus petit que `Int.max`, donc c'est une valeur initiale sûre pour « le plus petit vu jusqu'ici » :
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Comme tu l'as vu dans les leçons sur les chaînes, itérer sur une `String` te donne un `Character` à la fois. Un `Character` n'est pas une `String`, donc pour l'utiliser comme texte tu le convertis avec `String(c)`.
Quand le caractère est un chiffre, la propriété `wholeNumberValue` te donne sa valeur numérique en tant qu'`Int?` : elle vaut `nil` pour les caractères qui ne sont pas des chiffres.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Comme `Int(text)` et `Double(text)` retournent `nil` en cas d'échec, comparer le résultat avec `nil` te dit si un texte est un nombre de ce genre :
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Note la dernière ligne : tout texte accepté par `Int` est aussi accepté par `Double`, donc vérifie d'abord `Int` quand tu veux les distinguer.

---

Parfois tu as besoin de stocker ensemble des valeurs de types différents. Le type spécial `Any` peut contenir une valeur de **n'importe quel** type, donc un tableau déclaré comme `[Any]` peut mélanger des nombres, des chaînes et des booléens :
```swift
let items: [Any] = [1, "two", true]
```
Chaque élément se souvient quand même de son type réel, que `type(of:)` révèle. Pour manipuler la valeur comme son type réel, tu utilises une **conversion conditionnelle** avec `as?`, qui retourne un optionnel : il contient la valeur quand le type correspond et `nil` sinon :
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` est une solution de dernier recours : un tableau d'un seul type concret est plus sûr et plus facile à utiliser, donc préfère-le chaque fois que tu le peux.

---

Les conversions conditionnelles se chaînent naturellement avec `else if` pour gérer plusieurs types possibles, en convertissant chacun vers le type dont tu as besoin pour le résultat :
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
Un `Int` stocké dans `Any` reste un `Int` : `as? Double` sur lui retourne `nil`, car `as?` vérifie le type, il ne convertit pas les nombres.
