`List`는 단순히 값을 담는 것이 아니라 **한 가지 타입**의 값을 담습니다. 타입은 컬렉션 이름 바로 뒤에 꺾쇠 괄호 사이에 씁니다:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

여기서 `String`과 `int`는 **타입 인수**이며, 타입 인수를 받는 타입을 **제네릭**이라고 합니다. 리스트 클래스는 한 번만 작성되고, `List<String>`과 `List<int>`는 여기서 만들어진 서로 다른 두 타입입니다.

그 이점은 컴파일러가 안에 무엇이 있는지 안다는 것입니다:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first는 String
```

---

`List`만 제네릭 컬렉션인 것은 아닙니다. `Set`은 타입 인수를 하나 받고, `Map`은 **두 개**를 받습니다: 하나는 키용, 하나는 값용이며 그 순서대로입니다.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

빈 컬렉션 리터럴은 내용물에서 타입을 알아낼 수 없으므로, 리터럴 자체에 타입 인수를 씁니다:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

타입이 한번 알려지면 컬렉션에서 꺼내는 모든 값은 이미 올바른 타입을 가집니다: `ages['Ada']`는 `int?`이지 알 수 없는 값이 아닙니다.

---

Dart에는 `dynamic`이라는 타입도 있습니다. 이는 "무엇이든 허용"을 의미합니다. `List<dynamic>`은 모든 값을 받아들이므로 `List<String>`보다 더 편리해 보입니다:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // 허용됨
print(things.first.toUpperCase()); // 허용됨
```

문제는 코드를 작성하는 동안 아무것도 검사되지 않는다는 점입니다. `dynamic` 값에 대한 모든 호출은 프로그램이 실행되는 동안 해석되므로, `things.first.toUpperCse()` 같은 오타도 문제없이 컴파일되고 사용자 앞에서 터집니다.

제네릭이 그 대안입니다: **어떤** 타입으로도 동작하는 하나의 코드이면서, 각 사용에서는 여전히 **하나의** 타입으로 검사됩니다. 이 주제의 핵심이 바로 이것입니다.

---

Dart가 제공하는 제네릭 클래스에만 국한되지 않습니다: 직접 선언할 수도 있습니다. **타입 매개변수**는 클래스 이름 뒤 꺾쇠 괄호 사이에 오며, 그 이후로는 본문 안에서 일반 타입처럼 사용됩니다:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T`는 단지 자리표시자일 뿐입니다. `Box`가 생성될 때 명시적으로 또는 추론을 통해 채워집니다:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, 인자로부터 추론됨
print(a.value + 1);      // 8, 컴파일러는 value가 int임을 앎
```

문자 자체는 중요하지 않습니다: `T`는 "타입"을 위한 관례일 뿐 그 이상도 이하도 아닙니다.

---

함수는 제네릭 클래스 안에 있지 않아도 그 자체로 제네릭일 수 있습니다. 타입 매개변수는 이름과 매개변수 목록 사이에 옵니다:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, 여기서 T는 String
print(firstOf([10, 20]));        // 10, 여기서 T는 int
```

하나의 함수 본문이 한 번 검사되어 모든 타입에 재사용됩니다. 타입 인수는 보통 인수로부터 추론되지만, 추론할 근거가 없을 때는 명시적으로 쓸 수 있습니다:

```dart
final empty = firstOf<String>(<String>[]); // throw되지만 타입은 명확함
```

클래스 안의 메서드도 정확히 같은 규칙을 따릅니다.

---

제네릭 클래스 안에서 타입 매개변수는 어디에서나 볼 수 있습니다: 필드, 생성자 매개변수, 메서드 시그니처, 메서드 본문 어디에서나. 클래스 이름 옆에 한 번 선언되면 모든 멤버가 사용할 수 있습니다.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

객체를 생성하는 것이 타입을 결정합니다: `Holder<String>('fig')`는 `item`을 `String`으로 만들고, `Holder<int>(3)`은 이를 `int`로 만듭니다.

---

클래스는 쉼표로 구분하여 둘 이상의 타입 매개변수를 선언할 수 있습니다. `Map<K, V>`가 내장 예시입니다: 키용 타입 하나, 값용 타입 하나입니다.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

**순서**는 타입의 일부입니다: `Entry<String, int>`와 `Entry<int, String>`은 관련 없는 타입이며, 한쪽의 값을 다른 쪽에 할당할 수 없습니다. 타입 매개변수는 반환 타입에서 순서를 바꿀 수도 있는데, 이것이 메서드가 뒤집힌 버전의 객체를 돌려주는 방법입니다:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

견고한 널 안전성에서 물음표는 서로 다른 두 곳에 위치할 수 있고, 위치마다 의미가 다릅니다:

```dart
Box<int?> a = Box(null); // 존재하며 nullable int를 담고 있는 box
Box<int>? b = null;      // box가 전혀 없음, 있다면 int를 담음
```

`Box<int?>`에서는 **타입 인수**가 널 가능하므로 `a.value`의 타입은 `int?`이고 `null`일 수 있으며, `a` 자체는 항상 존재합니다. `Box<int>?`에서는 **변수**가 널 가능하므로 `b`는 `null`일 수 있고, 안의 값에 접근하려면 `b?.value`나 `b!.value`가 필요합니다.

일반 `T`는 `T extends Object?`를 의미하므로, `Box<int?>`처럼 널 가능한 타입 인수도 완전히 합법적입니다.

---

차이는 값을 사용하는 순간 중요해집니다. `Box<int?>`에서는 필드에 정상적으로 접근한 다음 그 안의 `null`을 처리하지만, `Box<int>?`에서는 사라진 박스를 먼저 넘어야 합니다:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, box는 있지만 내용물은 null

Box<int>? b = null;
print(b?.value ?? 0); // 0, box 자체가 없음
```

