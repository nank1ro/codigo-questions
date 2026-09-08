`String name = 'Ada';`처럼 타입과 함께 변수를 선언하는 방법은 이미 알고 있습니다. 하지만 값이 그저 **없는** 경우도 있습니다. 별명이 없는 사용자, 아무것도 찾지 못한 검색, 숫자로 바꿀 수 없는 문자열처럼 말이죠. Dart는 없는 값을 `null`로 표현합니다.

Dart 2.12부터 이 언어는 **건전한 널 안전성(sound null safety)**을 갖추고 있습니다. `String` 같은 일반 타입은 **절대로** `null`을 담을 수 없습니다. 대입하려고 하면 컴파일 오류가 나서 프로그램이 실행조차 되지 않습니다:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

값이 없을 수 있도록 하려면 타입 뒤에 물음표 `?`를 붙입니다. `String?`은 `String` 또는 `null`을 담으며, `null`을 출력하면 `null`이라는 단어가 표시됩니다:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

`?`가 없는 타입을 **널 불가능(non-nullable)**, `?`가 있는 타입을 **널 가능(nullable)**이라고 합니다.

---

**값 없이** 선언된 널 가능 변수는 `null`로 시작하므로 `= null`은 생략할 수 있습니다:

```dart
int? age;
print(age); // null
```

널 불가능 변수에는 그런 기본값이 없습니다. 값이 대입되기 전에 그것을 읽는 코드는 Dart가 컴파일을 거부합니다.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

`null`에 대해 메서드를 호출하거나 속성을 읽으면 프로그램이 죽기 때문에, Dart는 널 가능 값에 보통의 점을 사용하는 것을 허용하지 않습니다:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

**널 인식 접근** 연산자 `?.`가 이를 해결합니다. 값이 `null`이면 전체 식이 `null`이 되고 그 뒤는 평가되지 않으며, 그렇지 않으면 일반적인 `.`처럼 동작합니다:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

결과가 `null`일 수 있으므로 그 타입은 널 가능입니다. `text?.length`는 `int`가 아니라 `int?`입니다.

---

