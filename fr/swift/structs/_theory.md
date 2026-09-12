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
