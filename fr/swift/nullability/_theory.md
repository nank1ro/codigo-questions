Parfois une valeur est tout simplement absente : un utilisateur sans second prénom, une recherche qui ne trouve rien, un texte qui ne peut pas être converti en nombre.
Swift représente une valeur absente avec `nil`, mais une variable normale ne peut jamais la contenir :
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Pour autoriser une valeur absente, tu déclares un type **optionnel** en ajoutant un point d'interrogation `?` après le type.
Un `Int?` contient soit un `Int`, soit `nil` :
```swift
var age: Int? = 30
age = nil // autorisé
```
Une variable optionnelle déclarée sans valeur commence à `nil`.

---

Tu peux comparer un optionnel à `nil` en utilisant `==` et `!=`, et tu peux aussi le comparer directement à une valeur simple du type enveloppé :
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Souviens-toi que `Int?` et `Int` sont deux types différents : un `Int?` peut être vide, un `Int` ne l'est jamais.

---

Un optionnel est comme une boîte : avant d'utiliser la valeur qu'elle contient, tu dois l'ouvrir, ce que Swift appelle l'**extraction**.
Le moyen le plus rapide est l'**extraction forcée** avec un point d'exclamation `!` :
```swift
let score: Int? = 10
print(score! + 5) // 15
```
Le `!` indique à Swift "je suis sûr qu'il y a une valeur ici". Si tu te trompes et que l'optionnel est `nil`, le programme s'arrête immédiatement avec un plantage à l'exécution :
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
C'est pourquoi l'extraction forcée est considérée comme dangereuse : n'utilise-la que lorsque tu es certain que la valeur existe.

---

L'extraction forcée n'est sûre que lorsque tu as déjà vérifié que l'optionnel n'est pas `nil` :
```swift
if score != nil {
    print(score! * 2)
}
```

---

Vérifier `nil` puis extraire de force est verbeux. Swift propose la **liaison optionnelle** avec `if let`, qui extrait l'optionnel et stocke la valeur dans une nouvelle constante en une seule étape :
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value est un Int, pas un Int?
} else {
    print("No score")
}
```
Le corps du `if` ne s'exécute que lorsque l'optionnel contient une valeur ; à l'intérieur, `value` est un simple `Int` et n'a pas besoin de `!`.

---

Quand une valeur absente signifie "s'arrêter ici", `guard let` est plus clair que `if let`.
Il extrait l'optionnel et, si cela échoue, exécute le bloc `else`, qui doit quitter la portée actuelle (avec `return`, `break`, `continue` ou `throw`) :
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // name est un String à partir d'ici
}
```
Contrairement à `if let`, la constante extraite reste disponible pour le reste de la fonction, si bien que le chemin principal n'est pas imbriqué dans un `if`.

---

Une utilisation typique de `guard let` consiste à valider l'entrée d'une fonction au tout début et à renvoyer une valeur de repli lorsqu'elle est absente :
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Très souvent, tout ce que tu veux d'un optionnel, c'est sa valeur ou une valeur par défaut.
L'**opérateur de coalescence nil** `??` fait exactement cela : il extrait l'optionnel s'il a une valeur, sinon il renvoie la valeur à sa droite :
```swift
let score: Int? = nil
let points = score ?? 0 // points est un Int égal à 0
```
La valeur par défaut doit avoir le même type que la valeur enveloppée.
Tu peux enchaîner plusieurs `??` : la première valeur non `nil` l'emporte.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` est le moyen le plus court de transformer un optionnel en valeur simple lorsqu'une valeur par défaut raisonnable existe :
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Lors de l'enchaînement de `??`, Swift évalue de gauche à droite et s'arrête à la première valeur qui n'est pas `nil` ; la dernière valeur par défaut n'est utilisée que lorsque tous les optionnels précédents sont `nil`.

---

Accéder à une propriété ou appeler une méthode sur un optionnel nécessiterait de l'extraire d'abord.
Le **chaînage optionnel** avec `?.` le fait pour toi : si l'optionnel est `nil`, toute l'expression devient `nil`, sinon l'accès se poursuit :
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? contenant "SWIFT"
```
Le résultat est toujours un optionnel, même lorsque la propriété elle-même n'en est pas un.
Les chaînes peuvent être aussi longues que nécessaire, et elles se combinent bien avec `??` :
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

Le chaînage optionnel brille lorsque des données peuvent être absentes à plusieurs niveaux : un objet peut être `nil`, et l'une de ses propriétés peut l'être aussi.
Une seule chaîne `?.` gère les deux cas sans aucun `if`.

---

Un seul `if let` ou `guard let` peut extraire plusieurs optionnels à la fois : sépare les liaisons par des virgules.
Le corps ne s'exécute que si chaque optionnel a une valeur :
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
Tu peux aussi ajouter une condition booléenne après les liaisons, comme `if let n = number, n > 0`.

---

Lier plusieurs optionnels dans un seul `if let` garde le code plat : une seule branche `else` couvre chaque valeur absente.

---

De nombreuses opérations peuvent échouer, et Swift signale l'échec en renvoyant un optionnel.
Convertir du texte en nombre en est l'exemple classique : `Int("42")` renvoie un `Int?` contenant `42`, tandis que `Int("abc")` renvoie `nil`.
`Int("3.5")` est aussi `nil`, car le texte n'est pas un nombre entier ; utilise `Double("3.5")` pour les décimaux.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
D'autres exemples sont `array.first` (`nil` pour un tableau vide) et `dictionary[key]` (`nil` quand la clé est absente).

---

Comme une conversion peut échouer, son résultat est toujours un optionnel et doit être extrait avant utilisation, même quand tu es sûr que le texte est un nombre valide.

---

Les conversions faillibles s'associent naturellement à `guard let` : convertir, abandonner si le résultat est `nil`, puis travailler avec la valeur simple.

---

Parfois tu veux transformer la valeur à l'intérieur d'un optionnel et garder le résultat optionnel, sans extraire puis réenvelopper à la main.
Les optionnels ont une méthode `map` : elle applique la fermeture à la valeur si elle existe, et renvoie `nil` sinon.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? contenant 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Combinée à une conversion faillible, elle forme un pipeline compact : `Int(text).map { $0 + 1 }`.
