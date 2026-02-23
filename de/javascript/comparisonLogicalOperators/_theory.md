Lassen Sie uns mit dem **Gleich** `==` Vergleichsoperator beginnen.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob zwei Ausdrucke gleich sind, zum Beispiel:
```javascript
console.log(2 == 2);
// prints true
console.log(2 == 3);
// prints false
```

---

Fahren wir mit dem **Ungleich** `!=` Vergleichsoperator fort.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob zwei Ausdrucke **NICHT** gleich sind, zum Beispiel:
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3);
// prints true
```
Er ist genau das Gegenteil des *Gleich*-Operators

---

Fahren wir mit dem **Groer als** `>` Vergleichsoperator fort.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob ein Ausdruck groer als der andere ist, zum Beispiel:
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

Fahren wir mit dem **Kleiner als** `<` Vergleichsoperator fort.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

Fahren wir mit dem **Groer oder gleich** `>=` Vergleichsoperator fort.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob ein Ausdruck groer oder gleich dem anderen ist, zum Beispiel:
```javascript
console.log(2 >= 2);
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

Fahren wir mit dem **Kleiner oder gleich** `<=` Vergleichsoperator fort.
Er gibt einen **boolean** (`true` oder `false`) zuruck, der angibt, ob ein Ausdruck kleiner oder gleich dem anderen ist, zum Beispiel:
```javascript
console.log(2 <= 2);
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

Lassen Sie uns nun die **logischen** Operatoren sehen, beginnen wir mit dem ersten namens __UND__ `&&`.
Er gibt den ersten Operanden zuruck, der zu *false* auswertet, oder den letzten, wenn alle *true* sind.
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

Fahren wir mit dem **oder** `||` logischen Operator fort.
Er gibt den ersten Operanden zuruck, der zu *true* auswertet, oder den letzten, wenn alle *false* sind.
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

Lassen Sie uns mit dem **nicht** `!` logischen Operator beenden.
Er gibt einen Boolean zuruck, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
