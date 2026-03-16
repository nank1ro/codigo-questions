L'**operatore di uguaglianza** `==` confronta due valori e restituisce `true` se sono uguali, o `false` se non lo sono.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Il risultato di un confronto è sempre un valore `bool`.

---

The **not equal operator** `!=` returns `true` when two values are **different**, and `false` when they are the same.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

It is the opposite of `==`.

---

The **greater than operator** `>` returns `true` when the left value is strictly larger than the right value.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

If the left value is equal to or smaller than the right, it returns `false`.

---

The **less than operator** `<` returns `true` when the left value is strictly smaller than the right value.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

If the left value is equal to or larger than the right, it returns `false`.

---

L'**operatore maggiore di o uguale a** `>=` restituisce `true` quando il valore sinistro è più grande che **o uguale a** il valore destro.

```dart
int score = 50;
bool passed = score >= 50; // true
```

A differenza di `>`, questo operatore restituisce anche `true` quando entrambi i valori sono uguali.
