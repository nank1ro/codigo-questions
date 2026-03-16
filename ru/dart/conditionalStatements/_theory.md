Оператор **`if`** выполняет блок кода только тогда, когда условие равно `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

Код внутри фигурных скобок выполняется только тогда, когда условие `age >= 18` равно `true`.

---

Можно использовать `print()` внутри блока `if`, чтобы вывести сообщение при выполнении условия.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Если `isRaining` равно `false`, ничего не выводится.

---

Оператор **`if-else`** выполняет блок `if`, когда условие равно `true`, и блок `else`, когда оно равно `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Всегда выполняется ровно одна из двух ветвей.

---

**`else if`** позволяет последовательно проверять несколько условий. Выполняется первая ветвь, условие которой равно `true`, остальные пропускаются.

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

**Тернарный оператор** `condition ? expr1 : expr2` — компактный способ записать простое выражение `if-else`.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Если условие равно `true`, используется `expr1`; в противном случае используется `expr2`.
