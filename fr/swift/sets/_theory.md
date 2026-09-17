Un **Set** (ensemble) est une collection qui stocke des valeurs du même type sans ordre défini et, surtout, **sans doublons** : chaque valeur apparaît au plus une fois.
Les sets sont parfaits lorsque seule *la présence* des valeurs t'intéresse, et non leur nombre d'occurrences ou leur position.
Tu déclares un set avec le type `Set<Element>` et un littéral au style tableau :
```swift
let numbers: Set<Int> = [1, 2, 3]
```
L'annotation de type est obligatoire : sans elle, Swift créerait un tableau.
Si le littéral contient une valeur plus d'une fois, le set n'en garde qu'une seule copie :
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
La propriété `count` indique le nombre de valeurs distinctes que contient le set.

---

Comme les tableaux, les sets peuvent être des constantes (`let`) ou des variables (`var`). Seul un set `var` peut être modifié après sa création.
Pour créer un set vide, tu appelles l'initialiseur du type, car un littéral vide `[]` seul n'indiquerait pas à Swift quel type d'élément utiliser :
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
La propriété `isEmpty` vaut `true` lorsque le set ne contient aucun élément, exactement comme avec les tableaux.

---

Comme un set ne stocke jamais la même valeur deux fois, son `count` correspond au nombre de valeurs *distinctes*, peu importe le nombre de fois où chacune a été écrite dans le littéral.

---

Pour vérifier si une valeur se trouve dans un set, utilise la méthode `contains(_:)`, qui renvoie un `Bool` :
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
Cette vérification est très rapide sur un set, même avec des milliers d'éléments, ce qui est l'une des principales raisons de préférer un set à un tableau pour les tests d'appartenance.

---

Un set `var` peut être modifié avec `insert(_:)` et `remove(_:)` :
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
Insérer une valeur déjà présente n'a aucun effet, et supprimer une valeur absente ne provoque pas d'erreur.
`remove(_:)` renvoie la valeur supprimée sous forme d'optionnel (`nil` si rien n'a été supprimé), ce qui te permet de vérifier si la suppression a réellement eu lieu.
Pour vider complètement un set, appelle `removeAll()`.

---

Tu peux parcourir un set avec `for`-`in`, mais souviens-toi qu'un set **n'a pas d'ordre défini** : les éléments peuvent sortir dans n'importe quel ordre, et cet ordre peut changer d'une exécution à l'autre.
Lorsque l'ordre compte, appelle d'abord `sorted()` : il renvoie un nouveau **tableau** avec les éléments dans l'ordre croissant, en laissant le set inchangé.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 sur des lignes séparées
}
```

---

Les sets prennent en charge les opérations classiques de la théorie des ensembles. Chacune renvoie un **nouveau** set et laisse les originaux inchangés :
- `a.union(b)` contient chaque élément présent dans `a`, dans `b`, ou dans les deux
- `a.intersection(b)` ne contient que les éléments présents à la fois dans `a` et dans `b`
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

Deux autres opérations complètent la famille :
- `a.subtracting(b)` contient les éléments de `a` qui ne sont **pas** dans `b`
- `a.symmetricDifference(b)` contient les éléments présents dans `a` ou dans `b`, mais **pas dans les deux**
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
Contrairement à `union` et `intersection`, `subtracting` n'est pas symétrique : `a.subtracting(b)` et `b.subtracting(a)` sont généralement différents.

---

Les sets peuvent aussi être comparés entre eux. Ces méthodes renvoient un `Bool` :
- `a.isSubset(of: b)` vaut `true` lorsque chaque élément de `a` est aussi dans `b`
- `a.isSuperset(of: b)` vaut `true` lorsque `a` contient chaque élément de `b`
- `a.isDisjoint(with: b)` vaut `true` lorsque `a` et `b` n'ont aucun élément en commun
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

Les sets et les tableaux se convertissent facilement l'un en l'autre.
Passer un tableau à `Set(...)` construit un set à partir de ses éléments, ce qui est le moyen le plus rapide de **supprimer les doublons** :
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} in some order
```
Passer un set à `Array(...)` renvoie un tableau, mais comme un set n'a pas d'ordre, les éléments sortent dans une séquence imprévisible.
C'est pourquoi, quand tu as besoin d'un résultat ordonné, tu appelles plutôt généralement `sorted()` sur le set, qui renvoie déjà un tableau :
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
