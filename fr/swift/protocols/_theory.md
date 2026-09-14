Un **protocole** décrit ce qu'un type doit posséder, sans dire comment. C'est une liste d'exigences — des propriétés et des méthodes — que tout type qui l'adopte promet de fournir.

Tu en déclares un avec le mot-clé `protocol`. Une exigence de propriété s'écrit avec son type suivi d'un bloc qui indique comment elle peut être accédée : `{ get }` signifie que le type doit au moins te laisser la lire.
```swift
protocol Named {
    var name: String { get }
}
```
Un type **se conforme** au protocole en écrivant son nom après un deux-points et en fournissant tout ce que le protocole demande :
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Un protocole ne contient aucune donnée propre : c'est un contrat. Chaque type qui le satisfait peut être traité de la même manière par le reste de ton code.

---

Un protocole peut aussi exiger des **méthodes**. Tu écris la signature — le nom, les paramètres et le type de retour — et tu t'arrêtes là, sans corps :
```swift
protocol Greeter {
    func greet() -> String
}
```
Un type conforme doit déclarer une méthode avec exactement cette signature, et il fournit le corps :
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Si quelque chose diffère — le nom, un type de paramètre, le type de retour — le type n'est pas conforme, et le compilateur te dit quelle exigence manque.

---

Une exigence de propriété indique toujours comment la propriété peut être utilisée. `{ get }` demande seulement que la valeur puisse être lue ; `{ get set }` demande qu'elle puisse être lue **et** assignée :
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Un type conforme peut toujours donner plus que ce que le contrat demande : une propriété stockée déclarée avec `var` satisfait parfaitement `{ get }`. Il ne peut jamais donner moins — une constante `let`, ou une propriété calculée en lecture seule, ne peut pas satisfaire `{ get set }`.

---

Les protocoles ne se limitent pas aux structs. Une **classe** se conforme exactement de la même manière, en listant le protocole après un deux-points :
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
Si la classe hérite aussi d'une autre classe, la superclasse vient en premier dans la liste et les protocoles la suivent. Un type peut adopter plusieurs protocoles à la fois, séparés par des virgules.

---

Une **énumération** peut aussi se conformer. Elle n'a pas de propriétés stockées, donc une exigence de propriété est généralement satisfaite avec une propriété calculée qui fait un `switch` sur les cas :
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Structs, classes et énumérations : les trois adoptent les protocoles de la même manière, et le code écrit contre le protocole fonctionne avec chacune d'elles.

---

Un protocole rassemble généralement plus d'une exigence, et un type conforme doit satisfaire chacune d'elles :
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
L'ordre des exigences entre les accolades n'a pas d'importance, et l'ordre dans lequel le type conforme les fournit non plus : le compilateur vérifie seulement que rien ne manque.

---

Une struct est un type valeur, donc une méthode qui modifie l'une de ses propriétés stockées doit être marquée `mutating`. Quand cette méthode est une exigence de protocole, le protocole doit aussi le dire :
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Sans `mutating` dans le protocole, une struct ne pourrait jamais satisfaire l'exigence. Les classes sont des types référence et n'ont jamais besoin du mot-clé : une classe satisfait une exigence `mutating` avec une méthode ordinaire. Appeler une méthode mutante nécessite un `var` — sur un `let` c'est une erreur de compilation.

---

La conformité n'a pas à être déclarée à côté du type. Une **extension** peut l'ajouter plus tard, ce qui garde la déclaration du type elle-même concentrée sur ses données :
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
Cela fonctionne aussi pour les types que tu n'as pas écrits : tu peux faire conformer un type de la bibliothèque standard à l'un de tes protocoles sans toucher à son code source.

---

Une extension d'un **protocole** est un autre outil : elle ajoute des membres à tous les types qui se conforment, présents et futurs. C'est ainsi que tu donnes à une exigence une **implémentation par défaut** :
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` n'écrit jamais `greet()` et se conforme quand même. À l'intérieur de l'extension du protocole, tu peux utiliser chaque exigence du protocole — ici `name` — car tout type conforme est garanti de l'avoir.

---

Une extension de protocole peut aussi ajouter des membres que le protocole n'a jamais listés comme exigences. Ce sont des facilités supplémentaires, disponibles sur tout type conforme :
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` n'est pas une exigence, donc un type conforme n'a pas à la fournir — il l'obtient simplement.

---

Un protocole peut s'appuyer sur un autre. Écrire un nom de protocole après le deux-points fait que le nouveau protocole **hérite** de chaque exigence de l'ancien :
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Un type conforme à `Aged` doit fournir `age` *et* `name`, et il compte comme un type `Named` partout. Un protocole peut hériter de plusieurs protocoles à la fois, séparés par des virgules.

---

Une implémentation par défaut est un repli, pas une règle. Si un type conforme fournit sa propre version d'une exigence, c'est sa version qui s'exécute :
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, not 0
```
La valeur par défaut ne comble que les lacunes que le type laisse ouvertes.

---

La bibliothèque standard est construite à partir de protocoles, et tes propres types peuvent les adopter.

`Equatable` donne à un type l'opérateur `==`. Pour une struct dont toutes les propriétés stockées sont `Equatable`, déclarer la conformité suffit — Swift écrit `==` pour toi :
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` hérite de `Equatable` et ajoute l'ordre. Tu implémentes un seul opérateur, `<`, écrit comme une `static func` prenant les deux valeurs, et tu obtiens `>`, `<=`, `>=`, ainsi que `sorted()`, `min()` et `max()` sur les collections gratuitement :
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` décide de ce que `print` affiche pour ton type. Son unique exigence est une propriété `description` :
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Sans la conformité, afficher une struct produit un affichage par défaut comme `Coin(value: 25)`, et une simple propriété `description` ne change rien — `print` cherche le protocole. L'interpolation de chaîne utilise aussi `description`.

---

Un nom de protocole à lui seul n'est pas un type, c'est une contrainte, donc Swift te demande de dire laquelle de deux choses tu veux dire.

`some Shape` signifie *un type conforme précis*, fixé à la compilation. L'appelant ne sait jamais lequel, mais c'est toujours le même :
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` signifie *une boîte qui peut contenir n'importe quel type conforme*, et deux valeurs de ce type peuvent contenir des types différents. Tu en as besoin chaque fois que le type concret peut varier, comme dans un tableau mélangé :
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Tous deux te permettent d'appeler les exigences du protocole. Préfère `some` quand un seul type suffit, car il ne coûte rien à l'exécution ; tourne-toi vers `any` quand tu as vraiment besoin de mélanger des types.
