클래스는 `extend`로 슈퍼클래스를 단 하나만 가질 수 있지만, 서로 공통점이 없는 클래스들이 같은 동작을 필요로 하는 경우가 매우 많습니다. **mixin**은 여러 클래스가 얼마든지 가져다 쓸 수 있는 재사용 가능한 동작의 조각입니다.

**`mixin`** 키워드로 믹스인을 선언하고, 클래스는 **`with`** 키워드로 이를 가져옵니다:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish`는 자체 멤버를 하나도 선언하지 않았지만 모든 `Fish`는 `swim`을 가집니다. 믹스인의 멤버가 클래스의 멤버가 되기 때문입니다. 믹스인은 관련이 있든 없든 원하는 만큼 많은 클래스가 사용할 수 있습니다.

---

믹스인의 본문은 클래스의 본문과 똑같이 보입니다. 메서드, 게터, 필드를 완전히 같은 방식으로 작성합니다. 차이는 선언 자체로 할 수 있는 일에 있습니다.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

믹스인의 이름은 **타입**이기도 합니다. 그래서 `Server() is Timestamped`는 `true`이고 변수를 `Timestamped t = Server();`로 선언할 수 있습니다. 이제 관련 없는 두 클래스가 서로를 상속하지 않고도 하나의 구현을 공유합니다.

---

믹스인은 메서드에만 국한되지 않습니다. **필드**도 선언할 수 있으며, 믹스인을 사용하는 모든 클래스의 모든 객체는 그 필드의 자신만의 복사본을 가집니다.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

이것이 믹스인을 인터페이스 이상으로 만드는 점입니다. 믹스인은 데이터와 그 데이터를 다루는 코드를 모두 가져옵니다.

---

`mixin` 선언은 클래스가 **아닙니다**. 믹스인은 다른 클래스에 섞여 들어가기 위해서만 존재하므로 자체 생성자가 없고 인스턴스화하거나 상속할 수 없습니다:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

이름은 여전히 타입으로 동작하므로 `Team() is Scored`와 `Scored s = Team();`은 모두 괜찮습니다. 믹스인에는 생성자가 없으므로 널 불가능 필드는 위의 `int score = 0;`처럼 선언된 위치에서 초기화하거나(또는 `late`로 표시해야 합니다).

---

믹스인은 **본문 없이** 멤버를 선언할 수도 있습니다. 그런 멤버는 추상 멤버입니다. 믹스인이 이를 사용하고, 믹스인을 가져오는 클래스가 이를 제공해야 합니다.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

동작은 믹스인이 가져오고 데이터는 클래스가 가져옵니다. `final String name;` 같은 클래스의 필드만으로도 같은 이름의 추상 게터를 만족할 수 있습니다.

---

조각들을 합치면, 믹스인을 사용하는 프로그램은 세 부분으로 이루어집니다. `mixin` 선언, `with`로 이를 가져오는 하나 이상의 클래스, 그리고 공유 멤버를 호출하는 코드입니다.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

최상위 선언은 Dart에서 어떤 순서로든 작성할 수 있지만, 믹스인이 이를 사용하는 클래스보다 앞에 오면 파일을 위에서 아래로 읽기가 더 쉽습니다.

---

클래스는 **여러 믹스인을 한 번에** 사용할 수 있으며, `with` 뒤에 쉼표로 나열합니다. Dart는 이들을 **왼쪽에서 오른쪽으로** 적용하면서 각 믹스인을 이전 믹스인 위에 쌓습니다. 따라서 두 믹스인이 같은 멤버를 선언하면 목록에서 **마지막** 믹스인이 이깁니다:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

이 쌓임을 **선형화(linearization)**라고 합니다. `with A, B`는 `Object` → `A` → `B` → 클래스 자체의 체인을 만듭니다.

---

마지막 믹스인이 이기기 때문에, `with` 목록의 순서는 스타일의 세부 사항이 아니라 클래스 의미의 일부입니다. 순서를 바꾸면 객체가 최종적으로 갖게 되는 구현이 달라집니다:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

하나의 믹스인만 선언하는 멤버는 경쟁하지 않습니다. 순서와 상관없이 사용할 수 있습니다. `with X, Y`를 "`X`에서 시작해 `Y`가 이를 재정의하게 한다"고 읽으면 됩니다.

---

믹스인과 `extends`는 함께 동작합니다. 클래스는 슈퍼클래스**와** 믹스인 목록을 모두 가질 수 있으며, 믹스인은 항상 슈퍼클래스 **위에** 적용됩니다:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

여기서 체인은 `Object` → `Document` → `Timestamped` → `Report`입니다. 멤버는 체인의 끝부터 찾기 시작하므로 `Report().header()`는 먼저 `Timestamped`의 버전을 찾습니다. 슈퍼클래스와 믹스인에 같은 멤버를 선언하는 것은 완전히 합법입니다. 믹스인이 상속된 동작을 대체하거나 감싸는 방식이 바로 이것입니다.

---

클래스 본문은 체인의 맨 끝에 있으므로, 클래스에서 선언한 멤버는 믹스인에서 오는 같은 멤버를 **재정의**합니다. 재정의 내부에서 **`super`**는 믹스인이 제공한 버전에 도달합니다:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

믹스인 자체는 그대로입니다. `Guest`는 여전히 원래의 `greet`를 얻습니다. `super.greet()` 덕분에 `Host`는 공유 동작을 복사하는 대신 그 위에 자신의 동작을 쌓을 수 있습니다.

---

어떤 동작은 특정 클래스 위에서만 의미가 있고, 제 역할을 하려면 그 클래스의 멤버가 필요합니다. **`on`** 절이 이 요구 사항을 명시합니다:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal`은 두 가지 일을 합니다. 믹스인이 위의 `name`처럼 `Animal`의 멤버를 사용할 수 있게 하고, 믹스인을 사용할 수 있는 대상을 제한합니다. `Rock`은 `Animal`이 아니므로 `class Rock with Noisy {}`는 컴파일 타임 오류입니다.

