Nous avons déjà appris que pour assigner une valeur à une variable, nous pouvons utiliser le signe `=`, comme:
```c
int a = 5;
```

---

Nous avons déjà une variable initialisée `total`
```c
int total = 5;
```
Disons que nous voulons ajouter le nombre `2` à la variable `total`, nous pouvons écrire
```c
total = total + 2;
```
D'accord, ça marche! Mais il existe une version plus courte pour faire la même chose:
```c
total += 2;
```
Le signe `+=` s'appelle **addition assignment**.
Il ajoute une valeur à la valeur de la variable et assigne le résultat à cette variable.

---

Tout comme dans l'addition assignment, nous avons le **decrement assignment** `-=`.
La fonctionnalité est la même, la seule différence est qu'il effectue la soustraction.
Donc les éléments suivants sont exactement les mêmes
```c
num = num - 5;
// is equal to
num -= 5;
```

---

Voyons l'opérateur **multiplication assignment** `*=`.
Il multiplie la variable par une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```c
num = num * 5;
// is equal to
num *= 5;
```

---

Voyons l'opérateur **division assignment** `/=`.
Il divise la variable par une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```c
num = num / 5;
// is equal to
num /= 5;
```

---

Voyons l'opérateur **modulus assignment** `%=`.
Il calcule le modulus de la variable et d'une valeur et assigne le résultat à cette variable.
Donc les éléments suivants sont exactement les mêmes
```c
num = num % 5;
// is equal to
num %= 5;
```
