El **operador de igualdad** `==` compara dos valores y devuelve `true` si son iguales, o `false` si no lo son.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

El resultado de una comparación siempre es un valor `bool`.

---

El **operador de desigualdad** `!=` devuelve `true` cuando dos valores son **diferentes**, y `false` cuando son iguales.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

Es el opuesto de `==`.

---

El **operador mayor que** `>` devuelve `true` cuando el valor de la izquierda es estrictamente mayor que el valor de la derecha.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Si el valor de la izquierda es igual o menor que el de la derecha, devuelve `false`.

---

El **operador menor que** `<` devuelve `true` cuando el valor de la izquierda es estrictamente menor que el valor de la derecha.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Si el valor de la izquierda es igual o mayor que el de la derecha, devuelve `false`.

---

El **operador mayor que o igual a** `>=` devuelve `true` cuando el valor izquierdo es mayor que **o igual a** el valor derecho.

```dart
int score = 50;
bool passed = score >= 50; // true
```

A diferencia de `>`, este operador también devuelve `true` cuando ambos valores son iguales.
