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

---

O método `.remove(value)` remove o **primeiro** elemento igual a `value` de uma lista. Ele retorna `true` se um elemento foi removido, ou `false` se o valor não foi encontrado.

```dart
var colors = ['red', 'green', 'blue'];
bool removed = colors.remove('green');
print(removed); // true
print(colors); // [red, blue]
```

---

As propriedades `.first` e `.last` fornecem o primeiro e o último elemento de uma lista sem usar um índice.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.first); // red
print(colors.last); // blue
```

Ambas geram um erro se a lista estiver vazia.

---

A propriedade `.isEmpty` é `true` quando uma lista não tem elementos, e `.isNotEmpty` é `true` quando ela tem pelo menos um.

```dart
var colors = <String>[];
print(colors.isEmpty); // true
colors.add('red');
print(colors.isNotEmpty); // true
```

---

O método `.indexOf(value)` retorna o índice do primeiro elemento igual a `value`. Se o valor não estiver na lista, ele retorna `-1`.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.indexOf('green')); // 1
print(colors.indexOf('pink')); // -1
```

---

O método `.where()` mantém apenas os elementos para os quais uma função retorna `true`. Ele não retorna uma nova lista, mas um `Iterable` preguiçoso, então chame `.toList()` para transformar o resultado de volta em uma `List`.

```dart
var numbers = [1, 2, 3, 4];
List<int> big = numbers.where((n) => n > 2).toList();
print(big); // [3, 4]
```
