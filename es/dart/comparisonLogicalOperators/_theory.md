El **operador de igualdad** `==` compara dos valores y devuelve `true` si son iguales, o `false` si no lo son.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

El resultado de una comparación siempre es un valor `bool`.

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

El **operador mayor que o igual a** `>=` devuelve `true` cuando el valor izquierdo es mayor que **o igual a** el valor derecho.

```dart
int score = 50;
bool passed = score >= 50; // true
```

A diferencia de `>`, este operador también devuelve `true` cuando ambos valores son iguales.
