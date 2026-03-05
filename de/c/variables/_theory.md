Variablen sind Container zum Speichern von Datenwerten.
Jede Variable in C ist ein Objekt und wie in anderen Programmiersprachen hat C Befehle zum Deklarieren einer Variable.
Um eine Variable zu erstellen, müssen wir ihr einen **Typ** und einen **Namen** geben, wobei man beachten muss, dass dieser keine Leerzeichen enthalten darf.
Eine Variable wird in dem Moment erstellt, wenn Sie ihr zum ersten Mal einen Wert zuweisen.
Ein Beispiel für die Erstellung einer Variable namens `x` ist:
```c
int x = 1;
```
Auf diese Weise haben wir der _integer_-Variable namens `x` den Wert `1` zugewiesen.
Wenn wir die Variable `x` ausgeben, erhalten wir die Zahl `1` zurück:
```c
>>> printf("%i\n", x);
1
```

---

Variablen werden so genannt, weil der Wert, den sie speichern, sich ändern kann.
Wir können `x` aktualisieren, indem wir `=` verwenden und ihm einen neuen Wert geben.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

Wir können Variablen auch die Werte anderer Variablen zuweisen. Hier können wir der Variable `y` den Wert von `x` geben
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Wenn wir eine Variable aktualisieren, vergisst sie ihren vorherigen Wert.
Hier können wir die Variable `x` zweimal anzeigen und sehen, wie sich ihr Wert aktualisiert.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

In C können Zeichenkettenvariablen nur mit doppelten Anführungszeichen deklariert werden:
```c
char x[] = "May";
```

---

Wenn wir einen Variablennamen mit mehreren Wörtern haben möchten, verwenden wir **Snake Case**.
Das bedeutet, dass wir `_` verwenden, um die zusätzlichen Wörter zu verbinden.
