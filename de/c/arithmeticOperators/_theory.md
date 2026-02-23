Operatoren werden verwendet, um Operationen auf Variablen und Werten auszufuhren.
Fangen wir mit den arithmetischen Operatoren an, insbesondere mit dem **Additions** `+` Operator.
Er wird verwendet, um zwei Zahlen zu addieren, wie:
```
>>> 5 + 3
8
```

---

Fahren wir mit dem **Subtraktions** `-` Operator fort.
Er wird verwendet, um eine Zahl von einer anderen zu subtrahieren, wie:
```
>>> 5 - 3
2
```

---

Lassen Sie uns den **Multiplikations** `*` Operator sehen.
Er wird verwendet, um zwei Zahlen miteinander zu multiplizieren, wie:
```
>>> 5 * 3
15
```

---

Lassen Sie uns den **Divisions** `/` Operator sehen.
Er wird verwendet, um zwei Zahlen zu dividieren, wie:
```c
>>> 10 / 5
2
```

---

Lassen Sie uns den **Modulo** `%` Operator sehen.
Er wird verwendet, um den Rest nach einer Division zwischen zwei Zahlen zu finden, wie:
```
>>> 5 % 2
1
```
Dies ergibt 1, weil 5 geteilt durch 2 ein Quotient von 2 und einen Rest von 1 hat
```
>>> 9 % 3
0
```
Dies ergibt 0, weil 9 geteilt durch 3 ein Quotient von 3 hat und einen Rest von 0 lasst

---

C hat keinen **Exponentiation** Operator, also mussen wir die `pow()` Funktion aus der `math.h` Bibliothek verwenden.
Exponentiation entspricht der wiederholten Multiplikation der Basis: das heit, **b** mit Exponent *n* ist das Produkt der Multiplikation von *n* Basen:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Lassen Sie uns die **Ganzzahldivision** mit der `floor()` Funktion sehen.
Diese Funktion gibt den ganzzahligen Teil des Quotienten zuruck, zum Beispiel:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Auch als Ganzzahldivision bezeichnet. Der resultierende Wert ist eine ganze Zahl, obwohl der *Typ* des Ergebnisses nicht unbedingt int ist.
