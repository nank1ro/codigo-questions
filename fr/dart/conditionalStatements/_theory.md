Une **instruction `if`** exécute un bloc de code uniquement lorsqu'une condition est `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

Le code à l'intérieur des accolades s'exécute uniquement si la condition `age >= 18` est évaluée à `true`.

---

Tu peux utiliser `print()` à l'intérieur d'un bloc `if` pour afficher un message lorsqu'une condition est remplie.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Si `isRaining` est `false`, rien n'est affiché.

---

Une **instruction `if-else`** exécute le bloc `if` lorsque la condition est `true`, et le bloc `else` lorsqu'elle est `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Exactement l'une des deux branches s'exécute toujours.

---

**`else if`** permet de tester plusieurs conditions en séquence. La première branche dont la condition est `true` est exécutée, et le reste est ignoré.

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

L'**opérateur ternaire** `condition ? expr1 : expr2` est une façon compacte d'écrire une expression `if-else` simple.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Si la condition est `true`, `expr1` est utilisé ; sinon, `expr2` est utilisé.
