Der **Gleichheitsoperator** `==` vergleicht zwei Werte und gibt `true` zurück, wenn sie gleich sind, oder `false`, wenn sie nicht gleich sind.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Das Ergebnis eines Vergleichs ist immer ein `bool`-Wert.

---

Der **Ungleichheitsoperator** `!=` gibt `true` zurück, wenn zwei Werte **unterschiedlich** sind, und `false`, wenn sie gleich sind.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

Er ist das Gegenteil von `==`.

---

Der **Größer-als-Operator** `>` gibt `true` zurück, wenn der linke Wert strikt größer als der rechte Wert ist.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Wenn der linke Wert gleich oder kleiner als der rechte ist, gibt er `false` zurück.

---

Der **Kleiner-als-Operator** `<` gibt `true` zurück, wenn der linke Wert strikt kleiner als der rechte Wert ist.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Wenn der linke Wert gleich oder größer als der rechte ist, gibt er `false` zurück.

---

Der **Größer-oder-gleich-Operator** `>=` gibt `true` zurück, wenn der linke Wert größer als **oder gleich** dem rechten Wert ist.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Im Gegensatz zu `>` gibt dieser Operator auch `true` zurück, wenn beide Werte gleich sind.
