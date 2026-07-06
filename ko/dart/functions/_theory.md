**함수**는 특정 작업을 수행하는 재사용 가능한 코드 블록입니다. Dart에서는 반환 타입, 이름, `()` 쌍으로 함수를 정의합니다.

함수가 값을 반환하지 않을 때 반환 타입은 `void`입니다：

```dart
void sayHello() {
  print("Hello!");
}
```

함수를 호출하려면 이름 뒤에 `()`를 작성합니다：

```dart
sayHello(); // prints Hello!
```

---

함수는 호출자에게 **값을 반환**할 수 있습니다. 함수 이름 앞에 반환 타입을 선언하고, `return` 키워드를 사용해 값을 돌려줍니다：

```dart
int getAge() {
  return 25;
}
```

함수 이름 앞의 타입(`int`)은 함수가 반환할 값의 종류를 Dart에 알려줍니다. `String`, `int`, `double`, `bool` 등을 사용할 수 있습니다.

---

함수는 **매개변수**를 받을 수 있습니다 — 함수를 호출할 때 전달되는 값입니다. 매개변수는 타입과 이름을 함께 괄호 안에 선언합니다：

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

각 매개변수는 타입(`int`)과 이름(`n`)을 가집니다. 여러 매개변수는 쉼표로 구분합니다.

---

Dart는 `=>` 구문을 사용한 **화살표 함수**를 지원합니다. 함수 본문이 단일 표현식일 때 `{ return ...; }` 대신 `=>`로 단축할 수 있습니다：

```dart
// 일반 함수
int double(int n) {
  return n * 2;
}

// 화살표 함수 — 동일한 결과
int double(int n) => n * 2;
```

화살표 함수는 코드를 더 간결하게 만듭니다. `=>`는 중괄호와 `return` 키워드를 모두 대체합니다.

---

Dart는 **이름 있는 매개변수**를 지원합니다 — 중괄호 `{}`로 감싼 매개변수입니다. 이름 있는 매개변수는 이름으로 호출해야 하며, 기본값을 가지거나 `required`로 표시할 수 있습니다：

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

이름 있는 매개변수는 가독성을 향상시킵니다. 특히 함수에 매개변수가 많을 때 유용합니다.
