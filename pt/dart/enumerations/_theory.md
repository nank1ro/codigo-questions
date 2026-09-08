Uma **enumeração** (ou *enum*) define um tipo comum para um grupo de valores relacionados, para que você possa trabalhar com esses valores de forma segura em relação ao tipo. Em Dart você declara uma com a palavra-chave `enum`, listando seus **valores** separados por vírgulas:

```dart
enum Direction { north, south, east, west }
```

Por convenção, os nomes dos valores são escritos em `lowerCamelCase`, como as variáveis. Cada valor é acessado através do nome do enum, e imprimi-lo mostra tanto o enum quanto o valor:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Um enum deve ser declarado no **nível superior** de um arquivo, nunca dentro de uma função como `main`.

---

Todo valor de enum tem duas propriedades embutidas:

- `name` é o nome do valor como `String`
- `index` é sua posição na declaração, começando em `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Todo enum também tem uma lista constante chamada `values` que contém todos os seus valores na ordem de declaração. Você pode indexá-la como qualquer lista, ler seu `length`, ou percorrê-la com `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Como `values` é uma lista, você pode combiná-la com os métodos de lista que já conhece. Por exemplo, `.map()` com `.name` transforma os valores em uma lista de strings:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Percorrer `values` é a maneira habitual de processar todos os valores de um enum. Dentro do laço, o valor atual se comporta como qualquer outro objeto, então você pode ler o seu `index` e o seu `name` e usá-los diretamente em uma interpolação de string:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Cada valor de enum existe exatamente uma vez, então duas referências ao mesmo valor são sempre iguais. Compare-as com `==` e `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Uma instrução `switch` é a forma natural de ramificar sobre um enum, com um `case` por valor:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

Quando os cases cobrem **todos** os valores, o switch é *exaustivo* e não precisa de `default`. Se você esquecer um valor, o compilador reporta um erro em vez de deixar o bug chegar em tempo de execução.

---

Desde o Dart 3, um `switch` também pode ser usado como uma **expressão** que produz um valor. Cada case é escrito como `padrão => valor` e os cases são separados por vírgulas, sem a palavra-chave `case` e sem `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Assim como na forma de instrução, uma expressão switch sobre um enum deve ser exaustiva.
