Nous avons déjà appris que pour assigner une valeur à une variable, nous pouvons utiliser le signe `=`, comme :
```swift
let a = 5
```

---

Nous avons déjà une variable initialisée `total`
```swift
var total = 5
```
Disons que nous voulons ajouter le nombre `2` à la variable `total`, nous pouvons écrire
```swift
total = total + 2
```
D'accord, ça marche ! Mais il y a une version plus courte pour faire la même chose :
```swift
total += 2
```
Le signe `+=` s'appelle **addition assignment**.
Il ajoute une valeur à la valeur de la variable et assigne le résultat à cette variable.

---

Tout comme dans l'addition assignment, nous avons le **decrement assignment** `-=`.
La fonctionnalité est la même, la seule différence est qu'elle effectue la soustraction.
Les éléments suivants sont exactement les mêmes
```swift
var num = num - 5
// est égal à
num -= 5
```

---

Regardons l'opérateur **multiplication assignment** `*=`.
Il multiplie la variable par une valeur et assigne le résultat à cette variable.
Les éléments suivants sont exactement les mêmes
```swift
var num = num * 5
// est égal à
num *= 5
```

---

Regardons l'opérateur **division assignment** `/=`.
Il divise la variable par une valeur et assigne le résultat à cette variable.
Les éléments suivants sont exactement les mêmes
```swift
num = num / 5
// est égal à
num /= 5
```

---

Regardons l'opérateur **remainder assignment** `%=`.
Il calcule le reste de la variable et une valeur et assigne le résultat à cette variable.
Les éléments suivants sont exactement les mêmes
```swift
num = num % 5
// est égal à
num %= 5
```
