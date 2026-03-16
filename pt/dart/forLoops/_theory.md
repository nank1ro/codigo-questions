Um laço `for` repete um bloco de código um número definido de vezes. A sintaxe básica é:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: executado uma vez antes do laço começar (ex.: `int i = 0`)

**condition**: verificada antes de cada iteração; o laço para quando for falsa

**update**: executado após cada iteração (ex.: `i++`)

---

Você pode usar a variável do laço dentro do corpo para rastrear a contagem atual. Por exemplo, acumulando uma soma:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Após o laço, `total` é igual a 15.

---

Um laço `for` pode contar **para baixo** usando um decremento (`i--`) e uma condição `>=`:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

Isso é útil para contagens regressivas ou iteração reversa.

---

O laço `for-in` itera sobre cada elemento de uma coleção sem precisar de um índice:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

Cada iteração atribui o próximo elemento à variável do laço (`fruit` aqui).

---

A instrução `break` sai de um laço imediatamente quando uma condição é satisfeita:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

Isso é útil quando você está procurando um valor e deseja parar assim que ele for encontrado.