---

`on` 절이 있는 믹스인은 슈퍼클래스의 멤버를 자기 것처럼 읽을 수 있습니다. 그렇기 때문에 기존 타입을 꾸며 주는 동작을 두기에 좋은 자리가 됩니다:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square`는 `kind`를 재정의하고, `show`는 그 재정의를 자동으로 사용합니다. 믹스인은 항상 실제 객체의 멤버를 호출하기 때문입니다.

---

믹스인에 `on` 절이 있으면 그 타입의 멤버를 **재정의**할 수 있고, 체인에서 자기 아래에 있는 버전에 도달하기 위해 **`super`**를 호출할 수 있습니다:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log`는 믹스인 자신의 `log`가 아니라 그 아래에 있는 것입니다. 따라서 무한 재귀는 일어나지 않습니다. 이런 믹스인들을 `with A, B`로 여러 개 쌓으면 각 믹스인이 이전 믹스인을 감쌉니다. 호출은 **마지막** 믹스인에 먼저 들어와 슈퍼클래스까지 내려갑니다.

---

`mixin` 선언은 인스턴스화하거나 상속할 수 없고, 일반 `class`는 `with` 뒤에 사용할 수 없습니다. **두** 방식 모두로 동작하는 하나의 선언이 필요하다면 **`mixin class`**를 작성하세요:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

`mixin class`는 그 유연함의 대가로 두 가지 제약을 받습니다. `Object`를 상속해야 하므로 자체 `extends` 절을 가질 수 없고, 믹스인은 생성자를 절대 실행하지 않으므로 생성자를 선언해서는 안 됩니다.

---

믹스인, 상속, 인터페이스는 서로 다른 세 가지 문제를 해결합니다:

- **`extends`**는 클래스에 슈퍼클래스를 하나 부여하며, "한 종류" 관계를 위한 것입니다. 자리는 하나뿐이므로 가장 강한 관계에 써야 합니다.
- **`with`**는 서로 관련 없는 많은 클래스가 필요로 하는 동작을 추가합니다. 개수 제한이 없고, 구현은 복사되는 것이 아니라 공유됩니다.
- **`implements`**는 멤버 집합을 약속하지만 구현은 **전혀** 가져오지 않습니다. 모든 클래스가 본문을 직접 작성해야 합니다.

믹스인이 필요하다는 신호는, 공통 부모가 자연스럽지 않은 클래스들에 복사해 넣게 될 메서드가 있다는 것입니다. `Duck`, `Plane`, `Kite`가 모두 같은 `fly`를 필요로 하는 경우가 그렇습니다.

---

쌓인 믹스인은 작고 독립적인 규칙들을 하나의 클래스로 결합하는 방법입니다. 각 믹스인은 같은 멤버를 재정의하고 자기 몫을 한 뒤, `super`를 호출해 작업을 넘깁니다. 호출이 **마지막** 믹스인에 먼저 들어가므로, `with` 목록의 순서가 어떤 규칙이 어떤 규칙보다 먼저 실행되는지 결정합니다:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}`는 모든 입금을 두 배로 만듭니다. `Doubled` 뒤에 두 번째 믹스인을 추가하면, `Doubled`가 보기 전에 그 믹스인이 입금을 먼저 받습니다.
