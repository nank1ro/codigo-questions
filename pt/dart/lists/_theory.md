Em Dart, uma **lista** é uma coleção ordenada de itens. A maneira mais simples de criar uma lista é com a sintaxe literal `[]`:

```dart
List<int> numbers = [1, 2, 3];
```

Você também pode usar inferência de tipos com `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

A anotação de tipo `List<String>` informa ao Dart que cada elemento da lista deve ser uma `String`.

---

As listas em Dart são **indexadas a partir de zero**, ou seja, o primeiro elemento está no índice `0`, o segundo no índice `1`, e assim por diante.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

O acesso a um elemento por índice é feito com a sintaxe `list[index]`.

---

O método `.add()` adiciona um único elemento ao **final** de uma lista:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Note que `.add()` modifica a lista **no local** e retorna `void`.

---

A propriedade `.length` retorna o número de elementos em uma lista:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Uma lista vazia tem comprimento `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

O método `.contains()` verifica se uma lista inclui um determinado valor. Retorna `true` se encontrado, `false` caso contrário:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Isso é útil para verificações de pertencimento sem precisar de um laço.
