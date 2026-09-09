Une **fonction d'ordre supérieur** est une fonction qui prend une autre fonction en argument, en renvoie une, ou les deux. Tu as déjà rencontré `map`, `filter`, `reduce` et `sorted(by:)` : elles prennent une fermeture et l'appliquent aux éléments d'une collection. Swift en a beaucoup d'autres, et les connaître te permet de remplacer de longues boucles par une seule ligne lisible.
`compactMap` fonctionne comme `map`, mais la fermeture renvoie un optionnel et les résultats `nil` sont ignorés :
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` vaut `nil`, donc cet élément disparaît et le résultat est un `[Int]`, pas un `[Int?]`.

---

`flatMap` est destiné aux fermetures qui renvoient un **tableau** : au lieu de construire un tableau de tableaux, elle réunit tous les tableaux renvoyés en un seul résultat à plat :
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
La fermeture peut aussi transformer chaque tableau interne avant l'aplanissement, par exemple `teams.flatMap { $0.reversed() }` donne `["Bob", "Ann", "Cid"]`.

---

Les trois variantes de `map` ne diffèrent que par ce que renvoie la fermeture :
- `map` : n'importe quelle valeur, un résultat par élément
- `compactMap` : un optionnel, les résultats `nil` sont ignorés
- `flatMap` : un tableau, tous les résultats sont réunis en un seul tableau

La fermeture passée à `flatMap` peut elle-même appeler `map` sur le tableau interne, en imbriquant une transformation dans l'autre :
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` construit une nouvelle valeur accumulée à chaque étape, ce qui est coûteux quand le résultat est un tableau ou un dictionnaire. `reduce(into:)` donne à la fermeture l'accumulateur comme paramètre `inout`, si bien qu'il peut être modifié sur place sans `return` :
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` crée un dictionnaire vide, et `result[word, default: 0]` lit le compteur actuel ou `0` quand la clé est absente.

---

Certaines fonctions d'ordre supérieur répondent à une question sur la collection au lieu de la transformer. Elles prennent toutes une fermeture qui renvoie un `Bool` :
- `first(where:)` renvoie le premier élément qui satisfait la fermeture, ou `nil` s'il n'y en a aucun
- `contains(where:)` renvoie `true` si au moins un élément la satisfait
- `allSatisfy` renvoie `true` si tous les éléments la satisfont

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
Contrairement à `filter`, `first(where:)` s'arrête à la première correspondance et ne construit pas de nouveau tableau.

---

`contains(where:)` et `allSatisfy` remplacent le schéma courant d'une boucle avec une variable indicatrice. Les deux s'arrêtent dès que la réponse est connue : `contains(where:)` à la première correspondance, `allSatisfy` au premier élément qui échoue.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` est la forme à fermeture en fin d'appel de `contains(where:)`, à ne pas confondre avec `contains(_:)`, qui recherche une valeur précise.

---

Les fonctions d'ordre supérieur fonctionnent sur n'importe quel tableau, y compris les tableaux de tes propres structs. Enchaîner `filter` puis `map` est la façon habituelle de sélectionner certains éléments et d'extraire une valeur de chacun :
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Faire l'inverse, `map` puis `filter`, perdrait la propriété `pages` avant que la vérification puisse l'utiliser.

---

Quand une fermeture ne fait que lire une propriété, tu peux passer un **key path** à la place : `\.name` signifie « la propriété `name` de l'élément », et `map(\.name)` est équivalent à `map { $0.name }`.
Le tri par propriété utilise la fermeture habituelle à deux arguments, qui compare cette propriété sur les deux éléments :
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Pour trier selon **plusieurs critères**, compare la première propriété et reviens à la seconde uniquement lorsque les premières valeurs sont égales :
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Ici les personnes sont ordonnées par âge, et les personnes du même âge sont ordonnées par nom. La fermeture doit renvoyer `true` uniquement quand le premier élément doit venir avant le second, si bien que le cas d'égalité passe à la comparaison suivante.

---

`enumerated()` transforme un tableau en une séquence de paires `(offset, element)`, si bien qu'une fermeture peut utiliser la position de chaque élément en même temps que sa valeur :
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Comme chaque paire est un tuple, la fermeture peut aussi le déstructurer : `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` associe les éléments de deux séquences position par position, produisant une séquence de tuples. Elle s'arrête à la fin de la plus courte :
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Dans la fermeture, `$0` est l'élément de la première séquence et `$1` celui de la seconde. `zip` est une fonction libre, pas une méthode : tu écris `zip(a, b)`, pas `a.zip(b)`.

---

`forEach` est le jumeau d'ordre supérieur de la boucle `for-in` : il appelle la fermeture une fois par élément, dans l'ordre. La différence réside dans la façon de quitter la boucle. Dans une boucle `for-in` tu peux sortir avec `break` ou faire un `continue` ; dans une fermeture `forEach`, `break` et `continue` ne sont pas autorisés, et `return` ne met fin qu'à **l'appel en cours** de la fermeture, puis l'élément suivant est traité normalement :
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Utilise `forEach` pour un court effet de bord sur chaque élément, et `for-in` quand tu dois t'arrêter plus tôt.

---

`Dictionary(grouping:by:)` scinde une collection en un dictionnaire de tableaux. La fermeture calcule la **clé** de chaque élément, et tous les éléments ayant la même clé se retrouvent dans le même tableau :
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` transforme chaque valeur d'un dictionnaire en conservant les clés, si bien que c'est l'étape suivante naturelle après le regroupement :
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` prend des éléments du début **tant que** la fermeture renvoie `true`, et s'arrête au premier élément qui échoue, même si des éléments suivants passeraient à nouveau. `drop(while:)` en est le complément : il saute cette même suite initiale et renvoie tout le reste :
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Les deux renvoient un `ArraySlice`, une vue sur le tableau d'origine qui s'affiche comme un tableau et peut être converti en un avec `Array(...)`.

---

Tu peux écrire tes propres fonctions d'ordre supérieur. Une fonction qui prend une fermeture et **renvoie une nouvelle fermeture** construite à partir d'elle est un schéma courant : la fermeture renvoyée capture l'originale, si bien que le paramètre doit être `@escaping`.
Par exemple, `negate` transforme un prédicat en son contraire, prêt à être passé à `filter` :
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Note que `filter(negate(isEven))` passe la fermeture comme un argument normal, sans la syntaxe de fermeture en fin d'appel.

---

`map` et `filter` sur un tableau sont **avides** : chacun traite tout le tableau et en construit un nouveau avant que l'étape suivante ne s'exécute. Sur une grande collection, ou quand seul le premier résultat est nécessaire, c'est du travail gaspillé.
La propriété `lazy` renvoie une vue dont les opérations ne s'exécutent que quand un élément est réellement demandé, un élément à la fois à travers toute la chaîne :
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Ici seuls `1, 2, ..., 8` sont élevés au carré : `first(where:)` demande des éléments jusqu'à ce que l'un satisfasse la condition, et la chaîne s'arrête là. Sans `lazy`, `map` élèverait d'abord au carré les 1000 nombres.
