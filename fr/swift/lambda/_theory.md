Une **fermeture** est un bloc de code que tu peux transmettre et appeler plus tard, comme une fonction sans nom.
La syntaxe complète d'expression de fermeture place les paramètres et le type de retour entre accolades, suivis du mot-clé `in` et du corps :
```swift
{ (parameters) -> ReturnType in
    body
}
```
Comme toute autre valeur, une fermeture peut être stockée dans une constante puis appelée en utilisant le nom de la constante :
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Écrire chaque type à l'intérieur de la fermeture est souvent inutile. Lorsque la constante a un **type de fonction** explicite, Swift déduit les types des paramètres et du retour, donc tu n'as qu'à lister les noms des paramètres avant `in` :
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
Le type `(Int) -> Int` se lit « une fonction qui prend un `Int` et renvoie un `Int` ».
Lorsque le corps est une expression unique, le mot-clé `return` peut aussi être omis, on appelle cela un **retour implicite** :
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift va encore plus loin : à l'intérieur d'une fermeture, tu peux te référer aux arguments avec les **noms d'arguments abrégés** `$0`, `$1`, `$2`, etc., sans déclarer aucun paramètre ni le mot-clé `in`.
`$0` est le premier argument, `$1` le second :
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
Les types proviennent toujours de l'annotation `(Int, Int) -> Int`.

---

Comme les fermetures sont des valeurs, une fonction peut en accepter une comme paramètre. Le type du paramètre est simplement le type de fonction :
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
La fonction `apply` ne sait pas ce que fait `operation`, elle sait seulement qu'elle prend un `Int` et renvoie un `Int`, et l'appelle comme n'importe quelle autre fonction.

---

Quand une fermeture est le **dernier** argument d'une fonction, tu peux l'écrire après la parenthèse fermante de l'appel. C'est la syntaxe de **fermeture finale** :
```swift
print(apply(5) { $0 + 1 }) // 6
```
Si la fermeture est le seul argument, les parenthèses peuvent être complètement omises :
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Les deux formes appellent exactement la même fonction, la syntaxe finale est simplement plus facile à lire quand la fermeture est longue.

---

Les fermetures brillent avec les méthodes de tableau qui en prennent une comme argument. `map` appelle la fermeture sur chaque élément et renvoie un nouveau tableau avec les résultats :
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
Le tableau d'origine n'est pas modifié. Comme `map` prend une seule fermeture comme argument, la syntaxe de fermeture finale est la façon habituelle de l'appeler.

---

`filter` ne garde que les éléments pour lesquels la fermeture renvoie `true`. La fermeture reçoit un élément et doit renvoyer un `Bool` :
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Les éléments conservent leur ordre d'origine, et le résultat est un nouveau tableau du même type d'élément.

---

`reduce` combine tous les éléments en une seule valeur. Elle prend une valeur initiale et une fermeture à deux arguments : la valeur accumulée jusqu'ici et l'élément courant. La fermeture renvoie la nouvelle valeur accumulée :
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Ici `$0` commence à `1`, puis devient `1 * 1`, `1 * 2`, `2 * 3` et enfin `6 * 4`.
Comme `map`, `filter` et `reduce` renvoient toutes des valeurs, elles peuvent être chaînées : `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` renvoie un nouveau tableau trié. La fermeture reçoit deux éléments et renvoie `true` quand le premier doit venir **avant** le second :
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
La fermeture peut comparer n'importe quoi, par exemple `words.sorted { $0.count < $1.count }` trie les chaînes de la plus courte à la plus longue.
