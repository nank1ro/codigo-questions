Uma **instrução `if`** executa um bloco de código somente quando uma condição é `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

O código dentro das chaves é executado apenas se a condição `age >= 18` avaliar como `true`.

---

Você pode usar `print()` dentro de um bloco `if` para exibir uma mensagem quando uma condição é satisfeita.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Se `isRaining` for `false`, nada é impresso.

---

Uma **instrução `if-else`** executa o bloco `if` quando a condição é `true`, e o bloco `else` quando ela é `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Exatamente um dos dois ramos sempre é executado.

---

O **`else if`** permite testar múltiplas condições em sequência. O primeiro ramo cuja condição é `true` é executado, e os demais são ignorados.

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

O **operador ternário** `condition ? expr1 : expr2` é uma forma compacta de escrever uma expressão simples `if-else`.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Se a condição for `true`, `expr1` é usado; caso contrário, `expr2` é usado.
