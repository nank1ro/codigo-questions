Commençons par l'opérateur de comparaison d'**égalité** `==`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```javascript
console.log(2 == 2);
// affiche true
console.log(2 == 3);
// affiche false
```

---

Continuons avec l'opérateur de comparaison de **différence** `!=`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si deux expressions ne sont **PAS** égales, par exemple :
```javascript
console.log(2 != 2);
// affiche false
console.log(2 != 3);
// affiche true
```
C'est exactement l'opposé de l'opérateur d'*égalité*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```javascript
console.log(2 > 2);
// affiche false
console.log(3 > 2);
// affiche true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```javascript
console.log(2 < 2);
// affiche false
console.log(2 < 3);
// affiche true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
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
Il renvoie un **booléen** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
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
Il renvoie le premier opérande qui évalue à *false* ou le dernier si tous sont *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// affiche false
console.log(1 == 1 && 1 == 1.0);
// affiche true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il renvoie le premier opérande qui évalue à *true* ou le dernier si tous sont *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// affiche true
console.log(1 == 2 || 1 == 3);
// affiche false
```

---

Terminons avec l'opérateur logique **non** `!`.
Il renvoie un booléen qui est l'inverse de l'état logique d'une expression.
```javascript
console.log(!true);
// affiche false
console.log(!false);
// affiche true
console.log(!(2 == 2));
// affiche false
```
