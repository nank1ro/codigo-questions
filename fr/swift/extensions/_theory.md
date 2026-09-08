Une **extension** ajoute de nouvelles fonctionnalités à un type existant : un type de la bibliothèque standard comme `Int` ou `String`, ou une struct ou une classe que tu as écrite toi-même.
Tu écris le mot-clé `extension` suivi du nom du type, et tu places les nouveaux membres entre accolades :
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
À l'intérieur de l'extension, `self` est la valeur sur laquelle la méthode est appelée : dans `4.squared()` c'est `4`. Une fois l'extension définie, chaque `Int` du programme possède la nouvelle méthode, exactement comme si elle avait fait partie de `Int` depuis le début.

---

Les extensions fonctionnent sur n'importe quel type, même ceux dont tu n'as pas le code source. `String` vient de la bibliothèque standard, mais tu peux quand même lui ajouter de nouvelles méthodes :
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
À l'intérieur d'une extension, tu peux omettre `self.` lorsque tu appelles d'autres membres du type : `lowercased()` seul signifie `self.lowercased()`.

---

Une extension ne crée pas un nouveau type et ne copie pas l'ancien : elle ajoute des membres au type lui-même, donc chaque valeur existante et future de ce type les obtient.
C'est pourquoi les extensions sont si utiles avec les types que tu ne peux pas modifier, comme ceux de la bibliothèque standard ou d'un framework : tu ne peux pas ouvrir le fichier où `Int` est défini, mais tu peux l'étendre depuis n'importe quel fichier de ton programme.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

En plus des méthodes, une extension peut ajouter des **propriétés calculées** : des propriétés qui ne stockent pas une valeur mais la calculent à chaque fois qu'elles sont lues.
Une propriété calculée est déclarée avec `var`, une annotation de type et un corps entre accolades qui renvoie la valeur :
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Elle se lit comme n'importe quelle propriété, sans parenthèses : `7.isNegative`, et non `7.isNegative()`.

---

Les propriétés calculées dans les extensions conviennent aussi tout naturellement à `String`. La méthode `reversed()` renvoie les caractères dans l'ordre inverse, et `String(...)` les retransforme en chaîne :
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Comme pour les méthodes, `reversed()` à l'intérieur de l'extension signifie `self.reversed()`.

---

Les extensions peuvent ajouter des propriétés calculées mais **pas des propriétés stockées** : ceci ne compile pas :
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Une propriété stockée a besoin d'un espace dans chaque instance du type. Les valeurs `Int` existent déjà partout dans ton programme, et même dans du code compilé bien avant ton extension, donc leur disposition en mémoire ne peut pas changer. Une propriété calculée n'a besoin d'aucun espace, car ce n'est que du code qui s'exécute lorsque la propriété est lue.

---

`Int`, `String`, les tableaux et les structs sont des **types valeur** : une méthode ne peut pas changer la valeur sur laquelle elle est appelée, sauf si elle est marquée `mutating`. Les extensions peuvent aussi ajouter des méthodes `mutating` :
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
À l'intérieur d'une méthode `mutating`, tu peux assigner à `self`. La valeur doit être stockée dans un `var` : appeler `increment()` sur une constante `let` est une erreur de compilation.

---

Une méthode `mutating` peut prendre des paramètres comme n'importe quelle autre méthode, et peut remplacer `self` entièrement au lieu de le mettre à jour sur place :
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

Une extension peut ajouter de nouveaux **initialisateurs** à un type. Pour une struct, c'est le meilleur endroit pour les placer : un `init` écrit à l'intérieur du corps de la struct remplace l'initialisateur membre à membre automatique, tandis que celui ajouté dans une extension le conserve.
Le nouvel initialisateur délègue habituellement à un initialisateur existant avec `self.init(...)` :
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Les extensions ne servent pas qu'aux types des autres. Une façon courante d'organiser ton propre code est de garder les propriétés stockées dans le corps de la struct ou de la classe et d'ajouter le comportement dans une ou plusieurs extensions, chacune regroupant des membres liés :
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
Les membres ajoutés dans une extension peuvent utiliser les propriétés stockées directement, exactement comme s'ils étaient écrits à l'intérieur du type.

---

Une extension peut aussi faire conformer un type à un **protocole**, une liste d'exigences que le type promet d'implémenter. Écris le nom du protocole après le nom du type, séparé par un deux-points, et ajoute les membres requis dans le corps.
`CustomStringConvertible` est un protocole standard avec une seule exigence, une propriété calculée `description` de type `String`, que `print` utilise pour afficher la valeur :
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Garder chaque conformité à un protocole dans sa propre extension est la façon habituelle d'organiser un type Swift.

---

`Array` est un type générique : `[Int]` et `[String]` sont tous deux des tableaux, avec un type **`Element`** différent. Une extension de `Array` s'applique à tous, ce qui pose un problème lorsque le nouveau membre n'a de sens que pour certains éléments : tu ne peux pas additionner des nombres qui sont des chaînes.
Une clause `where` restreint l'extension aux tableaux dont `Element` est un type donné :
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` fonctionne, tandis que `["a", "b"].largest` est une erreur de compilation : la propriété n'existe pas sur `[String]`.

---

Les extensions peuvent ajouter des membres **statiques** : des propriétés et des méthodes qui appartiennent au type lui-même plutôt qu'à une seule valeur, marquées avec le mot-clé `static` et accessibles via le nom du type.
Un `static let` est autorisé même s'il stocke une valeur, car il n'y a qu'une seule copie pour tout le type, et non une par instance :
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
Un membre statique n'a pas de valeur `self` sur laquelle travailler : `Int.answer` est lu sur le type, pas sur un nombre.

---

Les méthodes statiques dans les extensions sont un bon endroit pour les petites fonctions de fabrique qui construisent une valeur du type. `String(repeating:count:)` est l'initialisateur standard qui répète un morceau de texte un certain nombre de fois :
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Les extensions peuvent seulement **ajouter** des membres, jamais remplacer ou redéfinir ceux qui existent déjà. `override` appartient aux sous-classes, qui sont un type différent de leur parent ; une extension est le même type, donc déclarer une méthode qui existe déjà est une erreur de redéclaration :
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
Si tu as besoin d'un comportement différent, ajoute une méthode avec un nouveau nom, ou écris une sous-classe lorsque le type est une classe.
