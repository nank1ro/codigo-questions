L'**opérateur d'égalité** `==` compare deux valeurs et retourne `true` si elles sont égales, ou `false` sinon.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Le résultat d'une comparaison est toujours une valeur `bool`.

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

L'**opérateur supérieur ou égal à** `>=` retourne `true` quand la valeur de gauche est plus grande que **ou égale à** la valeur de droite.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Contrairement à `>`, cet opérateur retourne aussi `true` quand les deux valeurs sont égales.
