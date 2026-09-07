**클래스**는 객체를 만들기 위한 설계도입니다. Dart에서는 `class` 키워드 뒤에 클래스 이름과 중괄호 한 쌍을 작성하여 클래스를 정의합니다:

```dart
class Animal {
  // fields and methods go here
}
```

관례적으로 클래스 이름에는 **PascalCase**(각 단어의 첫 글자를 대문자로 씀)를 사용합니다.

---

클래스는 각 객체의 데이터를 담는 **인스턴스 변수**(필드라고도 함)를 가질 수 있습니다. 클래스 본문 안에서 선언하며, 각각에 초기값을 부여합니다:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

이 클래스로 만들어진 각 객체는 자신만의 `name`과 `age`를 갖습니다.

---

**생성자**는 클래스로부터 객체를 생성(인스턴스화)할 때 실행되는 특별한 메서드입니다. 생성자는 클래스와 같은 이름을 가집니다:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

`this.name`으로 작성된 매개변수는 생성자에 전달된 값을 새 객체의 `name` 필드에 바로 저장합니다. 이런 방식으로 설정되는 필드는 초기값이 필요 없습니다.

객체는 `new` 키워드(Dart에서는 생략 가능)를 사용하거나 클래스 이름만으로 생성합니다:

```dart
var dog = Animal('Rex');
```

---

이전 연습에서 본 `this.x` 매개변수는 축약형입니다. 긴 형태는 생성자 본문 안에서 각 매개변수를 해당 필드에 대입합니다(`this.x`가 필드, `x`가 매개변수입니다):

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

같은 클래스는 다음과 같이 작성할 수도 있습니다:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

이 짧은 형태를 **initializing formals**라고 합니다.

---

**메서드**는 클래스 안에 정의된 함수입니다. 메서드는 객체의 동작을 나타냅니다:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

메서드는 점 표기법으로 객체에 대해 호출합니다: `dog.speak()`.

---

`this`는 클래스의 **현재 인스턴스**, 즉 메서드가 호출된 객체를 가리킵니다. 메서드 안에서 이를 사용해 객체 자신의 필드에 접근할 수 있습니다:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

여기서 `this.radius`는 `diameter()`가 호출된 circle의 `radius` 필드를 읽습니다. 같은 이름의 다른 변수가 없으면 `this.`는 생략할 수 있습니다: `radius * 2`도 동일하게 동작합니다.

---

Dart는 **이름 있는 생성자**를 지원하여 객체를 만드는 추가적인 방법을 정의할 수 있습니다. 이름 있는 생성자는 `ClassName.constructorName` 형태로 작성합니다:

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

콜론 뒤 부분은 **초기화 목록(initializer list)**입니다. 생성자 본문이 실행되기 전에 필드를 대입합니다. 이를 통해 원점에 객체를 만들 수 있습니다: `var p = Point.origin();`

---

**게터(getter)**는 계산된 값이나 비공개 값을 읽으며 속성 접근처럼 보이는 특별한 메서드입니다. `get` 키워드로 정의합니다:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

게터는 필드처럼 접근합니다: `circle.area`(괄호 없음).

화살표 `=> expr`은 값만 반환하는 본문 `{ return expr; }`의 축약형입니다. 게터뿐만 아니라 모든 함수나 메서드에도 사용할 수 있습니다:

```dart
double half(double n) => n / 2;
```

---

**세터(setter)**는 검증 로직을 실행하면서 값을 대입할 수 있게 해주는 특별한 메서드입니다. `set` 키워드로 정의합니다:

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

private임을 표시하기 위해 필드 이름 앞에 `_`를 붙이는 경우가 많습니다.

---

**상속(inheritance)**을 사용하면 한 클래스(**서브클래스**)가 다른 클래스(**슈퍼클래스**)를 확장하여 그 필드와 메서드를 재사용할 수 있습니다. `extends` 키워드를 사용합니다:

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog`는 `Animal`로부터 `name`과 `speak()`를 상속받고, 자신만의 메서드 `fetch()`를 추가합니다. 생성자를 선언하지 않은 클래스는 매개변수가 없는 기본 생성자를 가지므로, `var dog = Dog();`라고 작성한 다음 `dog.speak()`와 `dog.fetch()`를 모두 호출할 수 있습니다.

---

서브클래스의 생성자가 슈퍼클래스의 생성자를 호출해야 할 때는 **초기화 목록**에서 `super` 키워드를 사용합니다:

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)`는 `brand` 인자를 `Vehicle`의 생성자에 전달합니다.

---

**메서드 오버라이딩**을 사용하면 서브클래스가 슈퍼클래스에 이미 존재하는 메서드를 자신만의 구현으로 제공할 수 있습니다. `@override` 애너테이션을 사용합니다:

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`@override` 애너테이션은 슈퍼클래스의 메서드를 의도적으로 대체하고 있다는 것을 Dart(그리고 다른 개발자)에게 알려줍니다.

---

**추상 클래스**는 직접 인스턴스화할 수 없는 클래스입니다. 서브클래스가 반드시 구현해야 하는 메서드, 즉 계약을 정의하는 기반으로 사용됩니다. 본문을 생략하여 추상 메서드를 표시합니다:

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`Shape()`를 직접 인스턴스화하려고 하면 오류가 발생합니다.

---

**정적 멤버(static member)**는 특정 인스턴스가 아니라 클래스 자체에 속합니다. `static` 키워드로 선언하며, 클래스에 직접 접근합니다:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

정적 필드와 메서드는 모든 인스턴스가 공유합니다.

---

**팩토리 생성자**는 `factory` 키워드를 사용하며, 객체 생성을 제어할 수 있게 해줍니다. 예를 들어 캐시된 인스턴스나 서브타입을 반환할 수 있습니다:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

`Logger()`를 호출할 때마다 같은 인스턴스가 반환됩니다(싱글턴 패턴).
