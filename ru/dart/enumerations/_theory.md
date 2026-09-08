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
