**Set**은 **고유한** 값들의 컬렉션입니다: 같은 값은 최대 한 번만 나타날 수 있습니다. 맵과 마찬가지로 Set도 `{}` 리터럴 구문으로 생성하지만, `key: value` 쌍 대신 단순한 값을 담습니다:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

타입 어노테이션 `Set<int>`는 모든 요소가 `int`라고 Dart에 알립니다. 리스트나 맵과 마찬가지로, `var`는 리터럴로부터 타입을 추론합니다:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Set은 같은 값을 두 번 저장하지 않습니다. 리터럴에 중복된 값이 있으면 첫 번째로 나온 값만 유지되고 나머지는 아무 에러 없이 런타임에 버려집니다(값을 반복하는 리터럴에 대해서는 분석기가 경고를 표시합니다):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

`.length` 프로퍼티는 Set이 담고 있는 **고유한** 요소의 개수를 반환합니다:

```dart
print(letters.length); // 3
```

---

`.add(value)` 메서드는 값을 하나 추가합니다. 값이 추가되었으면 `true`를, 이미 Set에 있었다면 `false`를 반환하며 이 경우 아무것도 바뀌지 않습니다. `.addAll(iterable)` 메서드는 리스트나 다른 Set의 모든 요소를 추가하며, 마찬가지로 이미 존재하는 요소는 건너뜁니다:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

빈 `{}` 리터럴은 Set이 아니라 **맵**입니다. 빈 Set을 만들려면 타입을 지정하세요:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

`.remove(value)` 메서드는 Set에서 값을 삭제합니다. 값이 있었으면 `true`를, 없었으면 `false`를 반환합니다:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

모든 요소를 한 번에 삭제하려면 `.clear()`를 사용하세요.

---

Set에 값이 있는지 확인하려면 `bool`을 반환하는 `.contains(value)`를 사용하세요. `.isEmpty` 프로퍼티는 Set에 요소가 없을 때 `true`이고, `.isNotEmpty`는 요소가 하나 이상 있을 때 `true`입니다:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Dart의 기본 Set은 **삽입 순서**를 기억합니다: 출력하거나 반복문을 돌리면 요소들은 처음 추가된 순서로 나옵니다. 이미 있는 값을 추가해도 그 위치는 바뀌지 않습니다:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Set은 `Iterable`이므로 리스트와 마찬가지로 `for-in`으로 요소를 직접 반복할 수 있습니다. 인덱스는 없으며 요소는 삽입 순서로 방문됩니다:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
