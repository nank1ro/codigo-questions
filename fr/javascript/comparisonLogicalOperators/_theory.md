Commençons par l'opérateur de comparaison **égal** `==`.
Il retourne un **booléen** (`true` ou `false`) indiquant si deux expressions sont égales, par exemple :
```javascript
console.log(2 == 2);
// prints true
console.log(2 == 3);
// prints false
```

---

Continuons avec l'opérateur de comparaison **non égal** `!=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si deux expressions sont **PAS** égales, par exemple :
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3);
// prints true
```
C'est exactement l'opposé de l'opérateur *égal*

---

Continuons avec l'opérateur de comparaison **supérieur à** `>`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est supérieure à l'autre, par exemple :
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

Continuons avec l'opérateur de comparaison **inférieur à** `<`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est inférieure à l'autre, par exemple :
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

Continuons avec l'opérateur de comparaison **supérieur ou égal à** `>=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```javascript
console.log(2 >= 2);
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

Continuons avec l'opérateur de comparaison **inférieur ou égal à** `<=`.
Il retourne un **booléen** (`true` ou `false`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```javascript
console.log(2 <= 2);
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

Voyons maintenant les opérateurs **logiques**, commençons par le premier appelé __ET__ `&&`.
Il retourne le premier opérande qui évalue à *faux* ou le dernier s'ils sont tous *vrais*.
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

Continuons avec l'opérateur logique **ou** `||`.
Il retourne le premier opérande qui évalue à *vrai* ou le dernier s'ils sont tous *faux*.
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

Finissons avec l'opérateur logique **non** `!`.
Il retourne un booléen qui est l'inverse de l'état logique d'une expression.
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
