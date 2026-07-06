**클래스**는 객체를 만들기 위한 청사진입니다. 관련 데이터(필드)와 동작(메서드)을 함께 묶습니다.

Dart에서는 `class` 키워드 뒤에 클래스 이름(관례적으로 PascalCase)을 써서 클래스를 선언합니다:

```dart
class Car {
  String brand = 'Toyota';
}
```

클래스의 **인스턴스**(객체)는 다음과 같이 생성합니다:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

**생성자**는 클래스의 인스턴스를 만들 때 실행되는 특별한 메서드입니다. 객체의 필드를 초기화하는 데 사용됩니다.

Dart에서 가장 간단한 생성자는 **축약 문법** `this.fieldName`을 사용하여 매개변수를 필드에 직접 대입합니다:

```dart
class Car {
  String brand;
  Car(this.brand);
}

void main() {
  final car = Car('Toyota');
  print(car.brand); // Toyota
}
```

---

**메서드**는 클래스 내부에 정의된 함수입니다. 메서드는 객체의 동작을 나타냅니다.

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double area() {
    return 3.14 * radius * radius;
  }
}

void main() {
  final c = Circle(5);
  print(c.area()); // 78.5
}
```

메서드는 객체 자신의 필드에 이름으로 직접(또는 `this.fieldName`으로) 접근할 수 있습니다.

---

**게터**는 접근할 때 프로퍼티처럼 보이는 특별한 메서드입니다. `get` 키워드를 사용하여 정의합니다:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // 메서드 호출이 아닌 필드처럼 접근
}
```

게터는 필드에서 계산된 값에 유용합니다.

---

**상속**을 사용하면 클래스가 다른 클래스의 필드와 메서드를 재사용할 수 있습니다. `extends` 키워드를 사용하여 서브클래스(자식 클래스)를 만듭니다:

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('Meow');
  }
}
```

자식 클래스는 `super(...)`로 부모 생성자를 호출합니다. `@override` 어노테이션은 메서드가 부모의 버전을 재정의한다는 것을 나타냅니다.