없는 값은 **기본값**으로 대체해야 할 때가 많습니다. **if-null** 연산자 `??`는 왼쪽 피연산자가 `null`이 아니면 왼쪽을, 그렇지 않으면 오른쪽을 반환합니다:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??`는 오직 `null`에만 반응합니다. 빈 문자열 `''`이나 숫자 `0`은 실제 값이므로 그대로 유지됩니다.

`?.`는 널 가능한 결과를 만들기 때문에 `??`와 잘 어울립니다:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

널 안전성의 가장 큰 장점은 대부분의 `null` 실수를 사용자가 아니라 **컴파일러**가 찾아준다는 점입니다. 지금까지의 규칙:

- 널 불가능 타입(`String`, `int`, `List<int>`...)은 절대 `null`이 될 수 없다
- 널 가능 타입(`String?`, `int?`, `List<int>?`...)은 될 수 있고, 값 없이 선언하면 `null`로 시작한다
- 널 가능 값에 `.`을 쓰면 컴파일되지 않는다. `?.`를 쓰거나 `??`로 기본값을 주어야 한다

---

**if-null 대입** 연산자 `??=`는 변수가 현재 `null`인 **경우에만** 값을 대입하고, 그렇지 않으면 그대로 둡니다:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

키가 없을 수 있어 널 가능인 map의 항목에도 사용할 수 있습니다:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

컴파일러는 알 수 없더라도, 어떤 지점에서 널 가능 값이 `null`이 아니라는 것을 **당신**은 알 때가 있습니다. **널 단언** 연산자 `!`는 값이 존재한다고 약속함으로써 `String?`을 `String`으로 바꿉니다:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

주의하세요. `!`는 검사를 컴파일 시점에서 실행 시점으로 옮깁니다. 값이 **실제로** `null`이면 프로그램은 오류를 던지고 멈춥니다:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

`!`는 아껴서, 그리고 그 자리에 `null`이 오는 것 자체가 버그일 때만 사용하세요.

---

널 가능 값에 대해 살펴본 세 연산자의 차이를 기억하세요:

- `?.`는 값이 `null`일 때 `null`을 반환하며 절대 오류를 던지지 않는다
- `??`는 `null`을 기본값으로 대체한다
- `!`는 값이 존재한다고 가정하고, 없으면 **실행 시점에 오류를 던진다**

이 중 어느 것도 컴파일 오류가 아닙니다. 컴파일러는 당신의 `!`를 믿기 때문에, 약속이 깨졌다는 사실은 실행 중인 프로그램만이 알 수 있습니다.

---

널 가능 값을 `if`로 확인하는 것은 `!`보다 안전하며, Dart는 그에 대해 보상해 줍니다. `if (x != null)` 같은 검사 뒤에는 컴파일러가 블록 안에서 `x`가 `null`일 수 없음을 알기 때문에, 그곳에서 `x`를 널 불가능으로 취급합니다. 이를 **타입 승격**이라고 합니다:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

이른 반환 뒤에도 승격이 동작합니다:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

승격은 **지역 변수와 매개변수**에 적용됩니다. 이들의 값은 검사와 사용 사이에 몰래 바뀔 수 없기 때문입니다.

---

타입 승격은 외부에서 바뀔 수 있는 클래스 **필드**에는 **동작하지 않습니다**. 검사와 사용 사이에 다른 코드(서브클래스에서 오버라이드된 게터, 다른 메서드)가 그것을 다시 `null`로 설정할 수 있기 때문입니다:

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

표준적인 해결책은 필드를 **지역 변수**에 복사하는 것입니다. 지역 변수는 승격됩니다:

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

널 불가능 필드는 보통 생성자에서 값을 받아야 합니다. 값이 **나중에야**(파일을 읽은 뒤, 연결을 연 뒤...) 정해질 때는 필드에 `late`를 붙일 수 있습니다. 컴파일러는 초기화식이 없는 것을 받아들이고, 읽기 전에 당신이 값을 대입하리라 믿습니다.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

아직 값이 대입되지 않은 `late` 필드를 읽으면 실행 시점에 `LateInitializationError`가 발생합니다. `!`처럼 `late`도 컴파일 시점의 보장을 실행 시점의 검사와 맞바꾸므로, 반드시 지켜야 할 약속입니다.

`late`는 초기화식과 함께 쓸 수도 있으며, 이 경우 초기화식은 변수를 처음 읽을 때 **지연 실행**됩니다:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

널 가능성은 **이름 있는 매개변수**를 선언하는 방식에도 영향을 줍니다. 널 가능 타입의 이름 있는 매개변수는 선택적입니다. 호출자가 생략하면 그냥 `null`이 됩니다.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

널 불가능 타입이면서 기본값도 없는 이름 있는 매개변수는 생략되면 값이 없게 되므로, Dart는 그것을 `required`로 표시하도록 요구합니다. 그러면 호출자는 항상 그것을 전달해야 합니다:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

널 가능성은 컬렉션의 **요소**에도 적용됩니다. `List<int>`는 절대 `null`을 담지 않지만 `List<int?>`는 담을 수 있습니다:

```dart
List<int?> scores = [7, null, 9];
```

`List<int>?`와의 차이에 주의하세요. 이것은 리스트 자체가 없을 수 있지만, 있을 때는 진짜 숫자만 담는 리스트입니다.

`null` 요소를 없애려면 `nonNulls`를 사용합니다. 이것은 존재하는 값만 담고 `?` 없는 타입을 가진 `Iterable`을 반환합니다:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()`도 같은 일을 하며, 리스트에 여러 타입이 섞여 있을 때에도 동작합니다.

---

많은 라이브러리 함수가 무언가를 **할 수 없었음**을 알리기 위해 `null`을 사용합니다. 문자열을 숫자로 바꾸는 것이 대표적인 예입니다. `int.parse`는 텍스트가 숫자가 아니면 `FormatException`을 던지지만, `int.tryParse`는 대신 `null`을 반환하고 어떻게 할지 당신에게 맡깁니다:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

`int.tryParse`의 반환 타입은 `int?`이므로 배운 모든 것이 적용됩니다. 기본값에는 `??`, 연결에는 `?.`, 승격에는 `if` 검사를 사용하면 됩니다. `double.tryParse`도 같은 방식으로 동작합니다.

---

두 개의 연산자에도 널 인식 변형이 있습니다.

**널 인식 캐스케이드** `?..`는 객체가 `null`이 아닐 때만 캐스케이드 연산의 연쇄를 실행하고, 그렇지 않으면 전부 건너뜁니다:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

**널 인식 스프레드** `...?`는 널 가능 컬렉션의 요소를 리터럴에 넣고, 컬렉션이 `null`이면 아무것도 추가하지 않습니다:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

`?`가 없으면 `List<int>?`에 대한 `...extra`는 컴파일 오류가 됩니다.

---

실제 데이터에는 빈틈이 가득합니다. 비워 둔 양식 항목, 파일에서 빠진 열, 숫자라고 하기 어려운 문자열처럼 말이죠. 이 장의 도구들은 그런 데이터를 다루기 위해 자연스럽게 결합됩니다. 없는 요소를 버리려면 `nonNulls`, 안전하게 변환하려면 `int.tryParse`, 변환하지 못한 것을 처리하려면 `??`나 `if` 검사를 사용합니다.
