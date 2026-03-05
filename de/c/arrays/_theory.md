Arrays sind ein Datentyp, den du verwenden kannst, um eine Sammlung verschiedener Informationen als Sequenz unter einem einzigen Variablennamen zu speichern.
Ein Array speichert mehrere Werte eines einzelnen Typs und verwendet **Indizes**, um diese Werte zu unterscheiden.
Du kannst Elemente einem Array mit einem Ausdruck der folgenden Form zuweisen:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` ist der Datentyp, den du für das Array verwendest, zum Beispiel `int`, `double`, usw.
`array_name` ist der Name der Variablen, die die Elemente speichert.
`array_size` ist die maximale Größe, die das Array haben kann.
Schließlich sind `item1` und `item2` die Werte, die wir im Array speichern möchten

---

Du kannst auf ein einzelnes Element des Arrays durch seinen Index zugreifen.
Ein Index ist wie eine Adresse, die den Platz des Elements im Array kennzeichnet.
Der Index erscheint direkt nach dem Namen des Arrays, zwischen Klammern, wie folgt:
```
list_name[index];
```

Array-Indizes beginnen mit `0`, **nicht** `1`! Du greifst auf das erste Element eines Arrays wie folgt zu: `list_name[0]`.
Das zweite Element in einem Array hat den Index 1: `list_name[1]`.

---

Ein Listen-Index verhält sich wie jeder andere Variablenname! Er kann sowohl für den Zugriff als auch für die Zuweisung von Werten verwendet werden.
Du hast gesehen, wie du auf einen Listen-Index wie folgt zugreifst:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Ruft den Wert 5 ab
```
So funktioniert eine Zuweisung:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // gibt den neuen Wert 1 aus
```

---

Du kannst die Länge in Bytes eines Arrays berechnen, indem du die `sizeof` des Arrays erhältst und sie dann durch die Größe eines Elements dividierst.
Es funktioniert, weil jedes Element im Array denselben Typ und damit die gleiche Größe hat.
Die resultierende *Länge* ist die Anzahl der Elemente, die es enthält

---

Ein Array in C muss eine feste Länge haben.
Du kannst keine Elemente am Ende eines Arrays hinzufügen, nachdem du seine Größe deklariert hast.

---

In der C-Programmierung kannst du ein Array von Arrays erstellen.
Diese Arrays werden mehrdimensionale Arrays genannt, zum Beispiel:
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
