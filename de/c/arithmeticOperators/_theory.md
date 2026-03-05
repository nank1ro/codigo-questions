Operatoren werden verwendet, um Operationen an Variablen und Werten durchzuführen.
Beginnen wir mit den arithmetischen Operatoren, insbesondere mit dem **Additions**-Operator `+`.
Er wird verwendet, um zwei Zahlen zu addieren, wie:
```
>>> 5 + 3
8
```

---

Fahren wir mit dem **Subtraktions**-Operator `-` fort.
Er wird verwendet, um eine Zahl von einer anderen zu subtrahieren, wie:
```
>>> 5 - 3
2
```

---

Schauen wir uns den **Multiplikations**-Operator `*` an.
Er wird verwendet, um zwei Zahlen miteinander zu multiplizieren, wie:
```
>>> 5 * 3
15
```

---

Schauen wir uns den **Divisions**-Operator `/` an.
Er wird verwendet, um zwei Zahlen miteinander zu dividieren, wie:
```c
>>> 10 / 5
2
```

---

Schauen wir uns den **Modulo**-Operator `%` an.
Er wird verwendet, um den Rest nach einer Division zwischen zwei Zahlen zu finden, wie:
```
>>> 5 % 2
1
```
Dies ergibt 1, weil 5 geteilt durch 2 einen Quotienten von 2 und einen Rest von 1 hat
```
>>> 9 % 3
0
```
Dies ergibt 0, weil 9 geteilt durch 3 einen Quotienten von 3 hat und einen Rest von 0 hinterlässt

---

C hat keinen **Exponentiations**-Operator, daher müssen wir die in der Bibliothek `math.h` enthaltene Funktion `pow()` verwenden.
Die Exponentiation entspricht der wiederholten Multiplikation der Basis: Das heißt, **b** mit Exponent *n* ist das Produkt der Multiplikation von *n* Basen:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Schauen wir uns die **Ganzzahldivision** mit der Funktion `floor()` an.
Diese Funktion gibt den ganzzahligen Teil des Quotienten zurück, zum Beispiel:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Wird auch als Ganzzahldivision bezeichnet. Der resultierende Wert ist eine ganze Zahl, obwohl der Typ des Ergebnisses nicht unbedingt int ist.