`Box<int>?`에 `b.value`를 쓰면 아예 컴파일되지 않습니다: Dart는 존재하지 않을 수도 있는 것의 필드를 읽는 것을 거부합니다.

---

경계가 없는 `T`는 무엇이든 될 수 있으므로, 본문 안에서는 모든 객체가 가진 것만 사용할 수 있습니다. 다음은 컴파일되지 않습니다:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

**경계(bound)**가 이를 해결합니다. `T extends num`은 "`T`는 숫자만 될 수 있다"라고 말하고, 그 대가로 본문은 `num`이 제공하는 모든 것을 사용할 수 있습니다:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

경계는 호출 지점에서 검사됩니다: `half(4)`와 `half(2.5)`는 괜찮지만, `half('fig')`는 컴파일 시점 오류입니다. 경계는 양방향의 약속입니다. 더 좁은 인수를 주는 대신 그 안에서 더 많은 기능을 얻습니다.

---

경계의 키워드는 경계가 슈퍼클래스가 아니라 인터페이스일 때조차 항상 `extends`입니다. 타입 매개변수 목록에는 `implements`가 없습니다.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

경계가 없다면 `a > b`는 컴파일되지 않을 것입니다: 비교 연산자는 모든 객체가 아니라 `num`에 속합니다.

---

경계는 타입 매개변수 자신을 언급할 수도 있습니다. `Comparable<T>`는 `compareTo`를 통해 자신과 같은 종류와 자신을 비교하는 방법을 아는 모든 것의 인터페이스입니다:

```dart
print('fig'.compareTo('kiwi')); // 음수: fig가 먼저
print('kiwi'.compareTo('fig')); // 양수
print('fig'.compareTo('fig'));  // zero
```

따라서 `T extends Comparable<T>`는 "자기 자신과 비교될 수 있는 어떤 타입"으로 읽으며, 이것이 정렬이나 최댓값 함수에 정확히 필요한 것입니다:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String`과 `DateTime`은 둘 다 이를 직접 만족합니다. `int`와 `double`은 `Comparable<num>`을 구현하므로, 숫자 리스트는 단순히 `num`으로 비교됩니다.

---

같은 경계는 가장 작은 요소에도 그대로 동작합니다: 비교의 부호만 바뀝니다. `compareTo`는 수신자가 먼저 올 때 음수를 반환하므로, `item.compareTo(best) < 0`은 "이것이 더 작다"를 의미합니다.

---

제네릭 클래스는 다른 클래스처럼 이름 있는 생성자와 **팩토리** 생성자를 가질 수 있으며, 그 안에서도 타입 매개변수를 사용할 수 있습니다. 팩토리 생성자는 객체 자체를 만들지 않습니다: 본문을 실행하고 하나를 반환하므로, 원하는 어떤 방식으로든 인스턴스를 선택하거나 재사용하거나 만들 수 있습니다.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

타입 인수는 생성자 이름이 아니라 클래스에 붙습니다: `Box<int>.first(...)`. 팩토리 안에서 `<T>[]`는 실제 빈 `List<T>`이므로, 팩토리는 아직 알지 못하는 타입의 기본값을 만들기에 자연스러운 장소입니다.

---

경계 없이 쓴 타입 매개변수는 사실 경계가 없는 것이 아닙니다: `class Box<T>`는 `class Box<T extends Object?>`의 축약입니다. 그렇기 때문에 `Box<int?>`가 받아들여지고, 클래스 안에서 `value`가 널 불가능하다고 결코 가정할 수 없습니다.

널 가능한 타입 인수를 금지하려면 매개변수를 `Object`로 경계 지으세요:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object`는 `null`을 제외한 모든 것의 타입이므로, `T extends Object`는 "정말로 존재하기만 하면 무엇이든"으로 읽습니다.

---

`typedef`는 타입에 이름을 붙이며, 자체 타입 매개변수를 가질 수도 있습니다. 보통의 이유는 매번 풀어 쓰는 대신 함수 타입의 계열에 한 번만 이름을 붙이기 위함입니다:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>`는 `int Function(String)`을 쓰는 또 다른 방법일 뿐이므로 둘은 서로 바꿔 쓸 수 있습니다. 얻는 것은 가독성입니다: `Transform<I, O> transform`으로 선언된 매개변수는 함수의 용도를 말해주지만, `O Function(I)`는 생김새만 말해줍니다.

제네릭 typedef와 제네릭 함수는 자연스럽게 결합됩니다. 함수 자신의 타입 매개변수가 typedef의 타입 매개변수를 채웁니다.
