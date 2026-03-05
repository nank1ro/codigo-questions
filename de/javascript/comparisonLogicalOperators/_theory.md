Fangen wir mit dem **gleich** `==` Vergleichsoperator an.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke gleich sind, zum Beispiel:
```javascript
console.log(2 == 2);
// gibt true aus
console.log(2 == 3);
// gibt false aus
```

---

Lass uns mit dem **nicht gleich** `!=` Vergleichsoperator fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke **NICHT** gleich sind, zum Beispiel:
```javascript
console.log(2 != 2);
// gibt false aus
console.log(2 != 3);
// gibt true aus
```
Es ist genau das Gegenteil des *gleich* Operators

---

Lass uns mit dem **größer als** `>` Vergleichsoperator fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer als der andere ist, zum Beispiel:
```javascript
console.log(2 > 2);
// gibt false aus
console.log(3 > 2);
// gibt true aus
```

---

Lass uns mit dem **kleiner als** `<` Vergleichsoperator fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```javascript
console.log(2 < 2);
// gibt false aus
console.log(2 < 3);
// gibt true aus
```

---

Lass uns mit dem **größer als oder gleich** `>=` Vergleichsoperator fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer oder gleich dem anderen ist, zum Beispiel:
```javascript
console.log(2 >= 2);
// gibt true aus
console.log(3 >= 2);
// gibt true aus
console.log(3 >= 4);
// gibt false aus
```

---

Lass uns mit dem **kleiner als oder gleich** `<=` Vergleichsoperator fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als oder gleich dem anderen ist, zum Beispiel:
```javascript
console.log(2 <= 2);
// gibt true aus
console.log(3 <= 2);
// gibt false aus
console.log(3 <= 4);
// gibt true aus
```

---

Jetzt sehen wir uns die **logischen** Operatoren an. Fangen wir mit dem ersten an, genannt __UND__ `&&`.
Es gibt den ersten Operanden zurück, der zu *false* führt, oder den letzten, wenn alle *true* sind.
```javascript
console.log(2 == 2 && 2 == 3);
// gibt false aus
console.log(1 == 1 && 1 == 1.0);
// gibt true aus
```

---

Lass uns mit dem **ODER** `||` logischen Operator fortfahren.
Es gibt den ersten Operanden zurück, der zu *true* führt, oder den letzten, wenn alle *false* sind.
```javascript
console.log(2 == 2 || 2 == 3);
// gibt true aus
console.log(1 == 2 || 1 == 3);
// gibt false aus
```

---

Lass uns mit dem **NICHT** `!` logischen Operator fertig werden.
Es gibt einen booleschen Wert zurück, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```javascript
console.log(!true);
// gibt false aus
console.log(!false);
// gibt true aus
console.log(!(2 == 2));
// gibt false aus
```
