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

---

Desde o Dart 2.17, um enum pode declarar **campos** e um **construtor**, assim como uma classe. Isso é chamado de *enum aprimorado*. Cada valor então passa seus próprios argumentos para o construtor:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

Observe as três regras: a lista de valores termina com um **ponto e vírgula** `;`, os campos devem ser `final`, e o construtor deve ser `const`.

---

Um enum aprimorado também pode declarar **métodos** e **getters**. Dentro deles, `this` é o valor atual, então você pode usar diretamente seu `name`, `index` e campos:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

Um enum sem campos ainda pode declarar métodos: a lista de valores então termina com `;` e os membros vêm em seguida.

---

Para ir de uma `String` de volta a um valor de enum, chame `byName` na lista `values`. Ela retorna o valor cujo `name` corresponde exatamente:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Se nenhum valor tiver esse nome, `byName` lança um `ArgumentError`. Quando a string vem de uma entrada do usuário, `asNameMap()` é uma escolha mais segura: ela retorna um `Map<String, Direction>` de nomes para valores, então uma busca por um nome desconhecido resulta em `null` em vez de um erro:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Valores de enum são excelentes **chaves de map**: são únicos, fáceis de comparar, e o compilador garante que você use apenas valores reais. Declare o map com o enum como tipo da chave e busque os valores com `[]`:

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

Como em qualquer map, uma busca retorna `null` quando a chave não existe, então use `??` para fornecer um valor alternativo.

---

Um enum pode **implementar uma interface** com a palavra-chave `implements`. O enum então promete fornecer todos os membros que a interface declara, e seus valores podem ser usados em qualquer lugar onde esse tipo de interface seja esperado:

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

Um getter declarado na interface pode ser implementado tanto com um getter quanto com um campo `final` de mesmo nome.
