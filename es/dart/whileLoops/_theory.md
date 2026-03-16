Un bucle `while` repite un bloque de código mientras una condición sea `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

El bucle comprueba la condición **antes** de cada iteración. Cuando `i < 3` se vuelve `false`, el bucle se detiene.

---

Una variable contadora controla cuántas veces se ejecuta un bucle `while`.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

El contador comienza en `0`, y el bucle lo incrementa en cada iteración hasta que `count < 5` sea `false`.

---

Un bucle `do-while` es similar a un bucle `while`, pero **siempre ejecuta el cuerpo al menos una vez** — la condición se comprueba *después* de cada iteración.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Incluso si la condición es `false` desde el principio, el cuerpo se ejecuta una vez.

---

La condición de un bucle `while` puede incluir cualquier expresión booleana. En cuanto la condición se evalúa como `false`, el bucle termina.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Aquí, `n` se divide a la mitad en cada iteración usando la división entera (`~/`).

---

La palabra clave `break` sale de un bucle inmediatamente, independientemente de la condición del bucle.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Sin `break`, el bucle `while (true)` se ejecutaría para siempre. Aquí se detiene cuando `i` llega a `3`.
