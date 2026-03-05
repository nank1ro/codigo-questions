Nous avons déjà appris que pour assigner une valeur à une variable, nous pouvons utiliser le signe `=`, comme:
```javascript
let a = 5;
```

---

Nous avons déjà une variable inicisée `total`
```javascript
var total = 5;
```
Disons que nous voulons ajouter le nombre `2` à la variable `total`, nous pouvons écrire
```javascript
total = total + 2;
```
D'accord, ça marche! Mais il y a une version plus courte pour faire la même chose:
```javascript
total += 2;
```
Le signe `+=` s'appelle **addition assignment**.
Il ajoute une valeur à la valeur de la variable et assigne le résultat à cette variable.

---

Tout comme dans l'addition assignment, nous avons le **decrement assignment** `-=`.
La fonctionnalité est la même, la seule différence est qu'elle effectue la soustraction.
Donc les éléments suivants sont exactement les mêmes
```javascript
var num = num - 5;
// is equal to
num -= 5;
```

---

Voyons l'opérateur **multiplication assignment** `*=`.
Il multiplie la variable par une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```javascript
var num = num * 5;
// is equal to
num *= 5;
```

---

Voyons l'opérateur **division assignment** `/=`.
Il divise la variable par une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```javascript
num = num / 5;
// is equal to
num /= 5;
```

---

Voyons l'opérateur **remainder assignment** `%=`.
Il calcule le reste de la variable et d'une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```javascript
num = num % 5;
// is equal to
num %= 5;
```
