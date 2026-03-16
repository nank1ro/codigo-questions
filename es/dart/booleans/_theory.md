Un __booleano__ es un tipo de dato que puede contener solo uno de dos valores: `true` o `false`.
En Dart, el tipo booleano se declara con la palabra clave `bool`.

```dart
bool isRaining = true;
```

La variable `isRaining` almacena el valor `true`, lo que significa que actualmente está lloviendo.
Los valores booleanos siempre se escriben en minúsculas: `true` y `false`.

---

Al igual que cualquier otra variable, puedes imprimir un valor booleano con `print()`.
Cuando imprimes un booleano, Dart genera el texto `true` o `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Una variable booleana también puede contener el valor `false`.
Usa `false` cuando algo no es el caso.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Igual que `true`, `false` debe escribirse en minúsculas.

---

El __operador de negación__ `!` (también llamado "no") invierte un valor booleano.
Aplicar `!` a `true` da `false`, y aplicar `!` a `false` da `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

Esto es útil cuando quieres verificar lo opuesto a una condición.

---

Los booleanos se utilizan en toda la programación para representar condiciones e impulsar decisiones.
Siempre que tu programa necesita decidir entre dos posibilidades, un booleano está involucrado.

Ejemplos:
- ¿Está el usuario conectado? (`isLoggedIn`)
- ¿Está la puerta abierta? (`isDoorOpen`)
- ¿Ha sido enviado el pedido? (`isShipped`)
