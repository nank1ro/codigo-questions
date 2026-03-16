Um laço `while` repete um bloco de código enquanto uma condição for `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

O laço verifica a condição **antes** de cada iteração. Quando `i < 3` se torna `false`, o laço para.

---

Uma variável contadora controla quantas vezes um laço `while` é executado.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

O contador começa em `0`, e o laço o incrementa a cada iteração até que `count < 5` seja `false`.

---

Um laço `do-while` é semelhante a um laço `while`, mas **sempre executa o corpo pelo menos uma vez** — a condição é verificada *depois* de cada iteração.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Mesmo que a condição seja `false` desde o início, o corpo é executado uma vez.

---

A condição de um laço `while` pode envolver qualquer expressão booleana. Assim que a condição for avaliada como `false`, o laço termina.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Aqui, `n` é reduzido à metade a cada iteração usando divisão inteira (`~/`).

---

A palavra-chave `break` sai de um laço imediatamente, independentemente da condição do laço.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Sem `break`, o laço `while (true)` seria executado para sempre. Aqui ele para quando `i` chega a `3`.
