Una **sentencia `if`** ejecuta un bloque de código solo cuando una condición es `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

El código dentro de las llaves se ejecuta solo si la condición `age >= 18` se evalúa como `true`.

---

Puedes usar `print()` dentro de un bloque `if` para mostrar un mensaje cuando se cumple una condición.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Si `isRaining` es `false`, no se imprime nada.

---

Una **sentencia `if-else`** ejecuta el bloque `if` cuando la condición es `true`, y el bloque `else` cuando es `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Exactamente una de las dos ramas siempre se ejecuta.

---

**`else if`** permite probar múltiples condiciones en secuencia. Se ejecuta la primera rama cuya condición sea `true`, y el resto se omite.

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

El **operador ternario** `condition ? expr1 : expr2` es una forma compacta de escribir una expresión `if-else` simple.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Si la condición es `true`, se usa `expr1`; de lo contrario, se usa `expr2`.
