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

---

`==` vergleicht seine beiden Seiten, nachdem sie in einen gemeinsamen Typ umgewandelt wurden, weshalb `"5" == 5` `true` ergibt. Der strikte Operator `===` überspringt diese Umwandlung und verlangt zusätzlich, dass auch die Typen übereinstimmen.
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

`!=` wandelt vor dem Vergleich um, genau wie `==`, weshalb `"5" != 5` `false` ergibt. Sein striktes Gegenstück `!==` behandelt eine Zeichenkette und eine Zahl als unterschiedlich, egal was sie enthalten.
```javascript
console.log("5" !== 5); // true
```

---

Sind beide Seiten Zeichenketten, vergleicht `>` sie zeichenweise nach Code-Reihenfolge statt nach Länge, weshalb `"b" > "a"` `true` ergibt und auch `"apple" > "ant"` `true` ist.

---

`>=` wird von jeder Hälfte seines Namens erfüllt: `8 >= 8` ergibt `true`, weil die beiden Werte gleich sind, während das strengere `8 > 8` `false` ergibt.

---

Jeder Vergleich mit `NaN` liefert `false`, sogar entgegengesetzte: `NaN < 3` und `NaN >= 3` sind beide `false`, ein fehlgeschlagenes `<` bedeutet also nicht immer, dass die linke Seite größer ist.

---

Ist eine Seite eine Zeichenkette und die andere eine Zahl, wandelt `<=` die Zeichenkette zuerst in eine Zahl um, weshalb `"7" <= 8` `true` ergibt.
