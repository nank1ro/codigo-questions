Les tableaux sont un type de données que vous pouvez utiliser pour stocker une collection de différents éléments d'information en tant que séquence sous un seul nom de variable.
Un tableau stocke plusieurs valeurs d'un ou de plusieurs types et utilise des **indices** pour distinguer ces valeurs.
Vous pouvez assigner des éléments à un tableau avec une expression de la forme :
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` représente le type des éléments à l'intérieur du tableau, par exemple, il peut être `Int`, `String`, `Any`...

---

Vous pouvez accéder à un élément individuel du tableau par son index.
Un index est comme une adresse qui identifie la place de l'élément dans le tableau.
L'index apparaît directement après le nom du tableau, entre les crochets, comme ceci :
```swift
arrayName[index]
```

Les indices du tableau commencent par `0`, **pas** `1` ! Vous accédez au premier élément d'un tableau comme ceci : `arrayName[0]`.
Le deuxième élément d'un tableau se trouve à l'index 1 : `arrayName[1]`.

---

Un index de tableau se comporte comme n'importe quel autre nom de variable.
Il peut être utilisé pour accéder ainsi que pour assigner des valeurs.
Vous avez vu comment accéder à un index de tableau comme ceci :
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Affiche la valeur "Jeremiah"
print(names[0])
```
Voici comment fonctionne une assignation :
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assigner la nouvelle valeur "Jordan"
names[0] = "Jordan"
// Affiche la valeur "Jordan"
print(names[0])
```

---

Comme les chaînes de caractères, les tableaux ont une **longueur** `count`.
La longueur d'un tableau est le nombre d'éléments qu'il contient

---

Un tableau ne doit pas nécessairement avoir une longueur fixe.
Vous pouvez ajouter des éléments à la fin d'un tableau à tout moment !
Pour ajouter un élément à un tableau, nous utilisons la fonction `append` :
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Affiche ["a", "b", "c"]
```

---

Parfois, vous voulez accéder à une partie d'un tableau.
Considérez le code suivant :
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// affiche [2, 3]
```
Tout d'abord, nous créons un tableau appelé `numbers`.
Ensuite, nous prenons une sous-section du tableau et la stockons dans le tableau slice.
Nous le faisons en définissant les indices que nous voulons inclure après le nom du tableau : `numbers[1...2]`.
En Swift, nous pouvons inclure le dernier index en utilisant `...`, mais nous pouvons aussi exclure le dernier index en utilisant `..<`

---

En Swift, nous pouvons découper un tableau comme nous le souhaitons !
```swift
// Récupère les deux premiers éléments
listName[..<2]
// Récupère les éléments du quatrième au dernier
listName[3...]
```
Si votre tranche de tableau inclut le tout premier ou le dernier élément d'un tableau, l'index de cet élément n'a pas besoin d'être inclus

---

Les éléments du tableau peuvent être de n'importe quel type, si nous spécifions le type `Any` :
```swift
var arrayName: [Any] = ["one", 2, true]
```
En fait, ci-dessus nous avons, dans l'ordre, une chaîne de caractères, un entier et un booléen.
Mais nous pouvons aussi avoir des tableaux avec des tableaux !

---

Parfois, vous avez besoin de chercher un élément dans un tableau.
En Swift, nous pouvons utiliser la méthode `firstIndex()` :
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// affiche 1
```
Le code ci-dessus affiche le premier index qui contient la chaîne `"Zac"`, `1` dans ce cas.
Nous pouvons aussi insérer des éléments dans un tableau à un index spécifique, en utilisant la méthode `insert()` :
```swift
names.insert("Ali", at: 1)
// affiche ["Trevor", "Ali", "Zac", "Glenn"]
```
Le code ci-dessus insère `"Ali"` à l'index `1`, ce qui déplace tout, après cet index, vers le bas d'1

---

En Swift, nous pouvons boucler à travers un tableau de manière très simple en utilisant les mots-clés `for..in` :
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// affiche 1, 2, 3
```
Un nom de variable suit le mot-clé `for`, il se verra assigner la valeur de chaque élément du tableau à tour de rôle.

---

Les **tuples** sont comme des tableaux mais vous pouvez nommer les éléments et utiliser ces noms pour les référencer
Pour créer un tuple, nous utilisons les parenthèses `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
