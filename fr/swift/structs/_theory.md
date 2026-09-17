Une **struct** (abbréviation de *structure*) est un type que tu conçois toi-même pour garder ensemble des valeurs liées. Au lieu de jongler avec un `title` séparé et un `pages` séparé, tu décris un `Book` une seule fois et tu l'utilises partout.

Tu en déclares une avec le mot-clé `struct`, et les variables écrites à l'intérieur sont ses **propriétés stockées** :
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` est maintenant un type, exactement comme `Int` ou `String`. Tu accèdes à une propriété d'une instance avec un point :
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Tu n'as jamais écrit le code qui construit un `Book`, et pourtant `Book(title: "Swift", pages: 120)` a fonctionné. Swift l'écrit pour toi : chaque struct reçoit gratuitement un **initialiseur membre à membre**, un initialiseur dont les paramètres sont ses propriétés stockées, dans l'ordre où elles sont déclarées, chacun utilisant le nom de la propriété comme libellé d'argument :
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Les classes ne l'obtiennent pas gratuitement, c'est l'une des raisons pour lesquelles les structs sont le moyen le plus rapide de modéliser une valeur.

---

Une propriété stockée peut recevoir une **valeur par défaut** dès l'endroit où elle est déclarée. Swift déduit son type de cette valeur, donc tu peux omettre l'annotation de type :
```swift
struct Counter {
    var label: String
    var value = 0
}
```
L'initialiseur membre à membre transforme chaque propriété avec valeur par défaut en argument optionnel : passe-le pour remplacer la valeur par défaut, omets-le pour la conserver.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Une struct peut aussi contenir des **méthodes** : des fonctions écrites entre les accolades qui travaillent sur l'instance sur laquelle elles sont appelées. Dans une méthode, tu utilises les noms des propriétés directement, sans aucun préfixe :
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
Si un paramètre de la méthode masque un nom de propriété, écris `self.width` pour désigner la propriété de l'instance.

---

Une **propriété calculée** ressemble à une propriété mais se comporte comme une méthode : elle ne stocke rien, elle calcule sa valeur chaque fois que tu la lis. Tu écris le type, puis un bloc de code qui renvoie la valeur :
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, no parentheses
```
Les propriétés calculées ne font pas partie de l'initialiseur membre à membre, puisqu'il n'y a rien à stocker. Utilise-en une quand la valeur est dérivée des autres, et une méthode quand le travail a besoin de paramètres.

---

Une struct est un **type valeur** : l'assigner à une autre variable, ou la passer à une fonction, remet une *copie*. Modifier la copie laisse l'original intact.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Une classe est un **type référence** : `b = a` ferait pointer les deux noms vers la même instance, donc `b.x = 99` changerait aussi `a.x` en `99`.

C'est la vraie différence entre les deux, et la raison pour laquelle Swift modélise la plupart des données comme des structs : une valeur que tu détiens ne peut pas être modifiée dans ton dos par le code qui l'a reçue.

---

Comme une struct est une valeur, une méthode n'a pas le droit de changer ses propriétés sauf si tu le déclares avec le mot-clé `mutating` :
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
Une méthode `mutating` ne peut être appelée que sur une instance stockée dans une `var`. Sur une instance `let` la valeur est figée, donc `c.increase(by: 5)` ne compilerait pas.

---

Lorsque l'initialiseur membre à membre n'est pas la façon dont tu veux que ton type soit construit, écris ton propre **initialiseur**. Il est déclaré avec `init`, prend les paramètres que tu choisis, et doit donner une valeur à chaque propriété stockée avant de se terminer. À l'intérieur, `self` est l'instance en cours de création :
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Écrire un `init` entre les accolades de la struct remplace celui membre à membre, donc à partir de maintenant `Square(side: 5)` n'existe plus.

---

Certaines valeurs appartiennent au type lui-même plutôt qu'à une seule instance : un code de devise, une valeur par défaut partagée, une fabrique qui construit un cas courant. Marque-les `static` et lis-les à travers le nom du type :
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Ici `currency` est déclarée avec `let` parce qu'elle ne change jamais, donc c'est une constante partagée par tout le programme. `Money.currency` fonctionne sans créer un seul `Money`, tandis que `amount` a besoin d'une instance.

---

Deux structs ne peuvent pas être comparées avec `==` tant que le type ne dit pas qu'il le prend en charge. Tu fais cela en te conformant au **protocole** `Equatable`, écrit après un deux-points dans la déclaration :
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
Tu n'as pas besoin d'écrire `==` toi-même : quand chaque propriété stockée est déjà `Equatable`, Swift la synthétise pour toi, en comparant les propriétés une par une. Deux instances sont égales quand toutes leurs propriétés sont égales, ce qui est exactement ce à quoi tu t'attends d'une valeur.

---

Une struct est un type comme les autres, donc elle peut être stockée dans un tableau, un dictionnaire ou un set, et chaque outil que tu connais déjà continue de fonctionner sur elle :
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Rappelle-toi que le tableau contient des *copies* : lire `items[0]` dans une variable et la modifier ne touche pas le tableau.
