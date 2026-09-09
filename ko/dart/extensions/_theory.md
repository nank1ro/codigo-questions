직접 작성한 클래스에 메서드를 추가하는 방법은 이미 알고 있습니다. 하지만 코드가 Dart SDK 안에 있는 `String`, `int`, `List`는 어떨까요? 이들은 수정할 수 없지만, 메서드가 하나 더 있었으면 하는 경우가 자주 있습니다.

**확장(extension)**이 이 문제를 해결합니다: 확장은 소스 코드를 건드리지 않고 하위 클래스를 만들지도 않은 채 **기존** 타입에 새 멤버를 추가합니다. 구문은 다음과 같습니다:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

확장 내부에서 `this`는 멤버가 호출되는 값을 가리킵니다. 확장이 한 번 선언되면 그 멤버들은 타입 자체의 멤버와 똑같은 방식으로 호출됩니다:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

확장은 클래스와 함수와 나란히 파일의 **최상위 수준**에 선언하며, 절대로 `main` 안에 선언하지 않습니다.

---

확장은 숫자를 포함한 모든 타입에 동작합니다. 다음 확장은 모든 `int`에 자기 자신을 두 배로 만드는 메서드를 추가합니다:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

확장은 **타입**에 적용되기 때문에, 메서드를 변수뿐 아니라 **리터럴**에 바로 호출할 수도 있습니다. 음수 리터럴에는 괄호가 필요합니다. 그렇지 않으면 점이 마이너스 기호보다 먼저 읽힙니다:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

확장은 **게터(getter)**도 선언할 수 있으며, 게터는 괄호 없이 프로퍼티처럼 읽습니다. 확장 내부에서는 타입 자체의 멤버를 바로 호출할 수 있습니다: 클래스 내부와 마찬가지로 `this.`는 생략할 수 있습니다.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

멤버가 값을 **읽기만** 하고 매개변수를 받지 않는다면 게터를, 작업을 수행하거나 인수가 필요하다면 메서드를 선택하세요.

---

`on` 뒤의 타입은 `List<int>` 같은 **매개변수화된** 타입일 수 있습니다. 그러면 확장은 그 요소 타입의 리스트에만 적용됩니다: `[1, 2].total()`은 동작하지만 `['a', 'b'].total()`은 컴파일되지 않습니다.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

확장 내부에서 `this`는 그 리스트이므로, 평소처럼 순회하거나 인덱스로 접근하거나 `length`를 호출할 수 있습니다.

---

`List<int>`에 대한 확장은 `List<String>`에 사용할 수 없습니다. **모든** 요소 타입에 동작하는 확장 하나를 작성하려면, 확장에 **타입 매개변수**를 주고(이름 뒤 꺾쇠 괄호 사이에 씁니다) `on` 타입에 그것을 사용하세요:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T`는 "요소 타입이 무엇이든"에 해당하는 자리표시자입니다: `List<int>`에서는 `int`가 되고, `List<String>`에서는 `String`이 되므로, 위 게터는 그에 따라 `int`나 `String`을 반환합니다. 컴파일러가 호출할 때마다 `T`를 채워 넣어 줍니다.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

`String`에 대한 확장은 `String?`에 호출할 수 없습니다: 값이 `null`일 수 있고 컴파일러가 호출을 거부하기 때문입니다. 대신 확장을 **널 가능** 타입에 선언하면 `String?`에 메서드를 바로 호출할 수 있고, 그 안에서 `this`는 `String?` 타입이므로 `null`인 경우를 직접 처리해야 합니다. 예를 들어 `??`로 처리할 수 있습니다:

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

널 불가능 `int`는 `int?`가 기대되는 곳에 전달될 수 있으므로, 이 확장은 두 경우 모두 동작합니다.

---

확장은 메서드, 게터, 세터, 연산자를 추가할 수 있지만 **인스턴스 필드는 추가할 수 없습니다**. `int` 값은 메모리에서 고정된 배치를 가지며, 확장은 컴파일러가 점 구문으로 호출하도록 허용하는 함수들의 모음일 뿐입니다: 값마다 추가 데이터를 저장할 공간이 없습니다.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

확장 안의 게터와 세터는 `this`에서 값을 계산하거나 기존 멤버에 전달만 할 수 있습니다: 호출 사이에 어떤 것도 기억할 수 없습니다.

---

확장은 **static** 멤버를 선언할 수 있습니다. 클래스에서와 마찬가지로 static 멤버는 어떤 값이 아니라 확장 자체에 속하며, 확장하는 타입이 아니라 **확장의 이름**을 통해 접근합니다:

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

static 멤버는 확장하는 타입과 관련된 상수와 헬퍼 함수를 두기에 편리한 곳입니다.

---

확장은 SDK 타입만을 위한 것이 아닙니다: **여러분이 직접 작성한 클래스**도 확장할 수 있습니다. 이는 클래스가 여러분이 제어하지 않는 패키지에 있을 때, 또는 클래스를 작게 유지하면서 필요한 코드 곁에 선택적인 헬퍼를 추가하고 싶을 때 유용합니다.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

확장은 클래스 바깥에 작성한 코드와 똑같이 클래스의 public 필드와 메서드를 볼 수 있습니다.

---

Dart에서는 타입이 `+`, `*`, `==` 같은 연산자가 자신의 값들에 대해 무엇을 의미하는지 정의할 수 있습니다. 이를 위해 키워드 `operator` 뒤에 기호를 붙인 이름의 메서드를 사용합니다. 연산자의 오른쪽 항이 메서드의 매개변수입니다:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

확장은 연산자를 선언할 수 있으므로, 기존 타입에 아직 없는 새 연산자를 줄 수 있습니다. `String`은 `+`와 `*`는 가지고 있지만 `-`는 없으므로, 확장이 `'hello world' - 'o'`가 무엇을 의미하는지 정의할 수 있습니다.

---

확장이 타입이 **이미 가지고 있는** 멤버를 선언하면 어떻게 될까요? 타입 자체의 멤버가 항상 이깁니다: 확장 멤버는 타입 자체에 그 이름의 멤버가 없을 때만 고려됩니다. 확장 멤버는 조용히 무시되며, 오류도 오버라이드도 없습니다.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

따라서 확장은 멤버를 추가하고 빈틈을 메울 수 있지만, 기존 멤버가 동작하는 방식을 **바꿀** 수는 없습니다.

---

확장의 이름은 생략할 수 있습니다. **이름 없는** 확장도 같은 방식으로 동작하지만, 선언한 파일 안에서만 보입니다:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

두 확장이 같은 타입에 같은 멤버를 제공하는 순간 **이름**이 중요해집니다: 호출이 **모호**해져서 컴파일되지 않습니다. 이름이 있으면 두 가지 방법으로 충돌을 해결할 수 있습니다. 확장들이 서로 다른 파일에 있다면 import에서 그중 하나를 `show` 하거나 `hide` 할 수 있습니다:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

또는 어디서든 값을 확장 이름으로 감싸 마치 생성자처럼 확장을 **명시적으로** 적용할 수 있습니다:

```dart
print(Loud('hi').describe());
```

이름 없는 확장은 숨기거나 명시적으로 적용할 수 없으므로, 다른 사람이 import할 코드에서는 이름 있는 확장을 선호하세요.

---

제네릭 확장은 `where`와 `map`이 그렇듯 **함수**를 매개변수로 받을 수 있습니다. 함수 타입은 요소 타입 `T`로 작성하므로, 콜백은 올바른 타입의 요소를 받습니다:

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
