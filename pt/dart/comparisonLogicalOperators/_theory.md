O **operador de igualdade** `==` compara dois valores e retorna `true` se forem iguais, ou `false` se não forem.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

O resultado de uma comparação é sempre um valor `bool`.

---

O **operador de desigualdade** `!=` retorna `true` quando dois valores são **diferentes**, e `false` quando são iguais.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

É o oposto de `==`.

---

O **operador maior que** `>` retorna `true` quando o valor à esquerda é estritamente maior que o valor à direita.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

Se o valor à esquerda for igual ou menor que o da direita, retorna `false`.

---

O **operador menor que** `<` retorna `true` quando o valor à esquerda é estritamente menor que o valor à direita.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

Se o valor à esquerda for igual ou maior que o da direita, retorna `false`.

---

O **operador maior ou igual a** `>=` retorna `true` quando o valor à esquerda é maior que **ou igual a** o valor à direita.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Ao contrário de `>`, este operador também retorna `true` quando ambos os valores são iguais.
