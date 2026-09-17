**Перечисление** (или *enum*) определяет общий тип для группы связанных значений, чтобы вы могли безопасно работать с этими значениями с точки зрения типов. В Dart вы объявляете его с помощью ключевого слова `enum`, перечисляя его **значения** через запятую:

```dart
enum Direction { north, south, east, west }
```

По соглашению имена значений записываются в стиле `lowerCamelCase`, как у переменных. К каждому значению обращаются через имя enum, а при выводе на печать показываются и enum, и значение:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Enum должен быть объявлен на **верхнем уровне** файла, никогда внутри функции, такой как `main`.

---

У каждого значения enum есть два встроенных свойства:

- `name` — имя значения в виде `String`
- `index` — его позиция в объявлении, начиная с `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

У каждого enum также есть константный список `values`, который содержит все его значения в порядке объявления. Вы можете индексировать его, как любой список, читать его `length` или перебирать его циклом `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Поскольку `values` — это список, вы можете сочетать его с уже известными вам методами списков. Например, `.map()` вместе с `.name` превращает значения в список строк:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Перебор `values` — обычный способ обработать каждое значение перечисления. Внутри цикла текущее значение ведёт себя как любой другой объект, поэтому можно прочитать его `index` и `name` и сразу использовать их в интерполяции строки:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Каждое значение enum существует ровно один раз, поэтому две ссылки на одно и то же значение всегда равны. Сравнивайте их с помощью `==` и `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Оператор `switch` — естественный способ ветвления по enum, с одним `case` на каждое значение:

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

Когда case'ы охватывают **все** значения, switch считается *исчерпывающим* и не требует `default`. Если вы забудете значение, компилятор сообщит об ошибке, вместо того чтобы допустить баг до этапа выполнения.

---

Начиная с Dart 3, `switch` также можно использовать как **выражение**, которое возвращает значение. Каждый case записывается как `паттерн => значение`, а case'ы разделяются запятыми, без ключевого слова `case` и без `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Как и форма-оператор, switch-выражение над enum должно быть исчерпывающим.

---

Начиная с Dart 2.17, enum может объявлять **поля** и **конструктор**, как и класс. Это называется *расширенным enum*. Каждое значение передаёт свои собственные аргументы конструктору:

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

Обратите внимание на три правила: список значений заканчивается **точкой с запятой** `;`, поля должны быть `final`, а конструктор должен быть `const`.

---

Расширенный enum также может объявлять **методы** и **геттеры**. Внутри них `this` — это текущее значение, поэтому вы можете напрямую использовать его `name`, `index` и поля:

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

Enum без полей всё равно может объявлять методы: список значений в этом случае заканчивается `;`, а затем следуют члены.

---

Чтобы вернуться от `String` к значению enum, вызовите `byName` на списке `values`. Он возвращает значение, чьё `name` точно совпадает:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Если ни одно значение не имеет такого имени, `byName` выбрасывает `ArgumentError`. Когда строка приходит из пользовательского ввода, более безопасным выбором является `asNameMap()`: он возвращает `Map<String, Direction>` из имён в значения, поэтому поиск неизвестного имени даёт `null` вместо ошибки:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Значения enum отлично подходят в качестве **ключей карты**: они уникальны, их легко сравнивать, и компилятор проверяет, что вы используете только реальные значения. Объявите карту с enum в качестве типа ключа и ищите значения с помощью `[]`:

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

Как и в любой карте, поиск возвращает `null`, если ключ отсутствует, поэтому используйте `??`, чтобы указать значение по умолчанию.

---

Enum может **реализовывать интерфейс** с помощью ключевого слова `implements`. При этом enum обязуется предоставить каждый член, объявленный в интерфейсе, и его значения можно использовать везде, где ожидается этот тип интерфейса:

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

Геттер, объявленный в интерфейсе, можно реализовать либо геттером, либо полем `final` с тем же именем.
