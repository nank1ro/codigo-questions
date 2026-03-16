Un bucle `for` repite un bloque de código un número fijo de veces. La sintaxis básica es:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: se ejecuta una vez antes de que comience el bucle (p. ej., `int i = 0`)

**condition**: se comprueba antes de cada iteración; el bucle se detiene cuando es falsa

**update**: se ejecuta después de cada iteración (p. ej., `i++`)

---

Puedes usar la variable del bucle dentro del cuerpo para llevar el conteo actual. Por ejemplo, acumulando una suma:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Después del bucle, `total` es igual a 15.

---

Un bucle `for` puede contar **hacia atrás** usando un decremento (`i--`) y una condición `>=`:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

Esto es útil para cuentas regresivas o iteración en reversa.

---

El bucle `for-in` itera sobre cada elemento de una colección sin necesitar un índice:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

En cada iteración se asigna el siguiente elemento a la variable del bucle (`fruit` aquí).

---

La instrucción `break` sale de un bucle de inmediato cuando se cumple una condición:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

Esto es útil cuando se busca un valor y se quiere parar en cuanto se encuentre.
