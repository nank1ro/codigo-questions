Nous savons comment répéter du code en utilisant une boucle `while`.
Comme ce programme qui répète des instructions pour afficher `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Mais nous pouvons faire la même chose avec les boucles `for` :
```swift
for i in 0..<5 {
    print("hello")
}
```

---

Dans une boucle `for`, nous pouvons spécifier combien de fois nous aimerions que notre boucle s'exécute

---

Nous pouvons utiliser `..<` pour boucler jusqu'au nombre suivant exclu, ou `...` pour boucler jusqu'au nombre suivant inclus

---

La variable appelée `i` est la variable compteur.
Nous pouvons lui donner le nom que nous voulons.
Elle compte à quelle répétition de la boucle nous en sommes actuellement

---

La fonction `stride()` retourne une séquence de nombres.
Elle nécessite les paramètres _from_, _to_ et _by_.
Voici la syntaxe de la fonction :
```swift
stride(from:to:by:)
```
Gardez à l'esprit que la valeur `to` est exclue

---

Avec la fonction `stride()`, nous pouvons également utiliser des plages fermées, en utilisant :
```swift
stride(from:through:by:)
```
Dans ce cas, la valeur `through` est incluse

---

En Swift, nous avons aussi la boucle `forEach`.
En fait, `forEach` appelle la fermeture donnée sur chaque élément de la séquence dans le même ordre qu'une boucle `for-in` :
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9] 
numbers.forEach { num in 
    print(num)
}
```
Using the `forEach` method is distinct from a `for-in` loop in two important ways:
1. The `break` or `continue` statement cannot be used to exit the current call of the body closure or to skip subsequent calls.
2. Using the `return` statement in the body closure will only exit the closure and not the outer scope, and it won't skip subsequent calls.
