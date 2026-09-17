**열거형**(또는 *enum*)은 관련된 값들의 그룹에 대한 공통 타입을 정의하여, 그 값들을 타입 안전하게 다룰 수 있게 합니다. Dart에서는 `enum` 키워드로 선언하고, **값**을 쉼표로 구분하여 나열합니다:

```dart
enum Direction { north, south, east, west }
```

관례상 값의 이름은 변수처럼 `lowerCamelCase`로 작성합니다. 각 값은 enum 이름을 통해 접근하며, 출력하면 enum과 값이 함께 표시됩니다:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

enum은 파일의 **최상위 레벨**에 선언되어야 하며, `main`과 같은 함수 내부에는 선언할 수 없습니다.

---

모든 enum 값은 두 가지 내장 프로퍼티를 가집니다:

- `name`은 값의 이름을 `String`으로 나타낸 것
- `index`는 선언에서의 위치이며, `0`부터 시작합니다

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

모든 enum은 선언 순서대로 모든 값을 담고 있는 `values`라는 상수 리스트도 가지고 있습니다. 일반 리스트처럼 인덱스로 접근하거나, `length`를 읽거나, `for-in`으로 반복할 수 있습니다:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

`values`는 리스트이므로 이미 알고 있는 리스트 메서드와 결합해서 사용할 수 있습니다. 예를 들어 `.map()`과 `.name`을 함께 사용하면 값들을 문자열 리스트로 변환할 수 있습니다:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

`values`를 순회하는 것은 열거형의 모든 값을 처리하는 일반적인 방법입니다. 반복문 안에서 현재 값은 다른 객체와 똑같이 동작하므로, `index`와 `name`을 읽어 문자열 보간에 바로 사용할 수 있습니다:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

각 enum 값은 정확히 하나만 존재하므로, 같은 값을 가리키는 두 참조는 항상 같습니다. `==`와 `!=`로 비교하세요:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

`switch` 문은 enum으로 분기하는 자연스러운 방법이며, 값마다 하나의 `case`를 갖습니다:

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

모든 값을 **빠짐없이** 다루는 케이스가 있으면 그 switch는 *exhaustive*(완전함)로 간주되어 `default`가 필요 없습니다. 값을 하나라도 빠뜨리면, 버그가 런타임까지 남는 대신 컴파일러가 오류를 보고합니다.

---

Dart 3부터 `switch`는 값을 만들어내는 **표현식**으로도 사용할 수 있습니다. 각 케이스는 `pattern => value` 형태로 작성하며, `case` 키워드나 `break` 없이 쉼표로 구분합니다:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

문 형태와 마찬가지로, enum에 대한 switch 표현식도 완전해야(exhaustive) 합니다.

---

Dart 2.17부터 enum은 클래스처럼 **필드**와 **생성자**를 선언할 수 있습니다. 이를 *확장 enum*이라고 합니다. 각 값은 자신만의 인자를 생성자에 전달합니다:

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

세 가지 규칙에 주목하세요: 값 목록은 **세미콜론** `;`으로 끝나야 하고, 필드는 `final`이어야 하며, 생성자는 `const`여야 합니다.

---

확장 enum은 **메서드**와 **게터**도 선언할 수 있습니다. 그 안에서는 `this`가 현재 값이므로, 그 값의 `name`, `index`, 필드를 바로 사용할 수 있습니다:

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

필드가 없는 enum도 메서드를 선언할 수 있습니다. 이 경우 값 목록은 `;`으로 끝나고 그 뒤에 멤버가 이어집니다.

---

`String`에서 enum 값으로 되돌아가려면 `values` 리스트에 대해 `byName`을 호출하세요. 이는 `name`이 정확히 일치하는 값을 반환합니다:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

그 이름을 가진 값이 없으면 `byName`은 `ArgumentError`를 던집니다. 문자열이 사용자 입력에서 온 경우에는 `asNameMap()`이 더 안전한 선택입니다. 이는 이름에서 값으로의 `Map<String, Direction>`을 반환하므로, 알 수 없는 이름을 조회하면 오류 대신 `null`을 얻습니다:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

enum 값은 **맵의 키**로 아주 훌륭합니다: 유일하고, 비교하기 쉬우며, 컴파일러가 실제 값만 사용되는지 확인해 줍니다. enum을 키 타입으로 하는 맵을 선언하고 `[]`로 값을 조회하세요:

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

다른 맵과 마찬가지로, 키가 없으면 조회 결과는 `null`이므로 `??`로 대체 값을 제공하세요.

---

enum은 `implements` 키워드로 **인터페이스를 구현**할 수 있습니다. 그러면 enum은 인터페이스가 선언한 모든 멤버를 제공하기로 약속하며, 그 값들은 해당 인터페이스 타입이 필요한 곳이라면 어디서든 사용할 수 있습니다:

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

인터페이스에 선언된 게터는 게터로 구현하거나, 같은 이름의 `final` 필드로 구현할 수 있습니다.
