이름이 있는 함수, 예를 들어 `void sayHello() { ... }`를 선언하는 방법은 이미 알고 있습니다. Dart에서는 **이름 없는** 함수, 즉 **익명 함수**도 작성할 수 있습니다. 익명 함수는 이름 있는 함수와 같은 구성 요소(괄호 안의 매개변수와 중괄호 안의 본문)를 가지지만 반환 타입과 이름이 없습니다:

```dart
(String name) {
  print('Hello, $name!');
}
```

이름이 없기 때문에, 일반적으로 변수에 저장한 다음 그 변수를 함수처럼 호출하는 방식으로 사용합니다:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

닫는 중괄호 뒤의 `;`에 유의하세요. 대입은 일반적인 문장입니다.

---

익명 함수는 이름 있는 함수와 완전히 같은 방식으로 매개변수를 받고 값을 `return`할 수 있습니다. 반환 타입은 쓰지 않습니다. Dart가 본문의 `return` 문으로부터 **추론**합니다:

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

본문이 단일 표현식일 때, 익명 함수도 이름 있는 함수처럼 **화살표 구문** `=>`을 사용할 수 있습니다. 화살표는 중괄호와 `return` 키워드를 대체합니다:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

이 짧은 형태가 Dart에서 익명 함수를 작성하는 가장 흔한 방식입니다.

---

함수는 값이므로 타입을 가집니다. 함수의 타입은 **반환 타입**, 그 다음 `Function` 키워드, 그 다음 괄호 안의 **매개변수 타입** 순으로 씁니다:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

변수가 이렇게 타입이 지정되면, Dart가 선언된 타입으로부터 매개변수 타입을 추론하므로 익명 함수에서는 매개변수 타입을 생략할 수 있습니다:

```dart
int Function(int, int) add = (a, b) => a + b;
```

타입만 있는 `Function`은 매개변수와 반환 타입에 관계없이 모든 함수를 받아들일 수 있지만, 호출 방법에 대해서는 Dart에게 아무것도 알려주지 않습니다.

---

함수 타입도 일반 타입이기 때문에, 함수는 **다른 함수를 매개변수로** 받을 수 있습니다. 본문 안에서 이 매개변수는 다른 함수처럼 호출합니다:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

여기서 호출자는 두 번째 인자로 익명 함수를 전달함으로써 `apply`가 무엇을 할지 결정합니다.

---

Dart 컬렉션의 많은 메서드는 함수를 인자로 받으며, 익명 함수는 함수를 전달하는 자연스러운 방법입니다. 가장 간단한 것은 `forEach`로, 리스트의 모든 요소마다 주어진 함수를 한 번씩 호출합니다:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

매개변수 타입은 리스트로부터 추론되므로, 쓰지 않아도 `fruit`는 `String`입니다.

---

익명 함수를 받는 또 다른 아주 흔한 메서드는 `map`과 `where`입니다:

- `map`은 함수로 모든 요소를 변환하고 새 값을 반환합니다
- `where`는 함수가 `true`를 반환하는 요소만 남깁니다

둘 다 지연 평가되는 `Iterable`을 반환하므로, 결과를 `List`로 만들려면 `toList()`를 호출하세요:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

`map`과 `where`는 둘 다 `Iterable`을 반환하므로, 이들의 호출은 서로 연속해서 **연결**할 수 있습니다. 각 단계는 이전 단계의 결과를 받으며, `toList()`는 마지막에 한 번 호출합니다:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort`는 리스트를 제자리에서 재정렬합니다. 기본적으로 요소의 자연스러운 순서를 사용하지만, **두 요소를 비교**하여 음수, 0 또는 양수를 반환하는 익명 함수를 전달할 수도 있습니다. `compareTo`는 바로 그런 숫자를 반환하므로, 보통 이것을 이용해 만듭니다:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

비교에서 `a`와 `b`를 바꾸면 순서가 반대가 됩니다.

---

`reduce`는 리스트의 모든 요소를 하나의 값으로 결합합니다. 이 익명 함수는 두 개의 매개변수, 즉 **지금까지 누적된 값**과 **다음 요소**를 받아 새로운 누적 값을 반환합니다. 첫 번째 요소가 시작점으로 사용됩니다:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce`는 시작할 첫 번째 요소가 없기 때문에 빈 리스트에서는 오류를 던집니다.

---

함수는 **함수를 반환**할 수도 있습니다. 이때 반환 타입은 함수 타입이 되고, 본문은 익명 함수를 반환합니다:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

반환된 함수는 `makeAdder`가 끝난 후에도 `makeAdder`의 매개변수인 `amount`를 계속 사용한다는 점에 유의하세요. 이처럼 자신을 둘러싼 변수를 기억하는 함수를 **클로저**라고 합니다.

---

클로저는 자신이 캡처한 변수를 읽기만 하는 것이 아니라 그 변수를 **수정**할 수도 있으며, 변경 사항은 호출 사이에 유지됩니다. 이 덕분에 클래스 없이도 비공개 상태를 유지할 수 있습니다:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

`makeTimer()`를 호출할 때마다 완전히 새로운 `seconds` 변수가 만들어지므로, 두 타이머가 개수를 공유하는 일은 없습니다.
