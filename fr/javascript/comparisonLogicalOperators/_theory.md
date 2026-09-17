Commençons par l'opérateur de comparaison **égal** `==`.
Il retourne un **booléen** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```javascript
console.log(2 == 2);
// affiche true
console.log(2 == 3);
// affiche false
```

---

Continuons avec l'opérateur de comparaison **non égal** `!=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si deux expressions sont **PAS** égales, par exemple :
```javascript
console.log(2 != 2);
// affiche false
console.log(2 != 3);
// affiche true
```
C'est exactement l'opposé de l'opérateur *égal*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```javascript
console.log(2 > 2);
// affiche false
console.log(3 > 2);
// affiche true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```javascript
console.log(2 < 2);
// affiche false
console.log(2 < 3);
// affiche true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```javascript
console.log(2 >= 2);
// affiche true
console.log(3 >= 2);
// affiche true
console.log(3 >= 4);
// affiche false
```

---

Continuons avec l'opérateur de comparaison **inférieur ou égal à** `<=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```javascript
console.log(2 <= 2);
// affiche true
console.log(3 <= 2);
// affiche false
console.log(3 <= 4);
// affiche true
```

---

Voyons maintenant les opérateurs **logiques**, commençons par le premier appelé __ET__ `&&`.
Il retourne le premier opérande qui évalue à *faux* ou le dernier s'ils sont tous *vrais*.
```javascript
console.log(2 == 2 && 2 == 3);
// affiche false
console.log(1 == 1 && 1 == 1.0);
// affiche true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il retourne le premier opérande qui évalue à *vrai* ou le dernier s'ils sont tous *faux*.
```javascript
console.log(2 == 2 || 2 == 3);
// affiche true
console.log(1 == 2 || 1 == 3);
// affiche false
```

---

Finissons avec l'opérateur logique **non** `!`.
Il retourne un booléen qui est l'inverse de l'état logique d'une expression.
```javascript
console.log(!true);
// affiche false
console.log(!false);
// affiche true
console.log(!(2 == 2));
// affiche false
```

---

`==` compare ses deux côtés après les avoir convertis vers un type commun, donc `"5" == 5` vaut `true`. L'opérateur strict `===` évite cette conversion et exige en plus que les types correspondent.
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

`!=` convertit avant de comparer, tout comme `==`, donc `"5" != 5` vaut `false`. Son équivalent strict `!==` considère une chaîne et un nombre comme différents quel que soit leur contenu.
```javascript
console.log("5" !== 5); // true
```

---

Quand les deux côtés sont des chaînes, `>` les compare caractère par caractère selon leur ordre de code plutôt que par longueur, donc `"b" > "a"` vaut `true`, tout comme `"apple" > "ant"`.

---

`>=` est satisfait par l'une ou l'autre moitié de son nom : `8 >= 8` vaut `true` parce que les deux valeurs sont égales, tandis que le plus strict `8 > 8` vaut `false`.

---

Toute comparaison impliquant `NaN` renvoie `false`, même les comparaisons opposées : `NaN < 3` et `NaN >= 3` valent toutes les deux `false`, donc un `<` qui échoue ne signifie pas toujours que le côté gauche est plus grand.

---

Quand un côté est une chaîne et l'autre un nombre, `<=` convertit d'abord la chaîne en nombre, donc `"7" <= 8` vaut `true`.
